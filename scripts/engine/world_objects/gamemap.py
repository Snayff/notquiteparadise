from __future__ import annotations
from typing import Any, Dict, List, Tuple

import random
import logging
import json

from scripts.engine import dungen
from scripts.engine.core.constants import TILE_SIZE
from scripts.engine.core.definitions import ActorData
from scripts.engine.world_objects.tile import Tile


class GameMap:
    """
    Holds tiles for a map. Handles generation of the map and placement of the entities. Fills map with floors on
    init.
    """
    def __init__(self, map_name: str, seed: Any):
        self.name: str = map_name
        self.seed = seed
        self.rng = random.Random()
        self.rng.seed(self.seed)

        from scripts.engine import library
        _map_data = library.MAPS[map_name]
        self.width = _map_data.width
        self.height = _map_data.height

        # get details for an empty floor tile
        from scripts.engine import utility
        floor_sprite_path = _map_data.floor_sprite_path
        floor_sprite = utility.get_image(floor_sprite_path, (TILE_SIZE, TILE_SIZE))
        blocks_sight = False
        blocks_movement = False

        # populate with empty floor tiles
        self.tiles: List[List[Tile]] = [[
            Tile(x, y, floor_sprite, floor_sprite_path, blocks_sight, blocks_movement)
            for y in range(self.height)]
            for x in range(self.width)
        ]

        self.generation_info: str = ""

    def generate_new_map(self, player_data: ActorData):
        """
        Generate the map for the current game map. Creates tiles. Saves the values directly to the GameMap.
        """
        self.tiles, self.generation_info = dungen.generate(self.name, self.rng, player_data)

    def dump(self, path: str):
        """
        Dumps the dungeon tree into a file
        :param path: File path
        """
        with open(path, 'w') as fp:
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
                tiles[x].append(self.tiles[x][y].serialise())


        _dict = {
            "width": self.width,
            "height": self.height,
            "tiles": tiles,
            "seed": self.seed
        }
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

            game_map = GameMap(seed, algo_name, width, height)
            game_map.tiles = tiles
            return game_map
        except KeyError as e:
            logging.warning(f"GameMap.Deserialise: Incorrect key ({e.args[0]}) given. Data not loaded correctly.")
            raise Exception  # throw exception to hit outer error handler and exit
