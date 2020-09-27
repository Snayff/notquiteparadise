from __future__ import annotations

import json
import logging
import random
from typing import Any, Dict, List, Tuple

import numpy as np
from numpy import ndarray

from scripts.engine import dungen, world
from scripts.engine.component import Blocking, Position
from scripts.engine.core.constants import TILE_SIZE, TileCategory
from scripts.engine.core.definitions import ActorData
from scripts.engine.world_objects.tile import Tile


class GameMap:
    """
    Holds tiles for a map. Handles generation of the map and placement of the entities. Fills map with floors on
    init.
    """

    def __init__(self, map_name: str, seed: Any):
        # FIXME - fix deserialisation

        self.name: str = map_name
        self.seed = seed
        self.rng = random.Random()
        self.rng.seed(self.seed)

        from scripts.engine import library

        _map_data = library.MAPS[map_name]
        self.width = _map_data.width
        self.height = _map_data.height
        self.light_map: np.array = np.zeros((self.width, self.height), dtype=bool, order="F")
        self.tile_map: List[List[Tile]] = []

        # get details for a wall tile
        from scripts.engine import utility

        wall_sprite_path = _map_data.sprite_paths[TileCategory.WALL]
        wall_sprite = utility.get_image(wall_sprite_path)
        blocks_sight = True
        blocks_movement = True

        # populate tile_map with wall tiles
        for x in range(self.width):
            self.tile_map.append([])  # create new list for every col
            for y in range(self.height):
                self.tile_map[x].append(Tile(x, y, wall_sprite, wall_sprite_path, blocks_sight, blocks_movement))

        self.generation_info: str = ""

    def generate_new_map(self, player_data: ActorData):
        """
        Generate the map for the current game map. Creates tiles. Saves the values directly to the GameMap.
        """
        self.tile_map, self.generation_info = dungen.generate(self.name, self.rng, player_data)

    def dump(self, path: str):
        """
        Dumps the dungeon tree into a file
        :param path: File path
        """
        with open(path, "w") as fp:
            fp.write(json.dumps(self.generation_info, indent=4))

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

        _dict = {"width": self.width, "height": self.height, "tiles": tiles, "seed": self.seed}
        return _dict

    @classmethod
    def deserialise(cls, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the GameMap.
        """
        try:
            seed = serialised["seed"]
            algo_name = serialised["algorithm_name"]
            width = serialised["width"]
            height = serialised["height"]

            tiles: List[List[Tile]] = []
            for x in range(width):
                tiles.append([])
                for y in range(height):
                    tiles[x].append(Tile.deserialise(serialised["tiles"][x][y]))

            game_map = GameMap(seed, algo_name)
            game_map.tile_map = tiles
            return game_map
        except KeyError as e:
            logging.warning(f"GameMap.Deserialise: Incorrect key ({e.args[0]}) given. Data not loaded correctly.")
            raise Exception  # throw exception to hit outer error handler and exit
