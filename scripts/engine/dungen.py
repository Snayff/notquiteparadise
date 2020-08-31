from __future__ import annotations

import logging
from typing import Dict, Iterator, List, TYPE_CHECKING

import random

from dataclasses import dataclass, field

import tcod

from scripts.engine import library, utility, world
from scripts.engine.core.constants import Direction, TILE_SIZE, TileCategory, TileCategoryType
from scripts.engine.core.definitions import ActorData, MapData, RoomConceptData
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Optional, Tuple, List

__all__ = ["generate", "generate_steps"]


@dataclass
class DungeonGenerator:
    rng: random.Random

    # containers
    map_data: MapData
    rooms_data: Dict[str, RoomConceptData] = field(default_factory=dict)
    actors_data: Dict[str, ActorData] = field(default_factory=dict)
    placed_rooms: List[RoomConcept] = field(default_factory=list)
    map_of_categories: List[List[TileCategoryType]] = field(default_factory=list)
    positions_in_rooms: List[Tuple[int, int]] = field(default_factory=list)

    # parameters/config
    max_generate_room_attempts = 100  # lower number means likely less rooms
    max_place_room_attempts = 500  # lower number means likely less rooms
    max_place_entrance_attempts = 50  # lower number means likely less entrances (and poss more ignorant tunnels)
    max_make_room_accessible_attempts = 100  # lower number means likely more ignorant tunnels
    max_place_entity_attempts = 50  # lower number means likely less entities

    border_size = 4  # tiles to place around the outside of the map

    def is_in_bounds(self, x: int, y: int):
        """
        Check if a position is in the bounds of the map
        """
        if 0 < x < self.map_data.width - 1 and 0 < y < self.map_data.height - 1:
            return True
        else:
            return False

    def is_in_room(self, x: int, y: int) -> bool:
        """
        Check if a position is in a placed room.
        """
        if (x, y) in self.positions_in_rooms:
            return True
        else:
            return False

    def is_only_accessible_diagonally(self, x: int, y: int) -> bool:
        """
        Checks if a tile is only accessible via a diagonal move.
        """
        # can be reached by cardinal
        if self.count_adjacent_walls(x, y) > 0:
            return False

        # can be reached by diagonal
        if self.count_neighbouring_walls(x, y) > 0:
            return True

        # not accessible at all
        return False

    def is_in_border(self, x: int, y: int):
        """
        Check if a position is in the border of the map
        """
        border = self.border_size
        if (x < border or x > self.map_data.width - border - 1) and\
                (y < border or y > self.map_data.height - border - 1):
            return True
        else:
            return False

    def count_neighbouring_walls(self, x: int, y: int) -> int:
        """
        Get the number of walls in 8 directions.
        """
        wall_counter = 0
        width = self.map_data.width
        height = self.map_data.height

        for neighbor_x in range(x - 1, x + 2):
            for neighbor_y in range(y - 1, y + 2):
                # Edges are considered alive. Makes map more likely to appear naturally closed.
                if neighbor_x < 0 or neighbor_y < 0 or neighbor_y >= height or neighbor_x >= width:
                    wall_counter += 1
                elif self.map_of_categories[neighbor_x][neighbor_y] == TileCategory.WALL:
                    # exclude (x,y) from adjacency check
                    if (neighbor_x != x) or (neighbor_y != y):
                        wall_counter += 1

        return wall_counter

    def count_adjacent_walls(self, x: int, y: int) -> int:
        """
        Get the number of walls in 4 directions.
        """
        wall_counter = 0

        left = (x - 1, y)
        right = (x + 1, y)
        top = (x, y - 1)
        bot = (x, y + 1)

        for _x, _y in (left, right, top, bot):
            # count out of bounds as a wall
            if self.is_in_bounds(_x, _y):
                if self.map_of_categories[_x][_y] == TileCategory.WALL:
                    wall_counter += 1
            else:
                wall_counter += 1

        return wall_counter

    @property
    def map_of_tiles(self) -> List[List[Tile]]:
        """
        Returns an array of Tiles by converting values from map_of_categories to tiles.
        """
        generated_level = []
        width = self.map_data.width
        height = self.map_data.height

        # build the full size map and fill with tunnel sprites
        for x in range(width):
            generated_level.append([])
            for y in range(height):
                tile = _create_tile_from_category(x, y, self.map_of_categories[x][y], self.map_data.sprite_paths)
                generated_level[x].append(tile)

        # overwrite tunnel sprites with room sprites
        for room in self.placed_rooms:
            sprite_paths = library.ROOMS[room.key].sprite_paths
            start_x = room.start_x
            start_y = room.start_y
            for x in range(room.width):
                for y in range(room.height):
                    tile = _create_tile_from_category(start_x + x, start_y + y, room.tile_categories[x][y],
                                                      sprite_paths)
                    generated_level[start_x + x][start_y + y] = tile

        return generated_level

    @property
    def map_of_bools(self) -> List[List[bool]]:
        """
        Returns an array of bools by converting values from map_of_categories to bool. Floor == True, Wall == False.
        """

        bools_map = []
        width = self.map_data.width
        height = self.map_data.height

        for x in range(width):
            bools_map.append([])
            for y in range(height):
                if self.map_of_categories[x][y] == TileCategory.FLOOR:
                    bools_map[x].append(True)
                else:
                    bools_map[x].append(False)
        return bools_map

    @property
    def generation_string(self) -> str:
        gen_info = f"{self.map_data.name}: \n"
        for room in self.placed_rooms:
            gen_info += room.generation_info + "\n"

        return gen_info

    def get_room(self, x: int, y: int) -> Optional[RoomConcept]:
        """
        Returns the room at xy.
        """
        _room = RoomConcept([], "", "", x, y)
        for room in self.placed_rooms:
            if room.intersects(_room):
                return room
        return None

    def get_room_data(self, key: str) -> RoomConceptData:
        """
        Get the data for a room based on key.
        """
        if key in self.rooms_data:
            room_data = self.rooms_data[key]
        else:
            room_data = library.ROOMS[key]
            self.rooms_data[key] = room_data

        return room_data

    def get_actor_data(self, key: str) -> ActorData:
        """
        Get the data for an actor based on key.
        """
        if key in self.actors_data:
            actor_data = self.actors_data[key]
        else:
            actor_data = library.ACTORS[key]
            self.actors_data[key] = actor_data

        return actor_data

    def create_entities(self):
        """
        Create all entities listed in rooms
        """
        for room in self.placed_rooms:
            for actor_key, pos in room.actors.items():
                actor_data = self.get_actor_data(actor_key)

                # create actor
                if actor_key != "player":
                    actor = world.create_actor(actor_data, (pos[0], pos[1]))
                else:
                    actor = world.create_actor(actor_data, (pos[0], pos[1]), True)


