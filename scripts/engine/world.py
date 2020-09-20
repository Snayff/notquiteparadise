from __future__ import annotations

import dataclasses
import logging
import random
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Type, TypeVar, cast

import numpy as np
import pygame
import snecs
import tcod.map
from snecs import Component, Query, new_entity
from snecs.typedefs import EntityID

from scripts.engine import action, chronicle, debug, library, utility
from scripts.engine.component import (
    FOV,
    Aesthetic,
    Afflictions,
    Behaviour,
    Blocking,
    HasCombatStats,
    Identity,
    IsActor,
    IsGod,
    IsPlayer,
    Knowledge,
    Opinion,
    Position,
    Resources,
    Tracked,
    Traits,
)
from scripts.engine.core.constants import (
    ICON_SIZE,
    INFINITE,
    TILE_SIZE,
    Direction,
    DirectionType,
    HitType,
    HitTypeType,
    PrimaryStat,
    PrimaryStatType,
    RenderLayer,
    ResourceType,
    SecondaryStatType,
    ShapeType,
    TargetTag,
    TargetTagType,
    TraitGroup,
    TravelMethod,
    TravelMethodType,
)
from scripts.engine.core.data import store
from scripts.engine.core.definitions import ActorData, ProjectileData, TraitSpritePathsData, TraitSpritesData
from scripts.engine.thought import ProjectileBehaviour, SkipTurnBehaviour
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.combat_stats import CombatStats
from scripts.engine.world_objects.gamemap import Gamemap
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List
    from scripts.engine.action import Affliction, Skill

########################### LOCAL DEFINITIONS ##########################

_C = TypeVar("_C", bound=Component)  # to represent components where we don't know which is being used
get_entitys_components = snecs.all_components
get_components = Query
entity_has_component = snecs.has_component
serialise = snecs.serialize_world
deserialise = snecs.deserialize_world
move_world = snecs.ecs.move_world


################################ CREATE - INIT OBJECT - RETURN NEW OBJECT ###############################

def create_entity(components: List[Component] = None) -> EntityID:
    """
    Use each component in a list of components to create_entity an entity
    """
    if components is None:
        _components = []
    else:
        _components = components

    # create the entity
    entity = new_entity(_components)

    return entity


def create_god(god_name: str) -> EntityID:
    """
    Create an entity with all of the components to be a god. god_name must be in the gods json file.
    """
    data = library.GODS[god_name]
    god: List[Component] = []

    god.append(Identity(data.name, data.description))
    god.append(IsGod())
    god.append(Opinion())
    god.append((Resources(INFINITE, INFINITE)))
    entity = create_entity(god)

    logging.debug(f"God, '{data.name}', created.")

    return entity


def create_actor(actor_data: ActorData, spawn_pos: Tuple[int, int], is_player: bool = False) -> EntityID:
    """
    Create an entity with all of the components to be an actor. Returns entity ID.
    """
    components: List[Component] = []
    x, y = spawn_pos

    # get dimensions of actor
    occupied_tiles = []
    for offset in actor_data.position_offsets:
        occupied_tiles.append((offset[0] + x, offset[1] + y))

    #  choose a name
    name = random.choice(actor_data.possible_names)

    # actor components
    if is_player:
        components.append(IsPlayer())
    components.append(IsActor())
    components.append(Position(*occupied_tiles))
    components.append(Identity(name, actor_data.description))
    components.append(HasCombatStats())
    components.append(Blocking(True, library.GAME_CONFIG.default_values.entity_blocks_sight))
    components.append(Traits(actor_data.trait_names))
    components.append(FOV(create_fov_map()))
    components.append(Tracked(chronicle.get_time()))

    # get info from traits
    traits_paths = []  # for aesthetic

    move = action.skill_registry["move"]
    basic_attack = action.skill_registry["basic_attack"]
    known_skills = [move, basic_attack]  # for knowledge
    skill_order = ["basic_attack"]  # for knowledge
    perm_afflictions_names = []  # for affliction
    behaviour = None

    # loop each trait and get info for skills etc.
    for name in actor_data.trait_names:
        data = library.TRAITS[name]
        traits_paths.append(data.sprite_paths)
        if data.known_skills != ["none"]:

            for skill_name in data.known_skills:
                skill_data = library.SKILLS[skill_name]
                skill_class = action.skill_registry[skill_data.key]
                known_skills.append(skill_class)
                skill_order.append(skill_name)

        if data.permanent_afflictions != ["none"]:
            for _name in data.permanent_afflictions:
                perm_afflictions_names.append(_name)

        if data.group == TraitGroup.NPC:
            # FIXME - get behaviour
            behaviour = SkipTurnBehaviour

    # add aesthetic
    traits_paths.sort(key=lambda path: path.render_order, reverse=True)
    sprites = build_sprites_from_paths(traits_paths)

    # N.B. translation to screen coordinates is handled by the camera
    components.append(Aesthetic(sprites.idle, sprites, traits_paths, RenderLayer.ACTOR, (x, y)))

    # add skills to entity
    components.append(Knowledge(known_skills, skill_order))

    # create the entity
    entity = create_entity(components)

    # add permanent afflictions, since we can only add them once an entity is created
    perm_afflictions = []
    for name in perm_afflictions_names:
        # create the affliction with no specific source
        perm_afflictions.append(
            create_affliction(name, entity, entity, INFINITE)
        )
    add_component(entity, Afflictions(perm_afflictions))

    # add behaviour  N.B. Can only be added once entity is created
    if behaviour:
        add_component(entity, Behaviour(behaviour(entity)))

    # give full resources N.B. Can only be added once entity is created
    stats = create_combat_stats(entity)
    add_component(entity, Resources(stats.max_health, stats.max_stamina))

    logging.debug(f"Entity, '{name}', created.")

    return entity


