
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

    def use(self, target_pos):
        """
        Use the skill

        Args:
            target_pos (tuple): x y of the target
        """
        from scripts.global_singletons.managers import world_manager
        skill_data = library.get_skill_data(self.skill_tree_name, self.name)

        target_x, target_y = target_pos
        effected_tile = world_manager.Map.get_tile(target_x, target_y)

        # apply any effects
        for effect_name, effect_data in skill_data.effects.items():
            effect = world_manager.Skill.create_skill_effect(self, effect_data.effect_type)
            effect.trigger(effected_tile)

        # end the turn
        publisher.publish(EndTurnEvent(skill_data.time_cost))




