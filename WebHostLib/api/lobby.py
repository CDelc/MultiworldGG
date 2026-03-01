import json
import os
from datetime import datetime, timedelta
from uuid import UUID

from flask import request, session, jsonify
from markupsafe import Markup
from pony.orm import commit, select

from WebHostLib.api import api_endpoints
from WebHostLib.check import get_yaml_data, roll_options
from WebHostLib.models import (
    Lobby, LobbyPlayer, LobbyMessage, LobbyYaml, Room,
    LOBBY_OPEN, LOBBY_GENERATING, LOBBY_DONE, LOBBY_CLOSED,
    Generation, Seed, uuid4,
)
from WebHostLib import app


def _expire_lobby_if_needed(lobby: Lobby) -> None:
    if lobby.state in (LOBBY_OPEN, LOBBY_GENERATING):
        if datetime.utcnow() - lobby.last_activity > timedelta(minutes=lobby.timeout_minutes):
            lobby.state = LOBBY_CLOSED


def _get_player_in_lobby(lobby: Lobby) -> LobbyPlayer | None:
    return LobbyPlayer.get(lobby=lobby, session_id=session["_id"])


@api_endpoints.route('/lobby/<suuid:lobby>/status', methods=['GET'])
def lobby_status(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    old_state = lobby.state
    _expire_lobby_if_needed(lobby)
    if lobby.state != old_state:
        commit()

    after_message_id = request.args.get('after_message', 0, type=int)

    # Fetch players and yamls in two flat queries instead of N+1
    player_rows = select(
        p for p in LobbyPlayer if p.lobby == lobby
    ).order_by(LobbyPlayer.joined_at)[:]

    # Group yamls by player id using a single query with player_id included
    yamls_by_player: dict[int, list] = {}
    yaml_player_map = select(
        (y.id, y.filename, y.yaml_player_name, y.yaml_game, y.player.id)
        for y in LobbyYaml if y.lobby == lobby
    ).order_by(lambda i, f, n, g, p: i)[:]

    for y_id, y_filename, y_pname, y_game, p_id in yaml_player_map:
        yaml_info = {"id": y_id, "filename": y_filename}
        if y_pname:
            yaml_info["player_name"] = y_pname
        if y_game:
            yaml_info["game"] = y_game
        yamls_by_player.setdefault(p_id, []).append(yaml_info)

    players = []
    for p in player_rows:
        players.append({
            "id": p.id,
            "name": p.player_name,
            "is_owner": p.session_id == lobby.owner,
            "yamls": yamls_by_player.get(p.id, []),
        })

    messages = select(
        m for m in LobbyMessage
        if m.lobby == lobby and m.id > after_message_id
    ).order_by(LobbyMessage.id)[:200]

    message_list = [{
        "id": m.id,
        "sender": m.sender_name,
        "content": m.content,
        "time": m.sent_at.isoformat(),
        "system": m.player is None,
    } for m in messages]

    total_yamls = len(yaml_player_map)

    result = {
        "state": lobby.state,
        "title": lobby.title,
        "player_count": len(players),
        "players": players,
        "messages": message_list,
        "total_yamls": total_yamls,
        "max_yamls_per_player": lobby.max_yamls_per_player,
    }

    if lobby.state == LOBBY_DONE:
        from WebHostLib import to_url
        if lobby.seed:
            result["seed_id"] = to_url(lobby.seed.id)
        if lobby.room:
            result["room_id"] = to_url(lobby.room.id)

    # If generating, check if generation is done.
    # Re-read lobby state to avoid race where multiple pollers try to transition simultaneously.
    if lobby.state == LOBBY_GENERATING and lobby.generation_id:
        gen_id = lobby.generation_id
        seed = Seed.get(id=gen_id)
        if seed:
            # Guard: only transition if we're still GENERATING (another request may have beaten us)
            if lobby.state == LOBBY_GENERATING:
                lobby.seed = seed
                room = Room(seed=seed, owner=lobby.owner, tracker=uuid4())
                lobby.room = room
                lobby.state = LOBBY_DONE
                lobby.generation_id = None
                LobbyMessage(
                    lobby=lobby,
                    player=None,
                    sender_name="System",
                    content="Seed generated! Room is ready.",
                )
                try:
                    commit()
                except Exception:
                    # OptimisticCheckError — another request already transitioned.
                    # Just return current state; next poll will see DONE.
                    return jsonify(result)
            from WebHostLib import to_url
            result["state"] = LOBBY_DONE
            if lobby.seed:
                result["seed_id"] = to_url(lobby.seed.id)
            if lobby.room:
                result["room_id"] = to_url(lobby.room.id)
        else:
            gen = Generation.get(id=gen_id)
            if gen and gen.state == -1:  # STATE_ERROR
                gen_meta = json.loads(gen.meta)
                error = gen_meta.get("error", "Unknown error")
                lobby.state = LOBBY_OPEN
                lobby.generation_id = None
                LobbyMessage(
                    lobby=lobby,
                    player=None,
                    sender_name="System",
                    content=f"Generation failed: {error}",
                )
                commit()
                result["state"] = LOBBY_OPEN
            elif gen is None:
                lobby.state = LOBBY_OPEN
                lobby.generation_id = None
                LobbyMessage(
                    lobby=lobby,
                    player=None,
                    sender_name="System",
                    content="Generation failed unexpectedly. Please try again.",
                )
                commit()
                result["state"] = LOBBY_OPEN

    return jsonify(result)


@api_endpoints.route('/lobby/<suuid:lobby>/upload', methods=['POST'])
def lobby_upload_yaml(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    _expire_lobby_if_needed(lobby)
    if lobby.state != LOBBY_OPEN:
        return jsonify({"error": "Lobby is not accepting uploads"}), 400

    player = _get_player_in_lobby(lobby)
    if not player:
        return jsonify({"error": "You are not in this lobby"}), 403

    # Check YAML count limit
    current_count = len(player.yamls)
    if current_count >= lobby.max_yamls_per_player:
        return jsonify({"error": f"Maximum {lobby.max_yamls_per_player} YAML(s) per player"}), 400

    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    files = request.files.getlist('file')
    if not files:
        return jsonify({"error": "No file provided"}), 400

    # Limit upload to remaining slots
    remaining = lobby.max_yamls_per_player - current_count
    if len(files) > remaining:
        return jsonify({"error": f"You can only upload {remaining} more YAML(s)"}), 400

    # Validate using existing pipeline
    options = get_yaml_data(files)
    if isinstance(options, (str, Markup)):
        return jsonify({"error": str(options)}), 400

    # Roll options to validate games are supported and extract player names
    meta = json.loads(lobby.meta)
    plando_options = set(meta.get("plando_options", []))
    results, rolled = roll_options(options, plando_options)
    errors = {k: v for k, v in results.items() if isinstance(v, str)}
    if errors:
        error_msg = "; ".join(errors.values())
        return jsonify({"error": error_msg}), 400

    # Extract player names and games from rolled options
    new_names: dict[str, str] = {}  # filename -> resolved name
    new_games: dict[str, str] = {}  # filename -> game
    for filename, rolled_opts in rolled.items():
        name = getattr(rolled_opts, 'name', None) or os.path.splitext(filename)[0]
        new_names[filename] = name
        new_games[filename] = getattr(rolled_opts, 'game', '')

    # Check for duplicates within the uploaded batch
    seen_names: dict[str, str] = {}
    for filename, name in new_names.items():
        if name in seen_names:
            return jsonify({
                "error": f"Duplicate player name '{name}' in uploaded files: "
                         f"'{seen_names[name]}' and '{filename}'"
            }), 400
        seen_names[name] = filename

    # Check against existing YAMLs in the lobby
    existing_names = set(select(
        y.yaml_player_name for y in LobbyYaml
        if y.lobby == lobby and y.yaml_player_name is not None
    )[:])
    for filename, name in new_names.items():
        if name in existing_names:
            return jsonify({
                "error": f"Player name '{name}' (from '{filename}') is already used by another YAML in this lobby."
            }), 400

    # Store validated YAMLs
    uploaded = []
    for filename, content in options.items():
        if isinstance(content, str):
            content = content.encode('utf-8')
        yaml_record = LobbyYaml(
            lobby=lobby,
            player=player,
            filename=filename,
            yaml_player_name=new_names.get(filename),
            yaml_game=new_games.get(filename, ''),
            content=content,
        )
        commit()
        uploaded.append({"id": yaml_record.id, "filename": filename})

    lobby.last_activity = datetime.utcnow()
    commit()

    return jsonify({"uploaded": uploaded}), 201


@api_endpoints.route('/lobby/<suuid:lobby>/yaml/<int:yaml_id>', methods=['DELETE'])
def lobby_delete_yaml(lobby: UUID, yaml_id: int):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    if lobby.state != LOBBY_OPEN:
        return jsonify({"error": "Cannot modify YAMLs in current lobby state"}), 400

    yaml_record = LobbyYaml.get(id=yaml_id)
    if not yaml_record or yaml_record.lobby != lobby:
        return jsonify({"error": "YAML not found"}), 404

    player = _get_player_in_lobby(lobby)
    is_owner = lobby.owner == session["_id"]

    # Only the YAML owner or lobby owner can delete
    if not player or (yaml_record.player != player and not is_owner):
        return jsonify({"error": "Permission denied"}), 403

    filename = yaml_record.filename
    owner_name = yaml_record.player.player_name
    yaml_record.delete()

    LobbyMessage(
        lobby=lobby,
        player=None,
        sender_name="System",
        content=f"{owner_name}'s YAML '{filename}' was removed.",
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    return jsonify({"success": True})


@api_endpoints.route('/lobby/<suuid:lobby>/chat', methods=['POST'])
def lobby_chat(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    player = _get_player_in_lobby(lobby)
    if not player:
        return jsonify({"error": "You are not in this lobby"}), 403

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    content = data.get('message', '').strip()
    if not content:
        return jsonify({"error": "Empty message"}), 400
    if len(content) > 500:
        return jsonify({"error": "Message too long (max 500 characters)"}), 400

    msg = LobbyMessage(
        lobby=lobby,
        player=player,
        sender_name=player.player_name,
        content=content,
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    return jsonify({
        "id": msg.id,
        "sender": msg.sender_name,
        "content": msg.content,
        "time": msg.sent_at.isoformat(),
        "system": False,
    }), 201


@api_endpoints.route('/lobby/<suuid:lobby>/generate', methods=['POST'])
def lobby_generate(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    if lobby.owner != session["_id"]:
        return jsonify({"error": "Only the lobby owner can generate"}), 403

    if lobby.state != LOBBY_OPEN:
        return jsonify({"error": "Lobby is not in a state to generate"}), 400

    # Collect all YAMLs
    all_yamls = select(y for y in LobbyYaml if y.lobby == lobby).order_by(LobbyYaml.id)[:]
    if not all_yamls:
        return jsonify({"error": "No YAMLs uploaded yet"}), 400

    if len(all_yamls) > app.config["MAX_ROLL"]:
        return jsonify({
            "error": f"Too many YAMLs ({len(all_yamls)}). Maximum is {app.config['MAX_ROLL']}."
        }), 400

    # Build options dict from stored YAMLs
    # Prefix with player name + yaml id to guarantee uniqueness, since multiple
    # players may upload files with the same name (e.g. "my_settings.yaml").
    options = {}
    for yaml_record in all_yamls:
        unique_key = f"{yaml_record.player.player_name}_{yaml_record.id}_{yaml_record.filename}"
        options[unique_key] = yaml_record.content

    # Validate all options together
    meta = json.loads(lobby.meta)
    plando_options = set(meta.get("plando_options", []))
    results, gen_options = roll_options(options, plando_options)

    errors = {k: v for k, v in results.items() if isinstance(v, str)}
    if errors:
        error_msg = "; ".join(errors.values())
        LobbyMessage(
            lobby=lobby, player=None, sender_name="System",
            content=f"Generation validation failed: {error_msg}",
        )
        commit()
        return jsonify({"error": error_msg}), 400

    lobby.state = LOBBY_GENERATING
    LobbyMessage(
        lobby=lobby, player=None, sender_name="System",
        content="Seed generation started...",
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    # Use the queued generation path (same as /generate page)
    from pickle import PicklingError
    from Utils import restricted_dumps
    try:
        gen = Generation(
            options=restricted_dumps({name: vars(opts) for name, opts in gen_options.items()}),
            meta=json.dumps(meta),
            state=0,  # STATE_QUEUED
            owner=session["_id"],
        )
        commit()
        lobby.generation_id = gen.id
        commit()
    except PicklingError as e:
        lobby.state = LOBBY_OPEN
        lobby.generation_id = None
        LobbyMessage(
            lobby=lobby, player=None, sender_name="System",
            content=f"Generation failed: {e}",
        )
        commit()
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "generating"}), 202


@api_endpoints.route('/lobby/<suuid:lobby>/leave', methods=['POST'])
def lobby_leave(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    player = _get_player_in_lobby(lobby)
    if not player:
        return jsonify({"error": "You are not in this lobby"}), 400

    # Owner cannot leave (they should close the lobby instead)
    if lobby.owner == session["_id"]:
        return jsonify({"error": "The lobby owner cannot leave. Close the lobby instead."}), 400

    name = player.player_name
    # Clear message references and delete player's YAMLs
    for m in player.messages:
        m.player = None
    for y in player.yamls:
        y.delete()
    player.delete()

    LobbyMessage(
        lobby=lobby, player=None, sender_name="System",
        content=f"{name} left the lobby.",
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    return jsonify({"success": True})


@api_endpoints.route('/lobby/<suuid:lobby>/kick/<int:player_id>', methods=['POST'])
def lobby_kick(lobby: UUID, player_id: int):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    if lobby.owner != session["_id"]:
        return jsonify({"error": "Only the lobby owner can kick players"}), 403

    if lobby.state != LOBBY_OPEN:
        return jsonify({"error": "Cannot kick players in current state"}), 400

    target = LobbyPlayer.get(id=player_id)
    if not target or target.lobby != lobby:
        return jsonify({"error": "Player not found"}), 404

    if target.session_id == lobby.owner:
        return jsonify({"error": "Cannot kick the lobby owner"}), 400

    name = target.player_name
    for m in target.messages:
        m.player = None
    for y in target.yamls:
        y.delete()
    target.delete()

    LobbyMessage(
        lobby=lobby, player=None, sender_name="System",
        content=f"{name} was kicked from the lobby.",
    )
    lobby.last_activity = datetime.utcnow()
    commit()

    return jsonify({"success": True})


@api_endpoints.route('/lobby/<suuid:lobby>/close', methods=['POST'])
def lobby_close(lobby: UUID):
    lobby = Lobby.get(id=lobby)
    if not lobby:
        return jsonify({"error": "Lobby not found"}), 404

    if lobby.owner != session["_id"]:
        return jsonify({"error": "Only the lobby owner can close the lobby"}), 403

    if lobby.state == LOBBY_CLOSED:
        return jsonify({"error": "Lobby is already closed"}), 400

    lobby.state = LOBBY_CLOSED
    LobbyMessage(
        lobby=lobby, player=None, sender_name="System",
        content="The lobby was closed by the host.",
    )
    commit()

    return jsonify({"success": True})
