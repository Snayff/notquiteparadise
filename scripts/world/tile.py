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

        from scripts.global_instances.managers import world_manager

        if terrain:
            world_manager.Map.set_terrain_on_tile(self, terrain)

        if aspect:
            world_manager.Map.set_aspect_on_tile(self, aspect)

        if entity:
            world_manager.Map.set_entity_on_tile(self, entity)



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


