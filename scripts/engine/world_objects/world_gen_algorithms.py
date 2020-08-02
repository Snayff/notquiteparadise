'''
Taken from https://github.com/AtTheMatinee/dungeon-generation/blob/master/dungeonGenerationAlgorithms.py#L775
'''

import random
import tcod as libtcod
from typing import List, Tuple


class RoomAddition:
    '''
    What I'm calling the Room Addition algorithm is an attempt to
    recreate the dungeon generation algorithm used in Brogue, as
    discussed at https://www.rockpapershotgun.com/2015/07/28/how-do-roguelikes-generate-levels/
    I don't think Brian Walker has ever given a name to his
    dungeon generation algorithm, so I've taken to calling it the
    Room Addition Algorithm, after the way in which it builds the
    dungeon by adding rooms one at a time to the existing dungeon.
    This isn't a perfect recreation of Brian Walker's algorithm,
    but I think it's good enough to demonstrait the concept.
    '''

    def __init__(self, min_room_size: int):
        self.rooms: List[Tuple[Tuple[int, int], List[List[int]]]] = []
        self.level: List[List[int]] = []
        self.tunnels: List[Tuple[Tuple[int, int], Tuple[int, int], int]] = []
        self.rng = random.Random()

        self.ROOM_MAX_SIZE = 18  # max height and width for cellular automata rooms
        self.ROOM_MIN_SIZE = min_room_size  # min size in number of floor tiles, not height and width
        self.MAX_NUM_ROOMS = 30

        self.SQUARE_ROOM_MAX_SIZE = 12
        self.SQUARE_ROOM_MIN_SIZE = 6

        self.CROSS_ROOM_MAX_SIZE = 12
        self.CROSS_ROOM_MIN_SIZE = 6

        self.cavernChance = 0.40  # probability that the first room will be a cavern
        self.CAVERN_MAX_SIZE = 35  # max height an width

        self.wallProbability = 0.45
        self.neighbors = 4

        self.squareRoomChance = 0.2
        self.crossRoomChance = 0.15

        self.build_room_attempts = 500
        self.placeRoomAttempts = 20
        self.maxTunnelLength = 12

        self.includeShortcuts = True
        self.shortcutAttempts = 500
        self.shortcutLength = 5
        self.minPathfindingDistance = 50

    def generate_level_steps(self, seed, map_width, map_height):

        self.level = [[1 for _ in range(map_height)] for _ in range(map_width)]
        yield self.level
        self.rng.seed(seed)
        # generate the first room
        room = self.generate_room()
        room_width, room_height = self.get_room_dimensions(room)
        roomX = int((map_width / 2 - room_width / 2) - 1)
        roomY = int((map_height / 2 - room_height / 2) - 1)
        self.add_room(roomX, roomY, room)
        yield self.level
        # generate other rooms
        for i in range(self.build_room_attempts):
            room = self.generate_room()
            # try to position the room, get roomX and roomY
            roomX, roomY, wall_tile, direction, tunnel_length = self.place_room(room, map_width, map_height)
            if roomX and roomY:
                self.add_room(roomX, roomY, room)
                yield self.level
                self.add_tunnel(wall_tile, direction, tunnel_length)
                yield self.level
                if len(self.rooms) >= self.MAX_NUM_ROOMS:
                    break
        yield self.level
        if self.includeShortcuts:
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

            if choice < self.squareRoomChance:
                room = self.generate_room_square()
            elif self.squareRoomChance <= choice < (self.squareRoomChance + self.crossRoomChance):
                room = self.generate_room_cross()
            else:
                room = self.generate_room_cellular_automata()

        else:  # it's the first room
            choice = self.rng.random()
            if choice < self.cavernChance:
                room = self.generate_room_cavern()
            else:
                room = self.generate_room_square()

        return room

    def generate_room_cross(self):
        room_hor_width = int((self.rng.randint(self.CROSS_ROOM_MIN_SIZE + 2, self.CROSS_ROOM_MAX_SIZE)) / 2 * 2)

        room_vir_height = int((self.rng.randint(self.CROSS_ROOM_MIN_SIZE + 2, self.CROSS_ROOM_MAX_SIZE)) / 2 * 2)

        room_hor_height = int((self.rng.randint(self.CROSS_ROOM_MIN_SIZE, room_vir_height - 2)) / 2 * 2)

        room_vir_width = int((self.rng.randint(self.CROSS_ROOM_MIN_SIZE, room_hor_width - 2)) / 2 * 2)

        room = [[1
                 for y in range(room_vir_height)]
                for x in range(room_hor_width)]

        # Fill in horizontal space
        virOffset = int(room_vir_height / 2 - room_hor_height / 2)
        for y in range(virOffset, room_hor_height + virOffset):
            for x in range(0, room_hor_width):
                room[x][y] = 0

        # Fill in virtical space
        horOffset = int(room_hor_width / 2 - room_vir_width / 2)
        for y in range(0, room_vir_height):
            for x in range(horOffset, room_vir_width + horOffset):
                room[x][y] = 0

        return room

    def generate_room_square(self):
        roomWidth = self.rng.randint(self.SQUARE_ROOM_MIN_SIZE, self.SQUARE_ROOM_MAX_SIZE)
        roomHeight = self.rng.randint(max(int(roomWidth * 0.5), self.SQUARE_ROOM_MIN_SIZE),
                                    min(int(roomWidth * 1.5), self.SQUARE_ROOM_MAX_SIZE))

        room = [[1
                 for y in range(roomHeight)]
                for x in range(roomWidth)]

        room = [[0
                 for y in range(1, roomHeight - 1)]
                for x in range(1, roomWidth - 1)]

        return room

    def generate_room_cellular_automata(self):
        while True:
            # if a room is too small, generate another
            room = [[1
                     for y in range(self.ROOM_MAX_SIZE)]
                    for x in range(self.ROOM_MAX_SIZE)]

            # random fill map
            for y in range(2, self.ROOM_MAX_SIZE - 2):
                for x in range(2, self.ROOM_MAX_SIZE - 2):
                    if self.rng.random() >= self.wallProbability:
                        room[x][y] = 0

            # create distinctive regions
            for i in range(4):
                for y in range(1, self.ROOM_MAX_SIZE - 1):
                    for x in range(1, self.ROOM_MAX_SIZE - 1):

                        # if the cell's neighboring walls > self.neighbors, set it to 1
                        if self.get_adjacent_walls(x, y, room) > self.neighbors:
                            room[x][y] = 1
                        # otherwise, set it to 0
                        elif self.get_adjacent_walls(x, y, room) < self.neighbors:
                            room[x][y] = 0

            # floodfill to remove small caverns
            room = self.flood_fill(room)

            # start over if the room is completely filled in
            roomWidth, roomHeight = self.get_room_dimensions(room)
            for x in range(roomWidth):
                for y in range(roomHeight):
                    if room[x][y] == 0:
                        return room

    def generate_room_cavern(self):
        while True:
            # if a room is too small, generate another
            room = [[1
                     for y in range(self.CAVERN_MAX_SIZE)]
                    for x in range(self.CAVERN_MAX_SIZE)]

            # random fill map
            for y in range(2, self.CAVERN_MAX_SIZE - 2):
                for x in range(2, self.CAVERN_MAX_SIZE - 2):
                    if self.rng.random() >= self.wallProbability:
                        room[x][y] = 0

            # create distinctive regions
            for i in range(4):
                for y in range(1, self.CAVERN_MAX_SIZE - 1):
                    for x in range(1, self.CAVERN_MAX_SIZE - 1):

                        # if the cell's neighboring walls > self.neighbors, set it to 1
                        if self.get_adjacent_walls(x, y, room) > self.neighbors:
                            room[x][y] = 1
                        # otherwise, set it to 0
                        elif self.get_adjacent_walls(x, y, room) < self.neighbors:
                            room[x][y] = 0

            # floodfill to remove small caverns
            room = self.flood_fill(room)

            # start over if the room is completely filled in
            roomWidth, roomHeight = self.get_room_dimensions(room)
            for x in range(roomWidth):
                for y in range(roomHeight):
                    if room[x][y] == 0:
                        return room

    def flood_fill(self, room):
        '''
        Find the largest region. Fill in all other regions.
        '''
        roomWidth, roomHeight = self.get_room_dimensions(room)
        largestRegion = set()

        for x in range(roomWidth):
            for y in range(roomHeight):
                if room[x][y] == 0:
                    newRegion = set()
                    tile = (x, y)
                    toBeFilled = set([tile])
                    while toBeFilled:
                        tile = toBeFilled.pop()

                        if tile not in newRegion:
                            newRegion.add(tile)

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
                                    if direction not in toBeFilled and direction not in newRegion:
                                        toBeFilled.add(direction)

                    if len(newRegion) >= self.ROOM_MIN_SIZE:
                        if len(newRegion) > len(largestRegion):
                            largestRegion.clear()
                            largestRegion.update(newRegion)

        for tile in largestRegion:
            room[tile[0]][tile[1]] = 0

        return room

    def place_room(self, room, mapWidth, mapHeight):  # (self,room,direction,)
        roomX = None
        roomY = None

        roomWidth, roomHeight = self.get_room_dimensions(room)

        # try n times to find a wall that lets you build room in that direction
        for i in range(self.placeRoomAttempts):
            # try to place the room against the tile, else connected by a tunnel of length i

            wallTile = None
            direction = self.get_direction()
            while not wallTile:
                '''
                randomly select tiles until you find
                a wall that has another wall in the
                chosen direction and has a floor in the 
                opposite direction.
                '''
                # direction == tuple(dx,dy)
                tileX = self.rng.randint(1, mapWidth - 2)
                tileY = self.rng.randint(1, mapHeight - 2)
                if ((self.level[tileX][tileY] == 1) and
                        (self.level[tileX + direction[0]][tileY + direction[1]] == 1) and
                        (self.level[tileX - direction[0]][tileY - direction[1]] == 0)):
                    wallTile = (tileX, tileY)

            # spawn the room touching wallTile
            startRoomX = None
            startRoomY = None
            '''
            TODO: replace this with a method that returns a 
            random floor tile instead of the top left floor tile
            '''
            while not startRoomX and not startRoomY:
                x = self.rng.randint(0, roomWidth - 1)
                y = self.rng.randint(0, roomHeight - 1)
                if room[x][y] == 0:
                    startRoomX = wallTile[0] - x
                    startRoomY = wallTile[1] - y

            # then slide it until it doesn't touch anything
            for tunnelLength in range(self.maxTunnelLength):
                possibleRoomX = startRoomX + direction[0] * tunnelLength
                possibleRoomY = startRoomY + direction[1] * tunnelLength

                enoughRoom = self.get_overlap(room, possibleRoomX, possibleRoomY, mapWidth, mapHeight)

                if enoughRoom:
                    roomX = possibleRoomX
                    roomY = possibleRoomY

                    # build connecting tunnel
                    # Attempt 1
                    '''
                    for i in range(tunnelLength+1):
                        x = wallTile[0] + direction[0]*i
                        y = wallTile[1] + direction[1]*i
                        self.level[x][y] = 0
                    '''
                    # moved tunnel code into self.generateLevel()

                    return roomX, roomY, wallTile, direction, tunnelLength

        return None, None, None, None, None

    def add_room(self, roomX, roomY, room):
        roomWidth, roomHeight = self.get_room_dimensions(room)
        for x in range(roomWidth):
            for y in range(roomHeight):
                if room[x][y] == 0:
                    self.level[roomX + x][roomY + y] = 0

        self.rooms.append(((roomX, roomY), room))

    def add_tunnel(self, wallTile, direction, tunnelLength):
        # carve a tunnel from a point in the room back to
        # the wall tile that was used in its original placement

        startX = wallTile[0] + direction[0] * tunnelLength
        startY = wallTile[1] + direction[1] * tunnelLength
        # self.level[startX][startY] = 1
        real_length = 0
        x, y = 0, 0
        for i in range(self.maxTunnelLength):
            x = startX - direction[0] * i
            y = startY - direction[1] * i
            self.level[x][y] = 0
            real_length += 1
            # If you want doors, this is where the code should go
            if (x + direction[0]) == wallTile[0] and (y + direction[1]) == wallTile[1]:
                break
        tunnel = ((x, y), (direction[0], direction[1]), real_length)
        self.tunnels.append(tunnel)

    def get_room_dimensions(self, room):
        if room:
            roomWidth = len(room)
            roomHeight = len(room[0])
            return roomWidth, roomHeight
        else:
            roomWidth = 0
            roomHeight = 0
            return roomWidth, roomHeight

    def get_adjacent_walls(self, tileX, tileY, room):  # finds the walls in 8 directions
        wallCounter = 0
        for x in range(tileX - 1, tileX + 2):
            for y in range(tileY - 1, tileY + 2):
                if (room[x][y] == 1):
                    if (x != tileX) or (y != tileY):  # exclude (tileX,tileY)
                        wallCounter += 1
        return wallCounter

    def get_direction(self):
        # direction = (dx,dy)
        north = (0, -1)
        south = (0, 1)
        east = (1, 0)
        west = (-1, 0)

        direction = self.rng.choice([north, south, east, west])
        return direction

    def get_overlap(self, room, roomX, roomY, mapWidth, mapHeight):
        '''
        for each 0 in room, check the cooresponding tile in
        self.level and the eight tiles around it. Though slow,
        that should insure that there is a wall between each of
        the rooms created in this way.
        <> check for overlap with self.level
        <> check for out of bounds
        '''
        roomWidth, roomHeight = self.get_room_dimensions(room)
        for x in range(roomWidth):
            for y in range(roomHeight):
                if room[x][y] == 0:
                    # Check to see if the room is out of bounds
                    if ((1 <= (x + roomX) < mapWidth - 1) and
                            (1 <= (y + roomY) < mapHeight - 1)):
                        # Check for overlap with a one tile buffer
                        if self.level[x + roomX - 1][y + roomY - 1] == 0:  # top left
                            return False
                        if self.level[x + roomX][y + roomY - 1] == 0:  # top center
                            return False
                        if self.level[x + roomX + 1][y + roomY - 1] == 0:  # top right
                            return False

                        if self.level[x + roomX - 1][y + roomY] == 0:  # left
                            return False
                        if self.level[x + roomX][y + roomY] == 0:  # center
                            return False
                        if self.level[x + roomX + 1][y + roomY] == 0:  # right
                            return False

                        if self.level[x + roomX - 1][y + roomY + 1] == 0:  # bottom left
                            return False
                        if self.level[x + roomX][y + roomY + 1] == 0:  # bottom center
                            return False
                        if self.level[x + roomX + 1][y + roomY + 1] == 0:  # bottom right
                            return False

                    else:  # room is out of bounds
                        return False
        return True

    def add_shortcuts(self, mapWidth, mapHeight):
        '''
        I use libtcodpy's built in pathfinding here, since I'm
        already using libtcodpy for the iu. At the moment,
        the way I find the distance between
        two points to see if I should put a shortcut there
        is horrible, and its easily the slowest part of this
        algorithm. If I think of a better way to do this in
        the future, I'll implement it.
        '''

        # initialize the libtcodpy map
        libtcodMap = libtcod.map_new(mapWidth, mapHeight)
        self.recompute_path_map(mapWidth, mapHeight, libtcodMap)

        for i in range(self.shortcutAttempts):
            # check i times for places where shortcuts can be made
            while True:
                # Pick a random floor tile
                floorX = self.rng.randint(self.shortcutLength + 1, (mapWidth - self.shortcutLength - 1))
                floorY = self.rng.randint(self.shortcutLength + 1, (mapHeight - self.shortcutLength - 1))
                if self.level[floorX][floorY] == 0:
                    if (self.level[floorX - 1][floorY] == 1 or
                            self.level[floorX + 1][floorY] == 1 or
                            self.level[floorX][floorY - 1] == 1 or
                            self.level[floorX][floorY + 1] == 1):
                        break

            # look around the tile for other floor tiles
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x != 0 or y != 0:  # Exclude the center tile
                        newX = floorX + (x * self.shortcutLength)
                        newY = floorY + (y * self.shortcutLength)
                        if self.level[newX][newY] == 0:
                            # run pathfinding algorithm between the two points
                            # back to the libtcodpy nonesense
                            pathMap = libtcod.path_new_using_map(libtcodMap)
                            libtcod.path_compute(pathMap, floorX, floorY, newX, newY)
                            distance = libtcod.path_size(pathMap)

                            if distance > self.minPathfindingDistance:
                                # make shortcut
                                self.carve_shortcut(floorX, floorY, newX, newY)
                                self.recompute_path_map(mapWidth, mapHeight, libtcodMap)

        # destroy the path object
        libtcod.path_delete(pathMap)

    def recompute_path_map(self, mapWidth, mapHeight, libtcodMap):
        for x in range(mapWidth):
            for y in range(mapHeight):
                if self.level[x][y] == 1:
                    libtcod.map_set_properties(libtcodMap, x, y, False, False)
                else:
                    libtcod.map_set_properties(libtcodMap, x, y, True, True)

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
        roomWidth, roomHeight = self.get_room_dimensions(room)
        for x in range(roomWidth):
            for y in range(roomHeight):
                if room[x][y] == 0:
                    return True
        return False