from __future__ import annotations

import logging
import tcod.map
from typing import TYPE_CHECKING, Optional, Tuple
from scripts.engine import entity, utility
from scripts.engine.component import Position, Blocking
from scripts.engine.core.constants import TargetTag, FOVInfo, Shape, TargetTagType
from scripts.engine.core.store import store
from scripts.engine.world_objects.game_map import GameMap
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List, Tuple, Union


########################## CREATE #########################

def create_game_map(width, height):
    """
    Create new GameMap
    """
    store.current_game_map = GameMap(width, height)


def create_fov_map() -> tcod.map.Map:
    """
    Create an fov map
    """
    game_map = get_game_map()
    width = game_map.width
    height = game_map.height

    fov_map = tcod.map_new(width, height)

    for x in range(width):
        for y in range(height):
            tile = get_tile((x, y))
            if tile:
                tcod.map_set_properties(fov_map, x, y, not tile.blocks_sight, not tile.blocks_movement)

    return fov_map


############################# GET ###########################


def get_game_map() -> GameMap:
    """
    Get current game_map
    """
    return store.current_game_map


def get_tile(tile_pos: Union[Tuple[int, int], str]) -> Optional[Tile]:
    """
    Get the tile at the specified location. Use tile_x and tile_y OR tile_pos_string "x,y".
    Returns None if tile is out of bounds.
    """
    game_map = get_game_map()

    if isinstance(tile_pos, str):
        _x, _y = tile_pos.split(",")
        x = int(_x)  # str to int
        y = int(_y)
    else:
        x = tile_pos[0]
        y = tile_pos[1]

    if _is_tile_in_bounds(x, y):
        return game_map.tiles[x][y]
    else:
        logging.warning(f"Tried to get tile({x},{y}), which is out of bounds.")
        return None


def get_direction(start_pos: Union[Tuple[int, int], str], target_pos: Union[Tuple[int, int],
str]) -> Tuple[int, int]:
    """
    Get the direction between two locations. Positions expect either "x,y", or handles tuples (x, y)
    """
    start_tile = get_tile(start_pos)
    target_tile = get_tile(target_pos)

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


def get_tiles(start_x: int, start_y: int, coords: List[Tuple[int, int]]) -> List[Tile]:
    """
    Get multiple tiles based on starting position and coordinates given. Coords are relative  to start
    position given.
    """
    game_map = get_game_map()
    tiles = []

    for coord in coords:
        tile_x = coord[0] + start_x
        tile_y = coord[1] + start_y

        # make sure it is in bounds
        if _is_tile_in_bounds(tile_x, tile_y):
            tiles.append(game_map.tiles[tile_x][tile_y])

    return tiles


