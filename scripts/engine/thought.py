from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Tuple

from snecs.typedefs import EntityID

from scripts.engine import chronicle, library, world
from scripts.engine.action import Skill
from scripts.engine.component import Position
from scripts.engine.core.constants import ProjectileExpiry, TargetTag, TerrainCollision
from scripts.engine.core.definitions import ProjectileData
from scripts.engine.world_objects.tile import Tile

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
        should_activate = should_move = False

        # get info we definitely need
        entity = self.entity
        position = world.get_entitys_component(entity, Position)
        current_tile = world.get_tile((position.x, position.y))
        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
        target_tile = world.get_tile((current_tile.x + dir_x, current_tile.y + dir_y))

        # if we havent moved check for collision in current tile (it might be cast on top of enemy)
        if self.distance_travelled == 0:
            if world.tile_has_tag(current_tile, TargetTag.OTHER_ENTITY, entity):
                should_activate = True

        # if we havent travelled max distance or determined we should activate then move
        # N.b. not an elif because we want the precheck above to happen in isolation
        if self.distance_travelled < self.data.range and not should_activate:
            # can we move
            if world.tile_has_tag(target_tile, TargetTag.OPEN_SPACE):
                should_move = True

            else:
                should_activate, should_move = self._handle_collision(current_tile, target_tile)

        elif self.distance_travelled >= self.data.range:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                should_activate = True

                # update skill instance to new target
                self.data.skill_instance.target_tile = current_tile

            else:
                # at max range and not activating so kill attached entity
                world.kill_entity(entity)

        if should_activate:
            world.apply_skill(self.data.skill_instance)

            # die after activating
            world.kill_entity(entity)

        elif should_move:
            move = world.get_known_skill(entity, "move")
            move_cast = move(entity, self.data.skill_instance.target_tile, self.data.direction)
            world.apply_skill(move_cast)

            self.distance_travelled += 1
            chronicle.end_turn(entity, self.data.speed)

    def _handle_collision(self, current_tile: Tile, target_tile: Tile) -> Tuple[bool, bool]:
        """
        Handle collisions, returning should_activate, should_move and updating target tile and direction if needed
        """
        should_activate = should_move = False

        if world.tile_has_tags(target_tile, [TargetTag.BLOCKED_MOVEMENT, TargetTag.NO_ENTITY]):
            collision_type = self.data.terrain_collision

            if collision_type == TerrainCollision.ACTIVATE:
                should_activate = True

                # update skill instance to new target
                assert isinstance(self.data.skill_instance, Skill)
                self.data.skill_instance.target_tile = target_tile

            elif collision_type == TerrainCollision.FIZZLE:
                # get rid of projectile
                world.kill_entity(self.entity)

            elif collision_type == TerrainCollision.REFLECT:
                should_move = True

                # change direction and move
                new_dir = world.get_reflected_direction(
                    (current_tile.x, current_tile.y), (target_tile.x, target_tile.y)
                )
                self.data.direction = new_dir

        # blocked by entity
        elif world.tile_has_tag(target_tile, TargetTag.OTHER_ENTITY, self.entity):
            should_activate = True

            # update skill instance to new target
            assert isinstance(self.data.skill_instance, Skill)
            self.data.skill_instance.target_tile = target_tile

        # return outcomes
        return should_activate, should_move


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
