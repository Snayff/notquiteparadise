
import pygame

from scripts.core.constants import SkillEffectTypes
from scripts.events.game_events import EndTurnEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill_effects.apply_affliction import ApplyAfflictionSkillEffect
from scripts.skills.skill_effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.skill_effects.damage import DamageSkillEffect


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
        required_target = skill_data.required_target_type

        target = world_manager.Skill.get_target(target_pos, required_target)  # get the tile or entity

        # apply any skill_effects
        for effect_name, effect_data in skill_data.skill_effects.items():
            effect = world_manager.Skill.create_skill_effect(self, effect_data.effect_type)
            effect.trigger(target)

        # end the turn
        publisher.publish(EndTurnEvent(skill_data.time_cost))




