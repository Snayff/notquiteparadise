
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

        data = library.get_skill_data(skill_tree_name, skill_name)

        # skill_effects info
        effects = data.skill_effects  # list of skill_effects to process
        self.effects = []

        for effect in effects:
            from scripts.global_singletons.managers import world_manager
            created_effect = world_manager.Skill.create_skill_effect(self, effect["name"])

            # if we have an effect add it to internal list
            if created_effect:
                self.effects.append(created_effect)

    def use(self, target_pos):
        """
        Use the skill

        Args:
            target_pos (tuple): x y of the target
        """
        entity = self.owner.owner  # owner is actor, actor`s owner is entity
        from scripts.global_singletons.managers import world_manager
        skill_data = library.get_skill_data(self.skill_tree_name, self.name)
        required_target = world_manager.Skill.get_target_type_from_string(skill_data.required_target_type)

        target = world_manager.Skill.get_target(target_pos, required_target)  # get the tile or entity

        # apply any skill_effects
        if self.effects:
            for effect in self.effects:
                if effect.name is SkillEffectTypes.DAMAGE:
                    effect.trigger(entity, target)

                elif effect.name is SkillEffectTypes.MOVE:
                    effect.trigger(entity, target)

                elif effect.name is SkillEffectTypes.APPLY_AFFLICTION:
                    effect.trigger(entity, target)

                elif effect.name is SkillEffectTypes.CHANGE_TERRAIN:
                    effect.trigger(target)
        # end the turn
        publisher.publish(EndTurnEvent(skill_data.time_cost))




