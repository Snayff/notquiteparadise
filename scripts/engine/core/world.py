from __future__ import annotations

import logging
from typing import Dict, List, Optional, Tuple, Type, TYPE_CHECKING

import numpy as np
import snecs
from snecs.typedefs import EntityID

from scripts.engine.core import query, utility
from scripts.engine.core.component import FOV, Physicality, Position
from scripts.engine.internal.constant import (
    Direction,
    DirectionType,
    Height,
    TileTag,
    TileTagType,
    TravelMethod,
    TravelMethodType,
)
from scripts.engine.world_objects.game_map import GameMap
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List, Optional, Tuple

    from scripts.engine.internal.action import Skill


__all__ = ["get_game_map"]


########################### LOCAL DEFINITIONS ##########################

serialise = snecs.serialize_world
deserialise = snecs.deserialize_world
move_world = snecs.ecs.move_world


############################# GET - RETURN AN EXISTING SOMETHING ###########################

def get_game_map() -> GameMap:
    """
    Get current game_map. Raises AttributeError if game_map doesnt exist.
    """
    from scripts.engine.internal.data import store
    if store.current_game_map:
        game_map = store.current_game_map
    else:
        raise AttributeError("get_game_map: Tried to get the game_map but there isnt one.")
    return game_map


def get_tile(tile_pos: Tuple[int, int]) -> Tile:
    """
    Get the tile at the specified location. Raises exception if out of bounds or doesnt exist.
    """
    from scripts.engine.internal.data import store
    game_map = store.current_game_map  # not using get_game_map for performance
    assert isinstance(game_map, GameMap)
    x, y = tile_pos

    try:
        tile = game_map.tile_map[x][y]

    except IndexError:
        raise IndexError(f"Tried to get tile({x},{y}), which doesnt exist.")

    if _is_tile_in_bounds(tile, game_map):
        return tile
    else:
        raise IndexError(f"Tried to get tile({x},{y}), which is out of bounds.")


def get_tiles(start_pos: Tuple[int, int], coords: List[Tuple[int, int]]) -> List[Tile]:
    """
    Get multiple tiles based on starting position and coordinates given. Coords are relative  to start
    position given.
    """
    start_x, start_y = start_pos
    from scripts.engine.internal.data import store
    game_map = store.current_game_map  # not using get_game_map for performance
    assert isinstance(game_map, GameMap)
    tiles = []

    for coord in coords:
        x = coord[0] + start_x
        y = coord[1] + start_y

        # make sure it is in bounds
        tile = get_tile((x, y))
        if _is_tile_in_bounds(tile, game_map):
            tiles.append(game_map.tile_map[x][y])

    return tiles


