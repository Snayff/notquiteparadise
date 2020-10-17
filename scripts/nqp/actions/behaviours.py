from __future__ import annotations

import logging
import random
from typing import Tuple

from snecs.typedefs import EntityID

from scripts.engine import chronicle, library, world
from scripts.engine.action import Behaviour, Skill, init_action
from scripts.engine.component import Knowledge, Position
from scripts.engine.core.constants import ProjectileExpiry, TargetTag, TerrainCollision
from scripts.engine.core.definitions import ProjectileData
from scripts.engine.world_objects.tile import Tile


@init_action
class Projectile(Behaviour):
    """
    Move in direction, up to max_range (in tiles). Speed is time spent per tile moved.
    """

    def __init__(self, attached_entity: EntityID, data: ProjectileData):
        super().__init__(attached_entity)

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
        if self.distance_travelled == 0 and world.tile_has_tag(current_tile, TargetTag.OTHER_ENTITY, entity):
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
            move = world.get_known_skill(entity, "Move")
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

        return should_activate, should_move


@init_action
class SkipTurn(Behaviour):
    """
    Just skips turn
    """

    def act(self):
        name = world.get_name(self.entity)
        logging.debug(f"'{name}' skipped their turn.")
        chronicle.end_turn(self.entity, library.GAME_CONFIG.base_values.move_cost)


@init_action
class FollowPlayer(Behaviour):
    """
    Basic AI to follow the player
    """

    def act(self):
        entity = self.entity

        # get move direction
        player = world.get_player()
        move_dir = world.get_a_star_direction(entity, player)

        # get info for skill
        move = world.get_known_skill(entity, "Move")
        pos = world.get_entitys_component(entity, Position)
        target_tile = world.get_tile((pos.x, pos.y))
        name = world.get_name(entity)

        # attempt to use skill
        if world.can_use_skill(entity, "Move"):
            world.use_skill(entity, move, target_tile, move_dir)
            logging.debug(f"'{name}' moved to ({pos.x},{pos.y}).")
        else:
            logging.debug(f"'{name}' tried to move to ({pos.x},{pos.y}), but couldn`t.")

        chronicle.end_turn(entity, library.GAME_CONFIG.base_values.move_cost)


@init_action
class HuntPlayer(Behaviour):
    """
    Search and attack the player
    """

    def act(self):
        entity = self.entity

        # get distance
        player = world.get_player()
        player_pos = world.get_entitys_component(player, Position)
        pos = world.get_entitys_component(entity, Position)
        distance_to_player = world.get_chebyshev_distance((pos.x, pos.y), (player_pos.x, player_pos.y))

        # are we in range to attack?
        possible_skills = []
        knowledge = world.get_entitys_component(entity, Knowledge)
        for skill in knowledge.skills.values():
            in_range = skill.range >= distance_to_player
            not_move = skill.name != "Move"
            not_adjacent = distance_to_player > 1
            can_use = world.can_use_skill(entity, skill.name)
            if in_range and can_use and (not_move or not_adjacent):
                print(f"Can use skill; distance_to_player={distance_to_player} | skill_range={skill.range} | "
                      f"adjacent={not not_adjacent}")
                possible_skills.append(skill)

        # get direction
        skill_dir = world.get_a_star_direction(entity, player)

        # get skill info to move or attack
        if possible_skills:
            # pick a skill at random
            skill = random.choice(possible_skills)
            target_tile = world.get_tile((pos.x + skill_dir[0], pos.y + skill_dir[1]))
        else:
            skill = world.get_known_skill(entity, "Move")
            target_tile = world.get_tile((pos.x, pos.y))  # target tile is self as we need to move self

        # attempt to use skill
        name = world.get_name(entity)
        if world.can_use_skill(entity, skill.name):
            world.use_skill(entity, skill, target_tile, skill_dir)
        else:
            logging.debug(f"'{name}' tried to use {skill.f_name} from ({pos.x},{pos.y}) to ({target_tile.x}"
                          f",{target_tile.y}) but couldn`t.")

        chronicle.end_turn(entity, library.GAME_CONFIG.base_values.move_cost)

