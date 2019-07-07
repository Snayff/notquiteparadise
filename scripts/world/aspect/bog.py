import pygame

from scripts.core.constants import TILE_SIZE, AspectTypes, AfflictionTypes, TargetTypes, TargetTags, PrimaryStatTypes, \
    AfflictionCategory, SkillEffectTypes, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.world.aspect.aspect import Aspect


class Bog(Aspect):
    """
    Floor tile, doesnt block movement or sight
    """
    def __init__(self):
        super().__init__()
        self.name = "bog"

        aspect = library.get_aspect_data(self.name)

        self.sprite = pygame.image.load("assets/world/" + aspect.sprite).convert_alpha()

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))

        self.aspect_type = AspectTypes.BOG
        self.effects = []

        # create effects
        effects = aspect.skill_effects
        for effect in effects:
            created_effect = None
            effect_name = effect["name"]
            from scripts.global_singletons.managers import world_manager

            if effect_name == "damage":
                created_effect = world_manager.Skill.create_damage_effect(self, effect)

            elif effect_name == "change_terrain":
                created_effect = world_manager.Skill.create_change_terrain_effect(self, effect)

            elif effect_name == "apply_affliction":
                created_effect = world_manager.Skill.create_apply_affliction_effect(self, effect)

            # if we have an effect add it to internal list
            if created_effect:
                self.effects.append(created_effect)

    def trigger(self):
        if self.owner.has_entity:
            from scripts.global_singletons.managers import world_manager
            entity = world_manager.Map.get_entity_on_tile(self.owner)
            terrain = world_manager.Map.get_terrain_on_tile(self.owner)

            # attempt to apply on entity
            for effect in self.effects:

                if effect.effect_type == SkillEffectTypes.APPLY_AFFLICTION:
                    effect.trigger(None, entity)
                elif effect.effect_type == SkillEffectTypes.DAMAGE:
                    effect.trigger(None, entity)
                elif effect.effect_type == SkillEffectTypes.MOVE:
                    effect.trigger()
                elif effect.effect_type == SkillEffectTypes.CHANGE_TERRAIN:
                    effect.trigger(terrain)

                    log_string = f"{effect} not found in 'bog.trigger'"
                    publisher.publish(LoggingEvent(LoggingEventTypes.CRITICAL, log_string))
