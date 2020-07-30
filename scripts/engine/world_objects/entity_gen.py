from typing import List, Tuple
import scripts.engine.world as world
import scripts.engine.library as library
import random
from snecs.typedefs import EntityID


class EntityPoolEntry:
    """
    An entry for the entity pool.
    """

    def __init__(self, name: str, description: str, traits: List[str], offsets: List[Tuple[int, int]], is_player: bool,
                 max_per_room: int, weight: float):
        self.name = name
        self.offsets = offsets
        self.description = description
        self.traits = traits
        self.is_player = is_player
        self.max_per_room = max_per_room
        self.weight = weight


class EntityPool:

    def __init__(self):
        self.pool = []
        self.rng = random.Random()

    def add(self, name: str, description: str, offsets: List[Tuple[int, int]], traits: List[str], is_player: bool,
            max_per_room: int, weight: float):
        """
        Save an entity definition to the pool
        :param name: The actor name
        :param description: The actor description
        :param traits: The actor traits
        :param offsets: The actor offsets
        :param is_player: If the actor is a player
        :param max_per_room: Max actors per room
        :param weight: Weight for the entry
        """
        self.pool.append(
            EntityPoolEntry(name, description, traits, offsets, is_player, max_per_room, weight)
        )

    def seed(self, seed: int):
        """
        Seeds the pool's rng
        :param seed: The seed to use
        """
        self.rng.seed(seed)

    def spawn_players(self, rooms: List[Tuple[Tuple[int, int], List[List[int]]]]) -> List[EntityID]:
        """
        Spawns the players into rooms
        :param rooms: Rooms to spawn in
        :return:
        """
        players = [e for e in self.pool if e.is_player]
        actors = []
        for player in players:
            spawned = False
            while not spawned:
                room_pos, room = random.choice(rooms)
                x, y = room_pos
                actor = self._spawn_single_actor(room, player, x, y)
                if actor:
                    spawned = True
                    actors.append(actor)
        return actors

    def spawn_non_players(self, position: Tuple[int, int], room_cells: List[List[int]]) -> List[EntityID]:
        """
        Spawns random non player actors in the provded position and room cells
        :param position: Position of the room
        :param room_cells: room cells
        :return: The list of actors it spawned
        """
        x, y = position
        entry = self._pick_non_player_entry()

        max_per_room = min(entry.max_per_room, library.GAME_CONFIG.world_values.max_enemies_per_room)
        actors = []
        for _ in range(self.rng.randint(0, max_per_room)):
            actors.append(self._spawn_single_actor(room_cells, entry, x, y))
        return actors

    def _spawn_single_actor(self, room_cells: List[List[int]], entry: EntityPoolEntry, x: int, y: int):
        """
        Spawns a single actor with the given parameters
        :param room_cells: Room to spawn on
        :param entry: Entity entry
        :param x: Room x position
        :param y: Room y position
        :return: Actor spawned
        """
        cell_pos = self._get_random_room_cell(room_cells, entry.offsets)
        self._mark_actor_in_room(room_cells, cell_pos, entry)
        positions = [(w[0] + x + cell_pos[0], w[1] + y + cell_pos[1]) for w in entry.offsets]
        return world.create_actor(entry.name, entry.description, positions, entry.traits, entry.is_player)

    def _get_random_room_cell(self, room: List[List[int]], offsets: List[Tuple[int, int]]):
        """
        Find a random suitable position for a list of offsets
        :param room: Room to use
        :return: A suitable position
        """
        available = []
        for x in range(len(room)):
            for y in range(len(room[x])):
                if room[x][y] == 0:
                    available.append((x, y))
        cell = self.rng.choice(available)
        while self._collides(cell, room, offsets):
            cell = self.rng.choice(available)
        return cell

    @staticmethod
    def _mark_actor_in_room(room: List[List[int]], position: Tuple[int, int], entry: EntityPoolEntry):
        """
        Mark a room as occupied by an actor
        :param room: Room to mark
        :param position: Position of the actor in the room
        :param entry: Entry of the actor
        """
        for o_x, o_y in entry.offsets:
            x = position[0] + o_x
            y = position[1] + o_y
            room[x][y] = 1

    @staticmethod
    def _collides(position: Tuple[int, int], room: List[List[int]], offsets: List[Tuple[int, int]]):
        """
        Returns a bool that represents if the position with the offsets will collide in the room
        :param position: Position to use
        :param room: Room to use
        :param offsets: List of offsets to use
        :return: A boolean that represents collision
        """
        for offset in offsets:
            x = position[0] + offset[0]
            y = position[1] + offset[1]
            if room[x][y] == 1:
                return True
        return False

    def _pick_non_player_entry(self) -> EntityPoolEntry:
        """
        :return: A random entry from the pool
        """
        non_player_entries = [e for e in self.pool if not e.is_player]
        total = sum([e.weight for e in non_player_entries])
        # we normalize the weights
        return random.choices(population=non_player_entries, weights=[e.weight / total for e in non_player_entries], k=1)[0]


class EntityGeneration:

    def __init__(self, seed: int, rooms: List[Tuple[Tuple[int, int], List[List[int]]]]):
        self.pool: EntityPool = None
        self.rooms = rooms
        self.seed = seed

    def set_pool(self, pool: EntityPool):
        """
        Sets the entity pool to use
        :param pool: Entity pool to use
        """
        self.pool = pool

    def place_players(self):
        """
        Places the players into rooms
        """
        self.pool.seed(self.seed)
        return self.pool.spawn_players(self.rooms)

    def place_entities(self):
        """
        Places non players into rooms
        :return: The list of actors placed
        """
        self.pool.seed(self.seed)
        actors = []
        actors_per_room = {}
        i = 0
        for room in self.rooms:
            position, cells = room
            new_actors = self.pool.spawn_non_players(position, cells)
            actors += new_actors
            actors_per_room[i] = new_actors
            i += 1
        return actors, actors_per_room
