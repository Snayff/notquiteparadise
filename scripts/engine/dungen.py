from __future__ import annotations
from typing import TYPE_CHECKING

import random
import tcod as libtcod

from scripts.engine import library
from scripts.engine.core.constants import Direction, DirectionType, TILE_SIZE, TileCategory, TileCategoryType
from scripts.engine.core.definitions import MapData
from scripts.engine.world_objects.tile import Tile
from scripts.engine.world_objects.room import Room

if TYPE_CHECKING:
    from typing import Optional, Tuple, List

# containers
_placed_rooms: List[Room] = []  # rooms created
_map: List[List[Tile]] = []  # list of list of tiles to be passed back to the gamemap
_map_data: MapData = MapData()

# parameters/config
_generate_room_attempts = 100
_place_room_attempts = 20
_generate_shortcut_attempts = 100


def generate(map_name: str, rng: random.Random) -> Tuple[List[List[Tile]], str]:
    """
    Generate the map using the specified details.
    """
    global _map, _placed_rooms, _map_data
    
    # save map data to be used across functions while building
    _map_data = library.MAPS[map_name]
    
    # get required info from library
    width = _map_data.width
    height = _map_data.height

    # generate the level
    generate_map(rng)

    # ensure all borders are walls
    for x in range(width):
        for y in range(height):
            if _is_in_map_border(width, height, x, y):
                _create_wall_tile(x, y)

    # copy value to be returned to a local var
    generated_level = _map

    # build generation string
    gen_info = f"{map_name}: \n"
    for room in _placed_rooms:
        gen_info += room.generation_info + "\n"

    # clear existing info
    _map = []
    _placed_rooms = []

    return generated_level, gen_info


def _create_wall_tile(x: int, y: int) -> Tile:
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


def _create_floor_tile(x: int, y: int) -> Tile:
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

    for step in generate_map_in_steps(rng, width, height, max_rooms, include_shortcuts):
        yield step


def generate_map(rng: random.Random):
    """
    Generates the map.
    :return: The completed map.
    """
    width = _map_data.width
    height = _map_data.height
    include_shortcuts = _map_data.include_shortcuts
    max_rooms = _map_data.max_rooms

    for _ in generate_map_in_steps(rng, width, height, max_rooms, include_shortcuts):
        pass
    return _map


def generate_map_in_steps(rng: random.Random, width: int, height: int, max_rooms: int, include_shortcuts: bool):
    """
    Generate the next step of the level generation.
    """
    global _map

    # set everything to walls
    _map = [[_create_wall_tile(x, y)
        for y in range(height)]
        for x in range(width)]
    yield _map

    # generate the first room in the centre of the map
    room = generate_room(rng)
    if not room:
        raise Exception("Failed to generate level.")
    # pick random position to place the first room
    room_x = rng.randint(4, width - (room.width - 4))
    room_y = rng.randint(4, height - (room.height - 4))
    add_room_to_map(room_x, room_y, room)
    yield _map
    
    # generate other rooms
    # for i in range(_generate_room_attempts):
    #     room = generate_room(rng)
    #
    #     # try to find a position for the room
    #     room_pos, tunnel_pos, direction, tunnel_length = find_place_for_next_room(rng, room, width, height)
    #     if room_pos:
    #         add_room_to_map(room_pos[0], room_pos[1], room)
    #         yield _map
    #
    #         # from previous room
    #         add_direct_tunnel_to_map(tunnel_pos, direction, tunnel_length)
    #         yield _map
    #
    #         # check if enough rooms are places
    #         if len(_placed_rooms) >= max_rooms:
    #             break
    # yield _map
    # if include_shortcuts:
    #     add_shortcuts(rng, width, height)


############################ GENERATE ROOMS ############################

def generate_room(rng: random.Random) -> Room:
    """
    Select a room type to generate and return that room
    """
    room_weights = _map_data.room_weights
    options = [_generate_cellular_automata_room]
    weights = [room_weights["cellular"]]

    # pick a generation method based on weights
    room_generation_method = rng.choices(options, weights, k=1)[0]
    room = room_generation_method(rng)

    return room


