from __future__ import annotations
from typing import Any, Callable, TYPE_CHECKING

import random
import tcod as libtcod

from scripts.engine import library, utility, world
from scripts.engine.core.constants import Direction, DirectionType, TILE_SIZE, TileCategory, TileCategoryType
from scripts.engine.core.definitions import ActorData, MapData
from scripts.engine.world_objects.tile import Tile
from scripts.engine.world_objects.room import Room

if TYPE_CHECKING:
    from typing import Optional, Tuple, List

__all__ = ["generate", "generate_steps"]

# containers
_placed_rooms: List[Room] = []  # rooms created
_map_of_categories: List[List[TileCategoryType]] = []  # a list of a lists of tile categories
_map_data: MapData = MapData()

# parameters/config
_max_generate_room_attempts = 100
_max_place_room_attempts = 200
_max_generate_shortcut_attempts = 100
_max_room_entrances = 2
_extra_entrance_chance = 20
_room_extra_size = 0
_chance_of_tunnel_winding = 0


def generate(map_name: str, rng: random.Random,
        player_data: Optional[ActorData] = None) -> Tuple[List[List[Tile]], str]:
    """
    Generate the map using the specified details.
    """
    global _placed_rooms, _map_data, _map_of_categories
    
    # save map data to be used across functions while building
    _map_data = library.MAPS[map_name]
    
    # get required info from library
    width = _map_data.width
    height = _map_data.height

    # generate the level
    _generate_map_categories(rng, player_data)

    # TODO : add outer border (maybe add size as a global value and make all map take into account?)
    # ensure all borders are walls
    # for x in range(width):
    #     for y in range(height):
    #         if _is_in_map_border(width, height, x, y):
    #             _create_wall_tile(x, y)

    # create the map with tiles
    generated_level = []
    for x in range(width):
        generated_level.append([])
        for y in range(height):
            generated_level[x].append(_create_tile_from_category(x, y, _map_of_categories[x][y]))

    # build generation string
    gen_info = f"{map_name}: \n"
    for room in _placed_rooms:
        gen_info += room.generation_info + "\n"

    # clear existing info
    _map_of_categories = []
    _placed_rooms = []

    return generated_level, gen_info


############################ GENERATE LEVEL ############################

def generate_steps(map_name: str):
    """
    Generates a map, returning each step of the generation. Used for dev view.
    """
    global _placed_rooms, _map_data, _map_of_categories

    # save map data to be used across functions while building
    _map_data = library.MAPS[map_name]

    # create rng
    rng = random.Random()

    # get required info from library
    width = _map_data.width
    height = _map_data.height
    include_shortcuts = _map_data.include_shortcuts
    max_rooms = _map_data.max_rooms

    for step in _generate_map_in_steps(rng, width, height, max_rooms, include_shortcuts):
        yield step


def _generate_map_categories(rng: random.Random, player_data: Optional[ActorData] = None):
    """
    Generates the tile categories on the map.
    """
    width = _map_data.width
    height = _map_data.height
    include_shortcuts = _map_data.include_shortcuts
    max_rooms = _map_data.max_rooms

    for _ in _generate_map_in_steps(rng, width, height, max_rooms, include_shortcuts, player_data):
        pass


