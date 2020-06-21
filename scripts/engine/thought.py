from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.component import Position
from scripts.engine.core.constants import ProjectileExpiry, BASE_MOVE_COST
from scripts.engine.core.definitions import ProjectileData
from scripts.nqp.actions.skills import Move

if TYPE_CHECKING:
    pass


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
        position = world.get_entitys_component(entity, Position)
        tile = world.get_tile((position.x, position.y))

        # if we havent travelled max distance then move
        if self.distance_travelled < self.data.range:
            if tile:
                if world.pay_resource_cost(entity, Move.resource_type, Move.resource_cost):
                    if world.use_skill(entity, Move, tile, self.data.direction):
                        self.distance_travelled += 1
                        world.end_turn(entity, self.data.speed)

                    # movement blocked
                    # FIXME - handle Terrain collisions

        else:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                if tile:
                    if world.pay_resource_cost(entity, Move.resource_type, Move.resource_cost):
                        skill = world.get_known_skill(entity, self.data.skill_name)
                        world.use_skill(entity, skill, tile, self.data.direction)

            # at max range, kill regardless
            world.kill_entity(entity)


class SkipTurn(AIBehaviour):
    """
    Just skips turn
    """
    def __init__(self, attached_entity: int):
        self.entity = attached_entity

    def act(self):
        name = world.get_name(self.entity)
        logging.debug(f"'{name}' skipped their turn.")
        world.end_turn(self.entity, BASE_MOVE_COST)
