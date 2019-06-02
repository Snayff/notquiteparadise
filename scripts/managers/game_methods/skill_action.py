from scripts.core.constants import GameStates
from scripts.events.game_events import ChangeGameStateEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.effects.damage import DamageSkillEffect


class SkillAction:
    def __init__(self, manager):
        self.manager = manager

    def create_damage_effect(self, skill, effect):
        """
        Create the damage effect object

        Args:
            effect (dict): dict of effect values, from json

        Returns:
            DamageSkillEffect: The created effect object
        """
        query = self.manager.skill_query

        # get tags from effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(query.get_target_tags_from_tag_string(tag))

        target_type = query.get_target_type_from_string(effect["required_target_type"])
        damage_type = query.get_damage_type_from_string(effect["damage_type"])
        stat_to_target = query.get_secondary_stat_from_string(effect["stat_to_target"])

        # add effect object to skill
        created_effect = DamageSkillEffect(skill, effect["damage"], damage_type, target_type, target_tags,
                                           effect["accuracy"], stat_to_target)

        return created_effect

    def create_change_terrain_effect(self, skill, effect):
        """
        Create the change terrain effect object

        Args:
            skill ():
            effect (dict): dict of effect values, from json

        Returns:
            ChangeTerrainSkillEffect: The created effect object
        """
        query = self.manager.skill_query

        # get tags from effects
        target_tags = []
        for tag in effect["required_tags"]:
            target_tags.append(query.get_target_tags_from_tag_string(tag))

        target_type = query.get_target_type_from_string(effect["required_target_type"])
        new_terrain = query.get_target_tags_from_tag_string(effect["new_terrain"])

        # add effect object to skill
        created_effect = ChangeTerrainSkillEffect(skill, target_type, target_tags, new_terrain)

        return created_effect

    @staticmethod
    def activate_targeting_mode(skill):
        # TODO - should this be in UI manager?
        """
        Change game state to Targeting mode
        Args:
            skill ():
        """

        publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