def _generate_map_in_steps(rng: random.Random, width: int, height: int, max_rooms: int, include_shortcuts: bool,
        player_data: Optional[ActorData] = None):
    """
    Generate the next step of the level generation.
    """
    global _map_of_categories, _placed_rooms

    rooms_placed = 0
    placement_attempts = 0
    rooms_generated = 0

    # set everything to walls
    _map_of_categories = []
    for x in range(width):
        _map_of_categories.append([])  # create new list for every col
        for y in range(height):
            _map_of_categories[x].append(TileCategory.WALL)

    yield _map_of_categories

    # generate and place rooms
    while rooms_placed <= max_rooms and rooms_generated <= _max_generate_room_attempts:
        intersects = False
        found_place = False

        room = _generate_room(rng)
        rooms_generated += 1

        # find place for the room
        while placement_attempts < _max_place_room_attempts and not found_place:
            placement_attempts += 1

            # pick random location to place room
            room.start_x = start_x = rng.randint(1, max(1, width - room.width))
            room.start_y = start_y = rng.randint(1, max(1, height - room.height))

            # if placed there does room overlap any existing rooms?
            for _room in _placed_rooms:
                if room.intersects(_room):
                    intersects = True
                    break
                else:
                    intersects = False

            if not intersects:
                found_place = True

        if not found_place:
            break

        # doesnt intersect so paint room on map and add room to list
        for x in range(room.width):
            for y in range(room.height):
                _map_of_categories[start_x + x][start_y + y] = room.tile_categories[x][y]

        # place room
        _placed_rooms.append(room)
        rooms_placed += 1

        # do we need to spawn the player?
        if rooms_placed == 1 and player_data:
            world.create_actor(player_data, (start_x, start_y), True)

        # yield map after each room is painted
        yield _map_of_categories

    # handle anything dodgy
    if rooms_placed == 0:
        raise Exception("No rooms placed on the map.")

    # room placement complete, fill tunnels, without connecting to rooms
    for x in range(width):
        for y in range(height):
            # if its a wall, fill it in.
            if _map_of_categories[x][y] == TileCategory.WALL:
                _add_tunnels(x, y, rng)

                # yield map after each set of tunnels added
                yield _map_of_categories

    # join tunnels and rooms
    _join_tunnels_to_rooms(rng)

    # yield map after tunnels connected to rooms
    yield _map_of_categories


############################ GENERATE ROOMS ############################

def _generate_room(rng: random.Random) -> Room:
    """
    Select a room type to generate and return that room. If a generation method isnt provided then one is picked at
    random, using weightings in the data.
    """
    room_weights = _map_data.room_weights
    options = [_generate_cellular_automata_room, _generate_room_square]
    weights = [room_weights["cellular"], room_weights["square"]]

    # pick a generation method based on weights
    _room_generation_method = rng.choices(options, weights, k=1)[0]
    room = _room_generation_method(rng)

    return room


