import tcod


class FOVMethods:
    """
    Methods for querying the fov and fov related info and taking fov actions.
    """
    def __init__(self, manager):
        self.manager = manager

    def create_player_fov_map(self, width, height):
        """
        Create the fov map for the player
        """
        self.manager.player_fov_map = tcod.map_new(width, height)

        for x in range(width):
            for y in range(height):
                tile = self.manager.Map.get_tile(x, y)
                tcod.map_set_properties(self.get_player_fov(), x, y, not tile.blocks_sight,
                                        not tile.blocks_movement)

        self.set_player_fov_state(True)

    def recompute_player_fov(self, x, y, radius):
        """

        Args:
            x:
            y:
            radius:
        """
        tcod.map_compute_fov(self.get_player_fov(), x, y, radius, self.manager.light_walls,
                             self.manager.fov_algorithm)
        self.manager.Map.update_tile_visibility(self.manager.player_fov_map)
        self.set_player_fov_state(False)

    def is_tile_in_fov(self, tile_x, tile_y):
        """
        Check if  target tile is in player`s FOV

        Args:
            tile_x: x of tile
            tile_y: y of tile

        Returns:
            bool: True if tile is in FOV
        """

        return tcod.map_is_in_fov(self.get_player_fov(), tile_x, tile_y)

    def set_player_fov_state(self, dirty):
        """
        Set the player's FOV to dirty

        Args:
            dirty (bool):
        """
        self.manager.player_fov_is_dirty = dirty

    def get_player_fov(self):
        """
        Get the player fov map

        Returns:
            tcod.map.Map
        """
        return self.manager.player_fov_map
