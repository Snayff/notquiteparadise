import tcod

from scripts.core.constants import TILE_SIZE, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.managers.world_methods.action_methods import EntityAction
from scripts.managers.world_methods.existence_methods import EntityExistence
from scripts.managers.world_methods.query_methods import EntityQuery
from scripts.world.entity import Entity
from scripts.world.game_map import GameMap


class WorldManager:
    """
    Contains all world related functionality
    """
    def __init__(self):

        self.entity_query = EntityQuery(self)
        self.entity_existence = EntityExistence(self)
        self.entity_action = EntityAction(self)
        # TODO - create FOV container class

        self.game_map = None  # type: GameMap
        self.player = None  # type: Entity
        self.player_fov_map = None
        self.player_fov_is_dirty = False
        self.light_walls = True
        self.fov_algorithm = 0

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"WorldManager initialised."))

    def update(self):
        """
        Update the world manager:
            player fov
        """
        if self.player_fov_is_dirty:
            player = self.player
            self.recompute_player_fov(player.x, player.y, player.sight_range)

    def create_new_map(self, map_width, map_height):
        """
        Create new GameMap and create player fov
        """
        self.game_map = GameMap(map_width, map_height)
        self.create_player_fov_map()

    def create_player_fov_map(self):
        """
        Create the fov map for the player
        """
        self.player_fov_map = tcod.map_new(self.game_map.width, self.game_map.height)

        for x in range(self.game_map.width):
            for y in range(self.game_map.height):
                tile = self.game_map.get_tile(x,y)
                tcod.map_set_properties(self.player_fov_map, x, y, not tile.blocks_sight,
                                        not tile.blocks_movement)

        self.player_fov_is_dirty = True

    def recompute_player_fov(self, x, y, radius):
        """

        Args:
            x:
            y:
            radius:
        """
        tcod.map_compute_fov(self.player_fov_map, x, y, radius, self.light_walls, self.fov_algorithm)
        self.game_map.update_tile_visibility(self.player_fov_map)
        self.player_fov_is_dirty = False

    def is_tile_in_fov(self, tile_x, tile_y):
        """
        Check if  target tile is in player's FOV

        Args:
            tile_x: x of tile
            tile_y: y of tile

        Returns:
            bool: True if tile is in FOV
        """

        return tcod.map_is_in_fov(self.player_fov_map, tile_x, tile_y)

    @staticmethod
    def convert_xy_to_tile(x, y):
        """
        Convert an x y position to a tile ref

        Args:
            x:
            y:

        Returns :


        """
        tile_x = int(x / TILE_SIZE)
        tile_y = int(y / TILE_SIZE)

        return tile_x, tile_y

