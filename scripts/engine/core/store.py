from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from scripts.engine.core.constants import GameStates

if TYPE_CHECKING:
    pass

class Store:
    """
    Hold the current state info required by the engine
    """
    def __init__(self):
        self.current_game_state: GameStates = GameStates.GAME_INITIALISING
        self.previous_game_state: GameStates = GameStates.GAME_INITIALISING
        self.internal_clock = pygame.time.Clock()
        self.active_skill = None


store = Store()