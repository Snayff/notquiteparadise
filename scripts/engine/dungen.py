from __future__ import annotations
from typing import TYPE_CHECKING, Type

import random
import pygame
import tcod as libtcod

from scripts.engine import library
from scripts.engine.core.constants import Direction, TILE_SIZE
from scripts.engine.core.definitions import MapData

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List
    from scripts.engine.world_objects.tile import Tile

# containers
_rooms: List[Tuple[Tuple[int, int], List[List[int]]]] = []
_level: List[List[int]] = []
_tunnels: List[Tuple[Tuple[int, int], Tuple[int, int], int]] = []
_map_data: MapData = MapData()

# parameters/config
_generate_room_attempts = 500
_place_room_attempts = 20
_generate_shortcut_attempts = 500


def generate(map_name: str, rng: random.Random) -> Tuple[List[List[Tile]],
List[Tuple[Tuple[int, int], List[List[int]]]], List[Tuple[Tuple[int, int], Tuple[int, int], int]]]:
    """
    Generate the map using the specified details.
    """
    global _level, _rooms, _tunnels, _map_data
    
    # save map data to be used across functions while building
    _map_data = library.MAPS[map_name]
    
    # get required info from library
    width = _map_data.width
    height = _map_data.height

    
    # generate the level
    generate_level(rng)

    # ensure all borders are walls
    for x in range(width):
        for y in range(height):
            if _is_map_border(width, height, x, y):
                _get_wall_tile(x, y)

    # TODO - throughout module, replace assigning 1 or 0 with get floor or wall

    # copy value to be returned to a local var
    generated_level = _level

    # build generation string
    gen_info = ""
    # TODO - build the info

    # clear existing info
    _level = []
    _tunnels = []
    _rooms = []

    return generated_level, gen_info


def _get_wall_tile(x: int, y: int) -> Tile:
    """
    Gets a wall tile for the current map
    """
    from scripts.engine import utility
    wall_sprite_path = _map_data.wall_sprite_path
    wall_sprite = utility.get_image(wall_sprite_path, (TILE_SIZE, TILE_SIZE))
    blocks_sight = True
    blocks_movement = True

    tile = Tile(x, y, wall_sprite, wall_sprite_path, blocks_sight, blocks_movement)

    return tile


def _get_floor_tile(x: int, y: int) -> Tile:
    """
    Makes the tile at the coordinate a floor
    """
    from scripts.engine import utility
    floor_sprite_path = _map_data.floor_sprite_path
    floor_sprite = utility.get_image(floor_sprite_path, (TILE_SIZE, TILE_SIZE))
    blocks_sight = False
    blocks_movement = False

    tile = Tile(x, y, floor_sprite, floor_sprite_path, blocks_sight, blocks_movement)

    return tile


############################ GENERATE LEVEL ############################

def generate_steps(rng: random.Random):
    """
    Generates the map, returning each step of the generation
    :return: The state of the map at a step
    """
    width = _map_data.width
    height = _map_data.height
    include_shortcuts = _map_data.include_shortcuts
    max_rooms = _map_data.max_rooms

    for step in generate_level_steps(rng, width, height, max_rooms, include_shortcuts):
        yield step


def generate_level(rng: random.Random):
    """
    Generates the map.
    :return: The completed map.
    """
    width = _map_data.width
    height = _map_data.height
    include_shortcuts = _map_data.include_shortcuts
    max_rooms = _map_data.max_rooms

    for _ in generate_level_steps(rng, width, height, max_rooms, include_shortcuts):
        pass
    return _level