def create_projectile(creating_entity: EntityID, tile_pos: Tuple[int, int], data: ProjectileData) -> EntityID:
    """
    Create an entity with all of the components to be a projectile. Returns entity ID.
    """
    skill_name = data.skill_name
    projectile: List[Component] = []
    x, y = tile_pos

    name = get_name(creating_entity)
    projectile_name = f"{name}s {skill_name}s projectile"
    desc = f"{skill_name} on its way."
    projectile.append(Identity(projectile_name, desc))

    sprites = build_sprites_from_paths([data.sprite_paths], (TILE_SIZE, TILE_SIZE))

    # translation to screen coordinates is handled by the camera
    projectile.append(Aesthetic(sprites.move, sprites, [data.sprite_paths], RenderLayer.ACTOR, (x, y)))
    projectile.append(Tracked(chronicle.get_time_of_last_turn() - 1))  # allocate time to ensure they act next
    projectile.append(Position((x, y)))  # FIXME - check position not blocked before spawning
    projectile.append(Resources(999, 999))
    projectile.append(Afflictions())

    entity = create_entity(projectile)

    add_component(entity, Behaviour(ProjectileBehaviour(entity, data)))

    move = action.skill_registry["move"]
    known_skills = [move]
    add_component(entity, Knowledge(known_skills))

    logging.debug(f"{name}`s projectile created at ({x},{y}) heading {data.direction}.")

    return entity


def create_affliction(name: str, creator: EntityID, target: EntityID, duration: int) -> Affliction:
    """
    Creates an instance of an Affliction provided the name
    """
    affliction_data = library.AFFLICTIONS[name]
    affliction = action.affliction_registry[affliction_data.name](creator, target, duration)
    return affliction


def build_sprites_from_paths(sprite_paths: List[TraitSpritePathsData],
        desired_size: Tuple[int, int] = (TILE_SIZE, TILE_SIZE)) -> TraitSpritesData:
    """
    Build a TraitSpritesData class from a list of TraitSpritePathsData. For each member in TraitSpritePathsData,
    combines the sprites from each TraitSpritePathsData in the  list and flattens to a single surface.
    """
    paths: Dict[str, List[str]] = {}
    sprites: Dict[str, List[pygame.Surface]] = {}
    flattened_sprites: Dict[str, pygame.Surface] = {}

    # bundle into cross-trait sprite path lists
    for sprite_path in sprite_paths:
        char_dict = dataclasses.asdict(sprite_path)
        for name, path in char_dict.items():
            if name != "render_order":
                # check if key exists
                if name in paths:
                    paths[name].append(path)
                # if not init the dict
                else:
                    paths[name] = [path]

    # convert to sprites
    for name, path_list in paths.items():
        # override size for icon
        if name == "icon_path":
            desired_size = (ICON_SIZE, ICON_SIZE)

        sprites[name] = utility.get_images(path_list, desired_size)

    # flatten the images
    for name, surface_list in sprites.items():
        flattened_sprites[name] = utility.flatten_images(surface_list)

    # convert to dataclass
    converted = TraitSpritesData(**flattened_sprites)
    return converted


def create_fov_map() -> np.array:
    """
    Create a blank fov map
    """
    gamemap = get_gamemap()
    width = gamemap.width
    height = gamemap.height

    fov_map = np.zeros((width, height), dtype=bool, order="F")

    for x in range(width):
        for y in range(height):
            tile = get_tile((x, y))
            if tile:
                fov_map[x][y] = not tile.blocks_sight and not tile.blocks_movement

    return fov_map