def _generate_cellular_automata_room(rng: random.Random) -> Room:
    """
    Generate a room using cellular automata generation.
    """
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
            num_neighbours = count_neighbouring_walls(x, y, room_tile_cats)

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
    room = Room(tile_categories=room_tile_cats, design="cellular")
    return room

####################### PLACEMENT ##############################

def find_place_for_next_room(rng: random.Random, room: Room, width: int,
        height: int) -> Optional[Tuple[Tuple[int, int], Tuple[int, int], Direction, int]]:
    """
    Find am appropriate place for a room.

    :returns: room_placement_position, tunnel_placement_position, tunnel_direction, tunnel_length
    """
    room_width = room.width
    room_height = room.height
    max_tunnel_length = _map_data.max_tunnel_length

    # try n times to find a wall that lets you build room in that direction
    for i in range(_place_room_attempts):
        # try to place the room against the tile, else connected by a tunnel of length i
        tunnel_placement_position = None
        direction = rng.choice([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])
        while not tunnel_placement_position:
            # randomly select tiles until you find a wall that has another wall in the chosen direction and has a
            # floor in the opposite direction.
            tile_x = rng.randint(1, width - 2)
            tile_y = rng.randint(1, height - 2)
            if (_map[tile_x][tile_y].blocks_movement and
                    _map[tile_x + direction[0]][tile_y + direction[1]].blocks_movement and
                    not _map[tile_x - direction[0]][tile_y - direction[1]].blocks_movement):
                tunnel_placement_position = (tile_x, tile_y)

        # spawn the room touching wall_tile
        start_room_x = None
        start_room_y = None
        while not start_room_x and not start_room_y:
            x = rng.randint(0, room_width - 1)
            y = rng.randint(0, room_height - 1)
            if room.tile_categories[x][y] == TileCategory.FLOOR:
                start_room_x = tunnel_placement_position[0] - x
                start_room_y = tunnel_placement_position[1] - y

        # then slide it until it doesn't touch anything
        for tunnel_length in range(max_tunnel_length):
            possible_room_x = start_room_x + direction[0] * tunnel_length
            possible_room_y = start_room_y + direction[1] * tunnel_length

            has_enough_room = has_walled_exterior(room, possible_room_x, possible_room_y, width, height)

            if has_enough_room:
                room_x = possible_room_x
                room_y = possible_room_y

                return (room_x, room_y), tunnel_placement_position, direction, tunnel_length

    return None


def add_room_to_map(x: int, y: int, room: Room):
    """
    Add a room to the specified place on the map. Converts TileCategory to Tile.
    """
    global _placed_rooms, _map

    width = room.width
    height = room.height
    for _x in range(width):
        for _y in range(height):
            # use given xy and offset with tile xy to add Tile to map
            if room.tile_categories[_x][_y] == TileCategory.FLOOR:
                _map[x + _x][y + _y] = _create_floor_tile(x + _x, y + _y)
            else:
                _map[x + _x][y + _y] = _create_wall_tile(x + _x, y + _y)

    # add to room list
    _placed_rooms.append(room)


def add_direct_tunnel_to_map(tunnel_pos: Tuple[int, int], direction: DirectionType, tunnel_length: int):
    """
    Add a tunnel from a point in a direction for a specified length.
    """
    global _tunnels, _map

    max_tunnel_length = _map_data.max_tunnel_length
    real_length = 0
    x, y = 0, 0

    start_x = tunnel_pos[0] + direction[0] * tunnel_length
    start_y = tunnel_pos[1] + direction[1] * tunnel_length

    for i in range(max_tunnel_length):
        x = start_x - direction[0] * i
        y = start_y - direction[1] * i
        _map[x][y] = _create_floor_tile(x, y)
        real_length += 1
        if (x + direction[0]) == tunnel_pos[0] and (y + direction[1]) == tunnel_pos[1]:
            break