def generate_level_steps(rng: random.Random, width: int, height: int, max_rooms: int, include_shortcuts: bool):
    """
    Generate the next step of the level generation.
    """
    global _level
    
    _level = [[1 for _ in range(height)] for _ in range(width)]
    yield _level

    # generate the first room
    room = generate_room(rng)
    room_width, room_height = get_room_dimensions(room)
    room_x = int((width / 2 - room_width / 2) - 1)
    room_y = int((height / 2 - room_height / 2) - 1)
    add_room(room_x, room_y, room)
    yield _level
    
    # generate other rooms
    for i in range(_generate_room_attempts):
        room = generate_room(rng)

        # try to position the room, get room_x and room_y
        room_x, room_y, wall_tile, direction, tunnel_length = place_room(rng, room, width, height)
        if room_x and room_y:
            add_room(room_x, room_y, room)
            yield _level
            add_tunnel(wall_tile, direction, tunnel_length)
            yield _level
            if len(_rooms) >= max_rooms:
                break
    yield _level
    if include_shortcuts:
        add_shortcuts(rng, width, height)


############################ GENERATE ROOMS ############################

def generate_room(rng: random.Random):
    """
    select a room type to generate
    generate and return that room
    """
    room_weights = _map_data.room_weights
    options = [generate_room_square, generate_room_cross, generate_room_cellular_automata, generate_room_cavern]
    weights = [room_weights["square"], room_weights["cross"], room_weights["cellular"], room_weights["cavern"]]
    
    # pick a generation method based on weights
    room_generation = rng.choices(options, weights, k=1)[0]
    room = room_generation(rng)

    return room


def generate_room_cross(rng: random.Random):
    """
    Generate a cross shaped room.
    """
    room_min_area = _map_data.min_room_areas["cross"]
    room_max_area = _map_data.max_room_areas["cross"]

    room_hor_width = int((rng.randint(room_min_area + 2, room_max_area)) / 2 * 2)

    room_ver_height = int((rng.randint(room_min_area + 2, room_max_area)) / 2 * 2)

    room_hor_height = int((rng.randint(room_min_area, room_ver_height - 2)) / 2 * 2)

    room_ver_width = int((rng.randint(room_min_area, room_hor_width - 2)) / 2 * 2)

    room = [[1
             for y in range(room_ver_height)]
            for x in range(room_hor_width)]

    # Fill in horizontal space
    ver_offset = int(room_ver_height / 2 - room_hor_height / 2)
    for y in range(ver_offset, room_hor_height + ver_offset):
        for x in range(0, room_hor_width):
            room[x][y] = 0

    # Fill in vertical space
    hor_offset = int(room_hor_width / 2 - room_ver_width / 2)
    for y in range(0, room_ver_height):
        for x in range(hor_offset, room_ver_width + hor_offset):
            room[x][y] = 0

    return room


def generate_room_square(rng: random.Random):
    """
    Generate a square-shaped room.
    """
    room_min_area = _map_data.min_room_areas["square"]
    room_max_area = _map_data.max_room_areas["square"]
    
    room_width = rng.randint(room_min_area, room_max_area)
    room_height = rng.randint(max(int(room_width * 0.5), room_min_area),
                              min(int(room_width * 1.5), room_max_area))

    room = [[0
             for y in range(1, room_height - 1)]
            for x in range(1, room_width - 1)]

    return room


def generate_room_cellular_automata(rng):
    """
    Generate a square-shaped room.
    """
    room_max_area = _map_data.max_room_areas["cellular"]
    wall_probability = _map_data.chance_of_in_room_wall
    neighbours = _map_data.max_neighbouring_walls_in_room
    
    while True:
        # if a room is too small, generate another
        room = [[1
                 for y in range(room_max_area)]
                for x in range(room_max_area)]

        # random fill map
        for y in range(2, room_max_area - 2):
            for x in range(2, room_max_area - 2):
                if rng.random() >= wall_probability:
                    room[x][y] = 0

        # create distinctive regions
        for i in range(4):
            for y in range(1, room_max_area - 1):
                for x in range(1, room_max_area - 1):

                    # if the cell's neighboring walls > neighbours, set it to 1
                    if get_adjacent_walls(x, y, room) > neighbours:
                        room[x][y] = 1
                    # otherwise, set it to 0
                    elif get_adjacent_walls(x, y, room) < neighbours:
                        room[x][y] = 0

        # flood fill to remove small caverns
        room = flood_fill(room)

        # start over if the room is completely filled in
        room_width, room_height = get_room_dimensions(room)
        for x in range(room_width):
            for y in range(room_height):
                if room[x][y] == 0:
                    return room


