from __future__ import annotations

import dataclasses
import logging
import random
import pygame
import snecs
import tcod.map
from typing import TYPE_CHECKING, Optional, Tuple, Type, List, TypeVar, Any, cast
from snecs import Component, Query, new_entity
from snecs.typedefs import EntityID
from scripts.engine import utility, debug, chronicle
from scripts.engine.component import Position, Blocking, Resources, Knowledge, IsPlayer, Identity, People, Savvy, \
    Homeland, FOV, Aesthetic, IsGod, Opinion, IsActor, HasCombatStats, Tracked, Afflictions, Behaviour, \
    IsProjectile
from scripts.engine.core.constants import DEFAULT_SIGHT_RANGE, EffectType, MessageType, ShapeType, TargetTag, FOVInfo, \
    TargetTagType, DirectionType, Direction, ResourceType, INFINITE, TravelMethodType, TravelMethod, HitTypeType, \
    HitValue, HitType, HitModifier, TILE_SIZE, ICON_SIZE, ENTITY_BLOCKS_SIGHT
from scripts.engine.core.definitions import CharacteristicSpritesData, ProjectileData, CharacteristicSpritePathsData
from scripts.engine.core.store import store
from scripts.engine.library import library
from scripts.engine.thought import SkipTurn, ProjectileBehaviour
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.combat_stats import CombatStats
from scripts.engine.world_objects.gamemap import GameMap
from scripts.engine.world_objects.tile import Tile
from scripts.nqp.actions import skills
from scripts.nqp.actions.skills import Skill, BasicAttack, Move

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List

_C = TypeVar("_C", bound=Component)  # to represent components where we don't know which is being used
get_entitys_components = snecs.all_components
get_components = Query
entity_has_component = snecs.has_component


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
    data = library.get_god_data(god_name)
    god: List[Component] = []

    # get aesthetic info
    idle = utility.get_image(data.sprite_paths.idle, (TILE_SIZE, TILE_SIZE))
    icon = utility.get_image(data.sprite_paths.icon, (ICON_SIZE, ICON_SIZE))
    sprites = CharacteristicSpritesData(icon=icon, idle=idle)

    god.append(Identity(data.name, data.description))
    god.append(Aesthetic(sprites.idle, sprites, 0, 0))
    god.append(IsGod())
    god.append(Opinion())
    god.append((Resources(INFINITE, INFINITE)))
    entity = create_entity(god)

    # TODO - readd interventions

    logging.debug(f"{data.name} created.")

    return entity


def create_actor(name: str, description: str, x: int, y: int, people_name: str, homeland_name: str,
        savvy_name: str, is_player: bool = False) -> EntityID:
    """
    Create an entity with all of the components to be an actor. is_player is Optional and defaults to false.
    Returns entity ID.
    """
    # TODO - rename create player. add new method for create actor that uses actor/npc characteristic

    people_data = library.get_people_data(people_name)
    homeland_data = library.get_homeland_data(homeland_name)
    savvy_data = library.get_savvy_data(savvy_name)

    actor: List[Component] = []

    # actor components
    actor.append(IsActor())
    actor.append(Identity(name, description))
    actor.append(Position(x, y))  # TODO - check position not blocked before spawning
    actor.append(HasCombatStats())
    actor.append(Blocking(True, ENTITY_BLOCKS_SIGHT))
    actor.append(People(people_name))
    actor.append(Homeland(homeland_name))
    actor.append(Savvy(savvy_name))
    actor.append(FOV(create_fov_map()))
    actor.append(Tracked(chronicle.get_time()))

    # add aesthetic
    characteristics_paths = [homeland_data.sprite_paths, people_data.sprite_paths, savvy_data.sprite_paths]
    sprites = _create_characteristic_sprites(characteristics_paths)
    screen_x, screen_y = ui.world_to_screen_position((x, y))
    actor.append(Aesthetic(sprites.idle, sprites, screen_x, screen_y))

    # create the entity
    entity = create_entity(actor)

    # setup basic attack as a known skill and an interaction  # N.B. must be after entity creation
    basic_attack_name = "basic_attack"
    # TODO - rebuild interactions
    # use_skill_effect = UseSkillEffectData(skill_name=basic_attack_name, creators_name=name)
    # add_component(entity, Interactions({InteractionCause.ENTITY_COLLISION: [use_skill_effect]}))
    # N.B. All actors start with basic attack and move
    basic_attack = {
        "skill": BasicAttack,
        "cooldown": 0
    }
    move = {
        "skill": Move,
        "cooldown": 0
    }
    known_skills = {
        basic_attack_name: basic_attack,
        "move": move
    }
    skill_order = [basic_attack_name]  # move not added to skill order
    afflictions = Afflictions()

    # get skills and perm afflictions from characteristics
    characteristics = {
        1: people_data,
        2: homeland_data,
        3: savvy_data
    }
    for characteristic in characteristics.values():
        if characteristic.known_skills != ["none"]:
            for skill_name in characteristic.known_skills:
                skill = getattr(skills, skill_name)
                known_skills[skill_name] = skill
                skill_order.append(skill_name)
        if characteristic.permanent_afflictions != ["none"]:
            for affliction in characteristic.permanent_afflictions:
                afflictions[affliction] = INFINITE

    # add skills to entity
    add_component(entity, Knowledge(known_skills, skill_order))
    add_component(entity, afflictions)

    # give full resources N.B. Can only be added once entity is created
    stats = create_combat_stats(entity)
    add_component(entity, Resources(stats.max_health, stats.max_stamina))

    # player components
    if is_player:
        add_component(entity, IsPlayer())
    # TODO - alter in line with change to separating player and actor
    else:
        add_component(entity, Behaviour(SkipTurn(entity)))

    logging.debug(f"{name} created.")

    return entity


