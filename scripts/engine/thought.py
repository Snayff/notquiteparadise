from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.component import Position
from scripts.engine.core.constants import ProjectileExpiry, BASE_MOVE_COST, TargetTag, TerrainCollision
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
        # flags
        activate = False

        # get info we definitely need
        entity = self.entity
        position = world.get_entitys_component(entity, Position)
        tile = world.get_tile((position.x, position.y))

        # if we havent travelled max distance then move
        if self.distance_travelled < self.data.range and tile:
            # can move
            if world.can_use_skill(entity, "move"):
                activate = True
                skill = Move

            # cant move
            else:
                # blocked by terrain
                if world.tile_has_tag(tile, TargetTag.NO_ENTITY):
                    # handle terrain collision
                    collision = self.data.terrain_collision

                    if collision == TerrainCollision.ACTIVATE:
                        activate = True
                        skill = world.get_known_skill(entity, self.data.skill_name)

                    elif collision == TerrainCollision.FIZZLE:
                        # get rid of projectile
                        world.kill_entity(entity)
                        activate = False

                    elif collision == TerrainCollision.REFLECT:
                        # change direction and move
                        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
                        new_dir = world.get_reflected_direction((tile.x, tile.y), (tile.x + dir_x, tile.y + dir_y))
                        self.data.direction = new_dir
                        activate = True
                        skill = Move

                # blocked by entity
                elif world.tile_has_tag(tile, TargetTag.OTHER_ENTITY, entity):
                    activate = True

        elif self.distance_travelled >= self.data.range:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                activate = True
                skill = world.get_known_skill(entity, self.data.skill_name)
            else:
                # at max range so kill
                world.kill_entity(entity)

        if activate:
            if world.can_use_skill(entity, skill.name):
                world.use_skill(entity, skill, tile, self.data.direction)
                world.pay_resource_cost(entity, skill.resource_type, skill.resource_cost)

                # resolve post activation
                if skill.name == "move":
                    self.distance_travelled += 1
                    world.end_turn(entity, self.data.speed)
                else:
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
