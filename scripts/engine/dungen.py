from __future__ import annotations
from typing import TYPE_CHECKING

import random

from dataclasses import dataclass, field
from scripts.engine import library, utility, world
from scripts.engine.core.constants import Direction, TILE_SIZE, TileCategory, TileCategoryType
from scripts.engine.core.definitions import ActorData, MapData
from scripts.engine.world_objects.tile import Tile
from scripts.engine.world_objects.room import Room

if TYPE_CHECKING:
    from typing import Optional, Tuple, List

__all__ = ["generate", "generate_steps"]


@dataclass
class _DungeonGenerator:
    rng: random.Random

    # containers
    map_data: MapData
    placed_rooms: List[Room] = field(default_factory=list)
    map_of_categories: List[List[TileCategoryType]] = field(default_factory=list)
    positions_in_rooms: List[Tuple[int, int]] = field(default_factory=list)

    # parameters/config
    max_generate_room_attempts = 100
    max_place_room_attempts = 200
    max_room_entrances = 2
    extra_entrance_chance = 20
    room_extra_size = 0
    chance_of_tunnel_winding = 0

    def is_in_map_border(self, x: int, y: int) -> bool:
        """
        Returns a bool if given position is in the map's border
        """
        border_size = 4
        width = self.map_data.width
        height = self.map_data.height
        if (x <= border_size or x >= (width - border_size)) or (y <= border_size or y >= (height - border_size)):
            return True
        else:
            return False

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

    @property
    def map_of_tiles(self) -> List[List[Tile]]:
        """
        Convert map_of_categories to tiles
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


def generate(map_name: str, rng: random.Random,
        player_data: Optional[ActorData] = None) -> Tuple[List[List[Tile]], str]:
    """
    Generate the map using the specified details.
    """
    # create generator
    dungen = _DungeonGenerator(rng, library.MAPS[map_name])

    # generate the level
    _generate_map_categories(dungen, player_data)

    # TODO : add outer border (maybe add size as a global value and make all map take into account?)
    # ensure all borders are walls
    # for x in range(width):
    #     for y in range(height):
    #         if is_in_map_border(width, height, x, y):
    #             _create_wall_tile(x, y)


    return dungen.map_of_tiles, dungen.generation_string


############################ GENERATE LEVEL ############################

def generate_steps(map_name: str):
    """
    Generates a map, returning each step of the generation. Used for dev view.
    """

    # create generator
    dungen = _DungeonGenerator(random.Random(), library.MAPS[map_name])

    for step in _generate_map_in_steps(dungen):
        yield step


def _generate_map_categories(dungen: _DungeonGenerator, player_data: Optional[ActorData] = None):
    """
    Generates the tile categories on the map.
    """
    for _ in _generate_map_in_steps(dungen, player_data):
        pass


def _generate_map_in_steps(dungen: _DungeonGenerator, player_data: Optional[ActorData] = None):
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
                    _add_tunnels(dungen, x, y)

                    # yield map after each set of tunnels added
                    yield dungen.map_of_categories

    # join tunnels and rooms
    _join_tunnels_to_rooms(dungen)

    # yield map after tunnels connected to rooms
    yield dungen.map_of_categories


############################ GENERATE ROOMS ############################

def _generate_room(dungen: _DungeonGenerator) -> Room:
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


def _generate_cellular_automata_room(dungen: _DungeonGenerator,) -> Room:
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


def _generate_room_square(dungen: _DungeonGenerator) -> Room:
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

def _add_tunnels(dungen: _DungeonGenerator, x: int, y: int):
    """
    Follow a path from origin (xy) setting relevant position in map_of_categories to TileCategory.FLOOR. Uses flood
    fill.
    """
    to_fill_positions = set()
    to_fill_positions.add((x, y))
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

    while to_fill_positions:
        possible_directions = []

        # get next pos in set
        _x, _y = to_fill_positions.pop()

        # convert to floor
        dungen.map_of_categories[_x][_y] = TileCategory.FLOOR
        dungen.positions_in_rooms.append((_x, _y))

        # build room info
        room_tile_categories[room_x][room_y] = TileCategory.FLOOR

        # check for appropriate, adjacent wall tiles
        for direction in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
            x_dir = direction[0]
            y_dir = direction[1]
            in_bounds = dungen.is_in_bounds(_x + x_dir, _y + y_dir)
            in_room = dungen.is_in_room(_x + x_dir, _y + y_dir)
            num_walls = dungen.count_neighbouring_walls(_x + x_dir, _y + y_dir)

            # direction must be in bounds, not in a room and be surrounded by walls on all but 2 sides
            if in_bounds and not in_room and num_walls >= 6:
                # we dont want to break into rooms so must have 2 walls in direction
                if dungen.map_of_categories[_x + x_dir][_y + y_dir] == TileCategory.WALL and \
                        not dungen.is_in_room(_x + (x_dir * 2), _y + (y_dir * 2)):
                    possible_directions.append(direction)

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

    # create the tunnel as a room
    dungen.placed_rooms.append(Room(tile_categories=room_tile_categories, design="flood_fill", category="tunnel",
                               start_x=x, start_y=y))


def _join_tunnels_to_rooms(dungen: _DungeonGenerator):
    """
    Loop all rooms and if it isnt a tunnel then search the outer edge for two adjoining floors and break through to
    link the locations.
    """
    # loop all rooms that aren't tunnels
    for room in dungen.placed_rooms:
        if room.category != "tunnel":
            entrances = 0

            # roll for an extra entrance
            if dungen.rng.randint(1, 100) >= dungen.extra_entrance_chance:
                max_entrances = dungen.max_room_entrances + 1
            else:
                max_entrances = dungen.max_room_entrances

            # check top and bottom of room
            for x in range(1, room.width):
                above = ""
                below = ""
                y = 0

                # check top side
                if room.tile_categories[x][0] == TileCategory.WALL:
                    y = 0
                    above = dungen.map_of_categories[x + room.start_x][y + room.start_y - 1]
                    below = dungen.map_of_categories[x + room.start_x][y + room.start_y + 1]


                # check bottom side
                if room.tile_categories[x][room.height - 1] == TileCategory.WALL:
                    y = room.height - 1  # -1 due to counting from 0
                    above = dungen.map_of_categories[x + room.start_x][y + room.start_y - 1]
                    below = dungen.map_of_categories[x + room.start_x][y + room.start_y + 1]


                # check between two walls
                if above == TileCategory.FLOOR and below == TileCategory.FLOOR:
                    # make the wall a flor
                    dungen.map_of_categories[x + room.start_x][y + room.start_y] = TileCategory.FLOOR
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
                    left = dungen.map_of_categories[x + room.start_x - 1][y + room.start_y]
                    right = dungen.map_of_categories[x + room.start_x + 1][y + room.start_y]

                # check right side
                if room.tile_categories[0][y] == TileCategory.WALL:
                    x = room.width - 1  # -1 due to counting from 0
                    left = dungen.map_of_categories[x + room.start_x - 1][y + room.start_y]
                    right = dungen.map_of_categories[x + room.start_x + 1][y + room.start_y]

                # check between two walls
                if left == TileCategory.FLOOR and right == TileCategory.FLOOR:
                    # make the wall a flor
                    dungen.map_of_categories[x + room.start_x][y + room.start_y] = TileCategory.FLOOR
                    entrances += 1

                    # if enough entrances placed go to next room
                    if entrances >= max_entrances:
                        break