def generate_room_cavern(rng):
    """
    Generate a square-shaped room.
    """
    room_max_area = _map_data.max_room_areas["cavern"]
    neighbours = _map_data.max_neighbouring_walls_in_room
    wall_probability = _map_data.chance_of_in_room_wall

    while True:
        # if a room is too small, generate another
        room = [[1
                 for y in range(room_max_area)]
                for x in range(room_max_area)]

        # random fill map
        for y in range(2, room_max_area - 2):
            for x in range(2, room_max_area - 2):
                if rng.random() >= wall_probability:
                    room[x][y] = 0

        # create distinctive regions
        for i in range(4):
            for y in range(1, room_max_area - 1):
                for x in range(1, room_max_area - 1):

                    # if the cell's neighboring walls > neighbours, set it to 1
                    if get_adjacent_walls(x, y, room) > neighbours:
                        room[x][y] = 1
                    # otherwise, set it to 0
                    elif get_adjacent_walls(x, y, room) < neighbours:
                        room[x][y] = 0

        # flood fill to remove small caverns
        room = flood_fill(room)

        # start over if the room is completely filled in
        room_width, room_height = get_room_dimensions(room)
        for x in range(room_width):
            for y in range(room_height):
                if room[x][y] == 0:
                    return room


def flood_fill(room):
    """
    Find the largest region. Fill in all other regions.
    """
    room_width, room_height = get_room_dimensions(room)
    min_room_area = min(_map_data.min_room_areas.values())
    largest_region = set()

    for x in range(room_width):
        for y in range(room_height):
            if room[x][y] == 0:
                new_region = set()
                tile = (x, y)
                to_be_filled = set([tile])
                while to_be_filled:
                    tile = to_be_filled.pop()

                    if tile not in new_region:
                        new_region.add(tile)

                        room[tile[0]][tile[1]] = 1

                        # check adjacent cells
                        x = tile[0]
                        y = tile[1]
                        north = (x, y - 1)
                        south = (x, y + 1)
                        east = (x + 1, y)
                        west = (x - 1, y)

                        for direction in [north, south, east, west]:

                            if room[direction[0]][direction[1]] == 0:
                                if direction not in to_be_filled and direction not in new_region:
                                    to_be_filled.add(direction)

                if len(new_region) >= min_room_area:
                    if len(new_region) > len(largest_region):
                        largest_region.clear()
                        largest_region.update(new_region)

    for tile in largest_region:
        room[tile[0]][tile[1]] = 0

    return room


####################### PLACEMENT ##############################

def place_room(rng: random.Random, room, width: int, height: int):
    """
    Place a generated room on the map, checking for an appropriate place.
    """
    room_width, room_height = get_room_dimensions(room)
    max_tunnel_length = _map_data.max_tunnel_length

    # try n times to find a wall that lets you build room in that direction
    for i in range(_place_room_attempts):
        # try to place the room against the tile, else connected by a tunnel of length i
        wall_tile = None
        direction = rng.choice([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])
        while not wall_tile:
            # randomly select tiles until you find a wall that has another wall in the chosen direction and has a
            # floor in the opposite direction.
            tile_x = rng.randint(1, width - 2)
            tile_y = rng.randint(1, height - 2)
            if ((_level[tile_x][tile_y] == 1) and
                    (_level[tile_x + direction[0]][tile_y + direction[1]] == 1) and
                    (_level[tile_x - direction[0]][tile_y - direction[1]] == 0)):
                wall_tile = (tile_x, tile_y)

        # spawn the room touching wall_tile
        start_room_x = None
        start_room_y = None

        # FIXME: replace this with a method that returns a random floor tile instead of the top left floor tile
        while not start_room_x and not start_room_y:
            x = rng.randint(0, room_width - 1)
            y = rng.randint(0, room_height - 1)
            if room[x][y] == 0:
                start_room_x = wall_tile[0] - x
                start_room_y = wall_tile[1] - y

        # then slide it until it doesn't touch anything
        for tunnel_length in range(max_tunnel_length):
            possible_room_x = start_room_x + direction[0] * tunnel_length
            possible_room_y = start_room_y + direction[1] * tunnel_length

            enough_room = get_overlap(room, possible_room_x, possible_room_y, width, height)

            if enough_room:
                room_x = possible_room_x
                room_y = possible_room_y

                return room_x, room_y, wall_tile, direction, tunnel_length

    return None, None, None, None, None


