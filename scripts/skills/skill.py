import logging

from scripts.core.constants import SkillExpiryTypes, Directions, SkillTravelTypes, TargetTags, \
    SkillTerrainCollisions
from scripts.events.game_events import EndTurnEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher


class Skill:
    """
    A skill to be used by an actor

    Attributes:
            name(str):
            owner():
            skill_tree_name():
    """

    def __init__(self, owner, skill_tree_name, skill_name):
        self.owner = owner
        self.skill_tree_name = skill_tree_name
        self.name = skill_name

    def use(self, target_direction):
        """
        Use the skill

        Args:
            target_direction (tuple): x y of the target direction
        """
        from scripts.managers.world_manager import world
        data = library.get_skill_data(self.skill_tree_name, self.name)
        entity = self.owner.owner

        # initial values
        start_x = entity.x
        start_y = entity.y
        dir_x = abs(target_direction[0])  # abs to handle any mistaken values coming in
        dir_y = abs(target_direction[1])
        direction = (dir_x, dir_y)

        # flags
        activate = False
        found_target = False
        check_for_target = False

        logging.info(f"{entity.name} used {self.name} at ({start_x},{start_y}) in {Directions(direction)}...")

        # determine impact location N.B. +1 to make inclusive
        for distance in range(1, data.range + 1):
            current_x = start_x + (dir_x * distance)
            current_y = start_y + (dir_y * distance)
            tile = world.Map.get_tile(current_x, current_y)

            # did we hit terrain?
            if world.Map.tile_has_tag(tile, TargetTags.WALL, entity):
                # do we need to activate, reflect or fizzle?
                if data.terrain_collision == SkillTerrainCollisions.ACTIVATE:
                    activate = True
                    logging.debug(f"-> and hit a wall. Skill will activate at ({current_x},{current_y}).")
                    break
                elif data.terrain_collision == SkillTerrainCollisions.REFLECT:
                    # work out position of adjacent walls
                    adj_tile = world.Map.get_tile(current_x, current_y - dir_y)
                    collision_adj_y = world.Map.tile_has_tag(adj_tile, TargetTags.WALL)
                    adj_tile = world.Map.get_tile(current_x - dir_x, current_y)
                    collision_adj_x = world.Map.tile_has_tag(adj_tile, TargetTags.WALL)

                    # where did we collide?
                    if collision_adj_x and collision_adj_y:
                        # hit a corner, bounce back towards entity
                        dir_x *= -1
                        dir_y *= -1
                    elif collision_adj_x and not collision_adj_y:
                        # hit horizontal wall, revere y direction
                        dir_y *= -1
                    elif not collision_adj_x and collision_adj_y:
                        # hit a vertical wall, reverse x direction
                        dir_x *= -1
                    elif not collision_adj_x and not collision_adj_y:
                        # hit a single piece, on the corner, bounce back towards entity
                        dir_x *= -1
                        dir_y *= -1

                    logging.info(f"-> and hit a wall. Skill`s direction changed to ({dir_x},{dir_y}).")
                elif data.terrain_collision == SkillTerrainCollisions.FIZZLE:
                    activate = False
                    logging.info(f"-> and hit a wall. Skill fizzled at ({current_x},{current_y}).")
                    break

            # determine travel method
            if data.travel_type == SkillTravelTypes.PROJECTILE:
                # projectile can hit a target at any point during travel
                check_for_target = True
            elif data.travel_type == SkillTravelTypes.THROW:
                # throw can only hit target at end of travel
                if distance == data.range:
                    check_for_target = True
                else:
                    check_for_target = False

            # did we hit something that has the tags we need?
            if check_for_target:
                for tag in data.required_tags:
                    if not world.Map.tile_has_tag(tile, tag, entity):
                        found_target = False
                        break
                    else:
                        found_target = True
                        logging.debug(f"-> and found suitable target at ({current_x},{current_y}).")

            # have we found a suitable target?
            if found_target:
                activate = True
                break

        # if at end of range and activate not triggered
        if distance >= data.range and not activate:
            if data.expiry_type == SkillExpiryTypes.FIZZLE:
                activate = False
                logging.info(f"-> and hit nothing. Skill fizzled at ({current_x},{current_y}).")
            elif data.expiry_type == SkillExpiryTypes.ACTIVATE:
                activate = True
                logging.debug(f"-> and hit nothing. Skill will activate at ({current_x},{current_y}).")

        # deal with activation
        if activate:
            coords = world.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world.Map.get_tiles(current_x, current_y, coords)

            # apply any effects
            for effect_name, effect_data in data.effects.items():
                effect = world.Skill.create_effect(self, effect_data.effect_type)
                effect.trigger(effected_tiles)

            # end the turn
            publisher.publish(EndTurnEvent(entity, data.time_cost))
