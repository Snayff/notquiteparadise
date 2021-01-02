from __future__ import annotations

import logging
import random

from scripts.engine.core import chronicle, world
from scripts.engine.internal import library
from scripts.engine.internal.action import Behaviour
from scripts.engine.internal.component import Knowledge, Position
from scripts.engine.internal.constant import Direction, TargetTag


class SkipTurn(Behaviour):
    """
    Just skips turn
    """

    def act(self):
        name = world.get_name(self.entity)
        logging.debug(f"'{name}' skipped their turn.")
        chronicle.end_turn(self.entity, library.GAME_CONFIG.base_values.move_cost)


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


class SearchAndAttack(Behaviour):
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
