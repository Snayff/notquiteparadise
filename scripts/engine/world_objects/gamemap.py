from __future__ import annotations

from typing import Any, Dict, List, Tuple

import random
import logging
import json

from scripts.engine import dungen
from scripts.engine.world_objects.entity_gen import EntityGeneration, EntityPool
from scripts.engine.world_objects.tile import Tile
from snecs.typedefs import EntityID


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, map_name: str, seed: Any):
        self.name: str = map_name
        self.seed = seed
        self.rng = random.Random()
        self.rng.seed(self.seed)

        self.tiles: List[List[Tile]] = []
        self.rooms: List[Tuple[Tuple[int, int], List[List[int]]]] = []
        self.tunnels = []

        self.entity_gen = EntityGeneration(self.seed, self.rooms)
        self.actors_per_room: Dict[int, List[EntityID]] = {}

    def generate_level(self):
        """
        Generate the level for the current game map. Creates tiles. Saves the values directly to the GameMap.
        """
        self.tiles, self.rooms, self.tunnels = dungen.generate(self.name, self.rng)

    def populate(self, pool: EntityPool) -> Tuple[List[EntityID], List[EntityID]]:
        """
        Populate the gamemap with entities and players
        :return: The players and actors spawned
        """
        self.entity_gen.set_pool(pool)
        players = self.entity_gen.place_player()
        actors, actors_per_room = self.entity_gen.place_entities()
        self.actors_per_room = actors_per_room
        return players, actors

    def dump(self, path: str):
        """
        Dumps the dungeon tree into a file
        :param path: File path
        """
        rooms_data: Dict[str, Any] = {}
        rooms = self.rooms
        i = 0
        for room_pos, room_cells in rooms:
            area = self.calculate_room_area(room_cells)
            rooms_data[f"{i}"] = {
                "area": area,
                "actors": len(self.actors_per_room[i]),
                "aspects": 0
            }
            i += 1

        gen_content = self.world_gen_info
        content = {
            **gen_content,
            'rooms': rooms_data
        }
        with open(path, 'w') as fp:
            fp.write(json.dumps(content, indent=2))

    def calculate_room_area(self, room_cells: List[List[int]]) -> int:
        """
        Calculate the area of a room based on the cells given
        """
        area = 0
        for i in range(len(room_cells)):
            for j in range(len(room_cells[i])):
                if room_cells[i][j] == 0:
                    area += 1
        # take into account the door slot
        return area + 1

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
            "algorithm_name": self.algorithm_name,
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
