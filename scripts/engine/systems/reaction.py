from __future__ import annotations

import pygame

from scripts.engine import world
from scripts.engine.component import Position
from scripts.engine.core import queries
from scripts.engine.core.constants import GameEvent


__all__ = ["process_win_condition"]


def process_win_condition():
    """
    Process the win condition, checking if it has been met.
    """

    player = world.get_player()
    player_pos = world.get_entitys_component(player, Position)

    for entity, (position, _) in queries.position_and_win_condition:
        if player_pos.x == position.x and player_pos.y == position.y:
            event = pygame.event.Event(GameEvent.WIN_CONDITION_MET)
            pygame.event.post(event)
            break
