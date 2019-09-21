

from scripts.core.constants import TargetTags
from scripts.world.tile import Tile


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, width, height):
        self.tiles = []
        self.width = width
        self.height = height

        # populate map with floor terrain
        for x in range(self.width):
            # give each new row an empty list
            self.tiles.append([])
            for y in range(self.height):
                # add to the column
                self.tiles[x].append(Tile(x, y, terrain=TargetTags.FLOOR))

        # TODO remove - only for test
        if self.width > 10 and self.height > 10:
            from scripts.global_singletons.managers import world_manager
            world_manager.Map.set_terrain_on_tile(self.tiles[0][5], TargetTags.WALL)
            world_manager.Map.set_terrain_on_tile(self.tiles[10][2], TargetTags.WALL)
            world_manager.Map.add_aspect_to_tile(self.tiles[0][2], "bog")

