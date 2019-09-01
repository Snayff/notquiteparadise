
import pygame

from scripts.core.constants import EffectTypes
from scripts.events.game_events import EndTurnEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.effects.apply_affliction import ApplyAfflictionEffect
from scripts.skills.effects.change_terrain import ChangeTerrainEffect
from scripts.skills.effects.damage import DamageEffect


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

        # TODO - add cooldown

    def use(self, target_pos):
        """
        Use the skill

        Args:
            target_pos (tuple): x y of the target
        """
        from scripts.global_singletons.managers import world_manager
        data = library.get_skill_data(self.skill_tree_name, self.name)

        target_x, target_y = target_pos

        coords = world_manager.Skill.create_shape(data.shape, data.shape_size)
        effected_tiles = world_manager.Map.get_tiles(target_x, target_y, coords)

        # apply any effects
        for effect_name, effect_data in data.effects.items():
            effect = world_manager.Skill.create_effect(self, effect_data.effect_type)
            effect.trigger(effected_tiles)

        # end the turn
        publisher.publish(EndTurnEvent(data.time_cost))




