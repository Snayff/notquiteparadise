
import random

from scripts.core.constants import LoggingEventTypes, SecondaryStatTypes
from scripts.data_loaders.getters import get_value_from_afflictions_json
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.skill_effects.apply_affliction import ApplyAfflictionSkillEffect
from scripts.skills.skill_effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.skill_effects.damage import DamageSkillEffect
from scripts.skills.skill import Skill


class SkillAction:
    """
    Methods for taking actions with skills
    """
    def __init__(self, manager):
        self.manager = manager  # type: GameManager

    def create_damage_effect(self, skill, effect):
        """
        Create the damage effect object

        Args:
            skill (Skill): the skill that will contain this effect
            effect (dict): dict of effect values, from json

        Returns:
            DamageSkillEffect: The created effect object
        """
        query = self.manager.skill_query

        # get tags from skill_effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(query.get_target_tags_from_string(tag))

        target_type = query.get_target_type_from_string(effect["required_target_type"])
        damage_type = query.get_damage_type_from_string(effect["damage_type"])
        stat_to_target = query.get_secondary_stat_from_string(effect["stat_to_target"])

        # add effect object to skill
        created_effect = DamageSkillEffect(skill, target_type, target_tags, effect["damage"], damage_type,
                                           effect["accuracy"], stat_to_target)

        return created_effect

    def create_change_terrain_effect(self, skill, effect):
        """
        Create the change terrain effect object

        Args:
            skill (Skill): the skill that will contain this effect
            effect (dict): dict of effect values, from json

        Returns:
            ChangeTerrainSkillEffect: The created effect object
        """
        query = self.manager.skill_query

        # get tags from skill_effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(query.get_target_tags_from_string(tag))

        target_type = query.get_target_type_from_string(effect["required_target_type"])
        new_terrain = query.get_target_tags_from_string(effect["new_terrain"])

        # add effect object to skill
        created_effect = ChangeTerrainSkillEffect(skill, target_type, target_tags, new_terrain)

        return created_effect

    def create_apply_affliction_effect(self, skill, effect):
        """
        Create the apply affliction effect object

        Args:
            skill (Skill): the skill that will contain this effect
            effect (dict): dict of effect values, from json

        Returns:
            ApplyAfflictionSkillEffect: The created effect object
        """
        query = self.manager.skill_query

        # get the info for the APPLICATION of the affliction N.B. only create affliction at point of application
        target_type = query.get_target_type_from_string(effect["required_target_type"])

        # get tags from skill_effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(query.get_target_tags_from_string(tag))

        accuracy = effect["accuracy"]
        stat_to_target = query.get_secondary_stat_from_string(effect["stat_to_target"])
        affliction_name = effect["affliction_name"]
        affliction_duration = effect["duration"]
        affliction_values = get_value_from_afflictions_json(affliction_name)
        from scripts.global_instances.managers import game_manager
        affliction_category = game_manager.affliction_action.get_affliction_category_from_string(affliction_values["category"])

        # add effect object to skill
        created_effect = ApplyAfflictionSkillEffect(skill, target_type, target_tags, accuracy, stat_to_target,
                                                    affliction_name, affliction_category, affliction_duration)

        return created_effect

    @staticmethod
    def calculate_to_hit_score(attacker, defender, skill_accuracy, stat_to_target):
        """
        Get the to hit score from the stats of both entities
        Args:
            attacker ():
            defender ():
            skill_accuracy ():
            stat_to_target ():
        """
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, f"Get to hit scores..."))

        roll = random.randint(1, 100)
        modified_to_hit_score = attacker.combatant.secondary_stats.chance_to_hit + skill_accuracy + roll

        # get dodge score
        dodge_value = 0
        if stat_to_target == SecondaryStatTypes.DODGE_SPEED:
            dodge_value = defender.combatant.secondary_stats.dodge_speed
        elif stat_to_target == SecondaryStatTypes.DODGE_TOUGHNESS:
            dodge_value = defender.combatant.secondary_stats.dodge_toughness
        elif stat_to_target == SecondaryStatTypes.DODGE_INTELLIGENCE:
            dodge_value = defender.combatant.secondary_stats.dodge_intelligence

        # mitigate the to hit
        mitigated_to_hit_score = modified_to_hit_score - dodge_value

        # log the info
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return mitigated_to_hit_score

    @staticmethod
    def create_skill(actor, skill_tree_name, skill_name):
        """
        Create a SKill object
        Args:
            actor ():
            skill_tree_name ():
            skill_name ():

        Returns:
            Skill: The created skill
        """
        skill = Skill(actor, skill_tree_name, skill_name)

        return skill
