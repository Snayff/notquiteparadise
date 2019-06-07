import pygame

from scripts.data_loaders.getters import get_value_from_skill_json
from scripts.events.game_events import EndTurnEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.effects.change_terrain import ChangeTerrainSkillEffect
from scripts.skills.effects.damage import DamageSkillEffect


class Skill:
    """
    A skill to be used by an actor

    Args:
            name(str):
    """
    def __init__(self, skill_tree_name, skill_name):
        self.name = skill_name
        self.skill_tree_name = skill_tree_name

        skill_values = get_value_from_skill_json(skill_tree_name, skill_name)

        # aesthetic info
        self.description = skill_values["description"]  # the description of the skill
        self.icon = pygame.image.load("assets/skills/" + skill_values["icon"]).convert_alpha()  # icon showing theskill

        # targeting info
        self.range = skill_values["range"]  # how far away the skill can be used
        from scripts.global_instances.managers import game_manager
        self.required_target_type = game_manager.skill_query.get_target_type_from_string(skill_values[
                                                                                              "required_target_type"])
        required_tags = skill_values["required_tags"]
        self.required_tags = []

        for tag in required_tags:
            self.required_tags.append(game_manager.skill_query.get_target_tags_from_tag_string(tag))

        # resource info
        self.resource_type = skill_values["resource_type"]
        self.resource_cost = skill_values["resource_cost"]  # base value of resource spent to complete action
        self.time_cost = skill_values["time_cost"]  # base value of time spent to complete action
        self.cooldown = skill_values["cooldown"]  # how many rounds to wait between uses

        # effects info
        effects = skill_values["effects"]  # list of effects to process
        self.effects = []

        for effect in effects:
            created_effect = None
            effect_name = effect["name"]

            if effect_name == "damage":
                created_effect = game_manager.skill_action.create_damage_effect(self, effect)

            elif effect_name == "change_terrain":
                created_effect = game_manager.skill_action.create_change_terrain_effect(self, effect)

            elif effect_name == "apply_affliction":
                created_effect = game_manager.skill_action.create_apply_affliction_effect(self, effect)

            # if we have an effect add it to internal list
            if created_effect:
                self.effects.append(created_effect)

    def use(self, target_pos):
        """
        Use the skill

        Args:
            target_pos (tuple): x y of the target
        """
        entity = self.owner.owner  # owner is actor, actor's owner is entity
        from scripts.global_instances.managers import game_manager
        target = game_manager.skill_query.get_target(target_pos, self.required_target_type)  # get the tile or entity

        # apply any effects
        if self.effects:
            for effect in self.effects:

                if type(effect) is DamageSkillEffect:
                    effect.trigger(entity, target)

                elif type(effect) is ChangeTerrainSkillEffect:
                    effect.trigger(target)

        # end the turn
        publisher.publish(EndTurnEvent(self.time_cost))




