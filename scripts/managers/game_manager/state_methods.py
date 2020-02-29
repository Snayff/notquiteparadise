from __future__ import annotations

import pygame
import logging
from typing import TYPE_CHECKING
from scripts.core.constants import GameStates, VisualInfo

if TYPE_CHECKING:
    from scripts.managers.game_manager.game_manager import GameManager


class StateMethods:
    """
    Methods for taking actions with the state of the game
    """

    def __init__(self, manager):
        self._manager: GameManager = manager
        self._current_game_state: GameStates = GameStates.GAME_INITIALISING
        self._previous_game_state: GameStates = GameStates.GAME_INITIALISING
        self._internal_clock = pygame.time.Clock()
        self._active_skill = None

    ################### GET ##############################

    def get_current(self) -> GameStates:
        """
        Get the current game state
        """
        return self._current_game_state

    def get_previous(self) -> GameStates:
        """
        Get the previous game state
        """
        return self._previous_game_state

    def get_internal_clock(self):
        """
        Get the internal clock
        """
        return self._internal_clock

    def get_active_skill(self):
        """
        Get the active skill. Used for targeting mode.
        """
        return self._active_skill

    def get_delta_time(self) -> int:
        """
        get delta time and set frame rate with .tick()
        """
        return self._internal_clock.tick(VisualInfo.GAME_FPS) / 1000.0

    ################### SET ##############################

    def set_active_skill(self, skill):
        """
        Set the active skill. Used for targeting mode.
        """
        self._active_skill = skill

    ################### MANAGING STATE ###################

    def update_clock(self):
        """
        Tick the internal clock. Manages the frame rate.
        """
        # set frame rate
        self._internal_clock.tick(VisualInfo.GAME_FPS)

    def set(self, new_game_state):
        """
        Set the current game state
        """
        self._previous_game_state = self._current_game_state
        self._current_game_state = new_game_state

        log_string = f"Game_state updated from {self._previous_game_state} to {self._current_game_state}"
        logging.debug(log_string)