def get_direction(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> DirectionType:
    """
    Get the direction between two locations.
    """
    start_tile = get_tile(start_pos)
    target_tile = get_tile(target_pos)

    if start_tile and target_tile:
        dir_x = target_tile.x - start_tile.x
        dir_y = target_tile.y - start_tile.y
    else:
        # at least one of the tiles is out of bounds so return centre
        return Direction.CENTRE

    # handle any mistaken values coming in
    dir_x = utility.clamp(dir_x, -1, 1)
    dir_y = utility.clamp(dir_y, -1, 1)

    return dir_x, dir_y  # type: ignore


def get_entity_blocking_movement_map() -> np.ndarray:
    """
    Return a Numpy array of bools, True for blocking and False for open
    """

    game_map = get_game_map()
    blocking_map = np.zeros((game_map.width, game_map.height), dtype=bool, order="F")
    for entity, (pos, physicality) in query.position_and_physicality:
        assert isinstance(physicality, Physicality)
        assert isinstance(pos, Position)
        if physicality.blocks_movement:
            blocking_map[pos.x, pos.y] = True

    return blocking_map


def get_a_star_path(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> List[List[int]]:
    """
    Get a list of coords that dictates the path between 2 entities.
    """
    from scripts.engine.core.matter import create_pathfinder
    pathfinder = create_pathfinder()

    # add points
    pathfinder.add_root(start_pos)
    path = pathfinder.path_to(target_pos).tolist()
    assert isinstance(path, list)

    return path


def get_a_star_direction(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> Optional[DirectionType]:
    """
    Use a* pathfinding to get a direction from one entity to another. Does not allow diagonals.
    """
    path = get_a_star_path(start_pos, target_pos)

    # if there is a path then return direction
    if path:
        _start_pos = path[0]
        next_pos = path[1]
        move_dir = get_direction(_start_pos, next_pos)  # type: ignore  # list instead of tuple is fine
        return move_dir

    return None


def get_reflected_direction(
    active_entity: EntityID, current_pos: Tuple[int, int], target_direction: Tuple[int, int]
) -> DirectionType:
    """
    Use surrounding walls to understand how the object should be reflected.
    """
    current_x, current_y = current_pos
    dir_x, dir_y = target_direction

    # work out position of adjacent walls
    adj_tile = get_tile((current_x, current_y - dir_y))
    if adj_tile:
        collision_adj_y = tile_has_tag(active_entity, adj_tile, TileTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_y = True

    adj_tile = get_tile((current_x - dir_x, current_y))
    if adj_tile:
        collision_adj_x = tile_has_tag(active_entity, adj_tile, TileTag.BLOCKED_MOVEMENT)
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

    return dir_x, dir_y  # type: ignore


def get_euclidean_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> float:
    """
    Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
    This returns a float indicating the straight line distance between the two points.
    """
    dx = target_pos[0] - start_pos[0]
    dy = target_pos[1] - start_pos[1]
    import math  # only used in this method

    return math.sqrt(dx ** 2 + dy ** 2)


def get_chebyshev_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
    """
    Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
    This returns an int indicating the number of tile moves between the two points.
    """
    from scipy import spatial  # only used in this method

    distance = spatial.distance.chebyshev(start_pos, target_pos)
    return distance


def _get_furthest_free_position(
    active_entity: EntityID,
    start_pos: Tuple[int, int],
    target_direction: Tuple[int, int],
    max_distance: int,
    travel_type: TravelMethodType,
) -> Tuple[int, int]:
    """
    Checks each position in a line and returns the last position that doesnt block movement. If no position in
    range blocks movement then the last position checked is returned. If all positions in range block movement
    then starting position is returned.
    """
    start_x = start_pos[0]
    start_y = start_pos[1]
    dir_x = target_direction[0]
    dir_y = target_direction[1]
    current_x = start_x
    current_y = start_y
    free_x = start_x
    free_y = start_y
    check_for_target = False

    # determine travel method
    if travel_type == TravelMethod.STANDARD:
        # standard can hit a target at any point during travel
        check_for_target = True
    elif travel_type == TravelMethod.ARC:
        # throw can only hit target at end of travel
        check_for_target = False

    # determine impact location N.B. +1 to make inclusive as starting from 1
    for distance in range(1, max_distance + 1):

        # allow throw to hit target
        if travel_type == TravelMethod.ARC and distance == max_distance + 1:
            check_for_target = True

        # get current position
        current_x = start_x + (dir_x * distance)
        current_y = start_y + (dir_y * distance)
        tile = get_tile((current_x, current_y))

        if tile:
            # did we hit something causing standard to stop
            if tile_has_tag(active_entity, tile, TileTag.BLOCKED_MOVEMENT):
                # if we're ready to check for a target, do so
                if check_for_target:
                    # we hit something, go back to last free tile
                    current_x = free_x
                    current_y = free_y
                    break
            else:
                free_x = current_x
                free_y = current_y

    return current_x, current_y


def get_cast_positions(
    entity: EntityID, target_pos: Position, skills: List[Type[Skill]]
) -> Dict[Type[Skill], List[Tuple[int, int]]]:
    """
    Check through list of skills to find unblocked cast positions to target
    """
    skill_dict: Dict[Type[Skill], List[Tuple[int, int]]] = {}

    # loop all skills and all directions
    for skill in skills:
        skill_dict[skill] = []
        for direction in skill.target_directions:
            # work out from target pos, reversing direction as we are working from target, not towards them
            for _range in range(1, skill.range + 1):  # +1 to be inclusive
                x = target_pos.x + (-_range * direction[0])
                y = target_pos.y + (-_range * direction[1])

                # check tile is open and in vision
                tile = get_tile((x, y))
                has_tags = tile_has_tags(entity, tile, [TileTag.IS_VISIBLE, TileTag.OPEN_SPACE])
                has_self = tile_has_tag(entity, tile, TileTag.SELF)
                if has_tags or has_self:
                    skill_dict[skill].append((x, y))

                else:
                    # space blocked so further out spaces will be no good either
                    break

    return skill_dict


############################# QUERIES - CAN, IS, HAS - RETURN BOOL #############################

def tile_has_tag(active_entity: EntityID, tile: Tile, tag: TileTagType) -> bool:
    """
    Check if a given tag applies to the tile.  True if tag applies.
    """
    from scripts.engine.internal.data import store
    game_map = store.current_game_map  # not using get_game_map for performance
    assert isinstance(game_map, GameMap)

    # before we even check tags, lets confirm it is in bounds
    if not _is_tile_in_bounds(tile, game_map):
        return False

    if tag == TileTag.OPEN_SPACE:
        # if nothing is blocking movement
        if not tile.blocks_movement and not _tile_has_entity_blocking_movement(tile):
            return True
        else:
            return False
    elif tag == TileTag.BLOCKED_MOVEMENT:
        # if anything is blocking
        if tile.blocks_movement or _tile_has_entity_blocking_movement(tile):
            return True
        else:
            return False
    elif tag == TileTag.SELF:
        # if entity on tile is same as active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            return _tile_has_specific_entity(tile, active_entity)
        else:
            logging.warning("tile_has_tag: Tried to get TileTag.SELF but gave no active_entity.")
            return False
    elif tag == TileTag.OTHER_ENTITY:
        # if entity on tile is not active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            # check both possibilities. either the tile containing the active entity or not
            return _tile_has_other_entities(tile, active_entity)
        else:
            logging.warning("tile_has_tag: Tried to get TileTag.OTHER_ENTITY but gave no active_entity.")
            return False
    elif tag == TileTag.NO_ENTITY:
        # if the tile has no entity
        return not _tile_has_any_entity(tile)
    elif tag == TileTag.ANY:
        # if the tile is anything at all
        return True
    elif tag == TileTag.IS_VISIBLE:
        # if player can see the tile
        return _is_tile_visible_to_entity(tile, active_entity, game_map)
    elif tag == TileTag.NO_BLOCKING_TILE:
        # if tile isnt blocking movement
        if _is_tile_in_bounds(tile, game_map):
            return not tile.blocks_movement
        else:
            return False
    elif tag == TileTag.ACTOR:
        # if the tile contains an actor
        for query_result in query.actors:
            # this is a very dirty way to access the position of a query result
            # I don't want to scan for the position component since it would severely bog down performance if many
            # entities exist and this function is used frequently
            # structuring the results as a dict may be beneficial
            position = query_result[1][0]
            assert isinstance(position, Position)
            if (position.x, position.y) == (tile.x, tile.y):
                return True
        return False

    # If we've hit here it must be false!
    logging.warning(f"tile_has_tag: TileTag {tag} does not exist.")
    return False


def tile_has_tags(active_entity: EntityID, tile: Tile, tags: List[TileTagType]) -> bool:
    """
    Check a tile has all required tags
    """
    tags_checked = {}

    # assess all tags
    for tag in tags:
        tags_checked[tag] = tile_has_tag(active_entity, tile, tag)

    # if all tags came back true return true
    if all(value for value in tags_checked.values()):
        return True
    else:
        return False


def _is_tile_blocking_sight(tile: Tile) -> bool:
    """
    Check if a tile is blocking sight
    """
    # assumes tile are min or max height only.
    if tile.height == Height.MAX:
        return True
    return False


def _is_tile_visible_to_entity(tile: Tile, entity: EntityID, game_map: GameMap) -> bool:
    """
    Check if the specified tile is visible to the entity
    """
    from scripts.engine.core.matter import get_entitys_component
    fov_map = get_entitys_component(entity, FOV).map
    light_map = game_map.light_map

    # combine maps
    visible_map = fov_map & light_map  # type: ignore

    return bool(visible_map[tile.x, tile.y])


def _is_tile_in_bounds(tile: Tile, game_map: GameMap) -> bool:
    """
    Check if specified tile is in the map.
    """
    return (0 <= tile.x < game_map.width) and (0 <= tile.y < game_map.height)


def _tile_has_any_entity(tile: Tile) -> bool:
    """
    Check if the specified tile  has an entity on it
    """
    from scripts.engine.core.matter import get_entities_on_tile
    return len(get_entities_on_tile(tile)) > 0


def _tile_has_other_entities(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile has other entities apart from the provided active entity
    """
    from scripts.engine.core.matter import get_entities_on_tile
    entities_on_tile = get_entities_on_tile(tile)
    active_entity_is_on_tile = active_entity in entities_on_tile
    return (len(entities_on_tile) > 0 and not active_entity_is_on_tile) or (
        len(entities_on_tile) > 1 and active_entity_is_on_tile
    )


def _tile_has_specific_entity(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile  has the specified entity on it
    """
    from scripts.engine.core.matter import get_entities_on_tile
    return active_entity in get_entities_on_tile(tile)


def _tile_has_entity_blocking_movement(tile: Tile) -> bool:
    x = tile.x
    y = tile.y

    # Any entities that block movement?
    from scripts.engine.core.matter import get_components
    for entity, (position, physicality) in get_components([Position, Physicality]):
        assert isinstance(position, Position)
        assert isinstance(physicality, Physicality)

        if (x, y) in position and physicality.blocks_movement:
            return True
    return False


def _tile_has_entity_blocking_sight(tile: Tile, active_entity: EntityID) -> bool:
    x = tile.x
    y = tile.y

    from scripts.engine.core.matter import entity_has_component
    if entity_has_component(active_entity, Physicality):
        from scripts.engine.core.matter import get_entitys_component
        viewer_height = get_entitys_component(active_entity, Physicality).height
    else:
        # viewer has no height, assume everything blocks
        return True

    # Any entities that block sight?
    from scripts.engine.core.matter import get_components
    for entity, (position, physicality) in get_components([Position, Physicality]):
        assert isinstance(position, Position)
        assert isinstance(physicality, Physicality)

        if (x, y) in position and physicality.height > viewer_height:
            return True
    return False


def is_direction_blocked(entity: EntityID, dir_x: int, dir_y: int) -> bool:
    """
    Checks if the entity will collide with something when trying to move in the provided direction. Returns True
    if blocked.
    """
    collides = False
    direction_name = utility.value_to_member((dir_x, dir_y), Direction)
    from scripts.engine.core.matter import get_entitys_component
    position = get_entitys_component(entity, Position)

    for coordinate in position.coordinates:
        target_x = coordinate[0] + dir_x
        target_y = coordinate[1] + dir_y
        target_tile = get_tile((target_x, target_y))

        # check a tile was returned
        is_tile_blocking_movement = False
        if target_tile:
            is_tile_blocking_movement = tile_has_tag(entity, target_tile, TileTag.BLOCKED_MOVEMENT)

        # check if tile is blocked
        if is_tile_blocking_movement:
            # find out who is blocking
            for other_entity, (pos, physicality) in query.position_and_physicality:
                assert isinstance(pos, Position)
                assert isinstance(physicality, Physicality)
                if other_entity != entity and physicality.blocks_movement and (target_x, target_y) in pos.coordinates:
                    # blocked by entity
                    from scripts.engine.core.matter import get_name
                    blockers_name = get_name(other_entity)
                    name = get_name(entity)
                    logging.debug(
                        f"'{name}' tried to move {direction_name} to ({target_x},{target_y}) but was blocked"
                        f" by '{blockers_name}'. "
                    )
                    break
            collides = True

    return collides

