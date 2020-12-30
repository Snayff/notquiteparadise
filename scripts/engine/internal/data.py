from __future__ import annotations

import logging
import os
from typing import List, TYPE_CHECKING

import pygame
from snecs.typedefs import EntityID

from scripts.engine.internal.action import Affliction, Behaviour, Skill
from scripts.engine.internal.constant import GameState

if TYPE_CHECKING:
    from typing import Any, Dict, Optional, Type

    from scripts.engine.world_objects.game_map import GameMap

__all__ = ["store"]


class Store:
    """
    Hold the current state info required by the engine. Must be serialised.
    Should only be accessed via getters and setters, not directly.
    """

    def __init__(self):
        self.internal_clock = pygame.time.Clock()

        # used in state
        self.current_game_state: GameState = GameState.LOADING
        self.previous_game_state: GameState = GameState.LOADING
        self.active_skill = None

        # used in world
        self.current_game_map: Optional[GameMap] = None

        # used in chronicle
        self.turn_queue: Dict[EntityID, int] = {}  # (entity, time)
        self.round: int = 1  # count of the round
        self.time: int = 1  # total time of actions taken
        self.time_of_last_turn: int = 1
        self.round_time: int = 0  # tracker of time progressed in current round
        self.turn_holder: EntityID = -1  # current acting entity
        self.previous_turn_holder: EntityID = -1  # current acting entity

        ################### NOT SERIALISED #######################################

        # used to hold images called during runtime so only one copy ever exists.
        self.images: Dict[str, pygame.Surface] = {}

        # used to hold actions registered with the engine.
        self.skill_registry: Dict[str, Type[Skill]] = {}
        self.affliction_registry: Dict[str, Type[Affliction]] = {}
        self.behaviour_registry: Dict[str, Type[Behaviour]] = {}

        self.message_log: List[str] = []

    def serialise(self) -> Dict[str, Any]:
        """
        Serialise all data held in the store.
        """
        if self.current_game_map:
            game_map = self.current_game_map.serialise()
        else:
            game_map = {}

        _dict = {
            "current_game_state": self.current_game_state,
            "previous_game_state": self.previous_game_state,
            "current_game_map": game_map,
            "turn_queue": self.turn_queue,
            "round": self.round,
            "time": self.time,
            "time_of_last_turn": self.time_of_last_turn,
            "round_time": self.round_time,
            "turn_holder": self.turn_holder,
        }
        return _dict

    def deserialise(self, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the store.
        """
        try:
            self.current_game_state = serialised["current_game_state"]
            self.previous_game_state = serialised["previous_game_state"]
            from scripts.engine.world_objects.game_map import GameMap

            self.current_game_map = GameMap.deserialise(serialised["current_game_map"])
            self.turn_queue = serialised["turn_queue"]
            self.round = serialised["round"]
            self.time = serialised["time"]
            self.time_of_last_turn = serialised["time_of_last_turn"]
            self.round_time = serialised["round_time"]
            self.turn_holder = serialised["turn_holder"]
        except KeyError as e:
            logging.warning(f"Store.Deserialise: Incorrect key ({e.args[0]}) given. Data not loaded correctly.")

    def log_message(self, message: str):
        """
        Add a message to the log.
        """
        self.message_log.append(message)


if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    store = Store()
else:
    store = None  # type: ignore
