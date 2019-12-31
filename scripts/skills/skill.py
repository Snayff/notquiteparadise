
from scripts.events.game_events import EndTurnEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.managers.world_manager import world


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
        data = library.get_skill_data(self.skill_tree_name, self.name)

        # initial values
        start_x = self.owner.x
        start_y = self.owner.y
        dir_x = target_direction[0]
        dir_y = target_direction[1]

        # determine travel method
        
        # determine impact location
        for distance in range(1, data.range):

            current_x = start_x + (dir_x * distance)
            current_y = start_y + (dir_y * distance)
            tile = world.Map.get_tile(current_x, current_y)

            # did we hit something?

        # determine what happens on impact

        # deal with impact


        target_x, target_y = target_pos

        coords = world.Skill.create_shape(data.shape, data.shape_size)
        effected_tiles = world.Map.get_tiles(target_x, target_y, coords)

        # apply any effects
        for effect_name, effect_data in data.effects.items():
            effect = world.Skill.create_effect(self, effect_data.effect_type)
            effect.trigger(effected_tiles)

        # end the turn
        entity = self.owner.owner
        publisher.publish(EndTurnEvent(entity, data.time_cost))




