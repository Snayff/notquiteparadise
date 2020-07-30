from __future__ import annotations

from typing import List, Tuple, Dict, Any
from scripts.engine.world_objects.world_gen import DungeonGeneration
from scripts.engine.world_objects.entity_gen import EntityGeneration, EntityPool
from scripts.engine.world_objects.tile import Tile
from snecs.typedefs import EntityID
import json


class GameMap:
    """
    object to hold tile and fov
    """
    def __init__(self, seed: int, algorithm_name: str, width: int, height: int):
        self.tiles: List[List[Tile]] = []
        self.rooms: List[Tuple[Tuple[int, int], List[List[int]]]] = []
        self.width = width
        self.height = height
        self.seed = seed
        self.world_gen = DungeonGeneration(seed, algorithm_name, width, height)
        tiles, rooms = self.world_gen.generate()
        self.tiles = tiles
        self.rooms = rooms
        self.entity_gen = EntityGeneration(self.seed, self.rooms)
        self.actors_per_room: Dict[str, List[EntityID]] = {}

    def populate(self, pool: EntityPool):
        """
        Populate the gamemap with entities and players
        :return: The players and actors spawned
        """
        self.entity_gen.set_pool(pool)
        players = self.entity_gen.place_players()
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
            area = self.world_gen.calculate_room_area(room_cells)
            rooms_data[f"{i}"] = {
                "area": area,
                "actors": len(self.actors_per_room[i]),
                "aspects": 0
            }
            i += 1

        gen_content = self.world_gen.get_gen_info()
        content = {
            **gen_content,
            'rooms': rooms_data
        }
        with open(path, 'w') as fp:
            fp.write(json.dumps(content, indent=2))




