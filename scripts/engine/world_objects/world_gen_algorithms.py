"""
Taken from https://github.com/AtTheMatinee/dungeon-generation/blob/master/dungeonGenerationAlgorithms.py#L775
"""

import random
import tcod as libtcod
from typing import List, Tuple


class RoomAddition:
    """
    Add rooms one at a time and connect with tunnels.
    """

    def __init__(self, min_room_size: int):
        self.rooms: List[Tuple[Tuple[int, int], List[List[int]]]] = []
        self.level: List[List[int]] = []
        self.tunnels: List[Tuple[Tuple[int, int], Tuple[int, int], int]] = []
        self.rng = random.Random()

        self.room_max_size = 18  # max height and width for cellular automata rooms
        self.room_min_size = min_room_size  # min size in number of floor tiles, not height and width
        self.max_num_rooms = 30

        self.square_room_max_size = 12
        self.square_room_min_size = 6

        self.cross_room_max_size = 12
        self.cross_room_min_size = 6

        self.cavern_chance = 0.40  # probability that the first room will be a cavern
        self.cavern_max_size = 35  # max height an width

        self.wall_probability = 0.45
        self.neighbours = 4

        self.square_room_chance = 0.2
        self.cross_room_chance = 0.15

        self.build_room_attempts = 500
        self.place_room_attempts = 20
        self.max_tunnel_length = 12

        self.include_shortcuts = True
        self.shortcut_attempts = 500
        self.shortcut_length = 5
        self.min_pathfinding_distance = 50

    def generate_level_steps(self, seed, map_width, map_height):

        self.level = [[1 for _ in range(map_height)] for _ in range(map_width)]
        yield self.level
        self.rng.seed(seed)
        # generate the first room
        room = self.generate_room()
        room_width, room_height = self.get_room_dimensions(room)
        room_x = int((map_width / 2 - room_width / 2) - 1)
        room_y = int((map_height / 2 - room_height / 2) - 1)
        self.add_room(room_x, room_y, room)
        yield self.level
        # generate other rooms
        for i in range(self.build_room_attempts):
            room = self.generate_room()
            # try to position the room, get room_x and room_y
            room_x, room_y, wall_tile, direction, tunnel_length = self.place_room(room, map_width, map_height)
            if room_x and room_y:
                self.add_room(room_x, room_y, room)
                yield self.level
                self.add_tunnel(wall_tile, direction, tunnel_length)
                yield self.level
                if len(self.rooms) >= self.max_num_rooms:
                    break
        yield self.level
        if self.include_shortcuts:
            self.add_shortcuts(map_width, map_height)

        return self.level

    def generate_level(self, seed, map_width, map_height):
        for _ in self.generate_level_steps(seed, map_width, map_height):
            pass
        return self.level

    def generate_room(self):
        # select a room type to generate
        # generate and return that room
        if self.rooms:
            # There is at least one room already
            choice = self.rng.random()

            if choice < self.square_room_chance:
                room = self.generate_room_square()
            elif self.square_room_chance <= choice < (self.square_room_chance + self.cross_room_chance):
                room = self.generate_room_cross()
            else:
                room = self.generate_room_cellular_automata()

        else:  # it's the first room
            choice = self.rng.random()
            if choice < self.cavern_chance:
                room = self.generate_room_cavern()
            else:
                room = self.generate_room_square()

        return room

    def generate_room_cross(self):
        room_hor_width = int((self.rng.randint(self.cross_room_min_size + 2, self.cross_room_max_size)) / 2 * 2)

        room_ver_height = int((self.rng.randint(self.cross_room_min_size + 2, self.cross_room_max_size)) / 2 * 2)

        room_hor_height = int((self.rng.randint(self.cross_room_min_size, room_ver_height - 2)) / 2 * 2)

        room_ver_width = int((self.rng.randint(self.cross_room_min_size, room_hor_width - 2)) / 2 * 2)

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

    def generate_room_square(self):
        room_width = self.rng.randint(self.square_room_min_size, self.square_room_max_size)
        room_height = self.rng.randint(max(int(room_width * 0.5), self.square_room_min_size),
                                       min(int(room_width * 1.5), self.square_room_max_size))

        room = [[0
                 for y in range(1, room_height - 1)]
                for x in range(1, room_width - 1)]

        return room

    def generate_room_cellular_automata(self):
        while True:
            # if a room is too small, generate another
            room = [[1
                     for y in range(self.room_max_size)]
                    for x in range(self.room_max_size)]

            # random fill map
            for y in range(2, self.room_max_size - 2):
                for x in range(2, self.room_max_size - 2):
                    if self.rng.random() >= self.wall_probability:
                        room[x][y] = 0

            # create distinctive regions
            for i in range(4):
                for y in range(1, self.room_max_size - 1):
                    for x in range(1, self.room_max_size - 1):

                        # if the cell's neighboring walls > self.neighbours, set it to 1
                        if self.get_adjacent_walls(x, y, room) > self.neighbours:
                            room[x][y] = 1
                        # otherwise, set it to 0
                        elif self.get_adjacent_walls(x, y, room) < self.neighbours:
                            room[x][y] = 0

            # flood fill to remove small caverns
            room = self.flood_fill(room)

            # start over if the room is completely filled in
            room_width, room_height = self.get_room_dimensions(room)
            for x in range(room_width):
                for y in range(room_height):
                    if room[x][y] == 0:
                        return room

    def generate_room_cavern(self):
        while True:
            # if a room is too small, generate another
            room = [[1
                     for y in range(self.cavern_max_size)]
                    for x in range(self.cavern_max_size)]

            # random fill map
            for y in range(2, self.cavern_max_size - 2):
                for x in range(2, self.cavern_max_size - 2):
                    if self.rng.random() >= self.wall_probability:
                        room[x][y] = 0

            # create distinctive regions
            for i in range(4):
                for y in range(1, self.cavern_max_size - 1):
                    for x in range(1, self.cavern_max_size - 1):

                        # if the cell's neighboring walls > self.neighbours, set it to 1
                        if self.get_adjacent_walls(x, y, room) > self.neighbours:
                            room[x][y] = 1
                        # otherwise, set it to 0
                        elif self.get_adjacent_walls(x, y, room) < self.neighbours:
                            room[x][y] = 0

            # flood fill to remove small caverns
            room = self.flood_fill(room)

            # start over if the room is completely filled in
            room_width, room_height = self.get_room_dimensions(room)
            for x in range(room_width):
                for y in range(room_height):
                    if room[x][y] == 0:
                        return room

    def flood_fill(self, room):
        """
        Find the largest region. Fill in all other regions.
        """
        room_width, room_height = self.get_room_dimensions(room)
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

                    if len(new_region) >= self.room_min_size:
                        if len(new_region) > len(largest_region):
                            largest_region.clear()
                            largest_region.update(new_region)

        for tile in largest_region:
            room[tile[0]][tile[1]] = 0

        return room

    def place_room(self, room, map_width, map_height):  # (self,room,direction,)
        room_x = None
        room_y = None

        room_width, room_height = self.get_room_dimensions(room)

        # try n times to find a wall that lets you build room in that direction
        for i in range(self.place_room_attempts):
            # try to place the room against the tile, else connected by a tunnel of length i

            wall_tile = None
            direction = self.get_direction()
            while not wall_tile:
                """
                randomly select tiles until you find
                a wall that has another wall in the
                chosen direction and has a floor in the 
                opposite direction.
                """
                # direction == tuple(dx,dy)
                tile_x = self.rng.randint(1, map_width - 2)
                tile_y = self.rng.randint(1, map_height - 2)
                if ((self.level[tile_x][tile_y] == 1) and
                        (self.level[tile_x + direction[0]][tile_y + direction[1]] == 1) and
                        (self.level[tile_x - direction[0]][tile_y - direction[1]] == 0)):
                    wall_tile = (tile_x, tile_y)

            # spawn the room touching wall_tile
            startRoomX = None
            startRoomY = None
            """
            TODO: replace this with a method that returns a 
            random floor tile instead of the top left floor tile
            """
            while not startRoomX and not startRoomY:
                x = self.rng.randint(0, room_width - 1)
                y = self.rng.randint(0, room_height - 1)
                if room[x][y] == 0:
                    startRoomX = wall_tile[0] - x
                    startRoomY = wall_tile[1] - y

            # then slide it until it doesn't touch anything
            for tunnelLength in range(self.max_tunnel_length):
                possibleRoomX = startRoomX + direction[0] * tunnelLength
                possibleRoomY = startRoomY + direction[1] * tunnelLength

                enoughRoom = self.get_overlap(room, possibleRoomX, possibleRoomY, map_width, map_height)

                if enoughRoom:
                    room_x = possibleRoomX
                    room_y = possibleRoomY

                    # build connecting tunnel
                    # Attempt 1
                    """
                    for i in range(tunnel_length+1):
                        x = wall_tile[0] + direction[0]*i
                        y = wall_tile[1] + direction[1]*i
                        self.level[x][y] = 0
                    """
                    # moved tunnel code into self.generateLevel()

                    return room_x, room_y, wall_tile, direction, tunnelLength

        return None, None, None, None, None

    def add_room(self, room_x, room_y, room):
        room_width, room_height = self.get_room_dimensions(room)
        for x in range(room_width):
            for y in range(room_height):
                if room[x][y] == 0:
                    self.level[room_x + x][room_y + y] = 0

        self.rooms.append(((room_x, room_y), room))

    def add_tunnel(self, wall_tile, direction, tunnelLength):
        # carve a tunnel from a point in the room back to
        # the wall tile that was used in its original placement

        startX = wall_tile[0] + direction[0] * tunnelLength
        startY = wall_tile[1] + direction[1] * tunnelLength
        # self.level[startX][startY] = 1
        real_length = 0
        x, y = 0, 0
        for i in range(self.max_tunnel_length):
            x = startX - direction[0] * i
            y = startY - direction[1] * i
            self.level[x][y] = 0
            real_length += 1
            # If you want doors, this is where the code should go
            if (x + direction[0]) == wall_tile[0] and (y + direction[1]) == wall_tile[1]:
                break
        tunnel = ((x, y), (direction[0], direction[1]), real_length)
        self.tunnels.append(tunnel)

    def get_room_dimensions(self, room):
        if room:
            room_width = len(room)
            room_height = len(room[0])
            return room_width, room_height
        else:
            room_width = 0
            room_height = 0
            return room_width, room_height

    def get_adjacent_walls(self, tile_x, tile_y, room):  # finds the walls in 8 directions
        wall_counter = 0
        for x in range(tile_x - 1, tile_x + 2):
            for y in range(tile_y - 1, tile_y + 2):
                if (room[x][y] == 1):
                    if (x != tile_x) or (y != tile_y):  # exclude (tile_x,tile_y)
                        wall_counter += 1
        return wall_counter

    def get_direction(self):
        # direction = (dx,dy)
        north = (0, -1)
        south = (0, 1)
        east = (1, 0)
        west = (-1, 0)

        direction = self.rng.choice([north, south, east, west])
        return direction

    def get_overlap(self, room, room_x, room_y, map_width, map_height):
        """
        for each 0 in room, check the cooresponding tile in
        self.level and the eight tiles around it. Though slow,
        that should insure that there is a wall between each of
        the rooms created in this way.
        <> check for overlap with self.level
        <> check for out of bounds
        """
        room_width, room_height = self.get_room_dimensions(room)
        for x in range(room_width):
            for y in range(room_height):
                if room[x][y] == 0:
                    # Check to see if the room is out of bounds
                    if ((1 <= (x + room_x) < map_width - 1) and
                            (1 <= (y + room_y) < map_height - 1)):
                        # Check for overlap with a one tile buffer
                        if self.level[x + room_x - 1][y + room_y - 1] == 0:  # top left
                            return False
                        if self.level[x + room_x][y + room_y - 1] == 0:  # top center
                            return False
                        if self.level[x + room_x + 1][y + room_y - 1] == 0:  # top right
                            return False

                        if self.level[x + room_x - 1][y + room_y] == 0:  # left
                            return False
                        if self.level[x + room_x][y + room_y] == 0:  # center
                            return False
                        if self.level[x + room_x + 1][y + room_y] == 0:  # right
                            return False

                        if self.level[x + room_x - 1][y + room_y + 1] == 0:  # bottom left
                            return False
                        if self.level[x + room_x][y + room_y + 1] == 0:  # bottom center
                            return False
                        if self.level[x + room_x + 1][y + room_y + 1] == 0:  # bottom right
                            return False

                    else:  # room is out of bounds
                        return False
        return True

    def add_shortcuts(self, map_width, map_height):
        """
        Use libtcod's pathfinding to find the distance between two points and put a shortcut between them.
        """

        # initialize the libtcod map
        libtcod_map = libtcod.map_new(map_width, map_height)
        self.recompute_path_map(map_width, map_height, libtcod_map)

        for i in range(self.shortcut_attempts):
            # check i times for places where shortcuts can be made
            while True:
                # Pick a random floor tile
                floor_x = self.rng.randint(self.shortcut_length + 1, (map_width - self.shortcut_length - 1))
                floor_y = self.rng.randint(self.shortcut_length + 1, (map_height - self.shortcut_length - 1))
                if self.level[floor_x][floor_y] == 0:
                    if (self.level[floor_x - 1][floor_y] == 1 or
                            self.level[floor_x + 1][floor_y] == 1 or
                            self.level[floor_x][floor_y - 1] == 1 or
                            self.level[floor_x][floor_y + 1] == 1):
                        break

            # look around the tile for other floor tiles
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x != 0 or y != 0:  # Exclude the center tile
                        new_x = floor_x + (x * self.shortcut_length)
                        new_y = floor_y + (y * self.shortcut_length)
                        if self.level[new_x][new_y] == 0:
                            # run pathfinding algorithm between the two points
                            # back to the libtcod nonsense
                            path_map = libtcod.path_new_using_map(libtcod_map)
                            libtcod.path_compute(path_map, floor_x, floor_y, new_x, new_y)
                            distance = libtcod.path_size(path_map)

                            if distance > self.min_pathfinding_distance:
                                # make shortcut
                                self.carve_shortcut(floor_x, floor_y, new_x, new_y)
                                self.recompute_path_map(map_width, map_height, libtcod_map)

        # destroy the path object
        libtcod.path_delete(path_map)

    def recompute_path_map(self, map_width, map_height, libtcod_map):
        for x in range(map_width):
            for y in range(map_height):
                if self.level[x][y] == 1:
                    libtcod.map_set_properties(libtcod_map, x, y, False, False)
                else:
                    libtcod.map_set_properties(libtcod_map, x, y, True, True)

    def carve_shortcut(self, x1, y1, x2, y2):
        tunnel = None
        if x1 - x2 == 0:
            # Carve vertical tunnel
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.level[x1][y] = 0

        elif y1 - y2 == 0:
            # Carve Horizontal tunnel
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.level[x][y1] = 0

        elif (y1 - y2) / (x1 - x2) == 1:
            # Carve NW to SE Tunnel
            x = min(x1, x2)
            y = min(y1, y2)
            while x != max(x1, x2):
                x += 1
                self.level[x][y] = 0
                y += 1
                self.level[x][y] = 0

        elif (y1 - y2) / (x1 - x2) == -1:
            # Carve NE to SW Tunnel
            x = min(x1, x2)
            y = max(y1, y2)
            while x != max(x1, x2):
                x += 1
                self.level[x][y] = 0
                y -= 1
                self.level[x][y] = 0


    def check_room_exists(self, room):
        room_width, room_height = self.get_room_dimensions(room)
        for x in range(room_width):
            for y in range(room_height):
                if room[x][y] == 0:
                    return True
        return False
