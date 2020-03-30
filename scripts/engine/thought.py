from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from snecs.typedefs import EntityID


from scripts.engine import utility
from scripts.engine.component import Position
from scripts.engine.core.constants import ProjectileExpiry, MessageType, BASE_MOVE_COST
from scripts.engine.core.definitions import ProjectileData
from scripts.engine.core.event_core import publisher
from scripts.engine.event import MoveEvent, DieEvent, ExpireEvent, MessageEvent, EndTurnEvent

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class AIBehaviour(ABC):
    """
    Base class for AI behaviours.
    """
    @abstractmethod
    def act(self):
        """
        Perform the behaviour
        """
        pass


class ProjectileBehaviour(AIBehaviour):
    """
    Move in direction, up to max_range (in tiles). Speed is time spent per tile moved.
    """
    def __init__(self, attached_entity: EntityID, data: ProjectileData):
        self.entity = attached_entity  # the entity this component is attached too
        self.data = data
        self.distance_travelled = 0

    def act(self):
        entity = self.entity

        # if we havent travelled max distance then move
        if self.distance_travelled < self.data.range:
            position = world.get_entitys_component(entity, Position)
            publisher.publish(MoveEvent(entity, (position.x, position.y),
                                        (self.data.direction[0], self.data.direction[1]),
                                        self.data.travel_type, self.data.speed))
            self.distance_travelled += 1
        else:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                publisher.publish(ExpireEvent(entity))
            publisher.publish(DieEvent(entity))


class SkipTurn(AIBehaviour):
    """
    Just skips turn
    """
    def __init__(self, attached_entity: int):
        self.entity = attached_entity

    def act(self):
        name = world.get_name(self.entity)
        logging.debug(f"'{name}' skipped their turn.")
        publisher.publish((EndTurnEvent(self.entity, BASE_MOVE_COST)))