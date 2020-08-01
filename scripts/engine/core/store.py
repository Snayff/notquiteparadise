from __future__ import annotations

import logging

import pygame

from typing import Any, Optional, TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine.core.constants import GameState, GameStateType
from scripts.engine.world_objects.gamemap import GameMap

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Dict


class _Store:
    """
    Hold the current state info required by the engine. Must be serialised.
    Should only be accessed via getters and setters, not directly.
    """
    def __init__(self):
        self.internal_clock = pygame.time.Clock()

        # used in state
        self.current_game_state: GameStateType = GameState.LOADING
        self.previous_game_state: GameStateType = GameState.LOADING
        self.active_skill = None

        # used in world
        self.current_gamemap: Optional[GameMap] = None

        # used in chronicle
        self.turn_queue: Dict[EntityID, int] = {}  # (entity, time)
        self.round: int = 1  # count of the round
        self.time: int = 1  # total time of actions taken
        self.time_of_last_turn: int = 1
        self.round_time: int = 0  # tracker of time progressed in current round
        self.turn_holder: EntityID = -1  # current acting entity
        
    def serialise(self) -> Dict[str, Any]:
        """
        Serialise all data held in the store.
        """
        _dict = {
            "current_game_state": self.current_game_state,
            "previous_game_state": self.previous_game_state,
            "current_gamemap": self.current_gamemap,
            "turn_queue": self.turn_queue,
            "round": self.round,
            "time": self.time,
            "time_of_last_turn": self.time_of_last_turn,
            "round_time": self.round_time,
            "turn_holder": self.turn_holder
        }
        return _dict

    def deserialise(self, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the store.
        """
        try:
            self.current_game_state = serialised["current_game_state"]
            self.previous_game_state = serialised["previous_game_state"]
            self.current_gamemap = serialised["current_gamemap"]
            self.turn_queue = serialised["turn_queue"]
            self.round = serialised["round"]
            self.time = serialised["time"]
            self.time_of_last_turn = serialised["time_of_last_turn"]
            self.round_time = serialised["round_time"]
            self.turn_holder = serialised["turn_holder"]
        except KeyError:
            logging.error(f"Store:Deserialise: Incorrect key given. Data not loaded correctly.")


store = _Store()
