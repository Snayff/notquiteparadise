from __future__ import annotations

import logging
import random
from typing import Tuple

from snecs.typedefs import EntityID

from scripts.engine import chronicle, library, world
from scripts.engine.action import Behaviour, init_action, Skill
from scripts.engine.component import Knowledge, Position
from scripts.engine.core.constants import Direction, ProjectileExpiry, TargetTag, TerrainCollision
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
        should_activate = False
        should_move = False

        # get info we definitely need
        entity = self.entity
        pos = world.get_entitys_component(entity, Position)
        current_tile = world.get_tile((pos.x, pos.y))
        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
        target_tile = world.get_tile((current_tile.x + dir_x, current_tile.y + dir_y))

        # if we havent moved check for collision in current tile (it might be cast on top of enemy)
        if self.distance_travelled == 0 and world.tile_has_tag(entity, current_tile, TargetTag.OTHER_ENTITY):
            should_activate = True
            logging.debug(f"'{world.get_name(entity)}' collided with an entity on cast at" f"({pos.x},{pos.y}).")

        # if we havent travelled max distance or determined we should activate then move
        # N.b. not an elif because we want the precheck above to happen in isolation
        if self.distance_travelled < self.data.range and not should_activate:
            # can we move
            if world.tile_has_tag(entity, target_tile, TargetTag.OPEN_SPACE):
                should_move = True

            else:
                should_activate, should_move = self._handle_collision(current_tile, target_tile)

        elif self.distance_travelled >= self.data.range:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                should_activate = True

                # update skill instance to point to current position, for when it is applied
                self.data.skill_instance.target_tile = current_tile

            else:
                # at max range and not activating so kill attached entity
                world.kill_entity(entity)

        if should_activate:
            logging.debug(f"'{world.get_name(entity)}' is going to activate at ({pos.x},{pos.y}).")

            # apply skill, rather than using it, as the instance already exists and we are just using the effects
            world.apply_skill(self.data.skill_instance)

            # die after activating
            world.kill_entity(entity)

        elif should_move:
            logging.debug(
                f"'{world.get_name(entity)}' has {self.data.range - self.distance_travelled} range left and"
                f" is going to move from ({pos.x},{pos.y}) to "
                f"({pos.x + dir_x},{pos.y + dir_y})."
            )

            move = world.get_known_skill(entity, "Move")
            world.use_skill(entity, move, current_tile, self.data.direction)

            self.distance_travelled += 1
            chronicle.end_turn(entity, self.data.speed)

    def _handle_collision(self, current_tile: Tile, target_tile: Tile) -> Tuple[bool, bool]:
        """
        Handle collisions, returning should_activate, should_move and updating target tile and direction if needed
        """
        should_activate = should_move = False

        if world.tile_has_tags(self.entity, target_tile, [TargetTag.BLOCKED_MOVEMENT, TargetTag.NO_ENTITY]):
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
                    self.entity, (current_tile.x, current_tile.y), (target_tile.x, target_tile.y)
                )
                self.data.direction = new_dir

        # blocked by entity
        elif world.tile_has_tag(self.entity, target_tile, TargetTag.OTHER_ENTITY):
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

        # get position info
        pos = world.get_entitys_component(entity, Position)
        player = world.get_player()
        player_pos = world.get_entitys_component(player, Position)

        # get move direction
        move_dir = world.get_a_star_direction((pos.x, pos.y), (player_pos.x, player_pos.y))

        # get info for skill
        move = world.get_known_skill(entity, "Move")
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
class Basic(Behaviour):
    """
    Search and attack the player
    """

    def act(self):
        entity = self.entity
        pos = world.get_entitys_component(entity, Position)
        target = world.choose_target(entity)

        # if we have no target move in random direction
        if not target:
            self._move_randomly()
            return  # exit

        target_pos = world.get_entitys_component(target, Position)

        # what skills are ready to use?
        possible_skills = []
        knowledge = world.get_entitys_component(entity, Knowledge)
        for skill in knowledge.skills.values():
            if world.can_use_skill(entity, skill.name) and skill.name != "Move":
                possible_skills.append(skill)

        # where can we cast from?
        skill_cast_positions = world.get_cast_positions(entity, target_pos, possible_skills)

        # are we currently on a cast position?
        skills_can_cast = []
        for skill, cast_positions in skill_cast_positions.items():
            if (pos.x, pos.y) in cast_positions:
                skills_can_cast.append(skill)

        # if we can cast a skill now then pick one at random and cast
        if skills_can_cast:
            # get target tile
            skill_dir = world.get_direction((pos.x, pos.y), (target_pos.x, target_pos.y))
            target_tile = world.get_tile((pos.x + skill_dir[0], pos.y + skill_dir[1]))

            # set skill to cast
            skill_to_cast = random.choice(skills_can_cast)

            # cast whatever skill has been chosen
            world.use_skill(entity, skill_to_cast, target_tile, skill_dir)

            logging.debug(
                f"'{world.get_name(entity)}' cast {skill_to_cast.name} from ({pos.x},"
                f"{pos.y}) towards ({pos.x + skill_dir[0]},{pos.y + skill_dir[1]}), with range "
                f"{skill_to_cast.range}."
            )

            # end turn
            chronicle.end_turn(entity, skill_to_cast.time_cost)

        # we cant cast, find nearest cast_position
        else:
            # add all possible positions to pathfinder
            pathfinder = world.create_pathfinder()
            for cast_positions in skill_cast_positions.values():
                for cast_pos in cast_positions:
                    pathfinder.add_root(cast_pos)

            # get nearest location
            path = pathfinder.path_from((pos.x, pos.y))[1:].tolist()  # slice out starting pos
            assert isinstance(path, list)

            # check is path has any value - there might not have been any valid cast positions
            if path:
                nearest_pos = path[0]

                # get target tile
                skill_dir = world.get_a_star_direction((pos.x, pos.y), (nearest_pos[0], nearest_pos[1]))
                target_tile = world.get_tile((pos.x, pos.y))  # target tile for Move is current pos

                # set skill to cast to move
                skill_to_cast = knowledge.skills["Move"]

                # cast whatever skill has been chosen
                world.use_skill(entity, skill_to_cast, target_tile, skill_dir)

                logging.debug(
                    f"'{world.get_name(entity)}' moved towards a cast position, from ({pos.x},"
                    f"{pos.y}) to ({pos.x + skill_dir[0]},{pos.y + skill_dir[1]})."
                )

                # end turn
                chronicle.end_turn(entity, skill_to_cast.time_cost)
            else:
                # no valid cast position, just wander
                self._move_randomly()

    def _move_randomly(self):
        """
        Move self in random direction. End turn, whether moved or not.
        """
        entity = self.entity
        pos = world.get_entitys_component(entity, Position)
        knowledge = world.get_entitys_component(entity, Knowledge)
        move = knowledge.skills["Move"]
        cardinals = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

        # check spaces are free
        poss_directions = []
        for _dir in cardinals:
            x = pos.x + _dir[0]
            y = pos.y + _dir[1]

            tile = world.get_tile((x, y))
            has_tags = world.tile_has_tag(entity, tile, TargetTag.OPEN_SPACE)
            if has_tags:
                poss_directions.append((_dir[0], _dir[1]))

        # if any space we can move to, do so
        if poss_directions:
            move_dir = random.choice(poss_directions)
            target_tile = world.get_tile((pos.x, pos.y))  # target tile for Move is current pos

            world.use_skill(entity, move, target_tile, move_dir)

            logging.debug(
                f"'{world.get_name(entity)}' couldnt see a target so moved randomly from ({pos.x},"
                f"{pos.y}) to ({pos.x + move_dir[0]},{pos.y + move_dir[1]})."
            )

        chronicle.end_turn(entity, move.time_cost)
