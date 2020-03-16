from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from scripts.engine.core.constants import TravelMethodType, TargetTagType, ProjectileExpiryType, \
    TerrainCollision, ShapeType, ProjectileExpiry
from scripts.engine.core.event_core import publisher
from scripts.engine.event import MoveEvent, DieEvent, ExpireEvent
from scripts.engine.library import library

if TYPE_CHECKING:
    from typing import Type, Union, Optional, Any, Tuple, Dict, List


class _AIBehaviour(ABC):
    """
    Base class for AI behaviours.
    """
    @abstractmethod
    def act(self):
        """
        Perform the behaviour
        """
        pass


class Projectile(_AIBehaviour):
    """
    Move in direction, up to max_range (in tiles). Speed is time spent per tile moved.
    """
    def __init__(self, ent: int, direction: Tuple[int, int], speed: int, travel_type: TravelMethodType,
            max_range: int, expiry_type: ProjectileExpiryType):
        self.entity = ent
        self.expiry_type = expiry_type
        self.travel_type = travel_type
        self.direction = direction
        self.max_range = max_range
        self.speed = speed
        self.distance_travelled = 0

    def act(self):
        # if we havent travelled max distance then move
        if self.distance_travelled < self.max_range:
            publisher.publish(MoveEvent(self.entity, (self.direction[0], self.direction[1]), self.travel_type,
                                        self.speed))
            self.distance_travelled += 1
        else:
            # we have reached the limit, process expiry and then die
            if self.expiry_type == ProjectileExpiry.ACTIVATE:
                publisher.publish(ExpireEvent(self.entity))
            publisher.publish(DieEvent(self.entity))

    # TODO -
    # move in direction 1 tile, pay speed/time cost
    # rename  interaction cause to trigger
    # change terrain collision (everywhere) to an interaction/InteractionData
    # ? standardise effects to use interactions. interaction cause can be collision
    #   that would prevent any issues with multiple effects in same dict
    #   but doesn't solve wanting multiple of same effect from same cause e.g. damage types
    # introduce death interaction trigger
    # expiry to trigger interaction
    # implement robust way of checking interactions