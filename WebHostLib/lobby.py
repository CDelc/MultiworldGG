import json
from datetime import datetime, timedelta

from flask import flash, redirect, render_template, request, session, url_for, abort
from pony.orm import commit, db_session, select, desc, count
from werkzeug.security import generate_password_hash, check_password_hash

import Utils
from Utils import __version__
from WebHostLib import app, limiter
from WebHostLib.generate import get_meta
from WebHostLib.models import (
    Lobby, LobbyPlayer, LobbyMessage, LobbyYaml,
    LOBBY_OPEN, LOBBY_GENERATING, LOBBY_DONE, LOBBY_CLOSED,
    UUID,
)


def _expire_lobby_if_needed(lobby: Lobby) -> None:
    """Check if a lobby has expired due to inactivity and close it if so."""
    if lobby.state in (LOBBY_OPEN, LOBBY_GENERATING):
        now = datetime.utcnow()
        if now - lobby.last_activity > timedelta(minutes=lobby.timeout_minutes):
            lobby.state = LOBBY_CLOSED


def _get_player_in_lobby(lobby: Lobby) -> LobbyPlayer | None:
    """Get the current session's player record in a lobby, or None."""
    return LobbyPlayer.get(lobby=lobby, session_id=session["_id"])


@app.route('/lobbies')
def lobby_list():
    lobbies = select(
        l for l in Lobby if l.state == LOBBY_OPEN
    ).order_by(lambda l: desc(l.last_activity))[:50]

    any_expired = False
    for lobby in lobbies:
        old_state = lobby.state
        _expire_lobby_if_needed(lobby)
        if lobby.state != old_state:
            any_expired = True
    if any_expired:
        commit()

    active_lobbies = [l for l in lobbies if l.state != LOBBY_CLOSED]

    lobby_ids = [l.id for l in active_lobbies]
    player_counts = {}
    yaml_counts = {}
    if lobby_ids:
        for lid, cnt in select((p.lobby.id, count()) for p in LobbyPlayer if p.lobby.id in lobby_ids):
            player_counts[lid] = cnt
        for lid, cnt in select((y.lobby.id, count()) for y in LobbyYaml if y.lobby.id in lobby_ids):
            yaml_counts[lid] = cnt

    return render_template("lobbyList.html", lobbies=active_lobbies,
                           player_counts=player_counts, yaml_counts=yaml_counts)


@app.route('/lobby/create', methods=['GET', 'POST'])
def lobby_create():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('Lobby title is required.')
            return redirect(url_for('lobby_create'))
        if len(title) > 48:
            flash('Lobby title must be 48 characters or fewer.')
            return redirect(url_for('lobby_create'))

        password = request.form.get('password', '').strip()
        password_hash = generate_password_hash(password) if password else ""

        try:
            timeout_minutes = int(request.form.get('timeout_minutes', 30))
        except (ValueError, TypeError):
            timeout_minutes = 30
        timeout_minutes = max(1, min(timeout_minutes, 2880))  # 1 min to 2 days

        try:
            max_yamls = int(request.form.get('max_yamls_per_player', 1))
        except (ValueError, TypeError):
            max_yamls = 1
        max_yamls = max(1, min(max_yamls, 20))

        race = bool(request.form.get('race'))

        try:
            max_players = max(0, min(int(request.form.get('max_players', 0) or 0), 100))
        except (ValueError, TypeError):
            max_players = 0

        allow_custom_apworlds = bool(request.form.get('allow_custom_apworlds'))

        owned_active = count(
            l for l in Lobby
            if l.owner == session["_id"] and l.state in (LOBBY_OPEN, LOBBY_GENERATING)
        )
        if owned_active >= 3:
            flash('You can only host up to 3 active lobbies at a time. Close or finish an existing one first.')
            return redirect(url_for('lobby_create'))

        meta = get_meta(request.form, race)

        lobby = Lobby(
            title=title,
            owner=session["_id"],
            password_hash=password_hash,
            timeout_minutes=timeout_minutes,
            max_yamls_per_player=max_yamls,
            race=race,
            max_players=max_players,
            allow_custom_apworlds=allow_custom_apworlds,
            meta=json.dumps(meta),
            state=LOBBY_OPEN,
        )
        commit()

        creator_name = request.form.get('player_name', '').strip() or 'Host'
        player = LobbyPlayer(
            lobby=lobby,
            session_id=session["_id"],
            player_name=creator_name,
        )
        LobbyMessage(
            lobby=lobby,
            player=None,
            sender_name="System",
            content=f"{creator_name} created the lobby.",
        )
        commit()

        lobby.last_activity = datetime.utcnow()
        commit()

        return redirect(url_for('lobby_view', lobby=lobby.id))

    return render_template("lobbyCreate.html", race=False, version=__version__)


