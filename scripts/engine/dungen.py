from __future__ import annotations

import logging
from typing import List, TYPE_CHECKING

import random

from dataclasses import dataclass, field

import tcod

from scripts.engine import library, utility, world
from scripts.engine.core.constants import Direction, TILE_SIZE, TileCategory, TileCategoryType
from scripts.engine.core.definitions import ActorData, MapData
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Optional, Tuple, List

__all__ = ["generate", "generate_steps"]


@dataclass
class DungeonGenerator:
    rng: random.Random

    # containers
    map_data: MapData
    placed_rooms: List[Room] = field(default_factory=list)
    map_of_categories: List[List[TileCategoryType]] = field(default_factory=list)
    positions_in_rooms: List[Tuple[int, int]] = field(default_factory=list)

    # parameters/config
    max_generate_room_attempts = 100
    max_place_room_attempts = 200
    max_place_entrance_attempts = 50
    max_room_entrances = 2
    max_make_room_accessible_attempts = 100
    extra_entrance_chance = 10
    room_extra_size = 0
    chance_of_tunnel_winding = 10
    border_size = 4

    def is_in_bounds(self, x: int, y: int):
        """
        Check if a position is in the bounds of the map
        """
        width = self.map_data.width
        height = self.map_data.height

        if 0 < x < width - 1 and 0 < y < height - 1:
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

        for x in range(width):
            generated_level.append([])
            for y in range(height):
                generated_level[x].append(self._create_tile_from_category(x, y, self.map_of_categories[x][y]))

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

    def _create_tile_from_category(self, x: int, y: int, tile_category: TileCategoryType) -> Tile:
        """
        Convert a tile category into the relevant tile
        """
        if tile_category == TileCategory.WALL:
            sprite_path = self.map_data.wall_sprite_path
            sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
            blocks_sight = True
            blocks_movement = True
        else:  # tile_category == TileCategory.FLOOR:
            sprite_path = self.map_data.floor_sprite_path
            sprite = utility.get_image(sprite_path, (TILE_SIZE, TILE_SIZE))
            blocks_sight = False
            blocks_movement = False

        tile = Tile(x, y, sprite, sprite_path, blocks_sight, blocks_movement)

        return tile


@dataclass
class Room:
    """
    Details of a room. Used for world generation.
    """
    tile_categories: List[List[TileCategory]]  # what to place in a tile
    design: str  # algorithm used to generate
    category: str  # the type of room placed
    start_x: int = -1
    start_y: int = -1
    entities: List[str] = field(default_factory=list)


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
        gen_info = f"{self.category} | {self.design} | (w:{self.width}, h:{self.height}) " \
                   f"| available:{self.available_area}/ total:{self.total_area}."

        return gen_info

    @property
    def end_x(self) -> int:
        return self.start_x + self.width

    @property
    def end_y(self) -> int:
        return self.start_y + self.height

    def intersects(self, room: Room) -> bool:
        """
        Check if this room intersects with another.
        """
        if (self.start_x <= room.end_x and self.end_x >= room.start_x) and \
                (self.start_y <= room.end_y and self.end_y >= room.start_y):
            return True
        else:
            return False


############################ GENERATE MAP ############################

def generate(map_name: str, rng: random.Random,
        player_data: Optional[ActorData] = None) -> Tuple[List[List[Tile]], str]:
    """
    Generate the map using the specified details.
    """
    # create generator
    dungen = DungeonGenerator(rng, library.MAPS[map_name])

    # generate the level
    _generate_map_categories(dungen, player_data)

    return dungen.map_of_tiles, dungen.generation_string


def generate_steps(map_name: str):
    """
    Generates a map, returning each step of the generation. Used for dev view.
    """

    # create generator
    dungen = DungeonGenerator(random.Random(), library.MAPS[map_name])

    for step in _generate_map_in_steps(dungen):
        yield step


def _generate_map_categories(dungen: DungeonGenerator, player_data: Optional[ActorData] = None):
    """
    Generates the tile categories on the map.
    """
    for _ in _generate_map_in_steps(dungen, player_data):
        pass


