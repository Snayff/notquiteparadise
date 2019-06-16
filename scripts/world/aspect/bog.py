import pygame

from scripts.core.constants import TILE_SIZE, AspectTypes, AfflictionTypes, TargetTypes, TargetTags, PrimaryStatTypes, \
    AfflictionCategory
from scripts.world.aspect.aspect import Aspect


class Bog(Aspect):
    """
    Floor tile, doesnt block movement or sight
    """
    def __init__(self):
        super().__init__()
        self.name = "bog"
        self.sprite = pygame.image.load("assets/world/placeholder/78.png").convert_alpha()
        self.aspect_type = AspectTypes.BOG
        from scripts.skills.skill_effects.apply_affliction import ApplyAfflictionSkillEffect

        # create application effect
        # TODO - load from json
        required_target_type = TargetTypes.ENTITY
        required_tags = [TargetTags.OTHER_ENTITY]
        accuracy = 100
        stat_to_target = PrimaryStatTypes.SKULLDUGGERY
        affliction_name = "bogged_down"
        affliction_category = AfflictionCategory.BANE
        duration = 1

        self.effect = ApplyAfflictionSkillEffect(self, required_target_type, required_tags, accuracy, stat_to_target,
                                                 affliction_name, affliction_category, duration)

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))

    def trigger(self):
        if self.owner.has_entity:
            entity = self.owner.get_entity()

            # attempt to apply on entity
            self.effect.trigger(None, entity)