def create_projectile(creating_entity: EntityID, x: int, y: int, data: ProjectileData) -> EntityID:
    """
    Create an entity with all of the components to be a projectile. Returns entity ID.
    """
    skill_name = data.skill_name
    projectile: List[Component] = []

    name = get_name(creating_entity)
    projectile_name = f"{skill_name}s projectile"
    desc = f"{name}s {skill_name} projectile"
    projectile.append(Identity(projectile_name, desc))

    sprites = CharacteristicSpritesData(move=utility.get_image(data.sprite), idle=utility.get_image(data.sprite))
    screen_x, screen_y = ui.world_to_screen_position((x, y))
    projectile.append(Aesthetic(sprites.move, sprites, screen_x, screen_y))
    projectile.append(IsProjectile(creating_entity))
    projectile.append(Tracked(chronicle.get_time()))
    projectile.append(Position(x, y))  # TODO - check position not blocked before spawning
    entity = create_entity(projectile)


    # TODO - rebuild interactions
    # activate_skill = ActivateSkillEffectData(skill_name=skill_name, required_tags=data.required_tags,
    #                                          creator=name)
    # kill_entity = KillEntityEffectData(target_entity=entity)
    # add_component(entity, Interactions({InteractionCause.ENTITY_COLLISION: [activate_skill, kill_entity]}))

    add_component(entity, Behaviour(ProjectileBehaviour(entity, data)))

    logging.debug(f"{name}`s projectile created.")

    return entity


def _create_characteristic_sprites(sprite_paths: List[CharacteristicSpritePathsData]) -> CharacteristicSpritesData:
    """
    Build a CharacteristicSpritesData class from a list of sprite paths
    """
    paths: Dict[str, List[str]] = {}
    sprites: Dict[str, List[pygame.Surface]] = {}
    flattened_sprites: Dict[str, pygame.Surface] = {}

    # bundle into cross-characteristic sprite path lists
    for characteristic in sprite_paths:
        char_dict = dataclasses.asdict(characteristic)
        for name, path in char_dict.items():
            # check if key exists
            if name in paths:
                paths[name].append(path)
            # if not init the dict
            else:
                paths[name] = [path]

    # convert to sprites
    for name, path_list in paths.items():
        # get the size to convert to
        if name == "icon":
            size = (ICON_SIZE, ICON_SIZE)
        else:
            size = (TILE_SIZE, TILE_SIZE)

        sprites[name] = utility.get_images(path_list, size)

    # flatten the images
    for name, surface_list in sprites.items():
        flattened_sprites[name] = utility.flatten_images(surface_list)

    # convert to dataclass
    converted = CharacteristicSpritesData(**flattened_sprites)
    return converted


