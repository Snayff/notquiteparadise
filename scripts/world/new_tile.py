
from scripts.core.constants import TILE_SIZE


class NewTile:
    def __init__(self, x, y, entity=None, terrain=None, effect=None):
        self.x = x
        self.y = y
        self.is_visible = False
        self.entity = entity
        self.terrain = terrain
        self.effect = effect

        # set owners
        if entity:
            self.entity.owner = self
        if terrain:
            self.terrain.owner = self
        if effect:
            self.effect.owner = self

    @property
    def blocks_movement(self):
        """
        If anything on tile blocks ability to move

        Returns:
            bool: True if movement is blocked.
        """
        tile_blocks_movement = False

        if self.entity:
            if self.entity.blocks_movement:
                tile_blocks_movement = True
        elif self.terrain:
            if self.terrain.blocks_movement:
                tile_blocks_movement = True
        elif self.effect:
            if self.effect.blocks_movement:
                tile_blocks_movement = True

        return tile_blocks_movement

    @property
    def blocks_sight(self):
        """
        If anything on tile blocks ability to see

        Returns:
            bool: True if sight is blocked.
        """
        tile_blocks_sight = False

        if self.entity:
            if self.entity.blocks_sight:
                tile_blocks_sight = True
        elif self.terrain:
            if self.terrain.blocks_sight:
                tile_blocks_sight = True
        elif self.effect:
            if self.effect.blocks_sight:
                tile_blocks_sight = True

        return tile_blocks_sight

    def draw(self, surface):
        """
        Draw the tile on the specified surface

        Args:
            surface(pygame.Surface): The surface to draw to
        """
        draw_position = (self.x * TILE_SIZE, self.y * TILE_SIZE)

        if self.terrain:
            surface.blit(self.terrain.sprite, draw_position)

        if self.entity:
            surface.blit(self.entity.icon, draw_position)

        if self.effect:
            surface.blit(self.effect.sprite, draw_position)

    def set_entity(self, entity):
        """
        Set the new entity on the tile.

        Args:
            entity:
        """
        self.entity = entity
        self.entity.owner = self

    def remove_entity(self):
        """
        Remove entity from tile
        """
        self.entity.owner = None
        self.entity = None

    def set_terrain(self, terrain):
        """
        Set the new terrain on the tile.

        Args:
            terrain:
        """
        self.terrain = terrain
        self.terrain.owner = self

    def remove_terrain(self):
        """
        Remove terrain from tile
        """
        self.terrain.owner = None
        self.terrain = None

    def set_effect(self, effect):
        """
        Set the new effect on the tile.

        Args:
            effect:
        """
        self.effect = effect
        self.effect.owner = self

    def remove_effect(self):
        """
        Remove effect from tile
        """
        self.effect.owner = None
        self.effect = None