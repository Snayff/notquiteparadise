from __future__ import annotations

import pygame
from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core.constants import GameState, GameStateType

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Dict, Tuple


class _Store:
    """
    Hold the current state info required by the engine.
    Should only be accessed via getters and setters, not directly.
    """
    def __init__(self):
        # used in state
        self.current_game_state: GameStateType = GameState.LOADING
        self.previous_game_state: GameStateType = GameState.LOADING
        self.internal_clock = pygame.time.Clock()
        self.active_skill = None

        # used in world
        self.current_gamemap = None

        # used in chrono
        self.turn_queue: Dict[EntityID, int] = {}  # (entity, time)
        self.round: int = 1  # count of the round
        self.time: int = 1  # total time of actions taken
        self.time_of_last_turn: int = 1
        self.round_time: int = 0  # tracker of time progressed in current round
        self.turn_holder: int = -1  # current acting entity


store = _Store()