def create_gamemap(width, height):
    """
    Create new GameMap
    """
    store.current_gamemap = GameMap(width, height)


def create_fov_map() -> tcod.map.Map:
    """
    Create an fov map
    """
    gamemap = get_gamemap()
    width = gamemap.width
    height = gamemap.height

    fov_map = tcod.map_new(width, height)

    for x in range(width):
        for y in range(height):
            tile = get_tile((x, y))
            if tile:
                tcod.map_set_properties(fov_map, x, y, not tile.blocks_sight, not tile.blocks_movement)

    return fov_map


def create_combat_stats(entity: EntityID) -> CombatStats:
    """
    Create and return a stat object  for an entity.
    """
    return CombatStats(entity)


############################# GET - RETURN AN EXISTING SOMETHING ###########################

def get_gamemap() -> GameMap:
    """
    Get current gamemap
    """
    return store.current_gamemap


def get_tile(tile_pos: Tuple[int, int]) -> Tile:
    """
    Get the tile at the specified location. Use tile_x and tile_y. Raises exception if out of bounds or doesnt exist.
    """
    # TODO - clean up to only accept tuple
    gamemap = get_gamemap()
    x = tile_pos[0]
    y = tile_pos[1]

    try:
        _tile = gamemap.tiles[x][y]
        if _is_tile_in_bounds(_tile):
            return _tile

    except KeyError:
        logging.warning(f"Tried to get tile({x},{y}), which is out of bounds.")


def get_tiles(start_x: int, start_y: int, coords: List[Tuple[int, int]]) -> List[Tile]:
    """
    Get multiple tiles based on starting position and coordinates given. Coords are relative  to start
    position given.
    """
    gamemap = get_gamemap()
    tiles = []

    for coord in coords:
        tile_x = coord[0] + start_x
        tile_y = coord[1] + start_y

        # make sure it is in bounds
        tile = get_tile((tile_x, tile_y))
        if tile:
            if _is_tile_in_bounds(tile):
                tiles.append(gamemap.tiles[tile_x][tile_y])

    return tiles


def get_direction(start_pos: Union[Tuple[int, int], str], target_pos: Union[Tuple[int, int], str]) -> DirectionType:
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
        return Direction.CENTRE

    # handle any mistaken values coming in
    dir_x = utility.clamp(dir_x, -1, 1)
    dir_y = utility.clamp(dir_y, -1, 1)

    return dir_x, dir_y


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
    # gamemap = _manager.gamemap
    # entities = []
    # # TODO - update to use ECS
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


def get_reflected_direction(current_position: Tuple[int, int], target_direction: Tuple[int, int]) -> Tuple[int, int]:
    """
    Use surrounding walls to understand how the object should be reflected.
    """
    current_x, current_y = current_position
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

    return dir_x, dir_y


def _get_furthest_free_position(start_position: Tuple[int, int], target_direction: Tuple[int, int],
        max_distance: int, travel_type: TravelMethodType) -> Tuple[int, int]:
    """
    Checks each position in a line and returns the last position that doesnt block movement. If no position in
    range blocks movement then the last position checked is returned. If all positions in range block movement
    then starting position is returned.
    """
    start_x = start_position[0]
    start_y = start_position[1]
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
    if to_hit_score >= HitValue.CRIT:
        return HitType.CRIT
    elif to_hit_score >= HitValue.HIT:
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


def get_entity(unique_component: Type[Component]) -> Optional[EntityID]:
    """
    Get a single entity that has a component. If multiple entities have the given component only the
    first found is returned.
    """
    entities = []
    for entity, (flag,) in get_components([unique_component]):
        entities.append(entity)

    num_entities = len(entities)

    if num_entities > 1:
        logging.warning(f"Tried to get an entity with {unique_component} component but found {len(entities)} "
                        f"entities with that component.")
    elif num_entities == 0:
        logging.warning(f"Tried to get an entity with {unique_component} component but found none.")
        return None

    return entities[0]


def get_entitys_component(entity: EntityID, component: Type[_C]) -> _C:
    """
    Get an entity's component. Log if component not found.
    """
    if entity_has_component(entity, component):
        return snecs.entity_component(entity, component)
    else:
        debug.log_component_not_found(entity, component)
        raise Exception


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


