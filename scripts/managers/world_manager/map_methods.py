from __future__ import annotations

import logging
import math
import scipy.spatial

from typing import TYPE_CHECKING
from scripts.core.constants import TargetTags
from scripts.world.components import Position, Blocking
from scripts.world.game_map import GameMap
from scripts.world.tile import Tile

if TYPE_CHECKING:
    from typing import List, Tuple, Union
    from scripts.managers.world_manager.world_manager import WorldManager


class MapMethods:
    """
    Methods for querying game map and game map related info and taking game map actions.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        self._manager: WorldManager = manager
        self._current_game_map = None

    ########## CREATE ###############

    def create_game_map(self, width, height):
        """
        Create new GameMap and create player FOV
        """
        self._current_game_map = GameMap(width, height)

    ############# GET ###############

    def get_game_map(self) -> GameMap:
        """
        Get current game_map

        Returns:
            GameMap
        """
        return self._current_game_map

    def get_tile(self, tile_pos: Union[Tuple[int, int], str]) -> Union[Tile, None]:
        """
        Get the tile at the specified location. Use tile_x and tile_y OR tile_pos_string "x,y".
        Returns None if tile is out of bounds.
        """
        game_map = self.get_game_map()

        if isinstance(tile_pos, str):
            x, y = tile_pos.split(",")
            x = int(x)  # str to int
            y = int(y)
        else:
            x = tile_pos[0]
            y = tile_pos[1]

        if self._is_tile_in_bounds(x, y):
            return game_map.tiles[x][y]
        else:
            logging.warning(f"Tried to get tile({x},{y}), which is out of bounds.")
            return None

    def get_direction(self, start_pos: Union[Tuple[int, int], str], target_pos: Union[Tuple[int, int],
    str]) -> Tuple[int, int]:
        """
        Get the direction between two locations. Positions expect either "x,y", or handles tuples (x, y)
        """
        start_tile = self.get_tile(start_pos)
        target_tile = self.get_tile(target_pos)

        if start_tile and target_tile:
            dir_x = target_tile.x - start_tile.x
            dir_y = target_tile.y - start_tile.y
        else:
            # at least one of the tiles is out of bounds so return centre
            return 0, 0

        # handle any mistaken values coming in
        if dir_x > 1:
            dir_x = 1
        elif dir_x < -1:
            dir_x = -1

        if dir_y > 1:
            dir_y = 1
        elif dir_y < -1:
            dir_y = -1

        return dir_x, dir_y

    def get_tiles(self, start_tile_col, start_tile_row, coords):
        """
        Get multiple tiles based on starting position and coordinates given

        Args:
            start_tile_col (int):
            start_tile_row (int):
            coords (list[Tuple]): List of tuples holding x y. E.g. (x, y)

        Returns:
            List[Tile]:
        """
        game_map = self.get_game_map()
        tiles = []

        for coord in coords:
            tile_x = coord[0] + start_tile_col
            tile_y = coord[1] + start_tile_row

            # make sure it is in bounds
            if self._is_tile_in_bounds(tile_x, tile_y):
                tiles.append(game_map.tiles[tile_x][tile_y])

        return tiles

    @staticmethod
    def get_euclidean_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> float:
        """
        Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
        This returns a float indicating the straight line distance between the two points.

        Args:
            start_pos ():
            target_pos ():

        Returns:
            float: straight line distance

        """
        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]
        return math.sqrt(dx ** 2 + dy ** 2)

    @staticmethod
    def get_chebyshev_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
        """
        Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
        This returns an int indicating the number of tile moves between the two points.

        Args:
            start_pos ():
            target_pos ():

        Returns:
            int: distance in tiles

        """

        return scipy.spatial.distance.chebyshev(start_pos, target_pos)

    def get_direct_direction(self, start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
        """
        Get direction from an entity towards another entity`s location. Respects blocked tiles.

        Args:
            start_pos ():
            target_pos ():

        """
        # TODO - update to use EC
        pass
        #
        # log_string = f"{start_entity.name} is looking for a direct path to {target_entity.name}."
        # logging.debug(log_string)
        #
        # direction_x = target_entity.x - start_entity.x
        # direction_y = target_entity.y - start_entity.y
        # distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        #
        # direction_x = int(round(direction_x / distance))
        # direction_y = int(round(direction_y / distance))
        #
        # tile_is_blocked = self._manager.Map._is_tile_blocking_movement(start_entity.x + direction_x,
        #                                                               start_entity.y + direction_y)
        #
        # if not (tile_is_blocked or self.get_entity_at_position(start_entity.x + direction_x,
        #                                                     start_entity.y + direction_y)):
        #     log_string = f"{start_entity.name} found a direct path to {target_entity.name}."
        #     logging.debug(log_string)
        #
        #     return direction_x, direction_y
        # else:
        #     log_string = f"{start_entity.name} did NOT find a direct path to {target_entity.name}."
        #     logging.debug(log_string)
        #
        #     return start_entity.x, start_entity.y

    def get_a_star_direction(self, start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
        """
        Use a* pathfinding to get a direction from one entity to another
        Args:
            start_pos ():
            target_pos ():

        Returns:

        """
        # TODO - update to use EC
        pass
        #
        # max_path_length = 25
        # game_map = self._manager.game_map
        # entities = []
        # # TODO - update to use ECS
        # for ent, (pos, blocking) in self._manager.World.get_entitys_components(Position, Blocking):
        #     entities.append(ent)
        # entity_to_move = start_entity
        # target = target_entity
        #
        # log_string = f"{entity_to_move.name} is looking for a path to {target.name} with a*"
        # logging.debug(log_string)
        #
        # # Create a FOV map that has the dimensions of the map
        # fov = tcod.map_new(game_map.width, game_map.height)
        #
        # # Scan the current map each turn and set all the walls as unwalkable
        # for y1 in range(game_map.height):
        #     for x1 in range(game_map.width):
        #         tcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].blocks_sight,
        #                                 not game_map.tiles[x1][y1].blocks_movement)
        #
        # # Scan all the objects to see if there are objects that must be navigated around
        # # Check also that the object isn't self or the target (so that the start and the end points are free)
        # # The AI class handles the situation if self is next to the target so it will not use this A* function
        # # anyway
        # for entity in entities:
        #     if entity.blocks_movement and entity != entity_to_move and entity != target:
        #         # Set the tile as a wall so it must be navigated around
        #         tcod.map_set_properties(fov, entity.x, entity.y, True, False)
        #
        # # Allocate a A* path
        # # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        # my_path = tcod.path_new_using_map(fov, 1.41)
        #
        # # Compute the path between self`s coordinates and the target`s coordinates
        # tcod.path_compute(my_path, entity_to_move.x, entity_to_move.y, target.x, target.y)
        #
        # # Check if the path exists, and in this case, also the path is shorter than max_path_length
        # # The path size matters if you want the monster to use alternative longer paths (for example through
        # # other rooms) if for example the player is in a corridor
        # # It makes sense to keep path size relatively low to keep the monsters from running around the map if
        # # there`s an alternative path really far away
        # if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < max_path_length:
        #     # Find the next coordinates in the computed full path
        #     x, y = tcod.path_walk(my_path, True)
        #
        #     # convert to direction
        #     direction_x = x - entity_to_move.x
        #     direction_y = y - entity_to_move.y
        #
        #     log_string = f"{entity_to_move.name} found an a* path to {target.name}..."
        #     log_string2 = f"-> will move from [{entity_to_move.x},{entity_to_move.y}] towards [{x}," \
        #                   f"{y}] in direction " \
        #                   f"[{direction_x},{direction_y}]"
        #     logging.debug(log_string)
        #     logging.debug(log_string2)
        #
        # else:
        #     # no path found return no movement direction
        #     direction_x, direction_y = 0, 0
        #     log_string = f"{entity_to_move.name} did NOT find an a* path to {target.name}."
        #     logging.debug(log_string)
        #
        # # Delete the path to free memory
        # tcod.path_delete(my_path)
        # return direction_x, direction_y

    ############# QUERIES ############

    def tile_has_tag(self, tile: Tile, tag: TargetTags, active_entity: int = None) -> bool:
        """
        Check if a given tag applies to the tile.  True if tag applies.
        """
        if tag == TargetTags.OPEN_SPACE:
            # If in bounds check if anything is blocking
            if self._is_tile_in_bounds(tile.x, tile.y):
                return not self._is_tile_blocking_movement(tile.x, tile.y)
            else:
                return False
        elif tag == TargetTags.BLOCKED_MOVEMENT:
            # If in bounds check if anything is blocking
            if self._is_tile_in_bounds(tile.x, tile.y):
                return self._is_tile_blocking_movement(tile.x, tile.y)
            else:
                return True
        elif tag == TargetTags.SELF:
            return self._tile_has_entity(tile.x, tile.y, active_entity)
        elif tag == TargetTags.OTHER_ENTITY:
            return self._tile_has_other_entity(tile.x, tile.y, active_entity)
        elif tag == TargetTags.NO_ENTITY:
            return not self._tile_has_any_entity(tile.x, tile.y)
        elif tag == TargetTags.ANY:
            return True
        elif tag == TargetTags.IS_VISIBLE:
            return self._is_tile_visible_to_player(tile.x, tile.y)
        else:
            # catch all
            return False

    def tile_has_tags(self, tile: Tile, tags: List[TargetTags], active_entity: int = None) -> bool:
        """
        Check a tile has all required tags

        Args:
            tile():
            tags():
            active_entity():

        Returns:
            bool: True if tile has all tags
        """
        tags_checked = {}

        # assess all tags
        for tag in tags:
            tags_checked[tag] = self.tile_has_tag(tile, tag, active_entity)

        # if all tags came back true return true
        if all(value for value in tags_checked.values()):
            return True
        else:
            return False

    def _is_tile_blocking_sight(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if a tile is blocking sight

        Args:
            tile_x:
            tile_y:

        Returns:
            bool:
        """
        tile = self.get_tile((tile_x, tile_y))

        if tile:
            # Does the tile block movement?
            if tile.blocks_sight:
                return True

            # Any entities that block movement?
            for ent, (position, blocking) in self._manager.World.get_entitys_components(Position, Blocking):
                if position.x == tile.x and position.y == tile.y and blocking.blocks_sight:
                    return True

        # We found nothing blocking the tile
        return False

    def _is_tile_visible_to_player(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if the specified tile is visible to the player

        """
        tile = self.get_tile((tile_x, tile_y))
        if tile:
            return tile.is_visible
        else:
            return False

    def _is_tile_in_bounds(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if specified tile is in the map.
        """
        game_map = self.get_game_map()

        if (0 <= tile_x < game_map.width) and (0 <= tile_y < game_map.height):
            return True
        else:
            return False

    def _is_tile_blocking_movement(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if the specified tile is blocking movement
        Args:
            tile_x:
            tile_y:

        Returns:
            bool:

        """
        tile = self.get_tile((tile_x, tile_y))

        if tile:
            # Does the tile block movement?
            if tile.blocks_movement:
                return True

            # Any entities that block movement?
            for ent, (position, blocking) in self._manager.Entity.get_components(Position, Blocking):
                if position.x == tile.x and position.y == tile.y and blocking.blocks_movement:
                    return True

        # We found nothing blocking the tile
        return False

    def _tile_has_any_entity(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if the specified tile  has an entity on it
        Args:
            tile_x:
            tile_y:

        Returns:
            bool:

        """
        tile = self.get_tile((tile_x, tile_y))

        if tile:
            # Any entities on the tile?
            for ent, position in self._manager.World.get_entitys_component(Position):
                if position.x == tile.x and position.y == tile.y:
                    return True

        # We found no entities on the tile
        return False

    def _tile_has_other_entity(self, tile_x: int, tile_y: int, active_entity: int) -> bool:
        """
        Check if the specified tile  has an entity that isnt the active entity on it
        """
        tile = self.get_tile((tile_x, tile_y))

        if tile:
            # ensure active entity is the same as the targeted one
            for entity, position in self._manager.Entity.get_component(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity != entity:
                        return True

        # no other entity found
        return False

    def _tile_has_entity(self, tile_x: int, tile_y: int, active_entity: int) -> bool:
        """
        Check if the specified tile  has the active entity on it
        Args:
            active_entity :
            tile_x:
            tile_y:

        Returns:
            bool:

        """
        tile = self.get_tile((tile_x, tile_y))

        if tile:
            # ensure active entity is the same as the targeted one
            for entity, position in self._manager.World.get_entitys_component(Position):
                if position.x == tile.x and position.y == tile.y:
                    if active_entity == entity:
                        return True

        # no matching entity found
        return False