@app.route('/lobby/<suuid:lobby>')
def lobby_view(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        abort(404)

    old_state = lobby.state
    _expire_lobby_if_needed(lobby)
    if lobby.state != old_state:
        commit()

    if lobby.state == LOBBY_CLOSED:
        flash('This lobby has expired.')
        return redirect(url_for('lobby_list'))

    player = _get_player_in_lobby(lobby)
    is_owner = (lobby.owner == session["_id"])
    needs_password = bool(lobby.password_hash) and not player

    # Pre-fetch last 200 messages to avoid loading entire set in template
    recent_messages = list(select(
        m for m in LobbyMessage if m.lobby == lobby
    ).order_by(lambda m: desc(m.id))[:200])[::-1]

    yaml_count = count(y for y in LobbyYaml if y.lobby == lobby)
    player_count = count(p for p in LobbyPlayer if p.lobby == lobby)
    has_custom = bool(count(y for y in LobbyYaml if y.lobby == lobby and y.is_custom))
    is_full = lobby.max_players > 0 and player_count >= lobby.max_players

    meta = json.loads(lobby.meta)
    server_opts = meta.get("server_options", {})
    gen_opts = meta.get("generator_options", {})

    return render_template(
        "lobby.html",
        lobby=lobby,
        player=player,
        is_owner=is_owner,
        needs_password=needs_password,
        recent_messages=recent_messages,
        yaml_count=yaml_count,
        player_count=player_count,
        has_custom=has_custom,
        is_full=is_full,
        server_opts=server_opts,
        gen_opts=gen_opts,
        instance_name=Utils.instance_name or "Archipelago",
    )


@app.route('/lobby/<suuid:lobby>/join', methods=['POST'])
@limiter.limit("5 per minute")
def lobby_join(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        abort(404)

    old_state = lobby.state
    _expire_lobby_if_needed(lobby)
    if lobby.state != old_state:
        commit()

    if lobby.state != LOBBY_OPEN:
        flash('This lobby is no longer accepting new players.')
        return redirect(url_for('lobby_view', lobby=lobby.id))

    existing = _get_player_in_lobby(lobby)
    if existing:
        return redirect(url_for('lobby_view', lobby=lobby.id))

    active_memberships = count(
        p for p in LobbyPlayer
        if p.session_id == session["_id"] and p.lobby.state in (LOBBY_OPEN, LOBBY_GENERATING)
    )
    if active_memberships >= 5:
        flash('You can only be part of up to 5 active lobbies at a time.')
        return redirect(url_for('lobby_view', lobby=lobby.id))

    if lobby.max_players > 0:
        current_player_count = count(p for p in LobbyPlayer if p.lobby == lobby)
        if current_player_count >= lobby.max_players:
            flash('This lobby is full.')
            return redirect(url_for('lobby_view', lobby=lobby.id))

    if lobby.password_hash:
        password = request.form.get('password', '')
        if not check_password_hash(lobby.password_hash, password):
            flash('Incorrect lobby password.')
            return redirect(url_for('lobby_view', lobby=lobby.id))

    player_name = request.form.get('player_name', '').strip()
    if not player_name:
        flash('Please provide a display name.')
        return redirect(url_for('lobby_view', lobby=lobby.id))
    if len(player_name) > 32:
        flash('Display name must be 32 characters or fewer.')
        return redirect(url_for('lobby_view', lobby=lobby.id))

    existing_names = select(p.player_name for p in LobbyPlayer if p.lobby == lobby)[:]
    if player_name in existing_names:
        flash('That name is already taken in this lobby.')
        return redirect(url_for('lobby_view', lobby=lobby.id))

    player = LobbyPlayer(
        lobby=lobby,
        session_id=session["_id"],
        player_name=player_name,
    )
    LobbyMessage(
        lobby=lobby,
        player=None,
        sender_name="System",
        content=f"{player_name} joined the lobby.",
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    return redirect(url_for('lobby_view', lobby=lobby.id))