def get_primary_stat(entity: EntityID, primary_stat: str) -> int:
    """
    Get an entity's primary stat.
    """
    stat = primary_stat
    value = 0

    people = get_entitys_component(entity, People)
    if people:
        people_data = library.get_people_data(people.name)
        value += getattr(people_data, stat)

    savvy = get_entitys_component(entity, Savvy)
    if savvy:
        savvy_data = library.get_savvy_data(savvy.name)
        value += getattr(savvy_data, stat)

    homeland = get_entitys_component(entity, Homeland)
    if homeland:
        homeland_data = library.get_homeland_data(homeland.name)
        value += getattr(homeland_data, stat)

    afflictions = get_entitys_component(entity, Afflictions)
    for modifier in afflictions.stat_modifiers.values():
        if modifier[0] == stat:
            value += modifier[1]

    # ensure no dodgy numbers, like floats or negative
    value = max(1, int(value))

    return value


def get_player_fov() -> tcod.map.Map:
    """
    Get's the player's FOV component
    """
    player = get_player()
    if player:
        fov_c = get_entitys_component(player, FOV)
        if fov_c:
            return fov_c.map

    raise Exception


def get_known_skill(entity: EntityID, skill_name: str) -> Type[Skill]:
    """
    Get an entity's known skill from their Knowledge component.
    """
    knowledge = get_entitys_component(entity, Knowledge)
    if knowledge:
        try:
            return knowledge.skills[skill_name]["skill"]
        except KeyError:
            logging.warning(f"'{get_name(entity)}' tried to use a skill they dont know.")


def get_affected_entities(target_pos: Tuple[int, int], shape: ShapeType, shape_size: int):
    """
    Return a list of entities that are within the shape given, using target position as a centre point. Entity must
    have Position, Resources and Combat Stats to be eligible.
    """
    affected_entities = []
    affected_positions = []
    target_x = target_pos[0]
    target_y = target_pos[1]

    # get affected tiles
    coords = utility.get_coords_from_shape(shape, shape_size)
    for coord in coords:
        affected_positions.append((coord[0] + target_x, coord[1] + target_y))

    # get relevant entities in target area
    for entity, (position, *others) in get_components([Position, Resources, HasCombatStats]):
        if (position.x, position.y) in affected_positions:
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
            return _tile_has_specific_entity(tile, active_entity)
        else:
            logging.warning("Tried to get TargetTag.SELF but gave no active_entity.")
    elif tag == TargetTag.OTHER_ENTITY:
        # if entity on tile is not active entity
        if active_entity:
            # checks isnt self
            return not _tile_has_specific_entity(tile, active_entity)
        else:
            logging.warning("Tried to get TargetTag.OTHER_ENTITY but gave no active_entity.")
    elif tag == TargetTag.NO_ENTITY:
        # if the tile has no entity
        return _tile_has_any_entity(tile)
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
    x = tile.x
    y = tile.y
    # Any entities on the tile?
    for entity, (position,) in get_components([Position]):
        position = cast(Position, position)
        if position.x == x and position.y == y:
            return True

    # We found no entities on the tile
    return False


def _tile_has_specific_entity(tile: Tile, active_entity: int) -> bool:
    """
    Check if the specified tile  has the specified entity on it
    """
    x = tile.x
    y = tile.y
    # ensure active entity is the same as the returned one
    for entity, (position,) in get_components([Position]):
        position = cast(Position, position)
        if position.x == x and position.y == y:
            if active_entity == entity:
                return True

    # no matching entity found
    return False


def _tile_has_entity_blocking_movement(tile: Tile) -> bool:
    x = tile.x
    y = tile.y
    # Any entities that block movement?
    for entity, (position, blocking) in get_components([Position, Blocking]):
        position = cast(Position, position)
        blocking = cast(Blocking, blocking)
        if position.x == x and position.y == y and blocking.blocks_movement:
            return True
    return False


def _tile_has_entity_blocking_sight(tile: Tile) -> bool:
    x = tile.x
    y = tile.y
    # Any entities that block sight?
    for entity, (position, blocking) in get_components([Position, Blocking]):
        position = cast(Position, position)
        blocking = cast(Blocking, blocking)
        if position.x == x and position.y == y and blocking.blocks_sight:
            return True
    return False


