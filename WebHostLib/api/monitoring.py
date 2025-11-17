"""Monitoring API endpoints for active rooms and games."""
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from uuid import UUID

from flask import jsonify, request, abort
from pony.orm import db_session, select

from Utils import restricted_loads
from WebHostLib import app, to_url
from ..models import Room, Slot

from . import api_endpoints


def require_admin_token():
    """Check if admin token is required and validate it from request."""
    admin_token = app.config.get("MONITORING_ADMIN_TOKEN")
    
    # Block endpoints if no token is configured
    if not admin_token:
        abort(503)
    
    # Check for token in Authorization header (Bearer token format)
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        abort(401)
    provided_token = auth_header[7:]
    if provided_token != admin_token:
        abort(401)


def is_room_active(room: Room) -> bool:
    """Check if a room is currently active (hasn't timed out and has a valid port)."""
    # Only consider rooms with a valid port (> 0)
    if not room.last_port or room.last_port <= 0:
        return False
    now = datetime.utcnow()
    time_since_activity = now - room.last_activity
    return time_since_activity <= timedelta(seconds=room.timeout + 5)


def get_per_game_last_activity(room: Room) -> Dict[str, Optional[float]]:
    """Get the most recent activity timestamp for each game in a room.
    Returns a dict mapping game name to the most recent activity timestamp (or None if no activity)."""
    game_activity: Dict[str, Optional[float]] = {}
    
    if not room.multisave:
        for slot in room.seed.slots:
            if slot.game not in game_activity:
                game_activity[slot.game] = None
        return game_activity
    
    try:
        multisave = restricted_loads(room.multisave)
        client_activity_timers = multisave.get("client_activity_timers", [])
        
        # Map player_id to game name (player_id in slots matches the player index in activity timers)
        player_to_game: Dict[int, str] = {}
        for slot in room.seed.slots:
            player_to_game[slot.player_id] = slot.game
            if slot.game not in game_activity:
                game_activity[slot.game] = None
        
        # client_activity_timers is stored as tuple of ((team, player), timestamp) pairs
        # Handle both tuple and list formats
        if isinstance(client_activity_timers, (tuple, list)):
            for entry in client_activity_timers:
                if isinstance(entry, (tuple, list)) and len(entry) == 2:
                    (team, player_id), timestamp = entry
                    game = player_to_game.get(player_id)
                    if game:
                        if game_activity[game] is None or timestamp > game_activity[game]:
                            game_activity[game] = timestamp
    except Exception:
        for slot in room.seed.slots:
            if slot.game not in game_activity:
                game_activity[slot.game] = None
    
    return game_activity


@api_endpoints.route('/monitoring/rooms')
def monitoring_rooms() -> Dict[str, Any]:
    """Get a list of all active rooms with port and last activity time."""
    require_admin_token()
    with db_session:
        now = datetime.utcnow()
        rooms = select(
            room for room in Room if
            room.last_activity >= now - timedelta(days=3)
        )
        
        active_rooms = []
        for room in rooms:
            if is_room_active(room):
                games = [slot.game for slot in room.seed.slots]
                game_activity = get_per_game_last_activity(room)
                games_with_activity = [
                    {
                        "game": game,
                        "last_activity_timestamp": activity if activity else None,
                    }
                    for game, activity in game_activity.items()
                ]
                
                active_rooms.append({
                    "room_id": str(room.id),
                    "room_id_short": to_url(room.id),
                    "port": room.last_port,
                    "last_activity": room.last_activity.isoformat(),
                    "last_activity_timestamp": room.last_activity.timestamp(),
                    "time_until_timeout": (room.timeout - (now - room.last_activity).total_seconds()),
                    "games": games,
                    "games_with_activity": games_with_activity,
                    "player_count": len(room.seed.slots),
                    "creation_time": room.creation_time.isoformat(),
                })
        
        return jsonify({
            "active_rooms": active_rooms,
            "total_active_rooms": len(active_rooms),
            "timestamp": now.isoformat(),
        })


@api_endpoints.route('/monitoring/games')
def monitoring_games() -> Dict[str, Any]:
    """Get a list of all games with port and time of last action."""
    require_admin_token()
    with db_session:
        now = datetime.utcnow()
        rooms = select(
            room for room in Room if
            room.last_activity >= now - timedelta(days=3)
        )

        games_dict: Dict[str, List[Dict[str, Any]]] = {}
        
        for room in rooms:
            if not is_room_active(room):
                continue

            game_activity = get_per_game_last_activity(room)
            
            for slot in room.seed.slots:
                game = slot.game
                if game not in games_dict:
                    games_dict[game] = []
                
                game_last_activity = game_activity.get(game)
                
                games_dict[game].append({
                    "room_id": str(room.id),
                    "room_id_short": to_url(room.id),
                    "port": room.last_port,
                    "last_activity": room.last_activity.isoformat(),
                    "last_activity_timestamp": room.last_activity.timestamp(),
                    "game_last_activity_timestamp": game_last_activity if game_last_activity else None,
                    "player_name": slot.player_name,
                    "player_id": slot.player_id,
                    "time_until_timeout": (room.timeout - (now - room.last_activity).total_seconds()),
                })
        
        games_list = [
            {
                "game": game,
                "active_instances": instances,
                "instance_count": len(instances),
            }
            for game, instances in sorted(games_dict.items())
        ]
        
        return jsonify({
            "games": games_list,
            "total_games": len(games_dict),
            "total_instances": sum(len(instances) for instances in games_dict.values()),
            "timestamp": now.isoformat(),
        })



