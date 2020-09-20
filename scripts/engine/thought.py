from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine import chronicle, library, world
from scripts.engine.component import Position
from scripts.engine.core.constants import ProjectileExpiry, TargetTag, TerrainCollision
from scripts.engine.core.definitions import ProjectileData

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
        current_tile = world.get_tile((position.x, position.y))
        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
        target_tile = world.get_tile((current_tile.x + dir_x, current_tile.y + dir_y))
        move = world.get_known_skill(entity, "Move")
        skill_instance = move(self.entity, target_tile, self.data.direction)

        # if we havent moved check for collision in current tile (it might be cast on top of enemy)
        if self.distance_travelled == 0 and current_tile:
            if world.tile_has_tag(current_tile, TargetTag.OTHER_ENTITY, entity):
                activate = True
                skill_instance = self.data.skill_instance
                # if we are in the same tile we don't want to apply the effect to ourselves
                skill_instance.ignore_entities.append(entity)
                # update skill instance to new target
                skill_instance.target_tile = current_tile

        # if we havent travelled max distance then move
        # N.b. not an elif because we want the precheck above to happen in isolation
        if self.distance_travelled < self.data.range and target_tile and not activate:
            # can move
            if world.tile_has_tag(target_tile, TargetTag.OPEN_SPACE):
                activate = True
                move = world.get_known_skill(entity, "Move")
                skill_instance = move(self.entity, target_tile, self.data.direction)

            # cant move
            else:
                # blocked by terrain
                if world.tile_has_tags(target_tile, [TargetTag.BLOCKED_MOVEMENT, TargetTag.NO_ENTITY]):
                    # handle terrain collision
                    collision_type = self.data.terrain_collision

                    if collision_type == TerrainCollision.ACTIVATE:
                        activate = True
                        skill_instance = self.data.skill_instance

                        # update skill instance to new target
                        skill_instance.target_tile = target_tile

                    elif collision_type == TerrainCollision.FIZZLE:
                        # get rid of projectile
                        world.kill_entity(entity)
                        activate = False

                    elif collision_type == TerrainCollision.REFLECT:
                        # change direction and move
                        new_dir = world.get_reflected_direction((current_tile.x, current_tile.y),
                                                                (target_tile.x, target_tile.y))
                        self.data.direction = new_dir
                        activate = True
                        move = world.get_known_skill(entity, "Move")
                        skill_instance = move(self.entity, target_tile, new_dir)

                # blocked by entity
                elif world.tile_has_tag(target_tile, TargetTag.OTHER_ENTITY, entity):
                    activate = True
                    skill_instance = self.data.skill_instance

                    # update skill instance to new target
                    skill_instance.target_tile = target_tile

        elif self.distance_travelled >= self.data.range:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                activate = True
                skill_instance = self.data.skill_instance

                # update skill instance to new target
                skill_instance.target_tile = current_tile

            else:
                # at max range so kill
                world.kill_entity(entity)

        if activate and skill_instance:
            # use the skill_instance
            world.apply_skill(skill_instance)
            world.pay_resource_cost(entity, skill_instance.resource_type, skill_instance.resource_cost)

            # resolve post activation
            if skill_instance.key == "move":
                self.distance_travelled += 1
                chronicle.end_turn(entity, self.data.speed)
            else:
                # die after activating
                world.kill_entity(entity)


class SkipTurnBehaviour(AIBehaviour):
    """
    Just skips turn
    """
    def __init__(self, attached_entity: int):
        self.entity = attached_entity

    def act(self):
        name = world.get_name(self.entity)
        logging.debug(f"'{name}' skipped their turn.")
        chronicle.end_turn(self.entity, library.GAME_CONFIG.base_values.move_cost)