def add_indirect_tunnel_to_map(x1: int, y1: int, x2: int, y2: int):
    """
    Add a tunnel between two positions.
    """
    global _map

    if x1 - x2 == 0:
        # Carve vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            _map[x1][y] = _create_floor_tile(x1, y)

    elif y1 - y2 == 0:
        # Carve Horizontal tunnel
        for x in range(min(x1, x2), max(x1, x2) + 1):
            _map[x][y1] = _create_floor_tile(x, y1)

    elif (y1 - y2) / (x1 - x2) == 1:
        # Carve NW to SE Tunnel
        x = min(x1, x2)
        y = min(y1, y2)
        while x != max(x1, x2):
            x += 1
            _map[x][y] = _create_floor_tile(x, y)
            y += 1
            _map[x][y] = _create_floor_tile(x, y)

    elif (y1 - y2) / (x1 - x2) == -1:
        # Carve NE to SW Tunnel
        x = min(x1, x2)
        y = max(y1, y2)
        while x != max(x1, x2):
            x += 1
            _map[x][y] = _create_floor_tile(x, y)
            y -= 1
            _map[x][y] = _create_floor_tile(x, y)


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
            # Pick a random tile
            tile_x = rng.randint(shortcut_length + 1, (width - shortcut_length - 1))
            tile_y = rng.randint(shortcut_length + 1, (height - shortcut_length - 1))

            # look for a wall around the position given
            if _map[tile_x][tile_y].blocks_movement:
                if (_map[tile_x - 1][tile_y].blocks_movement or
                        _map[tile_x + 1][tile_y].blocks_movement or
                        _map[tile_x][tile_y - 1].blocks_movement or
                        _map[tile_x][tile_y + 1].blocks_movement):
                    break

        # look around the tile for floor tiles
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:  # Exclude the center tile
                    new_x = tile_x + (x * shortcut_length)
                    new_y = tile_y + (y * shortcut_length)
                    if not _map[new_x][new_y].blocks_movement:
                        # run pathfinding algorithm between the two points
                        # back to the libtcod nonsense
                        path_map = libtcod.path_new_using_map(libtcod_map)
                        libtcod.path_compute(path_map, tile_x, tile_y, new_x, new_y)
                        distance = libtcod.path_size(path_map)

                        if distance > min_pathfinding_distance:
                            # make shortcut
                            add_indirect_tunnel_to_map(tile_x, tile_y, new_x, new_y)
                            recompute_path_map(width, height, libtcod_map)

    # destroy the path object
    if path_map is not None:
        libtcod.path_delete(path_map)


######################### QUERIES & HELPER FUNCTIONS #################################


def count_neighbouring_walls(x: int, y: int, tile_categories: List[List[TileCategoryType]]) -> int:
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


def has_walled_exterior(room: Room, room_x: int, room_y: int, width: int, height: int) -> bool:
    """
    For each tile in room, check the corresponding tile in _map and the eight tiles around it. Though slow,
    that should insure that there is a wall between each of the rooms created in this way.
    """
    room_width = room.width
    room_height = room.height

    for x in range(room_width):
        for y in range(room_height):
            if room.tile_categories[x][y] == TileCategory.FLOOR:
                # Check to see if the room is out of bounds
                if (1 <= (x + room_x) < width - 1) and (1 <= (y + room_y) < height - 1):
                    # Check for overlap with a one tile buffer
                    if _map[x + room_x - 1][y + room_y - 1] == TileCategory.FLOOR:  # top left
                        return False
                    if _map[x + room_x][y + room_y - 1] == TileCategory.FLOOR:  # top center
                        return False
                    if _map[x + room_x + 1][y + room_y - 1] == TileCategory.FLOOR:  # top right
                        return False

                    if _map[x + room_x - 1][y + room_y] == TileCategory.FLOOR:  # left
                        return False
                    if _map[x + room_x][y + room_y] == TileCategory.FLOOR:  # center
                        return False
                    if _map[x + room_x + 1][y + room_y] == TileCategory.FLOOR:  # right
                        return False

                    if _map[x + room_x - 1][y + room_y + 1] == TileCategory.FLOOR:  # bottom left
                        return False
                    if _map[x + room_x][y + room_y + 1] == TileCategory.FLOOR:  # bottom center
                        return False
                    if _map[x + room_x + 1][y + room_y + 1] == TileCategory.FLOOR:  # bottom right
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
            if _map[x][y] == 1:
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