def is_tile_in_fov(x: int, y: int, fov_map) -> bool:
    """
    Check if  target tile is in player`s FOV
    """
    return tcod.map_is_in_fov(fov_map, x, y)


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
        logging.warning(f"'{get_name(entity)}' tried to use {skill_name} but doesnt know it.")
        return False

    # flags
    can_afford = not_on_cooldown = False

    can_afford = _can_afford_cost(entity, skill.resource_type, skill.resource_cost)

    knowledge = get_entitys_component(entity, Knowledge)
    cooldown = knowledge.skills[skill_name]["cooldown"]
    if cooldown <= 0:
        not_on_cooldown = True

    if can_afford and not_on_cooldown:
        return True

    # log/inform lack of affordability
    if not can_afford:
        # is it the player that can't afford it?
        if entity == player:
            ui.log_message(MessageType.LOG, "I cannot afford to do that.")
        else:
            logging.warning(f"'{get_name(entity)}' tried to use {skill_name}, which they can`t afford.")

    # log/inform on cooldown
    if not not_on_cooldown:
        # is it the player that's can't afford it?
        if entity == player:
            ui.log_message(MessageType.LOG, "I'm not ready to do that, yet.")
        else:
            logging.warning(f"'{get_name(entity)}' tried to use {skill_name}, but needs to wait {cooldown} more "
                            f"rounds.")


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
            sight_range = DEFAULT_SIGHT_RANGE

        # get the needed components
        fov = get_entitys_component(entity, FOV)
        pos = get_entitys_component(entity, Position)

        # compute the fov
        tcod.map_compute_fov(fov.map, pos.x, pos.y, sight_range, FOVInfo.LIGHT_WALLS, FOVInfo.FOV_ALGORITHM)

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


def use_skill(user: EntityID, skill: Type[Skill], target_tile: Tile, direction: Optional[DirectionType] = None)\
        -> bool:
    """
    Use the specified skill on the target tile, resolving all effects. Returns True is successful if criteria to use
    skill was met, False if not.
    """
    # ensure they are the right target type
    if tile_has_tags(target_tile, skill.required_tags, user):
        skill_cast = skill(user, target_tile, direction)
        for entity, effects in skill_cast.apply():
            effect_queue = list(effects)
            while effect_queue:
                effect = effect_queue.pop()
                effect_queue.extend(effect.evaluate())
        return True
    else:
        logging.debug(f"Target tile does not have tags required ({skill.required_tags}).")

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
    # TODO - modify by time modifier stat
    tracked = get_entitys_component(entity, Tracked)
    if tracked:
        tracked.time_spent += time_spent
        return True
    else:
        logging.warning(f"'{get_name(entity)}' has no tracked to spend time.")

    return False


def learn_skill(entity: EntityID, skill_name: str) -> bool:
    """
    Add the skill name to the entity's knowledge component.
    """
    if not entity_has_component(entity, Knowledge):
        add_component(entity, Knowledge())
    knowledge = get_entitys_component(entity, Knowledge)

    if knowledge:
        knowledge.skills[skill_name]["cooldown"] = library.get_skill_data(skill_name).cooldown
        knowledge.skill_order.append(skill_name)
        return True
    else:
        logging.warning(f"'{get_name(entity)}' has no knowledge to learn skill.")

    return False


################################ DEFINITE ACTIONS - CHANGE STATE - RETURN NOTHING  #############

def kill_entity(entity: EntityID):
    turn_queue = chronicle.get_turn_queue()

    # if  not player
    if entity != get_player():
        # if turn holder create new queue without them
        if entity == chronicle.get_turn_holder():
            chronicle.rebuild_turn_queue(entity)

            # ensure the game state reflects the new queue
            chronicle.next_turn()

        elif entity in turn_queue:
            # remove from turn queue
            turn_queue.pop(entity)

        # delete from world
        delete(entity)
    else:
        # TODO add player death
        # placeholder for player death
        ui.log_message(MessageType.LOG, "I should have died just then.")


def end_turn(entity: EntityID, time_spent: int):
    """
    Spend an entities time, progress time, move to next acting entity in queue.
    """
    if entity == chronicle.get_turn_holder():
        spend_time(entity, time_spent)
        chronicle.next_turn()
    else:
        name = get_name(entity)
        logging.warning(f"Tried to end {name}'s turn but they're not turn holder.")


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


