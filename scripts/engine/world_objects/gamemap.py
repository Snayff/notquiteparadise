from typing import List

from scripts.engine import utility
from scripts.engine.core.constants import TILE_SIZE
from scripts.engine.world_objects.tile import Tile


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, width: int, height: int):
        self.tiles: List[List[Tile]] = []
        self.width = width
        self.height = height

        # FIXME - move all the below out of game map to map gen
        floor_sprite = utility.get_image("assets/world/placeholder/_test.png", (TILE_SIZE, TILE_SIZE))
        wall_sprite = utility.get_image("assets/world/placeholder/_testWall.png", (TILE_SIZE, TILE_SIZE))

        # populate map with tiles
        for x in range(self.width):
            # give each new row an empty list
            self.tiles.append([])
            for y in range(self.height):
                # add to the column
                self.tiles[x].append(Tile(x, y, floor_sprite))
        
        
        # create an outer ring of walls
        for x in range(self.width):
            top_tile = self.tiles[x][0]
            bottom_tile = self.tiles[x][self.height - 1]
            
            top_tile.sprite = bottom_tile.sprite = wall_sprite
            top_tile.blocks_movement = bottom_tile.blocks_movement = True
            top_tile.blocks_sight = bottom_tile.blocks_sight = True
        
        for y in range(self.height):
            left_tile = self.tiles[0][y]
            right_tile = self.tiles[self.width - 1][y]

            left_tile.sprite = right_tile.sprite = wall_sprite
            left_tile.blocks_movement = right_tile.blocks_movement = True
            left_tile.blocks_sight = right_tile.blocks_sight = True
        
        # create some walls for testing
        wall1 = self.tiles[3][4]
        wall1.blocks_sight = True
        wall1.blocks_movement = True
        wall1.sprite = wall_sprite

        wall2 = self.tiles[6][7]
        wall2.blocks_sight = True
        wall2.blocks_movement = True
        wall2.sprite = wall_sprite

        wall3 = self.tiles[6][4]
        wall3.blocks_sight = True
        wall3.blocks_movement = True
        wall3.sprite = wall_sprite
