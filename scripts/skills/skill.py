import logging

from scripts.core.constants import SkillExpiryTypes, MessageEventTypes, Directions, SkillTravelTypes
from scripts.events.game_events import EndTurnEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.events.message_events import MessageEvent


class Skill:
    """
    A skill to be used by an actor

    Attributes:
            name(str):
            owner():
            skill_tree_name():
    """
    def __init__(self, owner,  skill_tree_name, skill_name):
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
        dir_x = target_direction[0]
        dir_y = target_direction[1]
        direction = (dir_x, dir_y)
        step = 1

        # flags
        activate = False
        found_target = False

        logging.info(f"{entity.name} used {self.name} at ({start_x},{start_y}) in {Directions(direction)}...")

        # determine travel method
        if data.travel_type == SkillTravelTypes.PROJECTILE:
            step = 1
        elif data.travel_type == SkillTravelTypes.THROW:
            step = data.range  # TODO - handle bounce

        # determine impact location N.B. +1 to make inclusive
        for distance in range(1, data.range + 1, step):
            current_x = start_x + (dir_x * distance)
            current_y = start_y + (dir_y * distance)
            tile = world.Map.get_tile(current_x, current_y)

            # if at end of range
            if distance == data.range:
                if data.expiry_type == SkillExpiryTypes.FIZZLE:
                    activate = False
                    logging.info(f"-> and hit nothing. Skill fizzled at ({current_x},{current_y}).")
                elif data.expiry_type == SkillExpiryTypes.ACTIVATE:
                    activate = True
                    logging.info(f"-> and hit nothing. Skill will activate at ({current_x},{current_y}).")
                    break

            # did we hit something that has the tags we need?
            for tag in data.required_tags:
                if not world.Map.tile_has_tag(tile, tag, entity):
                    found_target = False
                    break
                else:
                    found_target = True
                    logging.info(f"-> and found suitable target at ({current_x},{current_y}).")

            # have we found a suitable target?
            if found_target:
                activate = True
                break

        # deal with impact
        if activate:
            coords = world.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world.Map.get_tiles(current_x, current_y, coords)

            # apply any effects
            for effect_name, effect_data in data.effects.items():
                effect = world.Skill.create_effect(self, effect_data.effect_type)
                effect.trigger(effected_tiles)

            # end the turn
            publisher.publish(EndTurnEvent(entity, data.time_cost))