def get_direct_direction(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
    """
    Get direction from an entity towards another entity`s location. Respects blocked tiles.
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
    # tile_is_blocked = _manager.Map._is_tile_blocking_movement(start_entity.x + direction_x,
    #                                                               start_entity.y + direction_y)
    #
    # if not (tile_is_blocked or get_entity_at_position(start_entity.x + direction_x,
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


def get_a_star_direction(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
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
    # game_map = _manager.game_map
    # entities = []
    # # TODO - update to use ECS
    # for ent, (pos, blocking) in _manager.World.get_entitys_components(Position, Blocking):
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
    # # Check also that the object isn't  or the target (so that the start and the end points are free)
    # # The AI class handles the situation if  is next to the target so it will not use this A* function
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
    # # Compute the path between `s coordinates and the target`s coordinates
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


def get_tiles_in_range_and_fov_of_entity(range_from_centre: int, active_entity: int) -> List[Tile]:
    """
    Get all of the tiles within a specified range of the player that are also in the FOV
    """
    # FIXME - update to ECS
    pass
    # get the tiles in range
    # coords = utility.get_coords_from_shape(Shape.SQUARE, range_from_centre)  # square as LOS is square
    # tiles_in_range = get_tiles(active_entity.x, active_entity.y, coords)
    # tiles_in_range_and_fov = []
    #
    # # only take tiles in range and FOV
    # in_fov = is_tile_in_fov
    # for tile in tiles_in_range:
    #     if in_fov(tile.x, tile.y):
    #         tiles_in_range_and_fov.append(tile)
    #
    # return tiles_in_range_and_fov


############# QUERIES ############

def tile_has_tag(tile: Tile, tag: TargetTagType, active_entity: Optional[int] = None) -> bool:
    """
    Check if a given tag applies to the tile.  True if tag applies.
    """
    if tag == TargetTag.OPEN_SPACE:
        # If in bounds check if anything is blocking
        if _is_tile_in_bounds(tile.x, tile.y):
            return not _is_tile_blocking_movement(tile.x, tile.y)
        else:
            return False
    elif tag == TargetTag.BLOCKED_MOVEMENT:
        # If in bounds check if anything is blocking
        if _is_tile_in_bounds(tile.x, tile.y):
            return _is_tile_blocking_movement(tile.x, tile.y)
        else:
            return True
    elif tag == TargetTag.SELF:
        if active_entity:
            return _tile_has_entity(tile.x, tile.y, active_entity)
        else:
            logging.warning("Tried to get TargetTag.SELF but gave no active_entity.")
            return False
    elif tag == TargetTag.OTHER_ENTITY:
        if active_entity:
            return _tile_has_other_entity(tile.x, tile.y, active_entity)
        else:
            logging.warning("Tried to get TargetTag.OTHER_ENTITY but gave no active_entity.")
            return False
    elif tag == TargetTag.NO_ENTITY:
        return not _tile_has_any_entity(tile.x, tile.y)
    elif tag == TargetTag.ANY:
        return True
    elif tag == TargetTag.IS_VISIBLE:
        return _is_tile_visible_to_player(tile.x, tile.y)
    else:
        # catch all
        return False


def tile_has_tags(tile: Tile, tags: List[TargetTagType], active_entity: int = None) -> bool:
    """
    Check a tile has all required tags
    """
    tags_checked = {}

    # assess all tags
    for tag in tags:
        tags_checked[tag] = tile_has_tag(tile, tag, active_entity)

    # if all tags came back true return true
    if all(value for value in tags_checked.values()):
        return True
    else:
        return False


def _is_tile_blocking_sight(x: int, y: int) -> bool:
    """
    Check if a tile is blocking sight
    """
    tile = get_tile((x, y))

    if tile:
        # Does the tile block movement?
        if tile.blocks_sight:
            return True

        # Any entities that block movement?
        for ent, (position, blocking) in entity.get_components([Position, Blocking]):
            if position.x == tile.x and position.y == tile.y and blocking.blocks_sight:
                return True

    # We found nothing blocking the tile
    return False


def _is_tile_visible_to_player(x: int, y: int) -> bool:
    """
    Check if the specified tile is visible to the player
    """
    tile = get_tile((x, y))
    if tile:
        return tile.is_visible
    else:
        return False


def _is_tile_in_bounds(x: int, y: int) -> bool:
    """
    Check if specified tile is in the map.
    """
    game_map = get_game_map()

    if (0 <= x < game_map.width) and (0 <= y < game_map.height):
        return True
    else:
        return False


def _is_tile_blocking_movement(x: int, y: int) -> bool:
    """
    Check if the specified tile is blocking movement
    """
    tile = get_tile((x, y))

    if tile:
        # Does the tile block movement?
        if tile.blocks_movement:
            return True

        # Any entities that block movement?
        for ent, (position, blocking) in entity.get_components([Position, Blocking]):
            if position.x == tile.x and position.y == tile.y and blocking.blocks_movement:
                return True

    # We found nothing blocking the tile
    return False


def _tile_has_any_entity(x: int, y: int) -> bool:
    """
    Check if the specified tile  has an entity on it
    """
    tile = get_tile((x, y))

    if tile:
        # Any entities on the tile?
        for ent, (position, ) in entity.get_components([Position]):
            if position.x == tile.x and position.y == tile.y:
                return True

    # We found no entities on the tile
    return False


def _tile_has_other_entity(x: int, y: int, active_entity: int) -> bool:
    """
    Check if the specified tile  has an entity that isnt the active entity on it
    """
    tile = get_tile((x, y))

    if tile:
        # ensure active entity is the same as the targeted one
        for ent, (position, ) in entity.get_components([Position]):
            if position.x == tile.x and position.y == tile.y:
                if active_entity != ent:
                    return True

    # no other entity found
    return False


def _tile_has_entity(x: int, y: int, active_entity: int) -> bool:
    """
    Check if the specified tile  has the active entity on it
    """
    tile = get_tile((x, y))

    if tile:
        # ensure active entity is the same as the targeted one
        for ent, (position, ) in entity.get_components([Position]):
            if position.x == tile.x and position.y == tile.y:
                if active_entity == ent:
                    return True

    # no matching entity found
    return False


def is_tile_in_fov(x: int, y: int, fov_map) -> bool:
    """
    Check if  target tile is in player`s FOV
    """
    return tcod.map_is_in_fov(fov_map, x, y)


################################ ACTIONS ###############################

def recompute_fov(x: int, y: int, radius: int, fov_map: tcod.map.Map):
    """
    Recalc the  fov
    """
    tcod.map_compute_fov(fov_map, x, y, radius, FOVInfo.LIGHT_WALLS, FOVInfo.FOV_ALGORITHM)


def update_tile_visibility(fov_map: tcod.map.Map):
    """
    Update the target fov
    """
    game_map = get_game_map()

    for x in range(0, game_map.width):
        for y in range(0, game_map.height):
            game_map.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)


def get_reflected_direction(current_position: Tuple[int, int], target_direction: Tuple[int, int]) -> Tuple[int, int]:
    """
    Use surrounding walls to understand how the object should be reflected.
    """
    current_x, current_y = current_position
    dir_x, dir_y = target_direction

    # work out position of adjacent walls
    adj_tile = world.get_tile((current_x, current_y - dir_y))
    if adj_tile:
        collision_adj_y = world.tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_y = True

    adj_tile = world.get_tile((current_x - dir_x, current_y))
    if adj_tile:
        collision_adj_x = world.tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_x = True

    # where did we collide?
    if collision_adj_x:
        if collision_adj_y:
            # hit a corner, bounce back towards entity
            dir_x *= -1
            dir_y *= -1
        else:
            # hit horizontal wall, reverse y direction
            dir_y *= -1
    else:
        if collision_adj_y:
            # hit a vertical wall, reverse x direction
            dir_x *= -1
        else:  # not collision_adj_x and not collision_adj_y:
            # hit a single piece, on the corner, bounce back towards entity
            dir_x *= -1
            dir_y *= -1

    return dir_x, dir_y