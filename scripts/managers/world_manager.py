import tcod

from scripts.world.game_map import GameMap


class WorldManager:
    def __init__(self):
        self.game_map = None
        self.player_fov_map = None
        self.player_fov_is_dirty = False
        self.light_walls = True
        self.fov_algorithm = 0

    def create_new_map(self, map_width, map_height):
        """
        :return GameMap
        """
        self.game_map = GameMap(map_width, map_height)

    def create_player_fov_map(self):

        self.player_fov_map = tcod.map_new(self.game_map.width, self.game_map.height)

        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                tcod.map_set_properties(self.player_fov_map, x, y, not self.game_map.tiles[x][y].block_sight,
                                        not self.game_map.tiles[x][y].blocks_movement)

        self.player_fov_is_dirty = True

    def recompute_player_fov(self, x, y, radius):
        tcod.map_compute_fov(self.player_fov_map, x, y, radius, self.light_walls, self.fov_algorithm)
        self.player_fov_is_dirty = False