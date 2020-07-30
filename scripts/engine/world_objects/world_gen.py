from scripts.engine.world_objects.world_gen_algorithms import RoomAddition
from scripts.engine import utility, library
from scripts.engine.world_objects.tile import Tile
from scripts.engine.core.constants import TILE_SIZE
from typing import List, Tuple, Dict, Set, Any
import json
import collections


class DungeonGeneration:

    generation_algorithms = {
        'room_addition': RoomAddition,
    }

    def __init__(self, seed: int, algorithm_name: str, width: int, height: int):
        self.floor_sprite = utility.get_image("assets/world/placeholder/_test.png", (TILE_SIZE, TILE_SIZE))
        self.wall_sprite = utility.get_image("assets/world/placeholder/_testWall.png", (TILE_SIZE, TILE_SIZE))
        self.algorithm_name = algorithm_name
        self.seed = seed
        self.width = width
        self.height = height
        self.min_room_space = library.GAME_CONFIG.world_values.min_room_space
        self.algorithm = self._create_algorithm()
        self.tiles: List[List[Tile]] = \
            [[Tile(x, y, self.floor_sprite) for y in range(self.height)] for x in range(self.width)]

    def _create_algorithm(self):
        """
        Create the algorithm to be used from the name
        """
        return DungeonGeneration.generation_algorithms[self.algorithm_name](
            self.min_room_space
        )

    def generate(self) -> Tuple[List[List[Tile]], List[Tuple[Tuple[int, int], List[List[int]]]]]:
        """
        Generate the map using the specified algorithm
        """
        self.algorithm.generate_level(self.seed, self.width, self.height)

        for x in range(self.width):
            for y in range(self.height):
                # Is this a wall? Or is this a border?
                if self.algorithm.level[x][y] == 1 or self._is_map_border(x, y):
                    self._make_wall(x, y)
        return self.tiles, self.algorithm.rooms

    def _is_map_border(self, x: int, y: int):
        """
        Returns a bool that represents if this is a map border
        """
        return x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1

    def _make_wall(self, x: int, y: int):
        """
        Makes the tile at the coordinate a wall
        """
        self.tiles[x][y].blocks_sight = True
        self.tiles[x][y].blocks_movement = True
        self.tiles[x][y].sprite = self.wall_sprite

    def visualize(self):
        pass

    def _build_graph(self) -> Tuple[Dict[int, List[int]], Set[Tuple[int, int]], Dict[Tuple[int, int], int]]:
        """
        Builds a graph from the room data
        :return: The graph built
        """
        rooms = self.algorithm.rooms
        start_room = rooms[0]
        vertices: Set[Tuple[int, int]] = set(pos for pos, _ in rooms)
        vertices_names: Dict[Tuple[int, int], int] = {}
        i = 0
        for v in vertices:
            vertices_names[v] = i
            i += 1
        visited = set()
        edges: Dict[int, List[int]] = collections.defaultdict(list)
        queue = collections.deque([(vertices_names[start_room[0]], start_room[0])])
        while queue:
            parent, position = queue.pop()
            x, y = position
            if position in visited or self.algorithm.level[x][y] == 1:
                continue

            new_parent = parent
            if position in vertices:
                new_parent = vertices_names[position]
                if new_parent != parent:
                    edges[parent].append(new_parent)

            visited.add(position)
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                queue.append(
                    (new_parent, (x + direction[0], y + direction[1]))
                )
        return edges, vertices, vertices_names

    def _build_tree(self, edges: Dict[int, List[int]], vertices_name: Dict[Tuple[int, int], int]):
        """
        Builds a tree like representation from a graph
        :return: The representation
        """
        tree: Dict[str, Any] = {}
        root = self.algorithm.rooms[0][0]
        visited = set()

        def _traverse(node: int, structure: Dict[str, Any]):
            structure['name'] = node
            children_structure: List[Dict[str, Any]] = []
            # iterate over the neighbours
            for child in edges[node]:
                if child in visited:
                    continue
                visited.add(child)
                child_structure: Dict[str, Any] = {}
                _traverse(child, child_structure)
                children_structure.append(child_structure)
            structure['children'] = children_structure

        _traverse(vertices_name[root], tree)
        return tree

    def dump(self, path: str):
        """
        Dumps the dungeon tree into a file
        :param path: File path
        """
        edges, vertices, vertices_names = self._build_graph()
        room_graph = {
            'vertices': list(vertices_names.values()),
            'edges': edges,
            'tree': self._build_tree(edges, vertices_names)
        }

        content = {
            'seed': self.seed,
            'algorithm': self.algorithm_name,
            'width': self.width,
            'height': self.height,
            'min_room_space': self.min_room_space,
            'rooms': room_graph
        }

        with open(path, 'w') as fp:
            fp.write(json.dumps(content, indent=2))
