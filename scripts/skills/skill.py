
import pygame


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
        self.name = skill_name
        self.owner = owner
        self.skill_tree_name = skill_tree_name

        skill = library.get_skill_data(skill_tree_name, skill_name)

        # aesthetic info
        self.description = skill.description  # the description of the skill
        self.icon = pygame.image.load("assets/skills/" + skill.icon).convert_alpha()  # icon showing the skill

        # targeting info
        self.range = skill.range  # how far away the skill can be used
        from scripts.global_singletons.managers import world_manager
        self.required_target_type = world_manager.Skill.get_target_type_from_string(skill.required_target_type)
        required_tags = skill.required_tags
        self.required_tags = []

        for tag in required_tags:
            self.required_tags.append(world_manager.Skill.get_target_tags_from_string(tag))

        # resource info
        self.resource_type = skill.resource_type
        self.resource_cost = skill.resource_cost  # base value of resource spent to complete action
        self.time_cost = skill.time_cost  # base value of time spent to complete action
        self.cooldown = skill.cooldown  # how many rounds to wait between uses

        # skill_effects info
        effects = skill.skill_effects  # list of skill_effects to process
        self.effects = []

        for effect in effects:
            created_effect = None
            effect_name = effect["name"]

            if effect_name == "damage":
                created_effect = world_manager.Skill.create_damage_effect(self, effect)

            elif effect_name == "change_terrain":
                created_effect = world_manager.Skill.create_change_terrain_effect(self, effect)

            elif effect_name == "apply_affliction":
                created_effect = world_manager.Skill.create_apply_affliction_effect(self, effect)

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
        target = world_manager.Skill.get_target(target_pos, self.required_target_type)  # get the tile or entity

        # apply any skill_effects
        if self.effects:
            for effect in self.effects:

                # TODO - change to make use of the Enums
                if type(effect) is DamageSkillEffect:
                    effect.trigger(entity, target)

                elif type(effect) is ChangeTerrainSkillEffect:
                    effect.trigger(target)

                elif type(effect) is ApplyAfflictionSkillEffect:
                    effect.trigger(entity, target)

        # end the turn
        publisher.publish(EndTurnEvent(self.time_cost))




