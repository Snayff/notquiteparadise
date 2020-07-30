from typing import List, Tuple
import scripts.engine.world as world

class EntityPoolEntry:
    """
    An entry for the entity pool.
    """
    def __init__(self, name: str, description: str, traits: List[str], offset: List[List[int, int]], is_player: bool, max_per_room: int, weight: float):
        self.name = name
        self.offset = offset
        self.description = description
        self.traits = traits
        self.is_player = is_player
        self.max_per_room = max_per_room
        self.weight = weight


class EntityPool:

    def __init__(self):
        self.pool = []

    def add(self, name: str, description: str, traits: List[str], offset: List[List[int, int]], is_player: bool, max_per_room: int, weight: float):
        """
        Save an entity definition to the pool
        :param name: The actor name
        :param description: The actor description
        :param traits: The actor traits
        :param offset: The actor offsets
        :param is_player: If the actor is a player
        :param max_per_room: Max actors per room
        :param weight: Weight for the entry
        """
        self.pool.append(
            EntityPoolEntry(name, description, traits, offset, is_player, max_per_room, weight)
        )

    def seed(self, seed: int):
        """
        Seeds the pool's rng
        :param seed: The seed to use
        """
        self.rng.seed(seed)

    def spawn_players(self, rooms: List[Tuple[Tuple[int, int], List[List[int]]]]) -> List[EntityID]:
        x, y = position
        entry =
        actor = world.create_actor(entry.name, entry.desc, [(w[0] + x, w[1] + y) for w in entry.offset], ["training_dummy"])



class EntityGeneration:

    def __init__(self, seed: int, pool: EntityPool, rooms: List[Tuple[Tuple[int, int], List[List[int]]]]):
        self.pool = pool
        self.rooms = rooms
        self.seed = seed

    def place(self):
        for room in rooms:
            x, y, cells = room
            entity = pool.pick()