@dataclass
class RoomConcept:
    """
    Details of a room. Used for world generation.
    """
    tile_categories: List[List[TileCategory]]  # what to place in a tile  # FIXME - can we remove?
    design: str  # algorithm used to generate
    key: str  # the type of room placed
    start_x: int = -1
    start_y: int = -1
    actors: Dict[str, Tuple[int, int]] = field(default_factory=dict)  # key, position

    @property
    def available_area(self) -> int:
        """
        Number of unblocked tiles.
        """
        unblocked_count = 0
        for row in self.tile_categories:
            for tile_cat in row:
                if tile_cat == TileCategory.FLOOR:
                    unblocked_count += 1
        return unblocked_count

    @property
    def total_area(self) -> int:
        """
        Number of tiles in room.
        """
        count = 0
        for row in self.tile_categories:
            for tile_cat in row:
                count += 1
        return count

    @property
    def width(self) -> int:
        """
        Widest width.
        """
        return len(self.tile_categories)

    @property
    def height(self) -> int:
        """
        Tallest height
        """
        try:
            height = len(self.tile_categories[0])
        except IndexError:
            height = 0
            logging.error("Something referenced room height before the room had any tile categories.")

        return height

    @property
    def generation_info(self) -> str:
        """
        Return the generation information about the room
        """
        gen_info = f"{self.key} | {self.design} | (w:{self.width}, h:{self.height}) " \
                   f"| available:{self.available_area}/ total:{self.total_area}. Actors:{self.actors}"

        return gen_info

    @property
    def end_x(self) -> int:
        return self.start_x + self.width

    @property
    def end_y(self) -> int:
        return self.start_y + self.height

    @property
    def centre_x(self) -> int:
        centre_x = (self.width // 2) + self.start_x
        return centre_x

    @property
    def centre_y(self) -> int:
        centre_y = (self.height // 2) + self.start_y
        return centre_y

    def intersects(self, room: RoomConcept) -> bool:
        """
        Check if this room intersects with another.
        """
        if (self.start_x <= room.end_x and self.end_x >= room.start_x) and \
                (self.start_y <= room.end_y and self.end_y >= room.start_y):
            return True
        else:
            return False


############################ GENERATE MAP ############################

def generate(map_name: str, rng: random.Random, player_data: ActorData) -> Tuple[List[List[Tile]], str]:
    """
    Generate the map using the specified details.
    """
    # create generator
    dungen = DungeonGenerator(rng, library.MAPS[map_name])

    # generate the level
    for _ in _generate_map_in_steps(dungen):
        pass

    # generate entities
    for _ in _generate_entities_in_steps(dungen, player_data):
        pass

    # create the generated entities
    dungen.create_entities()

    return dungen.map_of_tiles, dungen.generation_string


def generate_steps(map_name: str) -> Iterator:
    """
    Generates a map, returning each step of the generation. Used for dev view.
    """

    # create generator
    dungen = DungeonGenerator(random.Random(), library.MAPS[map_name])

    for step in _generate_map_in_steps(dungen):
        yield step

    for step in _generate_entities_in_steps(dungen):
        yield step


def _generate_map_in_steps(dungen: DungeonGenerator) -> Iterator:
    """
    Generate the next step of the map generation.
    """
    rooms_placed = 0
    placement_attempts = 0
    rooms_generated = 0

    # set everything to walls
    dungen.map_of_categories = []
    map_width = dungen.map_data.width
    map_height = dungen.map_data.height
    for x in range(map_width):
        dungen.map_of_categories.append([])  # create new list for every col
        for y in range(map_height):
            dungen.map_of_categories[x].append(TileCategory.WALL)

    yield dungen.map_of_categories

    # get room options for this map
    rooms = dungen.map_data.rooms
    room_names = []
    room_weights = []

    # break out names and weights
    for name, weight in rooms.items():
        room_names.append(name)
        room_weights.append(weight)

    # generate and place rooms
    max_rooms = dungen.rng.randint(dungen.map_data.min_rooms, dungen.map_data.max_rooms)
    max_generate_room_attempts = dungen.max_generate_room_attempts
    while rooms_placed <= max_rooms and rooms_generated <= max_generate_room_attempts:
        found_place = False

        room = _generate_room(dungen, room_names, room_weights)
        rooms_generated += 1

        # find place for the room
        while placement_attempts < dungen.max_place_room_attempts and not found_place:
            placement_attempts += 1
            found_place = _place_room(dungen, room)

        # if no place found for the room try again
        if not found_place:
            continue

        # doesnt intersect so paint room on map and add room to list
        for room_x in range(room.width):
            for room_y in range(room.height):
                map_x = room.start_x + room_x
                map_y = room.start_y + room_y
                in_bounds = dungen.is_in_bounds(map_x, map_y)
                in_border = dungen.is_in_border(map_x, map_y)
                if in_bounds and not in_border:
                    dungen.map_of_categories[map_x][map_y] = room.tile_categories[room_x][room_y]
                    dungen.positions_in_rooms.append((map_x, map_y))

        # place room
        dungen.placed_rooms.append(room)
        rooms_placed += 1

        # yield map after each room is painted
        yield dungen.map_of_categories

    # handle anything dodgy
    if rooms_placed == 0:
        raise Exception("No rooms placed on the map.")

    # room placement complete, fill tunnels, without connecting to rooms
    for x in range(map_width):
        for y in range(map_height):

            # check is not part of a room
            if not dungen.is_in_room(x, y):
                # if its a wall, start a tunnel
                if dungen.map_of_categories[x][y] == TileCategory.WALL:
                    if _add_tunnel(dungen, x, y):
                        yield dungen.map_of_categories

    # join rooms to tunnels
    for room in dungen.placed_rooms:
        _add_entrances(dungen, room)
        yield dungen.map_of_categories

    _make_rooms_accessible(dungen)
    yield dungen.map_of_categories

    _add_border_to_map(dungen)
    yield dungen.map_of_categories

    # this is needed due to cardinal only movement
    _open_diagonal_only_positions(dungen)
    yield dungen.map_of_categories

    _make_rooms_accessible(dungen)
    yield dungen.map_of_categories

    _remove_deadends(dungen)
    yield dungen.map_of_categories


def _generate_entities_in_steps(dungen: DungeonGenerator, player_data: Optional[ActorData] = None) -> Iterator:
    """
    Add entities to all rooms using the room data. Also places player.
    """
    # randomise order of rooms
    rooms = dungen.placed_rooms
    dungen.rng.shuffle(rooms)

    # we might not have player data if we are viewing generations
    if player_data:
        # put player in first room
        player_room = rooms[0]
        placed = False
        placement_attempts = 0
        while placement_attempts <= 1000 and not placed:
            xy = _find_place_for_actor(dungen, player_room, player_data)
            placement_attempts += 1

            if xy:
                x, y = xy

                # add player data to list so we can use it when creating the entities
                dungen.actors_data["player"] = player_data

                # log actor in room
                player_room.actors["player"] = (x, y)
                dungen.map_of_categories[x][y] = TileCategory.PLAYER

                placed = True

        # just in case player hasnt been placed
        if not placed:
            raise Exception("Dungen: Unable to place player.")

    yield dungen.map_of_categories

    # work through all rooms and populate
    skipped_player_room = False
    for room in rooms:

        # make sure to skip player room as that is handled differently
        if not skipped_player_room:
            skipped_player_room = True
            continue

        room_key = room.key
        room_data = dungen.get_room_data(room_key)

        # generate the actor
        actors_placed = 0
        placement_attempts = 0
        max_attempts = dungen.max_place_entity_attempts
        max_actors = dungen.rng.randint(room_data.min_actors, room_data.max_actors)

        # if this room is empty of actors go to next room
        if max_actors == 0:
            continue

        # try and place the actor
        while actors_placed <= max_actors and placement_attempts <= max_attempts:
            actor_data = _generate_actor(dungen, room_data)

            # try to place the actor
            xy = _find_place_for_actor(dungen, room, actor_data)
            placement_attempts += 1
            if xy:
                x, y = xy

                # log actor in room (for generation string)
                room.actors[actor_data.key] = (x, y)

                # mark actors on map, handle multi tile.
                for pos in actor_data.position_offsets:
                    dungen.map_of_categories[x + pos[0]][y + pos[1]] = TileCategory.ACTOR

                actors_placed += 1

                yield dungen.map_of_categories


############################ ROOMS ############################

def _generate_room(dungen: DungeonGenerator, room_names: List[str], room_weights: List[float]) -> RoomConcept:
    """
    Select a room type to generate and return that room. If a generation method isnt provided then one is picked at
    random, using weightings in the data.
    """
    design_methods = {
        "square": _generate_room_square,
        "cellular": _generate_cellular_automata_room
    }

    # pick a room based on weights
    room_name = dungen.rng.choices(room_names, room_weights, k=1)[0]
    room_data = library.ROOMS[room_name]
    room = design_methods[room_data.design](dungen, room_data)

    return room


def _generate_cellular_automata_room(dungen: DungeonGenerator, room_data: RoomConceptData) -> RoomConcept:
    """
    Generate a room using cellular automata generation.
    """
    pass
    chance_of_spawning_wall = dungen.map_data.chance_of_spawning_wall
    birth_limit = 4
    death_limit = 3

    # randomly pick a size for the room
    min_tiles_per_side = 4
    width = dungen.rng.randint(min_tiles_per_side, dungen.map_data.max_room_areas["cellular"] // min_tiles_per_side)
    min_height = max(min_tiles_per_side, dungen.map_data.min_room_areas["cellular"] // width)
    max_height = max(min_tiles_per_side, dungen.map_data.max_room_areas["cellular"] // width)
    height = dungen.rng.randint(min_height, max_height)

    # populate the room with floor
    room_tile_cats = [[TileCategory.FLOOR for y in range(height)] for x in range(width)]

    # randomly place some walls
    for y in range(height):
        for x in range(width):
            if dungen.rng.random() <= chance_of_spawning_wall:
                room_tile_cats[x][y] = TileCategory.WALL

    # spawn new walls around neighbours
    for y in range(height):
        for x in range(width):
            num_neighbours = dungen.count_neighbouring_walls(x, y)

            # if we have a wall check if enough neighbours to keep alive
            if room_tile_cats[x][y] == TileCategory.WALL:
                if num_neighbours < death_limit:
                    room_tile_cats[x][y] = TileCategory.FLOOR
                else:
                    room_tile_cats[x][y] = TileCategory.WALL
            else:
                # we have a floor so see if enough neighbours to birth new wall
                if num_neighbours > birth_limit:
                    room_tile_cats[x][y] = TileCategory.WALL
                else:
                    room_tile_cats[x][y] = TileCategory.FLOOR

    # convert to room
    room = RoomConcept(tile_categories=room_tile_cats, design="cellular", key=room_data.key)
    return room


def _generate_room_square(dungen: DungeonGenerator, room_data: RoomConceptData) -> RoomConcept:
    """
    Generate a square-shaped room.
    """
    map_width = dungen.map_data.width
    map_height = dungen.map_data.height

    # ensure not bigger than the map
    room_width = min(dungen.rng.randint(room_data.min_width, room_data.max_width), map_width)
    room_height = min(dungen.rng.randint(room_data.min_height, room_data.max_height), map_height)

    # populate area with floor categories
    tile_categories = []
    for x in range(room_width):
        tile_categories.append([])
        for y in range(room_height):
            tile_categories[x].append(TileCategory.FLOOR)

    # convert to room
    room = RoomConcept(tile_categories=tile_categories, design="square", key=room_data.key)

    return room


def _place_room(dungen: DungeonGenerator, room: RoomConcept) -> bool:
    """
    Place room in random location. Updates room start_x and start_y. Returns True if valid placement found.
    """
    intersects = False
    map_width = dungen.map_data.width
    map_height = dungen.map_data.height

    # pick random location to place room
    room.start_x = dungen.rng.randint(1, max(1, map_width - room.width - 1))
    room.start_y = dungen.rng.randint(1, max(1, map_height - room.height - 1))

    # if placed there does room overlap any existing rooms?
    for _room in dungen.placed_rooms:
        if room.intersects(_room):
            intersects = True
            break

    if not intersects:
        return True
    else:
        return False


####################### MAP AMENDMENTS ##############################

def _add_tunnel(dungen: DungeonGenerator, x: int, y: int) -> bool:
    """
    Follow a path from origin (xy) setting relevant position in map_of_categories to TileCategory.FLOOR. Uses flood
    fill. Returns True if tunnel added
    """
    added_tunnel = False
    to_fill_positions = set()
    last_direction = (0, 0)

    # check position we've been given is OK before entering loop
    in_bounds = dungen.is_in_bounds(x, y)
    in_room = dungen.is_in_room(x, y)
    num_walls = dungen.count_neighbouring_walls(x, y)  # only start where no other floors are
    if in_bounds and not in_room and num_walls >= 8:
        # first position is good, add to list
        to_fill_positions.add((x, y))

    while to_fill_positions:
        possible_directions = []

        # get next pos in set
        _x, _y = to_fill_positions.pop()

        # convert to floor
        dungen.map_of_categories[_x][_y] = TileCategory.FLOOR
        dungen.positions_in_rooms.append((_x, _y))
        added_tunnel = True

        # check for appropriate, adjacent wall tiles
        for x_dir, y_dir in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
            x_check = _x + x_dir
            y_check = _y + y_dir

            in_bounds = dungen.is_in_bounds(x_check, y_check)
            in_room = dungen.is_in_room(x_check, y_check)
            num_walls = dungen.count_adjacent_walls(x_check, y_check)  # can only move cardinal so check that

            # direction must be in bounds, not in a room and be surrounded by walls on all but X sides
            # N.B. the lower the num walls the more overlapping and joined up the tunnels are
            if in_bounds and not in_room and num_walls >= 3:
                if dungen.map_of_categories[x_check][y_check] == TileCategory.WALL and \
                        not dungen.is_in_room(_x + (x_dir * 2), _y + (y_dir * 2)):
                    possible_directions.append((x_dir, y_dir))

        # choose next direction to go in
        if possible_directions:
            # pick a possible position, preferring previous direction, unless tunnel winds
            if last_direction in possible_directions and \
                    dungen.rng.randint(1, 100) > dungen.map_data.chance_of_tunnel_winding:
                new_direction = last_direction
            else:
                new_direction = dungen.rng.choice(possible_directions)

            # add next position to be checked
            to_fill_positions.add((_x + new_direction[0], _y + new_direction[1]))

            # update last direction
            last_direction = new_direction

    return added_tunnel


def _add_ignorant_tunnel(dungen: DungeonGenerator, start_x: int, start_y: int, end_x: int, end_y: int):
    """
    Create a tunnel between two points, ignoring all terrain on the way
    """
    x = min(start_x, end_x)
    y = min(start_y, end_y)
    max_x = max(start_x, end_x) - 1
    max_y = max(start_y, end_y) - 1

    while x < max_x:
        if dungen.is_in_bounds(x, y):
            dungen.map_of_categories[x][y] = TileCategory.FLOOR
        x += 1
    while y < max_y:
        if dungen.is_in_bounds(x, y):
            dungen.map_of_categories[x][y] = TileCategory.FLOOR
        y += 1


def _add_entrances(dungen: DungeonGenerator, room: RoomConcept):
    """
    Loop the outer edge of the room for two adjoining floors and break through to link the locations.
    """
    # FIXME - not actually joining to floor spaces so just creating random floors

    entrances = 0
    attempts = 0
    placed_entrances = set()

    print(f"Add entrance to room: x:{room.start_x} | end_x:{room.end_x} | y:{room.start_y} | end_y:{room.end_y}")

    # roll for an extra entrance
    base_num_entrances = dungen.map_data.max_room_entrances
    if dungen.rng.randint(1, 100) >= dungen.map_data.extra_entrance_chance:
        _max_entrances = base_num_entrances + 1
    else:
        _max_entrances = base_num_entrances

    # roll for max entrances, ensure minimum 1
    max_entrances = dungen.rng.randint(1, max(1, _max_entrances))

    # find somewhere to place the entrance
    while attempts <= dungen.max_place_entrance_attempts and entrances <= max_entrances:
        attempts += 1
        poss_positions = []

        # pick random positions
        top_pos = (room.start_x + dungen.rng.randint(1, room.width - 1), room.start_y - 1)
        top_pos2 = top_pos[0], top_pos[1] - 1

        bot_pos = (room.start_x + dungen.rng.randint(1, room.width - 1), room.start_y + room.height + 1)
        bot_pos2 = bot_pos[0], bot_pos[1] + 1

        left_pos = (room.start_x - 1, room.start_y + dungen.rng.randint(1, room.height - 1))
        left_pos2 = left_pos[0] - 1, left_pos[1]

        right_pos = (room.start_x + room.width + 1, room.start_y + dungen.rng.randint(1, room.height - 1))
        right_pos2 = right_pos[0] + 1, right_pos[1]

        print(f"-> Random pos: top:{top_pos}:{top_pos2} | bot:{bot_pos}:{bot_pos2} | left:{left_pos}"
              f":{left_pos2} | right:{right_pos}:{right_pos2}")

        # note which ones are applicable
        for _pos, _pos2 in (
                (top_pos, top_pos2),
                (bot_pos, bot_pos2),
                (left_pos, left_pos2),
                (right_pos, right_pos2)):
            pos2_is_floor = False
            x, y = _pos2

            # if second pos in bounds then first and target must be
            in_bounds = dungen.is_in_bounds(x, y)
            in_border = dungen.is_in_border(x, y)
            if in_bounds and not in_border:
                if dungen.map_of_categories[x][y] == TileCategory.FLOOR:
                    pos2_is_floor = True

            # if target is wall and one after is floor and not already a placed entrance
            if pos2_is_floor and _pos not in placed_entrances:
                poss_positions.append(_pos)

        # pick one of the possible options and update the map
        if poss_positions:
            pos = dungen.rng.choice(poss_positions)
            dungen.map_of_categories[pos[0]][pos[1]] = TileCategory.DEBUG
            placed_entrances.add(pos)

            print(f"-> Placed entrance: {_pos}")

            entrances += 1


def _remove_deadends(dungen: DungeonGenerator):
    """
    Find all instances where a tunnel has a deadend and uncarve it, converting it back to a wall.
    """
    deadends = set()

    # find initial deadends
    for x in range(0, dungen.map_data.width):
        for y in range(0, dungen.map_data.height):
            if dungen.map_of_categories[x][y] == TileCategory.FLOOR and\
                    dungen.count_adjacent_walls(x, y) >= 3:
                deadends.add((x, y))

    while deadends:
        _x, _y = deadends.pop()

        # mark as wall
        dungen.map_of_categories[_x][_y] = TileCategory.WALL

        # check around where we just amended for new deadends
        for x_dir, y_dir in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT, Direction.UP_LEFT,
        Direction.UP_RIGHT, Direction.DOWN_LEFT, Direction.DOWN_RIGHT):
            x_check = _x + x_dir
            y_check = _y + y_dir

            in_bounds = dungen.is_in_bounds(x_check, y_check)
            if in_bounds:
                tile_cat = dungen.map_of_categories[x_check][y_check]
                num_walls = dungen.count_adjacent_walls(x_check, y_check)

                if num_walls >= 3 and tile_cat == TileCategory.FLOOR:
                    deadends.add((x_check, y_check))


def _open_diagonal_only_positions(dungen: DungeonGenerator):
    """
    Find positions where they can only be accessed via a diagonal and set surrounding tiles to floor.
    """
    for x in range(dungen.map_data.width):
        for y in range(dungen.map_data.height):
            if dungen.is_only_accessible_diagonally(x, y):
                for x_dir, y_dir in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
                    x_check = x + x_dir
                    y_check = y + y_dir
                    in_bounds = dungen.is_in_bounds(x_check, y_check)
                    in_border = dungen.is_in_border(x_check, y_check)
                    if in_bounds and not in_border:
                        dungen.map_of_categories[x_check][y_check] = TileCategory.FLOOR


def _add_border_to_map(dungen: DungeonGenerator):
    """
    Add a border of walls around the map
    """
    # top and bottom
    for x in range(0, dungen.map_data.width):
        for y in range(0, dungen.border_size):
            dungen.map_of_categories[x][y] = TileCategory.WALL
            dungen.map_of_categories[x][dungen.map_data.height - y - 1] = TileCategory.WALL

    # left and right
    for x in range(0, dungen.border_size):
        for y in range(0, dungen.map_data.height):
            dungen.map_of_categories[x][y] = TileCategory.WALL
            dungen.map_of_categories[dungen.map_data.width - x - 1][y] = TileCategory.WALL


def _make_rooms_accessible(dungen: DungeonGenerator):
    """
    Pick a room as the anchor and make sure all other floor tiles can connect to it via pathfinding.
    """
    # FIXME - connect room to nearest and prevent that room connecting back to the first. Creates a tree. 

    bools_map = dungen.map_of_bools

    # start by picking one room that all other rooms should connect to
    anchor_room = dungen.rng.choice(dungen.placed_rooms)

    # pick spot in room as anchor and make sure it is open
    anchor_x = anchor_room.centre_x
    anchor_y = anchor_room.centre_y
    dungen.map_of_categories[anchor_x][anchor_y] = TileCategory.FLOOR

    # loop all rooms
    counter = 0
    add_path_counter = 0
    for room in dungen.placed_rooms:
        counter += 1
        x = room.centre_x
        y = room.centre_y

        # ensure the centre of the room is open
        dungen.map_of_categories[x][y] = TileCategory.FLOOR

        # check if route is possible between anchor and target
        pathfinder = tcod.path.Dijkstra(bools_map, 0)
        pathfinder.set_goal(x, y)
        path = pathfinder.get_path(anchor_x, anchor_y)

        # if no possible route, make one
        if not path:
            _add_ignorant_tunnel(dungen, anchor_x, anchor_y, x, y)
            add_path_counter += 1


####################### ENTITIES ##############################

def _generate_actor(dungen: DungeonGenerator, room_data: RoomConceptData) -> ActorData:
    """
    Pick an actor using the possible options in the room and their weighting and return the actor's data.
    """
    # pick an actor
    keys = []
    weights = []
    for key, weight in room_data.actors.items():
        keys.append(key)
        weights.append(weight)
    actor_key = dungen.rng.choices(keys, weights, k=1)[0]

    # get the actor data
    actor_data = dungen.get_actor_data(actor_key)

    return actor_data


def _find_place_for_actor(dungen: DungeonGenerator, room: RoomConcept,
        actor_data: ActorData) -> Optional[Tuple[int, int]]:
    """
    Keep picking random locations in a room to place the actor. Returns xy if successful.
    """
    # pick random location to place actor
    x = room.start_x + dungen.rng.randint(1, max(1, room.width - 1))
    y = room.start_y + dungen.rng.randint(1, max(1, room.height - 1))

    # check if actor is blocked
    blocked = True
    for pos in actor_data.position_offsets:
        offset_x = x + pos[0]
        offset_y = y + pos[1]

        # only need to check tile category as that capture entity placement too
        if dungen.map_of_categories[offset_x][offset_y] == TileCategory.FLOOR:
            blocked = False
        else:
            blocked = True

    # if blocked try again
    if not blocked:
        return x, y
    else:
        return None


####################### HELPER FUNCTIONS ##############################

def _create_tile_from_category(x: int, y: int, tile_category: TileCategoryType,
        sprite_paths: Dict[str, str]) -> Tile:
    """
    Convert a tile category into the relevant tile. If it isnt a wall it is floor by default.
    """
    if tile_category == TileCategory.WALL:
        sprite_path = sprite_paths[TileCategory.WALL]
        sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
        blocks_sight = True
        blocks_movement = True
    else:  # tile_category == TileCategory.FLOOR:
        sprite_path = sprite_paths[TileCategory.FLOOR]
        sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
        blocks_sight = False
        blocks_movement = False

    tile = Tile(x, y, sprite, sprite_path, blocks_sight, blocks_movement)

    return tile
