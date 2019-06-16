from scripts.core.constants import TILE_SIZE, TargetTypes, TargetTags
from scripts.world.entity import Entity
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.wall import Wall


class Tile:
    """
    A Tile on the GameMap. Can contain an Entity, a Terrain and an Effect.

    Attributes:
        x(int): tile_x
        y(int): tile_y
        is_visible(bool): if tile is visible to player
        entity(Entity): the entity on the tile
        terrain(Terrain): the terrain on the tile, such as floor or wall
        aspect(Aspect): the aspect of the tile, such as smoke or fire
    """

    def __init__(self, x, y, entity=None, terrain=None, aspect=None):
        self.x = x
        self.y = y
        self.is_visible = False
        self.entity = None
        self.terrain = None
        self.aspect = None

        if terrain:
            self.set_terrain(terrain)

        if aspect:
            self.set_aspect(aspect)

        if entity:
            self.set_entity(entity)

    def has_tag(self, target_tag, active_entity=None):
        """
        Check if a given tag applies to the tile

        Args:
            target_tag (TargetTags): tag to check
            active_entity (Entity): entity using a skill

        Returns:
            bool: True if tag applies.
        """
        if target_tag == TargetTags.FLOOR:
            return self.is_floor
        elif target_tag == TargetTags.WALL:
            return self.is_wall
        elif target_tag == TargetTags.SELF:
            # ensure active entity is the same as the targeted one
            if active_entity == self.entity:
                return True
            else:
                return False
        elif target_tag == TargetTags.OTHER_ENTITY:
            # ensure active entity is NOT the same as the targeted one
            if active_entity != self.entity:
                return True
            else:
                return False
        elif target_tag == TargetTags.NO_ENTITY:
            return not self.has_entity
        else:
            return False  # catch all

    @property
    def is_floor(self):
        """
        Check if the tag is applicable

        Returns:
            bool: True if tag is applicable
        """
        if self.terrain:
            if isinstance(self.terrain, Floor):
                return True

        return False

    @property
    def is_wall(self):
        """
        Check if the tag is applicable

        Returns:
            bool: True if tag is applicable
        """
        if self.terrain:
            if isinstance(self.terrain, Wall):
                return True

        return False

    @property
    def has_entity(self):
        """
        Check if the tag is applicable

        Returns:
            bool: True if tag is applicable
        """
        if self.entity:
            return True

        return False

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
        elif self.aspect:
            if self.aspect.blocks_movement:
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
        elif self.aspect:
            if self.aspect.blocks_sight:
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

        if self.aspect:
            surface.blit(self.aspect.sprite, draw_position)

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

    def set_aspect(self, aspect):
        """
        Set the new aspect on the tile.

        Args:
            aspect:
        """
        self.aspect = aspect
        self.aspect.owner = self

    def remove_aspect(self):
        """
        Remove aspect from tile
        """
        self.aspect.owner = None
        self.aspect = None

    def get_entity(self):
        """
        Get the entity from the Tile

        Returns:
            Entity: The Entity on the tile

        """
        return self.entity

    def trigger_aspect_effect(self):
        """
        Trigger the effect of the Aspect
        """
        if self.aspect:
            self.aspect.trigger()

    def get_terrain(self):
        """
        Get the terrain from the Tile

        Returns:
            Terrain: The terrain on the tile

        """
        return self.terrain