def create_combat_stats(entity: EntityID) -> CombatStats:
    """
    Create and return a stat object  for an entity.
    """
    return CombatStats(entity)


############################# GET - RETURN AN EXISTING SOMETHING ###########################

def get_gamemap() -> Gamemap:
    """
    Get current gamemap
    """
    if store.current_gamemap:
        gamemap = store.current_gamemap
    else:
        raise Exception("get_gamemap: Tried to get the gamemap but there isnt one.")
    return gamemap


def get_tile(tile_pos: Tuple[int, int]) -> Tile:
    """
    Get the tile at the specified location. Raises exception if out of bounds or doesnt exist.
    """
    gamemap = get_gamemap()
    x = tile_pos[0]
    y = tile_pos[1]

    try:
        _tile = gamemap.tiles[x][y]

    except IndexError:
        raise Exception(f"Tried to get tile({x},{y}), which doesnt exist.")

    if _is_tile_in_bounds(_tile):
        return _tile
    else:
        raise Exception(f"Tried to get tile({x},{y}), which is out of bounds.")


def get_tiles(start_pos: Tuple[int, int], coords: List[Tuple[int, int]]) -> List[Tile]:
    """
    Get multiple tiles based on starting position and coordinates given. Coords are relative  to start
    position given.
    """
    start_x, start_y = start_pos
    gamemap = get_gamemap()
    tiles = []

    for coord in coords:
        x = coord[0] + start_x
        y = coord[1] + start_y

        # make sure it is in bounds
        tile = get_tile((x, y))
        if tile:
            if _is_tile_in_bounds(tile):
                tiles.append(gamemap.tiles[x][y])

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

    return cast(DirectionType, (dir_x, dir_y))