def _generate_map_in_steps(dungen: DungeonGenerator, player_data: Optional[ActorData] = None):
    """
    Generate the next step of the level generation.
    """
    rooms_placed = 0
    placement_attempts = 0
    rooms_generated = 0
    start_x = 0
    start_y = 0

    # set everything to walls
    dungen.map_of_categories = []
    width = dungen.map_data.width
    height = dungen.map_data.height
    for x in range(width):
        dungen.map_of_categories.append([])  # create new list for every col
        for y in range(height):
            dungen.map_of_categories[x].append(TileCategory.WALL)

    yield dungen.map_of_categories

    # generate and place rooms
    while rooms_placed <= dungen.map_data.max_rooms and rooms_generated <= dungen.max_generate_room_attempts:
        intersects = False
        found_place = False

        room = _generate_room(dungen)
        rooms_generated += 1

        # find place for the room
        while placement_attempts < dungen.max_place_room_attempts and not found_place:
            placement_attempts += 1

            # pick random location to place room
            room.start_x = start_x = dungen.rng.randint(1, max(1, width - room.width))
            room.start_y = start_y = dungen.rng.randint(1, max(1, height - room.height))

            # if placed there does room overlap any existing rooms?
            for _room in dungen.placed_rooms:
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
                dungen.map_of_categories[start_x + x][start_y + y] = room.tile_categories[x][y]
                dungen.positions_in_rooms.append((start_x + x, start_y + y))

        # place room
        dungen.placed_rooms.append(room)
        rooms_placed += 1

        # do we need to spawn the player?
        if rooms_placed == 1 and player_data:
            world.create_actor(player_data, (start_x, start_y), True)

        # yield map after each room is painted
        yield dungen.map_of_categories

    # handle anything dodgy
    if rooms_placed == 0:
        raise Exception("No rooms placed on the map.")

    # room placement complete, fill tunnels, without connecting to rooms
    for x in range(width):
        for y in range(height):

            # check not part of a room
            if not dungen.is_in_room(x, y):
                # if its a wall, fill it in.
                if dungen.map_of_categories[x][y] == TileCategory.WALL:
                    if _add_tunnels(dungen, x, y):
                        # yield map after each tunnel is successfully  added
                        yield dungen.map_of_categories

    # join rooms to tunnels
    for room in dungen.placed_rooms:
        _add_entrances(dungen, room)
        yield dungen.map_of_categories

    _add_border_to_map(dungen)
    yield dungen.map_of_categories

    # make diagonal only positions accessible to cardinal movement
    _open_diagonal_only_positions_on_map(dungen)
    yield dungen.map_of_categories

    _make_rooms_accessible(dungen)
    yield dungen.map_of_categories

    _make_rooms_accessible(dungen)
    yield dungen.map_of_categories

    _remove_deadends_from_map(dungen)
    yield dungen.map_of_categories


############################ GENERATE ROOMS ############################

def _generate_room(dungen: DungeonGenerator) -> Room:
    """
    Select a room type to generate and return that room. If a generation method isnt provided then one is picked at
    random, using weightings in the data.
    """
    room_weights = dungen.map_data.room_weights
    options = [_generate_cellular_automata_room, _generate_room_square]
    weights = [room_weights["cellular"], room_weights["square"]]

    # pick a generation method based on weights
    _room_generation_method = dungen.rng.choices(options, weights, k=1)[0]
    room = _room_generation_method(dungen)

    return room


def _generate_cellular_automata_room(dungen: DungeonGenerator, ) -> Room:
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
    room = Room(tile_categories=room_tile_cats, design="cellular", category="tbc")
    return room


