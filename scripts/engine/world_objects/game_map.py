from __future__ import annotations

import json
import logging
import random
from typing import Any, Dict, List

import numpy as np
from pygame.constants import BLEND_RGBA_MULT

from scripts.engine.core import dungen
from scripts.engine.internal import library
from scripts.engine.internal.constant import Height, MAP_BORDER_SIZE, TILE_SIZE, TileCategory
from scripts.engine.internal.definition import ActorData
from scripts.engine.world_objects import lighting
from scripts.engine.world_objects.lighting import LightBox
from scripts.engine.world_objects.tile import Tile

__all__ = ["GameMap"]


class GameMap:
    """
    Holds tiles for a map. Handles generation of the map and placement of the entities. Fills map with floors on
    init.
    """

    def __init__(self, map_name: str, seed: Any):
        self.is_dirty = True

        self.name: str = map_name
        self.seed = seed
        self.rng = random.Random()
        self.rng.seed(seed)

        _map_data = library.MAPS[map_name]
        self.width = _map_data.width + (MAP_BORDER_SIZE * 2)
        self.height = _map_data.height + (MAP_BORDER_SIZE * 2)
        map_size = (self.width, self.height)

        self.light_map: np.ndarray = np.zeros(map_size, dtype=bool, order="F")  # what positions are lit
        self.tile_map: List[List[Tile]] = []  # array of all Tiles

        window = library.VIDEO_CONFIG.base_window
        self.light_box: LightBox = lighting.LightBox((window.width, window.height), BLEND_RGBA_MULT)  # lighting that
        # needs processing

        self._block_movement_map: np.ndarray = np.zeros(map_size, dtype=bool, order="F")  # array for move blocked
        self._block_sight_map: np.ndarray = np.zeros(map_size, dtype=bool, order="F")  # array for sight blocked
        self._air_tile_positions: List[List[int]] = []  # what positions dont block sight

        self.generation_info: str = ""

        self._init_tile_map()

    ################ INIT ##################################################

    def _init_tile_map(self):
        """
        Only called during init to populate tile map with walls
        """
        from scripts.engine.internal import library

        _map_data = library.MAPS[self.name]

        # get details for a wall tile
        from scripts.engine.core import utility

        wall_sprite_path = _map_data.sprite_paths[TileCategory.WALL]
        wall_sprite = utility.get_image(wall_sprite_path)
        height = Height.MIN
        blocks_movement = True

        # populate tile_map with wall tiles
        for x in range(self.width):
            self.tile_map.append([])  # create new list for every col
            for y in range(self.height):
                self.tile_map[x].append(Tile(x, y, wall_sprite, wall_sprite_path, blocks_movement, height))

    ################## MAP GEN #############################################

    def generate_new_map(self, player_data: ActorData):
        """
        Generate the map for the current game map. Creates tiles. Saves the values directly to the GameMap.
        """
        self.tile_map, self.generation_info = dungen.generate(self.name, self.rng, player_data)
        self.is_dirty = True

    def dump(self, path: str):
        """
        Dumps the dungeon tree into a file
        """
        with open(path, "w") as fp:
            fp.write(json.dumps(self.generation_info, indent=4))

    ################### DATA MANAGEMENT ####################################

    def _refresh_internals(self):
        """
        Refresh the data in the self._block_movement_map and self._block_sight_map
        """
        block_movement_map = [[not tile.blocks_movement for tile in columns] for columns in self.tile_map]
        self._block_movement_map = np.asarray(block_movement_map, dtype=np.int8)

        # assumes tiles only have min or max height
        block_sight_map = [[not tile.height == Height.MAX for tile in columns] for columns in self.tile_map]
        self._block_sight_map = np.asarray(block_sight_map, dtype=np.int8)

        # get all the non-blocking, or "air", tiles.
        self._air_tile_positions = np.argwhere(self._block_sight_map == 1).tolist()
        # self.block_sight_map == 1 does the if not block_sight_map part of the loop.
        # np.argwhere gets the indexes of all nonzero elements.
        # tolist converts this back into a nested list.

        # update the walls in the light box
        lighting.generate_walls(self.light_box, self._air_tile_positions, TILE_SIZE)

    ################### SERIALISATION #####################################

    def serialise(self) -> Dict[str, Any]:
        """
        Serialise the game map to dict.
        """
        tiles: List[List[Dict]] = []
        # build list of lists
        for x in range(self.width):
            # give each new row an empty list
            tiles.append([])
            for y in range(self.height):
                # add to the column
                tiles[x].append(self.tile_map[x][y].serialise())

        _dict = {"width": self.width, "height": self.height, "tiles": tiles, "seed": self.seed, "map_name": self.name}
        return _dict

    @classmethod
    def deserialise(cls, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the GameMap.
        """
        try:
            seed = serialised["seed"]
            map_name = serialised["map_name"]
            width = serialised["width"]
            height = serialised["height"]

            tiles: List[List[Tile]] = []
            for x in range(width):
                tiles.append([])
                for y in range(height):
                    tiles[x].append(Tile.deserialise(serialised["tiles"][x][y]))

            game_map = GameMap(map_name, seed)
            game_map.tile_map = tiles
            return game_map

        except KeyError as e:
            logging.warning(f"GameMap.Deserialise: Incorrect key ({e.args[0]}) given. Data not loaded correctly.")
            raise KeyError  # throw exception to hit outer error handler and exit

    ################### PROPERTIES ########################################

    @property
    def block_movement_map(self) -> np.ndarray:
        """
        Return a copy of an array containing ints, 0 for blocked and 1 for open
        """
        if self.is_dirty:
            self._refresh_internals()
            self.is_dirty = False

        return self._block_movement_map.copy("F")

    @property
    def block_sight_map(self) -> np.ndarray:
        """
        Return a copy of an array containing ints, 0 for blocked and 1 for open
        """
        if self.is_dirty:
            self._refresh_internals()
            self.is_dirty = False

        return self._block_sight_map.copy("F")

    @property
    def air_tile_positions(self) -> List[List[int]]:
        """
        Return a copy of an array containing ints, 0 for blocked and 1 for open
        """
        if self.is_dirty:
            self._refresh_internals()
            self.is_dirty = False

        return self._air_tile_positions.copy()