def add_room(x: int, y: int, room):
    """
    Add a room to the specified place on the map.
    """
    global _rooms

    room_width, room_height = get_room_dimensions(room)
    for x in range(room_width):
        for y in range(room_height):
            if room[x][y] == 0:
                _level[x + x][y + y] = 0

    _rooms.append(((x, y), room))


def add_tunnel(wall_tile, direction, tunnel_length):
    """
    Add a tunnel from a point in the room back to the wall tile that was used in its original placement
    """
    global _tunnels

    max_tunnel_length = _map_data.max_tunnel_length
    real_length = 0
    x, y = 0, 0

    start_x = wall_tile[0] + direction[0] * tunnel_length
    start_y = wall_tile[1] + direction[1] * tunnel_length

    for i in range(max_tunnel_length):
        x = start_x - direction[0] * i
        y = start_y - direction[1] * i
        _level[x][y] = 0
        real_length += 1
        # N.B. If you want doors, this is where the code should go
        if (x + direction[0]) == wall_tile[0] and (y + direction[1]) == wall_tile[1]:
            break
    tunnel = ((x, y), (direction[0], direction[1]), real_length)
    _tunnels.append(tunnel)


def carve_shortcut(x1: int, y1: int, x2: int, y2: int):
    """
    Create a tunnel between two positions.
    """
    if x1 - x2 == 0:
        # Carve vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            _level[x1][y] = 0

    elif y1 - y2 == 0:
        # Carve Horizontal tunnel
        for x in range(min(x1, x2), max(x1, x2) + 1):
            _level[x][y1] = 0

    elif (y1 - y2) / (x1 - x2) == 1:
        # Carve NW to SE Tunnel
        x = min(x1, x2)
        y = min(y1, y2)
        while x != max(x1, x2):
            x += 1
            _level[x][y] = 0
            y += 1
            _level[x][y] = 0

    elif (y1 - y2) / (x1 - x2) == -1:
        # Carve NE to SW Tunnel
        x = min(x1, x2)
        y = max(y1, y2)
        while x != max(x1, x2):
            x += 1
            _level[x][y] = 0
            y -= 1
            _level[x][y] = 0