def _generate_cellular_automata_room(rng: random.Random) -> Room:
    """
    Generate a room using cellular automata generation.
    """
    pass
    chance_of_spawning_wall = _map_data.chance_of_spawning_wall
    birth_limit = 4
    death_limit = 3

    # randomly pick a size for the room
    min_tiles_per_side = 4
    width = rng.randint(min_tiles_per_side, _map_data.max_room_areas["cellular"] // min_tiles_per_side)
    min_height = max(min_tiles_per_side, _map_data.min_room_areas["cellular"] // width)
    max_height = max(min_tiles_per_side, _map_data.max_room_areas["cellular"] // width)
    height = rng.randint(min_height, max_height)

    # populate the room with floor
    room_tile_cats = [[TileCategory.FLOOR for y in range(height)] for x in range(width)]

    # randomly place some walls
    for y in range(height):
        for x in range(width):
            if rng.random() <= chance_of_spawning_wall:
                room_tile_cats[x][y] = TileCategory.WALL

    # spawn new walls around neighbours
    for y in range(height):
        for x in range(width):
            num_neighbours = _count_neighbouring_walls(x, y, room_tile_cats)

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
    room = Room(tile_categories=room_tile_cats, design="cellular", category="tbc")
    return room


def _generate_room_square(rng: random.Random) -> Room:
    """
    Generate a square-shaped room.
    """
    room_min_area = _map_data.min_room_areas["square"]
    room_max_area = _map_data.max_room_areas["square"]
    map_height = _map_data.height

    # ensure not bigger than the map
    room_width = rng.randint(room_min_area, room_max_area)
    room_height = min(rng.randint(max(int(room_width * 0.5), room_min_area),
                              min(int(room_width * 1.5), room_max_area)), map_height)

    # populate area with floor categories
    tile_categories = []
    for x in range(room_width - 1):
        tile_categories.append([])
        for y in range(room_height - 1):
            tile_categories[x].append(TileCategory.FLOOR)

    # convert to room
    room = Room(tile_categories=tile_categories, design="square", category="tbc")

    return room


####################### MAP AMENDMENTS ##############################

def _add_shortcuts(rng, width, height):
    """
    Use libtcod's pathfinding to find the distance between two points and put a shortcut between them.
    """
    shortcut_length = _map_data.shortcut_length
    min_pathfinding_distance = _map_data.min_path_distance_for_shortcut

    # initialize the libtcod map
    libtcod_map = libtcod.map_new(width, height)
    _recompute_path_map(width, height, libtcod_map)
    path_map = None

    # check i times for places where shortcuts can be made
    for i in range(_max_generate_shortcut_attempts):
        while True:
            # Pick a random tile
            tile_x = rng.randint(shortcut_length + 1, (width - shortcut_length - 1))
            tile_y = rng.randint(shortcut_length + 1, (height - shortcut_length - 1))

            # look for a wall around the position given
            if _map_of_categories[tile_x][tile_y].blocks_movement:
                if (_map_of_categories[tile_x - 1][tile_y].blocks_movement or
                        _map_of_categories[tile_x + 1][tile_y].blocks_movement or
                        _map_of_categories[tile_x][tile_y - 1].blocks_movement or
                        _map_of_categories[tile_x][tile_y + 1].blocks_movement):
                    break

        # look around the tile for floor tiles
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:  # Exclude the center tile
                    new_x = tile_x + (x * shortcut_length)
                    new_y = tile_y + (y * shortcut_length)
                    if not _map_of_categories[new_x][new_y].blocks_movement:
                        # run pathfinding algorithm between the two points
                        # back to the libtcod nonsense
                        path_map = libtcod.path_new_using_map(libtcod_map)
                        libtcod.path_compute(path_map, tile_x, tile_y, new_x, new_y)
                        distance = libtcod.path_size(path_map)

                        if distance > min_pathfinding_distance:
                            # make shortcut
                            #add_tunnel_to_map(tile_x, tile_y, new_x, new_y)
                            _recompute_path_map(width, height, libtcod_map)

    # destroy the path object
    if path_map is not None:
        libtcod.path_delete(path_map)


def _add_tunnels(x: int, y: int, rng: random.Random):
    """
    Follow a path from origin (xy) setting relevant position in _map_of_categories to TileCategory.FLOOR. Uses flood
    fill.
    """
    global _map_of_categories, _placed_rooms

    to_fill_positions = set()
    to_fill_positions.add((x, y))
    last_direction = (0, 0)
    room_tile_categories = []

    # take note of current positions to be used to create the tunnel room
    end_x = x
    end_y = y

    while to_fill_positions:
        possible_directions = []

        # get next item in set
        _x, _y = to_fill_positions.pop()

        # check for adjacent possible tiles
        for direction in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
            if _is_in_bounds(_x + direction[0], _y + direction[1]):
                if _map_of_categories[_x + direction[0]][_y + direction[1]] == TileCategory.WALL:
                    possible_directions.append(direction)

        if possible_directions:
            # pick a possible position, preferring previous direction
            if last_direction in possible_directions and rng.randint(1, 100) > _chance_of_tunnel_winding:
                new_direction = last_direction
            else:
                new_direction = rng.choice(possible_directions)

            # set new position to floor
            _map_of_categories[_x + new_direction[0]][_y + new_direction[1]] = TileCategory.FLOOR

            # next position to check
            next_x = x + (new_direction[0] * 2)
            next_y = y + (new_direction[1] * 2)
            if _is_in_bounds(next_x, next_y):
                _map_of_categories[next_x][next_y] = TileCategory.FLOOR

                # add next position to be checked
                to_fill_positions.add((next_x, next_y))

            # capture last direction and current xy used
            last_direction = new_direction
            end_x = _x
            end_y = _y

    # get the positions of the tunnel, modifying to start from 1
    for room_x in range(end_x - x - 1):
        room_tile_categories.append([])
        for room_y in range(end_y - y - 1):
            room_tile_categories[room_x].append(_map_of_categories[room_x + x][room_y + y])  # use offset back in pos

    # create the tunnel as a room
    _placed_rooms.append(Room(tile_categories=room_tile_categories, design="flood_fill", category="tunnel",
                              start_x=x, start_y=y))


def _join_tunnels_to_rooms(rng: random.Random):
    """
    Loop all rooms and if it isnt a tunnel then search the outer edge for two adjoining floors and break through to
    link the locations.
    """
    global _placed_rooms, _map_of_categories

    # loop all rooms that aren't tunnels
    for room in _placed_rooms:
        if room.category != "tunnel":
            entrances = 0

            # roll for an extra entrance
            if rng.randint(1, 100) >= _extra_entrance_chance:
                max_entrances = _max_room_entrances + 1
            else:
                max_entrances = _max_room_entrances

            # check top and bottom of room
            for x in range(1, room.width):
                above = ""
                below = ""
                y = 0

                # check top side
                if room.tile_categories[x][0] == TileCategory.WALL:
                    y = 0
                    above = _map_of_categories[x + room.start_x][y + room.start_y - 1]
                    below = _map_of_categories[x + room.start_x][y + room.start_y + 1]


                # check bottom side
                if room.tile_categories[x][room.height - 1] == TileCategory.WALL:
                    y = room.height - 1  # -1 due to counting from 0
                    above = _map_of_categories[x + room.start_x][y + room.start_y - 1]
                    below = _map_of_categories[x + room.start_x][y + room.start_y + 1]


                # check between two walls
                if above == TileCategory.FLOOR and below == TileCategory.FLOOR:
                    # make the wall a flor
                    _map_of_categories[x + room.start_x][y + room.start_y] = TileCategory.FLOOR
                    entrances += 1

                    # if enough entrances placed go to next room
                    if entrances >= max_entrances:
                        break

            # check left and right of room
            for y in range(1, room.height):
                left = ""
                right = ""
                x = 0

                # check left side
                if room.tile_categories[0][y] == TileCategory.WALL:
                    x = 0
                    left = _map_of_categories[x + room.start_x - 1][y + room.start_y]
                    right = _map_of_categories[x + room.start_x + 1][y + room.start_y]

                # check right side
                if room.tile_categories[0][y] == TileCategory.WALL:
                    x = room.width - 1  # -1 due to counting from 0
                    left = _map_of_categories[x + room.start_x - 1][y + room.start_y]
                    right = _map_of_categories[x + room.start_x + 1][y + room.start_y]

                # check between two walls
                if left == TileCategory.FLOOR and right == TileCategory.FLOOR:
                    # make the wall a flor
                    _map_of_categories[x + room.start_x][y + room.start_y] = TileCategory.FLOOR
                    entrances += 1

                    # if enough entrances placed go to next room
                    if entrances >= max_entrances:
                        break


######################### QUERIES & HELPER FUNCTIONS #################################

def _count_neighbouring_walls(x: int, y: int, tile_categories: List[List[TileCategoryType]]) -> int:
    """
    Get the number of walls in 8 directions.
    """
    wall_counter = 0
    width = len(tile_categories)
    height = len(tile_categories[0])

    for neighbor_x in range(x - 1, x + 2):
        for neighbor_y in range(y - 1, y + 2):
            # Edges are considered alive. Makes map more likely to appear naturally closed.
            if neighbor_x < 0 or neighbor_y < 0 or neighbor_y >= height or neighbor_x >= width:
                wall_counter += 1
            elif tile_categories[neighbor_x][neighbor_y] == TileCategory.WALL:
                # exclude (x,y) from adjacency check
                if (neighbor_x != x) or (neighbor_y != y):
                    wall_counter += 1

    return wall_counter


def _recompute_path_map(width: int, height: int, libtcod_map):
    """
    Recompute the pathfinding on the libtcod map. Updates the map directly.
    """
    for x in range(width):
        for y in range(height):
            if _map_of_categories[x][y] == 1:
                libtcod.map_set_properties(libtcod_map, x, y, False, False)
            else:
                libtcod.map_set_properties(libtcod_map, x, y, True, True)


def _is_in_map_border(width: int, height: int, x: int, y: int) -> bool:
    """
    Returns a bool if given position is in the map's border
    """
    border_size = 4

    if (x <= border_size or x >= (width - border_size)) or (y <= border_size or y >= (height - border_size)):
        return True
    else:
        return False


def _is_in_bounds(x: int, y: int):
    """
    Check if a position is in the bounds of the map
    """
    width = _map_data.width
    height = _map_data.height

    if 0 < x < width - 1 and 0 < y < height - 1:
        return True
    else:
        return False


def _create_tile_from_category(x: int, y: int, tile_category: TileCategoryType) -> Tile:
    """
    Convert a tile category into the relevant tile
    """
    if tile_category == TileCategory.WALL:
        sprite_path = _map_data.wall_sprite_path
        sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
        blocks_sight = True
        blocks_movement = True
    elif tile_category == TileCategory.FLOOR:
        sprite_path = _map_data.floor_sprite_path
        sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
        blocks_sight = False
        blocks_movement = False

    tile = Tile(x, y, sprite, sprite_path, blocks_sight, blocks_movement)


    return tile