def _generate_room_square(dungen: DungeonGenerator) -> Room:
    """
    Generate a square-shaped room.
    """
    room_min_area = dungen.map_data.min_room_areas["square"]
    room_max_area = dungen.map_data.max_room_areas["square"]
    map_height = dungen.map_data.height

    # ensure not bigger than the map
    room_width = dungen.rng.randint(room_min_area, room_max_area)
    room_height = min(dungen.rng.randint(max(int(room_width * 0.5), room_min_area),
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

def _add_tunnels(dungen: DungeonGenerator, x: int, y: int) -> bool:
    """
    Follow a path from origin (xy) setting relevant position in map_of_categories to TileCategory.FLOOR. Uses flood
    fill. Returns True if tunnel added
    """
    added_tunnel = False
    to_fill_positions = set()
    last_direction = (0, 0)
    room_tile_categories = []

    # FIXME - this make every tunnel take up the space of the entire map.
    #  if we swap to numpy we can add rows and cols more easily and expand the array as required.
    width = dungen.map_data.width
    height = dungen.map_data.height
    for _room_x in range(width):
        room_tile_categories.append([])
        for _room_y in range(height):
            room_tile_categories[_room_x].append(TileCategory.WALL)

    room_x = 0
    room_y = 0

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

        # build room info
        room_tile_categories[room_x][room_y] = TileCategory.FLOOR
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
            if in_bounds and not in_room and num_walls >= 2:
                if dungen.map_of_categories[x_check][y_check] == TileCategory.WALL and \
                        not dungen.is_in_room(_x + (x_dir * 2), _y + (y_dir * 2)):
                    possible_directions.append((x_dir, y_dir))

        # choose next direction to go in
        if possible_directions:
            # pick a possible position, preferring previous direction
            if last_direction in possible_directions and \
                    dungen.rng.randint(1, 100) > dungen.chance_of_tunnel_winding:
                new_direction = last_direction
            else:
                new_direction = dungen.rng.choice(possible_directions)

            # add next position to be checked
            to_fill_positions.add((_x + new_direction[0], _y + new_direction[1]))

            # update last direction
            last_direction = new_direction

            # update room xy
            room_x += new_direction[0]
            room_y += new_direction[1]

    return added_tunnel


def _add_ignorant_tunnel(dungen: DungeonGenerator, start_x: int, start_y: int, end_x: int, end_y: int):
    """
    Create a tunnel between two points, ignoring all terrain on the way
    """
    x = min(start_x, end_x)
    y = min(start_y, end_y)
    while x != max(start_x, end_x):
        x += 1
        dungen.map_of_categories[x][y] = TileCategory.FLOOR
    while y != max(start_y, end_y):
        y += 1
        dungen.map_of_categories[x][y] = TileCategory.FLOOR


def _add_entrances(dungen: DungeonGenerator, room: Room):
    """
    Loop all rooms and if it isnt a tunnel then search the outer edge for two adjoining floors and break through to
    link the locations.
    """
    entrances = 0
    attempts = 0

    # roll for an extra entrance
    if dungen.rng.randint(1, 100) >= dungen.extra_entrance_chance:
        max_entrances = dungen.max_room_entrances + 1
    else:
        max_entrances = dungen.max_room_entrances

    while attempts <= dungen.max_place_entrance_attempts and entrances <= max_entrances:
        attempts += 1
        poss_positions = []

        # pick random positions
        top_pos = (room.start_x + dungen.rng.randint(0, room.width - 1), room.start_y - 1)
        next_top_pos = top_pos[0], top_pos[1] - 1

        bot_pos = (room.start_x + dungen.rng.randint(0, room.width - 1), room.start_y + room.height + 1)
        next_bot_pos = bot_pos[0], bot_pos[1] + 1

        left_pos = (room.start_x - 1, room.start_y + dungen.rng.randint(0, room.height - 1))
        next_left_pos = left_pos[0] - 1, left_pos[1]

        right_pos = (room.start_x + room.width + 1, room.start_y + dungen.rng.randint(0, room.height - 1))
        next_right_pos = right_pos[0] + 1, right_pos[1]

        # note which ones are applicable
        for _pos, _next_pos in (
                (top_pos, next_top_pos),
                (bot_pos, next_bot_pos),
                (left_pos, next_left_pos),
                (right_pos, next_right_pos)):
            next_pos_is_floor = False

            in_bounds = dungen.is_in_bounds(_pos[0], _pos[1])
            if dungen.is_in_bounds(_next_pos[0], _next_pos[1]):
                if dungen.map_of_categories[_next_pos[0]][_next_pos[1]] == TileCategory.FLOOR:
                    next_pos_is_floor = True


            if in_bounds and next_pos_is_floor:
                poss_positions.append(_pos)

        # pick one of the possible options and update the map
        if poss_positions:
            pos = dungen.rng.choice(poss_positions)
            dungen.map_of_categories[pos[0]][pos[1]] = TileCategory.FLOOR

            entrances += 1


def _remove_deadends_from_map(dungen: DungeonGenerator):
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


def _open_diagonal_only_positions_on_map(dungen: DungeonGenerator):
    """
    Find positions where they can only be accessed via a diagonal and set surrounding tiles to floor.
    """
    for x in range(dungen.map_data.width):
        for y in range(dungen.map_data.height):
            if dungen.is_only_accessible_diagonally(x, y):
                for x_dir, y_dir in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
                    x_check = x + x_dir
                    y_check = y + y_dir
                    if dungen.is_in_bounds(x_check, y_check):
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
    bools_map = dungen.map_of_bools

    # start with picking one room that everything should connect to
    anchor_room = dungen.rng.choice(dungen.placed_rooms)

    # pick spot in room as anchor
    anchor_x = anchor_room.start_x + (anchor_room.width // 2)
    anchor_y = anchor_room.start_y + (anchor_room.height // 2)
    dungen.map_of_categories[anchor_x][anchor_y] = TileCategory.FLOOR

    # loop all rooms
    for room in dungen.placed_rooms:
        x = room.start_x + (room.width // 2)
        y = room.start_y + (room.height // 2)
        dungen.map_of_categories[x][y] = TileCategory.FLOOR

        # check if route is possible between anchor and target
        pathfinder = tcod.path.Dijkstra(bools_map, 0)
        pathfinder.set_goal(x, y)
        path = pathfinder.get_path(anchor_x, anchor_y)

        # if no possible route, make one
        if not path:
            _add_ignorant_tunnel(dungen, anchor_x, anchor_y, x, y)
