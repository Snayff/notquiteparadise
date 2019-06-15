import pygame

from scripts.core.constants import TILE_SIZE, AspectTypes, AfflictionTypes
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

        # catch any images not resized and resize them
        if self.sprite.get_size() != (TILE_SIZE, TILE_SIZE):
            self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))

    def trigger(self):
        from scripts.global_instances.managers import game_manager
        if self.owner.has_entity:
            entity = self.owner.get_entity()
            affliction = game_manager.affliction_action.create_affliction(AfflictionTypes.BOGGED_DOWN, 1, entity)