################################## NOT WORKING ###########################

# def generate_room_cross(rng: random.Random) -> Room:
#     """
#     Generate a cross shaped room.
#     """
#     room_min_area = _map_data.min_room_areas["cross"]
#     room_max_area = _map_data.max_room_areas["cross"]
#
#     room_hor_width = int((rng.randint(room_min_area + 2, room_max_area)) / 2 * 2)
#     room_ver_width = int((rng.randint(room_min_area, room_hor_width - 2)) / 2 * 2)
#     room_ver_height = int((rng.randint(room_min_area + 2, room_max_area)) / 2 * 2)
#     room_hor_height = int((rng.randint(room_min_area, room_ver_height - 2)) / 2 * 2)
#
#     # fill with walls
#     tile_categories = [[TileCategory.WALL
#         for y in range(room_ver_height)]
#         for x in range(room_hor_width)]
#
#     # Fill in horizontal space
#     ver_offset = int(room_ver_height / 2 - room_hor_height / 2)
#     for y in range(ver_offset, room_hor_height + ver_offset):
#         for x in range(0, room_hor_width):
#             tile_categories[x][y] = TileCategory.FLOOR
#
#     # Fill in vertical space
#     hor_offset = int(room_hor_width / 2 - room_ver_width / 2)
#     for y in range(0, room_ver_height):
#         for x in range(hor_offset, room_ver_width + hor_offset):
#             tile_categories[x][y] = TileCategory.FLOOR
#
#     # convert to room
#     room = Room(tile_categories=tile_categories, design="cross")
#
#     return room
#
#
# def generate_room_square(rng: random.Random) -> Room:
#     """
#     Generate a square-shaped room.
#     """
#     room_min_area = _map_data.min_room_areas["square"]
#     room_max_area = _map_data.max_room_areas["square"]
#
#     room_width = rng.randint(room_min_area, room_max_area)
#     room_height = rng.randint(max(int(room_width * 0.5), room_min_area),
#                               min(int(room_width * 1.5), room_max_area))
#
#     tile_categories = [[TileCategory.FLOOR
#         for y in range(1, room_height - 1)]
#         for x in range(1, room_width - 1)]
#
#     # convert to room
#     room = Room(tile_categories=tile_categories, design="square")
#
#     return room
#
#
# def generate_room_cellular_automata(rng) -> Room:
#     """
#     Generate a room using cellular automata.
#     """
#     room_max_area = _map_data.max_room_areas["cellular"]
#     wall_probability = _map_data.chance_of_spawning_wall
#     neighbours = _map_data.max_neighbouring_walls_in_room
#
#     for _ in range(_generate_room_attempts):
#
#         # fill with floor
#         tile_categories = [[TileCategory.FLOOR
#             for y in range(room_max_area)]
#             for x in range(room_max_area)]
#
#         # random fill map
#         for y in range(2, room_max_area - 2):
#             for x in range(2, room_max_area - 2):
#                 if rng.random() >= wall_probability:
#                     tile_categories[x][y] = TileCategory.WALL
#
#         # create distinctive regions
#         for i in range(4):
#             for y in range(1, room_max_area - 1):
#                 for x in range(1, room_max_area - 1):
#
#                     # if the cell's neighboring walls > neighbours, set it to 1
#                     if count_neighbouring_walls(x, y, tile_categories) > neighbours:
#                         tile_categories[x][y] = TileCategory.WALL
#                     # otherwise, set it to 0
#                     elif count_neighbouring_walls(x, y, tile_categories) < neighbours:
#                         tile_categories[x][y] = TileCategory.FLOOR
#
#         # flood fill to remove small caverns
#         tile_categories = flood_fill(tile_categories)
#
#         # convert to room
#         room = Room(tile_categories=tile_categories, design="cellular")
#
#         # start over if the room is completely filled in
#         width = room.width
#         height = room.height
#         for x in range(width):
#             for y in range(height):
#                 if tile_categories[x][y] == TileCategory.FLOOR:
#                     # return non entirely-filled room
#                     return room
#
#
# def generate_room_cavern(rng):
#     """
#     Generate a cavern-type room.
#     """
#     room_max_area = _map_data.max_room_areas["cavern"]
#     neighbours = _map_data.max_neighbouring_walls_in_room
#     wall_probability = _map_data.chance_of_spawning_wall
#
#     while True:
#         tile_categories = [[TileCategory.WALL
#             for y in range(room_max_area)]
#             for x in range(room_max_area)]
#
#         # random fill map
#         for y in range(2, room_max_area - 2):
#             for x in range(2, room_max_area - 2):
#                 if rng.random() >= wall_probability:
#                     tile_categories[x][y] = TileCategory.WALL
#
#         # create distinctive regions
#         for i in range(4):
#             for y in range(1, room_max_area - 1):
#                 for x in range(1, room_max_area - 1):
#
#                     # if the cell's neighboring walls > neighbours, set it to 1
#                     if count_neighbouring_walls(x, y, tile_categories) > neighbours:
#                         tile_categories[x][y] = TileCategory.WALL
#                     # otherwise, set it to 0
#                     elif count_neighbouring_walls(x, y, tile_categories) < neighbours:
#                         tile_categories[x][y] = TileCategory.FLOOR
#
#         # flood fill to remove small caverns
#         tile_categories = flood_fill(tile_categories)
#
#         # convert to room
#         room = Room(tile_categories=tile_categories, design="cavern")
#
#         # start over if the room is completely filled in
#         width = room.width
#         height = room.height
#         for x in range(width):
#             for y in range(height):
#                 if tile_categories[x][y] == 0:
#                     return room
#
#
# def flood_fill(tile_categories: List[List[TileCategoryType]]):
#     """
#     Find the largest region. Fill in all other regions.
#     """
#     room_width = len(tile_categories)
#     room_height = len(tile_categories[0])
#     min_room_area = min(_map_data.min_room_areas.values())
#     largest_region = set()
#
#     for x in range(room_width):
#         for y in range(room_height):
#             if tile_categories[x][y] == TileCategory.FLOOR:
#                 new_region = set()
#                 tile = (x, y)
#                 to_be_filled = set([tile])
#                 while to_be_filled:
#                     tile = to_be_filled.pop()
#
#                     if tile not in new_region:
#                         new_region.add(tile)
#
#                         tile_categories[tile[0]][tile[1]] = TileCategory.WALL
#
#                         # check adjacent cells
#                         x = tile[0]
#                         y = tile[1]
#                         north = (x, y - 1)
#                         south = (x, y + 1)
#                         east = (x + 1, y)
#                         west = (x - 1, y)
#
#                         for direction in [north, south, east, west]:
#
#                             if tile_categories[direction[0]][direction[1]] == TileCategory.FLOOR:
#                                 if direction not in to_be_filled and direction not in new_region:
#                                     to_be_filled.add(direction)
#
#                 if len(new_region) >= min_room_area:
#                     if len(new_region) > len(largest_region):
#                         largest_region.clear()
#                         largest_region.update(new_region)
#
#     for tile in largest_region:
#         tile_categories[tile[0]][tile[1]] = TileCategory.FLOOR
#
#     return tile_categories