def add_shortcuts(rng, width, height):
    """
    Use libtcod's pathfinding to find the distance between two points and put a shortcut between them.
    """
    shortcut_length = _map_data.shortcut_length
    min_pathfinding_distance = _map_data.min_path_distance_for_shortcut

    # initialize the libtcod map
    libtcod_map = libtcod.map_new(width, height)
    recompute_path_map(width, height, libtcod_map)
    path_map = None

    # check i times for places where shortcuts can be made
    for i in range(_generate_shortcut_attempts):
        while True:
            # Pick a random floor tile
            floor_x = rng.randint(shortcut_length + 1, (width - shortcut_length - 1))
            floor_y = rng.randint(shortcut_length + 1, (height - shortcut_length - 1))
            if _level[floor_x][floor_y] == 0:
                if (_level[floor_x - 1][floor_y] == 1 or
                        _level[floor_x + 1][floor_y] == 1 or
                        _level[floor_x][floor_y - 1] == 1 or
                        _level[floor_x][floor_y + 1] == 1):
                    break

        # look around the tile for other floor tiles
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:  # Exclude the center tile
                    new_x = floor_x + (x * shortcut_length)
                    new_y = floor_y + (y * shortcut_length)
                    if _level[new_x][new_y] == 0:
                        # run pathfinding algorithm between the two points
                        # back to the libtcod nonsense
                        path_map = libtcod.path_new_using_map(libtcod_map)
                        libtcod.path_compute(path_map, floor_x, floor_y, new_x, new_y)
                        distance = libtcod.path_size(path_map)

                        if distance > min_pathfinding_distance:
                            # make shortcut
                            carve_shortcut(floor_x, floor_y, new_x, new_y)
                            recompute_path_map(width, height, libtcod_map)

    # destroy the path object
    if path_map is not None:
        libtcod.path_delete(path_map)


######################### QUERIES & HELPER FUNCTIONS #################################

def get_room_dimensions(room) -> Tuple[int, int]:
    """
    Get the width and height of the room.
    """
    if room:
        room_width = len(room)
        room_height = len(room[0])
        return room_width, room_height
    else:
        room_width = 0
        room_height = 0
        return room_width, room_height


def get_adjacent_walls(x, y, room) -> int:
    """
    Get the number of  walls in 8 directions
    """
    wall_counter = 0
    for _x in range(x - 1, x + 2):
        for _y in range(y - 1, y + 2):
            if room[_x][_y] == 1:
                # exclude (x,y) from adjacency check
                if (_x != x) or (_y != y):
                    wall_counter += 1
    return wall_counter


def get_overlap(room, room_x, room_y, width, height):
    """
    for each 0 in room, check the corresponding tile in
    _level and the eight tiles around it. Though slow,
    that should insure that there is a wall between each of
    the rooms created in this way.
    """
    room_width, room_height = get_room_dimensions(room)
    for x in range(room_width):
        for y in range(room_height):
            if room[x][y] == 0:
                # Check to see if the room is out of bounds
                if ((1 <= (x + room_x) < width - 1) and
                        (1 <= (y + room_y) < height - 1)):
                    # Check for overlap with a one tile buffer
                    if _level[x + room_x - 1][y + room_y - 1] == 0:  # top left
                        return False
                    if _level[x + room_x][y + room_y - 1] == 0:  # top center
                        return False
                    if _level[x + room_x + 1][y + room_y - 1] == 0:  # top right
                        return False

                    if _level[x + room_x - 1][y + room_y] == 0:  # left
                        return False
                    if _level[x + room_x][y + room_y] == 0:  # center
                        return False
                    if _level[x + room_x + 1][y + room_y] == 0:  # right
                        return False

                    if _level[x + room_x - 1][y + room_y + 1] == 0:  # bottom left
                        return False
                    if _level[x + room_x][y + room_y + 1] == 0:  # bottom center
                        return False
                    if _level[x + room_x + 1][y + room_y + 1] == 0:  # bottom right
                        return False

                else:  # room is out of bounds
                    return False
    return True


def recompute_path_map(width: int, height: int, libtcod_map):
    """
    Recompute the pathfinding on the libtcod map. Updates the map directly.
    """
    for x in range(width):
        for y in range(height):
            if _level[x][y] == 1:
                libtcod.map_set_properties(libtcod_map, x, y, False, False)
            else:
                libtcod.map_set_properties(libtcod_map, x, y, True, True)


def _is_map_border(width: int, height: int, x: int, y: int) -> bool:
    """
    Returns a bool if given position is in the map's border
    """
    border_size = 4

    if (x <= border_size or x >= (width - border_size)) or (y <= border_size or y >= (height - border_size)):
        return True
    else:
        return False