def update_tile_visibility(fov_map: tcod.map.Map):
    """
    Update the the visibility of the tiles on the came map
    """
    gamemap = get_gamemap()

    for x in range(0, gamemap.width):
        for y in range(0, gamemap.height):
            gamemap.tiles[x][y].is_visible = tcod.map_is_in_fov(fov_map, x, y)


def judge_action(entity: EntityID, action_name: str):
    """
    Have all entities alter opinions of the entity based on the skill used, if they have an attitude towards
    the tags in that skill.
    """
    # TODO - assign tags to replace actions previously used
    # TODO - loop through tags on the skill and see if the god cares about the tags

    for god, (is_god, opinion, identity) in get_components([IsGod, Opinion, Identity]):
        # cast for typing
        opinion = cast(Opinion, opinion)
        identity = cast(Identity, identity)

        attitudes = library.get_god_attitudes_data(identity.name)

        # check if the god has an attitude towards the action and apply the opinion change,
        # adding the entity to the dict if necessary
        if action_name in attitudes:
            if entity in opinion.opinions:
                opinion.opinions[entity] = opinion.opinions[entity] + attitudes[action_name].opinion_change
            else:
                opinion.opinions[entity] = attitudes[action_name].opinion_change

            name = get_name(entity)
            logging.info(f"'{identity.name}' reacted to '{name}' using {action_name}.  New "
                         f"opinion = {opinion.opinions[entity]}")


def remove_affliction(entity: EntityID, affliction_name: str):
    """
    Remove affliction from active list and undo any stat modification.
    """
    afflictions = get_entitys_component(entity, Afflictions)

    if affliction_name in afflictions.active:
        # if it  is affect_stat remove the affect
        affliction = afflictions.active[affliction_name]
        if EffectType.AFFECT_STAT in affliction.identity_tags:
            afflictions.stat_modifiers.pop(affliction_name)

        # remove from active list
        afflictions.active.pop(affliction_name)

############################## ASSESS - REVIEW STATE - RETURN OUTCOME ########################################

def calculate_damage(base_damage: int, damage_mod_amount: int, resist_value: int, hit_type: HitTypeType) -> int:
    """
    Work out the damage to be dealt.
    """
    logging.debug(f"Calculate damage...")

    # mitigate damage with defence
    mitigated_damage = (base_damage + damage_mod_amount) - resist_value

    # apply to hit modifier to damage
    if hit_type == HitType.CRIT:
        modified_damage = mitigated_damage * HitModifier.CRIT
    elif hit_type == HitType.HIT:
        modified_damage = mitigated_damage * HitModifier.HIT
    else:
        modified_damage = mitigated_damage * HitModifier.GRAZE

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

    roll = random.randint(-3, 3)
    # TODO - move hit variance to somewhere more easily configurable
    # TODO - use tcod random (so as to use a seed)

    modified_to_hit_score = attacker_accuracy + skill_accuracy + roll

    mitigated_to_hit_score = modified_to_hit_score - stat_to_target_value

    # log the info
    log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
    logging.debug(log_string)

    return mitigated_to_hit_score


def choose_interventions(entity: EntityID, action: Any) -> List[Tuple[EntityID, str]]:
    """
    Have all entities consider intervening. Action can be str if matching name, e.g. affliction name,
    or class attribute, e.g. Hit Type name. Returns a list of tuples containing (god_entity_id, intervention name).
    """
    chosen_interventions = []
    desire_to_intervene = 10
    desire_to_do_nothing = 75  # weighting for doing nothing # TODO - move magic number to config

    for entity, (is_god, opinion, identity, knowledge) in get_components([IsGod, Opinion, Identity, Knowledge]):
        # cast for typing
        opinion = cast(Opinion, opinion)
        identity = cast(Identity, identity)
        knowledge = cast(Knowledge, knowledge)

        attitudes = library.get_god_attitudes_data(identity.name)
        action_name = action

        # check if the god has an attitude towards the action and increase likelihood of intervening
        if action_name in attitudes:
            desire_to_intervene = 30

        # get eligible interventions and their weightings. Need separate lists for random.choices
        eligible_interventions = []
        intervention_weightings = []
        for intervention_name in knowledge.skills.keys():
            intervention_data = library.get_god_intervention_data(identity.name, intervention_name)

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