def get_direct_direction(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
    """
    Get direction from an entity towards another entity`s location. Respects blocked tiles.
    """
    # FIXME - update to use EC
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
    """
    # FIXME - update to use EC
    pass
    #
    # max_path_length = 25
    # gamemap = _manager.gamemap
    # entities = []
    # for entity, (pos, blocking) in _manager.get_entitys_components(Position, Blocking):
    #     entities.append(entity)
    # entity_to_move = start_entity
    # target = target_entity
    #
    # log_string = f"{entity_to_move.name} is looking for a path to {target.name} with a*"
    # logging.debug(log_string)
    #
    # # Create a FOV map that has the dimensions of the map
    # fov = tcod.map_new(gamemap.width, gamemap.height)
    #
    # # Scan the current map each turn and set all the walls as unwalkable
    # for y1 in range(gamemap.height):
    #     for x1 in range(gamemap.width):
    #         tcod.map_set_properties(fov, x1, y1, not gamemap.tiles[x1][y1].blocks_sight,
    #                                 not gamemap.tiles[x1][y1].blocks_movement)
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


def get_reflected_direction(current_pos: Tuple[int, int], target_direction: Tuple[int, int]) -> DirectionType:
    """
    Use surrounding walls to understand how the object should be reflected.
    """
    current_x, current_y = current_pos
    dir_x, dir_y = target_direction

    # work out position of adjacent walls
    adj_tile = get_tile((current_x, current_y - dir_y))
    if adj_tile:
        collision_adj_y = tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
    else:
        # found no tile
        collision_adj_y = True

    adj_tile = get_tile((current_x - dir_x, current_y))
    if adj_tile:
        collision_adj_x = tile_has_tag(adj_tile, TargetTag.BLOCKED_MOVEMENT)
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

    return cast(DirectionType, (dir_x, dir_y))


def _get_furthest_free_position(start_pos: Tuple[int, int], target_direction: Tuple[int, int],
        max_distance: int, travel_type: TravelMethodType) -> Tuple[int, int]:
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
        if travel_type == TravelMethod.ARC:
            if distance == max_distance + 1:
                check_for_target = True

        # get current position
        current_x = start_x + (dir_x * distance)
        current_y = start_y + (dir_y * distance)
        tile = get_tile((current_x, current_y))

        if tile:
            # did we hit something causing standard to stop
            if tile_has_tag(tile, TargetTag.BLOCKED_MOVEMENT):
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


def get_hit_type(to_hit_score: int) -> HitTypeType:
    """
    Get the hit type from the to hit score
    """
    hit_types_data = library.GAME_CONFIG.hit_types

    if to_hit_score >= hit_types_data.crit.value:
        return HitType.CRIT
    elif to_hit_score >= hit_types_data.hit.value:
        return HitType.HIT
    else:
        return HitType.GRAZE


def get_player() -> EntityID:
    """
    Get the player.
    """
    for entity, (flag,) in get_components([IsPlayer]):
        return entity
    raise ValueError


def get_entitys_component(entity: EntityID, component: Type[_C]) -> _C:
    """
    Get an entity's component. Will raise exception if entity does not have the component.  Use entity_has_component
    to check.
    """
    if entity_has_component(entity, component):
        return snecs.entity_component(entity, component)
    else:
        name = get_name(entity)
        raise Exception(f"'{name}'({entity}) tried to get {component.__name__}, but it was not found.")


def get_name(entity: EntityID) -> str:
    """
    Get an entity's Identity component's name.
    """
    identity = get_entitys_component(entity, Identity)
    if identity:
        name = identity.name
    else:
        name = "not found"

    return name


def get_primary_stat(entity: EntityID, primary_stat: PrimaryStatType) -> int:
    """
    Get an entity's primary stat.
    """
    stat = primary_stat
    value = 0

    stat_data = library.BASE_STATS_PRIMARY[stat]
    value += stat_data.base_value

    trait = get_entitys_component(entity, Traits)
    if trait:
        for name in trait.names:
            data = library.TRAITS[name]
            value += getattr(data, stat)

    afflictions = get_entitys_component(entity, Afflictions)
    if afflictions:
        for modifier in afflictions.stat_modifiers.values():
            if modifier[0] == stat:
                value += modifier[1]

    # ensure no dodgy numbers, like floats or negative
    value = max(1, int(value))

    return value


def get_secondary_stat(entity: EntityID, secondary_stat: SecondaryStatType) -> int:
    """
    Get an entity's secondary stat.
    """
    stat = secondary_stat
    value = 0

    # base values
    stat_data = library.BASE_STATS_SECONDARY[stat]
    value += stat_data.base_value

    # values from primary stats
    value += get_primary_stat(entity, PrimaryStat.VIGOUR) * stat_data.vigour_mod
    value += get_primary_stat(entity, PrimaryStat.CLOUT) * stat_data.clout_mod
    value += get_primary_stat(entity, PrimaryStat.SKULLDUGGERY) * stat_data.skullduggery_mod
    value += get_primary_stat(entity, PrimaryStat.BUSTLE) * stat_data.bustle_mod
    value += get_primary_stat(entity, PrimaryStat.EXACTITUDE) * stat_data.exactitude_mod

    # afflictions
    afflictions = get_entitys_component(entity, Afflictions)
    if afflictions:
        for modifier in afflictions.stat_modifiers.values():
            if modifier[0] == stat:
                value += modifier[1]

    # ensure no dodgy numbers, like floats or negative
    value = max(1, int(value))

    return value


def get_known_skill(entity: EntityID, skill_name: str) -> Type[Skill]:
    """
    Get an entity's known skill from their Knowledge component.
    """
    knowledge = get_entitys_component(entity, Knowledge)
    try:
        if knowledge:
            return knowledge.skills[skill_name]
    except KeyError:
        pass

    logging.warning(f"'{get_name(entity)}' tried to use a skill, '{skill_name}', they dont know.")
    raise Exception("Skill not found")


def get_affected_entities(target_pos: Tuple[int, int], shape: ShapeType, shape_size: int,
        shape_direction: Optional[Tuple[int, int]] = None):
    """
    Return a list of entities that are within the shape given, using target position as a centre point. Entity must
    have Position, Resources to be eligible.
    """
    affected_entities = []
    affected_positions = []
    target_x = target_pos[0]
    target_y = target_pos[1]

    # get affected tiles
    coords = utility.get_coords_from_shape(shape, shape_size, shape_direction)
    for coord in coords:
        affected_positions.append((coord[0] + target_x, coord[1] + target_y))

    # get relevant entities in target area
    for entity, (position, *others) in get_components([Position, Resources]):
        assert isinstance(position, Position)  # for mypy typing
        for affected_pos in affected_positions:
            if affected_pos in position:
                affected_entities.append(entity)

    return affected_entities


############################# QUERIES - CAN, IS, HAS - RETURN BOOL #############################

def tile_has_tag(tile: Tile, tag: TargetTagType, active_entity: Optional[int] = None) -> bool:
    """
    Check if a given tag applies to the tile.  True if tag applies.
    """
    # before we even check tags, lets confirm it is in bounds
    if not _is_tile_in_bounds(tile):
        return False

    if tag == TargetTag.OPEN_SPACE:
        # if nothing is blocking movement
        if not _is_tile_blocking_movement(tile) and not _tile_has_entity_blocking_movement(tile):
            return True
    elif tag == TargetTag.BLOCKED_MOVEMENT:
        # if anything is blocking
        if _is_tile_blocking_movement(tile) or _tile_has_entity_blocking_movement(tile):
            return True
    elif tag == TargetTag.SELF:
        # if entity on tile is same as active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            return _tile_has_specific_entity(tile, active_entity)
        else:
            logging.warning("Tried to get TargetTag.SELF but gave no active_entity.")
    elif tag == TargetTag.OTHER_ENTITY:
        # if entity on tile is not active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            # check both possibilities. either the tile containing the active entity or not
            return _tile_has_other_entities(tile, active_entity)
        else:
            logging.warning("Tried to get TargetTag.OTHER_ENTITY but gave no active_entity.")
    elif tag == TargetTag.NO_ENTITY:
        # if the tile has no entity
        return not _tile_has_any_entity(tile)
    elif tag == TargetTag.ANY:
        # if the tile is anything at all
        return True
    elif tag == TargetTag.IS_VISIBLE:
        # if player can see the tile
        return _is_tile_visible_to_player(tile)
    elif tag == TargetTag.NO_BLOCKING_TILE:
        # if tile isnt blocking movement
        if _is_tile_in_bounds(tile):
            return not _is_tile_blocking_movement(tile)

    # If we've hit here it must be false!
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


def _is_tile_blocking_sight(tile: Tile) -> bool:
    """
    Check if a tile is blocking sight
    """
    # Does the tile block sight?
    return tile.blocks_sight


def _is_tile_visible_to_player(tile: Tile) -> bool:
    """
    Check if the specified tile is visible to the player
    """
    return tile.is_visible


def _is_tile_in_bounds(tile: Tile) -> bool:
    """
    Check if specified tile is in the map.
    """
    gamemap = get_gamemap()

    if (0 <= tile.x < gamemap.width) and (0 <= tile.y < gamemap.height):
        return True
    else:
        return False


def _is_tile_blocking_movement(tile: Tile) -> bool:
    """
    Check if the specified tile is blocking movement
    """
    return tile.blocks_movement


def _tile_has_any_entity(tile: Tile) -> bool:
    """
    Check if the specified tile  has an entity on it
    """
    return len(get_entities_on_tile(tile)) > 0


def get_entities_on_tile(tile: Tile) -> List[EntityID]:
    """
    Return a list of all the entities in that tile
    """
    x = tile.x
    y = tile.y
    entities = []
    for entity, (position,) in get_components([Position]):
        position = cast(Position, position)
        if (x, y) in position:
            entities.append(entity)
    return entities


def _tile_has_other_entities(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile has other entities apart from the provided active entity
    """
    entities_on_tile = get_entities_on_tile(tile)
    active_entity_is_on_tile = active_entity in entities_on_tile
    return (len(entities_on_tile) > 0 and not active_entity_is_on_tile) or \
           (len(entities_on_tile) > 1 and active_entity_is_on_tile)


def _tile_has_specific_entity(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile  has the specified entity on it
    """
    return active_entity in get_entities_on_tile(tile)


def _tile_has_entity_blocking_movement(tile: Tile) -> bool:
    x = tile.x
    y = tile.y
    # Any entities that block movement?
    for entity, (position, blocking) in get_components([Position, Blocking]):
        position = cast(Position, position)
        blocking = cast(Blocking, blocking)
        if (x, y) in position and blocking.blocks_movement:
            return True
    return False


def _tile_has_entity_blocking_sight(tile: Tile) -> bool:
    x = tile.x
    y = tile.y
    # Any entities that block sight?
    for entity, (position, blocking) in get_components([Position, Blocking]):
        position = cast(Position, position)
        blocking = cast(Blocking, blocking)
        if (x, y) in position and blocking.blocks_sight:
            return True
    return False


def is_tile_in_fov(tile_pos: Tuple[int, int], fov_map) -> bool:
    """
    Check if  target tile is in player`s FOV
    """
    x, y = tile_pos
    return fov_map[x][y]


def _can_afford_cost(entity: EntityID, resource: ResourceType, cost: int) -> bool:
    """
    Check if entity can afford the resource cost
    """
    resources = get_entitys_component(entity, Resources)
    name = get_name(entity)

    # Check if cost can be paid
    value = getattr(resources, resource.lower())
    if value - cost >= 0:
        logging.debug(f"'{name}' can afford cost.")
        return True
    else:
        logging.info(f"'{name}' cannot afford cost.")
        return False


def can_use_skill(entity: EntityID, skill_name: str) -> bool:
    """
    Check if entity can use skill. Checks cooldown and resource affordability.
    """
    player = get_player()
    skill = get_known_skill(entity, skill_name)

    # if we dont have skill we cant do anything
    if not skill:
        return False

    # flags
    can_afford = not_on_cooldown = False

    can_afford = _can_afford_cost(entity, skill.resource_type, skill.resource_cost)

    knowledge = get_entitys_component(entity, Knowledge)
    if knowledge:
        cooldown: int = knowledge.cooldowns[skill_name]
        if cooldown <= 0:
            not_on_cooldown = True
    else:
        not_on_cooldown = False
        cooldown = INFINITE

    if can_afford and not_on_cooldown:
        return True

    # log/inform lack of affordability
    if not can_afford:
        # is it the player that can't afford it?
        if entity == player:
            ui.log_message("I cannot afford to do that.")
        else:
            logging.warning(f"'{get_name(entity)}' tried to use {skill_name}, which they can`t afford.")

    # log/inform on cooldown
    if not not_on_cooldown:
        # is it the player that's can't afford it?
        if entity == player:
            ui.log_message("I'm not ready to do that, yet.")
        else:
            if cooldown == INFINITE:
                cooldown_msg = "unknown"
            else:
                cooldown_msg = str(cooldown)
            logging.warning(f"'{get_name(entity)}' tried to use {skill_name}, but needs to wait "
                            f"{cooldown_msg} more rounds.")

    # we've reached the end, no good.
    return False


################################ CONDITIONAL ACTIONS - CHANGE STATE - RETURN SUCCESS STATE  #############

def recompute_fov(entity: EntityID) -> bool:
    """
    Recalculate an entity's FOV
    """
    if entity_has_component(entity, FOV) and entity_has_component(entity, Position):
        # get sight range
        if entity_has_component(entity, HasCombatStats):
            stats = create_combat_stats(entity)
            sight_range = stats.sight_range
        else:
            sight_range = 0

        # get the needed components
        fov = get_entitys_component(entity, FOV)
        pos = get_entitys_component(entity, Position)

        # compute the fov
        if fov and pos:
            transparency = create_fov_map()
            maps = []
            for coordinate in pos.coordinates:
                fov_map = tcod.map.compute_fov(transparency, coordinate, sight_range, fov.light_walls, fov.algorithm)
                maps.append(fov_map)

            fov.map = maps[0]
            for m in maps:
                fov.map |= m
            # update tiles if it is player
            if entity == get_player():
                update_tile_visibility(fov.map)

        return True
    return False


def pay_resource_cost(entity: EntityID, resource: ResourceType, cost: int) -> bool:
    """
    Remove the resource cost from the using entity
    """
    resources = get_entitys_component(entity, Resources)
    name = get_name(entity)

    if resources:
        resource_value = getattr(resources, resource.lower())

        if resource_value != INFINITE:
            resource_left = resource_value - cost
            setattr(resources, resource.lower(), resource_left)

            logging.info(f"'{name}' paid {cost} {resource} and has {resource_left} left.")
            return True
        else:
            logging.info(f"'{name}' paid nothing as they have infinite {resource}.")
    else:
        logging.warning(f"'{name}' tried to pay {cost} {resource} but Resources component not found.")

    return False


def use_skill(user: EntityID, skill: Type[Skill], target_tile: Tile, direction: DirectionType) -> bool:
    """
    Use the specified skill on the target tile, usually creating a projectile. Returns True is successful if
    criteria to use skill was met, False if not.
    """
    # N.B. we init so that any overrides of the Skill.init are applied
    skill_cast = skill(user, target_tile, direction)

    # ensure they are the right target type
    if tile_has_tags(skill_cast.target_tile, skill_cast.required_tags, user):
        skill_cast.use()
        return True
    else:
        logging.info(f"Could not use skill, target tile does not have required tags ({skill.required_tags}).")

    return False


def apply_skill(skill_instance: Skill) -> bool:
    """
     Resolve the skill's effects. Returns True is successful if criteria to apply skill was met, False if not.
    """
    skill = skill_instance
    # ensure they are the right target type
    if tile_has_tags(skill.target_tile, skill.required_tags, skill.user):
        for entity, effects in skill_instance.apply():
            if entity not in skill.ignore_entities:
                effect_queue = list(effects)
                while effect_queue:
                    effect = effect_queue.pop()
                    effect_queue.extend(effect.evaluate())
        return True
    else:
        logging.info(
            f"Could not apply skill \"{skill.key}\", target tile does not have required tags ({skill.required_tags}).")

    return False


def set_skill_on_cooldown(skill_instance: Skill) -> bool:
    """
    Sets a skill on cooldown
    """
    user = skill_instance.user
    name = skill_instance.key
    knowledge = get_entitys_component(user, Knowledge)
    if knowledge:
        knowledge.set_skill_cooldown(name, skill_instance.base_cooldown)
        return True
    return False


def apply_affliction(affliction_instance: Affliction) -> bool:
    """
    Apply the affliction's effects. Returns True is successful if criteria to trigger the affliction was met,
    False if not.
    """
    affliction = affliction_instance
    target = affliction_instance.affected_entity
    position = get_entitys_component(target, Position)
    if position:
        target_tile = get_tile((position.x, position.y))

        # ensure they are the right target type
        if tile_has_tags(target_tile, affliction.required_tags, affliction.creator):
            for entity, effects in affliction.apply():
                effect_queue = list(effects)
                while effect_queue:
                    effect = effect_queue.pop()
                    effect_queue.extend(effect.evaluate())
            return True
        else:
            logging.info(f"Could not apply affliction \"{affliction.key}\", target tile does not have required "
                         f"tags ({affliction.required_tags}).")

    return False


def take_turn(entity: EntityID) -> bool:
    """
    Process the entity's Behaviour component. If no component found then EndTurn event is fired.
    """
    logging.debug(f"'{get_name(entity)}' is beginning their turn.")
    behaviour = get_entitys_component(entity, Behaviour)
    if behaviour:
        behaviour.behaviour.act()
        return True
    else:
        logging.critical(f"'{get_name(entity)}' has no behaviour to use.")

    return False


def apply_damage(entity: EntityID, damage: int) -> bool:
    """
    Remove damage from entity's health. Return remaining health.
    """
    resource = get_entitys_component(entity, Resources)
    if resource:
        resource.health -= damage
        return True
    else:
        logging.warning(f"'{get_name(entity)}' has no resource so couldnt apply damage.")

    return False


def spend_time(entity: EntityID, time_spent: int) -> bool:
    """
    Add time_spent to the entity's total time spent.
    """
    tracked = get_entitys_component(entity, Tracked)
    if tracked:
        tracked.time_spent += time_spent
        return True
    else:
        logging.warning(f"'{get_name(entity)}' has no tracked to spend time.")

    return False


################################ DEFINITE ACTIONS - CHANGE STATE - RETURN NOTHING  #############

def kill_entity(entity: EntityID):
    # if not player
    if entity != get_player():
        # delete from world
        delete(entity)

        turn_queue = chronicle.get_turn_queue()

        # if turn holder create new queue without them
        if entity == chronicle.get_turn_holder():

            # ensure the game state reflects the new queue
            chronicle.next_turn(entity)

        elif entity in turn_queue:
            # remove from turn queue
            turn_queue.pop(entity)

    else:
        # placeholder for player death
        ui.log_message("I should have died just then.")


def delete(entity: EntityID):
    """
    Queues entity for removal from the world_objects. Happens at the next run of process.
    """
    if entity:
        if snecs.exists(entity, snecs.world.default_world):
            snecs.schedule_for_deletion(entity)
            name = get_name(entity)
            logging.info(f"'{name}' ({entity}) added to stack to be deleted on next frame.")
        else:
            logging.warning(f"Tried to delete entity {entity} but they don't exist!")
    else:
        logging.error("Tried to delete an entity but entity was None.")


def add_component(entity: EntityID, component: Component):
    """
    Add a component to the entity
    """
    snecs.add_component(entity, component)


def update_tile_visibility(fov_map: np.array):
    """
    Update the the visibility of the tiles on the came map
    """
    gamemap = get_gamemap()
    width = gamemap.width
    height = gamemap.height

    for x in range(0, width):
        for y in range(0, height):
            gamemap.tiles[x][y].is_visible = bool(fov_map[x][y])  # cast to bool as otherwise is _bool from numpy


def judge_action(entity: EntityID, action_name: str):
    """
    Have all entities alter opinions of the entity based on the skill used, if they have an attitude towards
    the tags in that skill.
    """
    for god, (is_god, opinion, identity) in get_components([IsGod, Opinion, Identity]):
        # cast for typing
        opinion = cast(Opinion, opinion)
        identity = cast(Identity, identity)

        attitudes = library.GODS[identity.name].attitudes

        # check if the god has an attitude towards the action and apply the opinion change,
        # adding the entity to the dict if necessary
        if action_name in attitudes.keys():
            if entity in opinion.opinions:
                opinion.opinions[entity] = opinion.opinions[entity] + attitudes[action_name].opinion_change
            else:
                opinion.opinions[entity] = attitudes[action_name].opinion_change

            name = get_name(entity)
            logging.info(f"'{identity.name}' reacted to '{name}' using {action_name}.  New "
                         f"opinion = {opinion.opinions[entity]}")


def remove_affliction(entity: EntityID, affliction: Affliction):
    """
    Remove affliction from active list and undo any stat modification.
    """
    afflictions = get_entitys_component(entity, Afflictions)
    if afflictions:
        afflictions.remove(affliction)


def learn_skill(entity: EntityID, skill_name: str):
    """
    Add the skill name to the entity's knowledge component.
    """
    if not entity_has_component(entity, Knowledge):
        add_component(entity, Knowledge([]))
    knowledge = get_entitys_component(entity, Knowledge)
    if knowledge:
        skill_class = action.skill_registry[skill_name]
        knowledge.learn_skill(skill_class)


############################## ASSESS - REVIEW STATE - RETURN OUTCOME ########################################

def calculate_damage(base_damage: int, damage_mod_amount: int, resist_value: int, hit_type: HitTypeType) -> int:
    """
    Work out the damage to be dealt.
    """
    logging.debug(f"Calculate damage...")

    # mitigate damage with defence
    mitigated_damage = (base_damage + damage_mod_amount) - resist_value

    # get modifiers
    hit_types_data = library.GAME_CONFIG.hit_types

    # apply to hit modifier to damage
    if hit_type == HitType.CRIT:
        modified_damage = mitigated_damage * hit_types_data.crit.modifier
    elif hit_type == HitType.HIT:
        modified_damage = mitigated_damage * hit_types_data.hit.modifier
    else:
        modified_damage = mitigated_damage * hit_types_data.graze.modifier

    # round down the dmg
    int_modified_damage = int(modified_damage)

    # log the info
    log_string = f"-> Initial:{base_damage}, Mitigated: {format(mitigated_damage, '.2f')},  Modified" \
                 f":{format(modified_damage, '.2f')}, Final: {int_modified_damage}"
    logging.debug(log_string)

    return int_modified_damage


def calculate_to_hit_score(attacker_accuracy: int, skill_accuracy: int, stat_to_target_value: int) -> int:
    """
    Get the to hit score based on the stats of both entities and a random roll.
    """
    logging.debug(f"Get to hit scores...")

    # roll for the random value to add to the to_hit score.
    roll = random.randint(-3, 3)

    modified_to_hit_score = attacker_accuracy + skill_accuracy + roll

    mitigated_to_hit_score = modified_to_hit_score - stat_to_target_value

    # log the info
    log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
    logging.debug(log_string)

    return mitigated_to_hit_score


def choose_interventions(entity: EntityID, action_name: str) -> List[Tuple[EntityID, str]]:
    """
    Have all entities consider intervening. Action can be str if matching name, e.g. affliction name,
    or class attribute, e.g. Hit Type name. Returns a list of tuples containing (god_entity_id, intervention name).
    """
    chosen_interventions = []
    desire_to_intervene = 10
    desire_to_do_nothing = 75  # weighting for doing nothing

    for entity, (is_god, opinion, identity, knowledge) in get_components([IsGod, Opinion, Identity, Knowledge]):
        # cast for typing
        opinion = cast(Opinion, opinion)
        identity = cast(Identity, identity)
        knowledge = cast(Knowledge, knowledge)

        attitudes = library.GODS[identity.name].attitudes

        # check if the god has an attitude towards the action and increase likelihood of intervening
        if action_name in attitudes:
            desire_to_intervene = 30

        # get eligible interventions and their weightings. Need separate lists for random.choices
        eligible_interventions = []
        intervention_weightings = []
        for intervention_name in knowledge.skill_names:
            intervention_data = library.GODS[identity.name].interventions[intervention_name]

            # is the god willing to intervene i.e. does the opinion score meet the required opinion
            try:
                opinion_score = opinion.opinions[entity]
            except KeyError:
                opinion_score = 0

            required_opinion = intervention_data.required_opinion
            # check if greater or lower, depending on whether required opinion is positive or negative
            if 0 <= required_opinion < opinion_score:
                amount_exceeding_requirement = opinion_score - required_opinion

                eligible_interventions.append(intervention_name)
                intervention_weightings.append(amount_exceeding_requirement)

            elif 0 > required_opinion > opinion_score:
                amount_exceeding_requirement = required_opinion - opinion_score  # N.B. opposite to above
                eligible_interventions.append(intervention_name)
                intervention_weightings.append(amount_exceeding_requirement)

        # add chance to do nothing
        eligible_interventions.append("Nothing")
        intervention_weightings.append(desire_to_do_nothing - desire_to_intervene)

        # which intervention, if any, shall the god consider using?
        chosen_intervention, = random.choices(eligible_interventions, intervention_weightings)
        # N.B. use , to unpack the result

        # if god has chosen to take an action then add to list
        if chosen_intervention != "Nothing":
            chosen_interventions.append((entity, chosen_intervention))

    return chosen_interventions
