from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from scripts.engine.core.constants import ProjectileTravelType, TargetTagType, ProjectileExpiryType, \
    ProjectileTerrainCollision, ShapeType
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


class JustMove(_AIBehaviour):
    """
    Move in direction, up to max_range (in tiles). Speed is time spent per tile moved.
    """
    def __init__(self, direction: Tuple[int, int], speed: int, travel_type: ProjectileTravelType, max_range: int,
         expiry_type: ProjectileExpiryType):
        self.expiry_type = expiry_type
        self.travel_type = travel_type
        self.direction = direction
        self.range = max_range
        self.speed = speed

    def act(self):
        pass
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