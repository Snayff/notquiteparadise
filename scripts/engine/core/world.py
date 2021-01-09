from __future__ import annotations

import logging
import random
from typing import Dict, List, Optional, Tuple, Type, TYPE_CHECKING, TypeVar

import numpy as np
import snecs
import tcod
from snecs import Component, new_entity, Query
from snecs.typedefs import EntityID

from scripts.engine.core import chronicle, query, utility
from scripts.engine.core.component import (
    Aesthetic,
    Afflictions,
    Exists,
    FOV,
    HasCombatStats,
    Identity,
    Immunities,
    IsActive,
    IsPlayer,
    Knowledge,
    Lifespan,
    LightSource,
    Opinion,
    Physicality,
    Position,
    Reaction,
    Resources,
    Thought,
    Tracked,
    Traits,
)
from scripts.engine.core.effect import (
    AffectCooldownEffect,
    AffectStatEffect,
    AlterTerrainEffect,
    ApplyAfflictionEffect,
    DamageEffect,
    Effect,
    MoveActorEffect,
)
from scripts.engine.core.utility import build_sprites_from_paths
from scripts.engine.internal import library
from scripts.engine.internal.constant import (
    Direction,
    DirectionType,
    EffectType,
    Height,
    HitType,
    HitTypeType,
    INFINITE,
    PrimaryStat,
    PrimaryStatType,
    RenderLayer,
    ResourceType,
    SecondaryStatType,
    ShapeType,
    TILE_SIZE,
    TileTag,
    TileTagType,
    TraitGroup,
    TravelMethod,
    TravelMethodType,
)
from scripts.engine.internal.data import store
from scripts.engine.internal.definition import (
    ActorData,
    AffectCooldownEffectData,
    AffectStatEffectData,
    AlterTerrainEffectData,
    ApplyAfflictionEffectData,
    DamageEffectData,
    DelayedSkillData,
    EffectData,
    GodData,
    MoveActorEffectData,
    ProjectileData,
    TerrainData,
)
from scripts.engine.internal.event import event_hub, MessageEvent
from scripts.engine.world_objects import lighting
from scripts.engine.world_objects.combat_stats import CombatStats
from scripts.engine.world_objects.game_map import GameMap
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List, Optional, Tuple

    from scripts.engine.internal.action import Affliction, Skill

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
    Use each component in a list of components to create an entity
    """
    if components is None:
        _components = []
    else:
        _components = components

    # add Exists, as all entities need it
    _components.append(Exists())

    # create the entity
    entity = new_entity(_components)

    return entity


def create_god(god_data: GodData) -> EntityID:
    """
    Create an entity with all of the components to be a god. god_name must be in the gods json file.
    """
    god: List[Component] = []

    god.append(Identity(god_data.name, god_data.description))
    god.append(Opinion(god_data.attitudes))
    god.append(Reaction(god_data.reactions))
    god.append((Resources(INFINITE, INFINITE)))
    entity = create_entity(god)

    logging.debug(f"God Entity, '{god_data.name}', created.")

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
    components.append(Position(*occupied_tiles))
    components.append(Identity(name, actor_data.description))
    components.append(HasCombatStats())
    components.append(Physicality(True, actor_data.height))
    components.append(Traits(actor_data.trait_names))
    components.append(FOV())
    components.append(Tracked(chronicle.get_time()))
    components.append(Immunities())

    # set up light
    radius = 2  # TODO - pull radius and colour from external data
    colour = (255, 255, 255)
    alpha = 200
    light_id = create_light(spawn_pos, radius, colour, alpha)
    components.append(LightSource(light_id, radius))

    # get info from traits
    traits_paths = []  # for aesthetic

    move = store.skill_registry["Move"]
    basic_attack = store.skill_registry["BasicAttack"]
    known_skills = [move, basic_attack]  # for knowledge
    skill_order = ["BasicAttack"]  # for knowledge
    perm_afflictions_names = []  # for affliction
    behaviour = None

    # loop each trait and get info for skills etc.
    for name in actor_data.trait_names:
        data = library.TRAITS[name]
        traits_paths.append(data.sprite_paths)
        if data.known_skills != ["none"]:

            for skill_name in data.known_skills:
                skill_class = store.skill_registry[skill_name]
                known_skills.append(skill_class)
                skill_order.append(skill_name)

        if data.permanent_afflictions != ["none"]:
            for _name in data.permanent_afflictions:
                perm_afflictions_names.append(_name)

        if data.group == TraitGroup.NPC:
            behaviour = store.behaviour_registry[actor_data.behaviour_name]

    # add aesthetic
    traits_paths.sort(key=lambda path: path.render_order, reverse=True)
    sprites = build_sprites_from_paths(traits_paths)

    # N.B. translation to screen coordinates is handled by the camera
    components.append(Aesthetic(sprites.idle, sprites, traits_paths, RenderLayer.ACTOR, (x, y)))

    # add skills to entity
    components.append(Knowledge(known_skills, skill_order))

    # create the entity
    entity = create_entity(components)

    # add permanent afflictions post creation,  since we can only add them once an entity is created
    perm_afflictions = []
    for name in perm_afflictions_names:
        # create the affliction with no specific source
        perm_afflictions.append(create_affliction(name, entity, entity, INFINITE))
    add_component(entity, Afflictions(perm_afflictions))

    # add behaviour  N.B. Can only be added once entity is created
    if behaviour:
        add_component(entity, Thought(behaviour(entity)))

    # give full resources N.B. Can only be added once entity is created
    stats = create_combat_stats(entity)
    add_component(entity, Resources(stats.max_health, stats.max_stamina))

    logging.debug(f"Actor Entity, '{name}', created.")

    return entity


def create_terrain(terrain_data: TerrainData, spawn_pos: Tuple[int, int], lifespan: int = INFINITE) -> EntityID:
    """
    Create terrain
    """
    components: List[Component] = []
    x, y = spawn_pos

    # get dimensions of actor
    occupied_tiles = []
    for offset in terrain_data.position_offsets:
        occupied_tiles.append((offset[0] + x, offset[1] + y))

    # terrain components
    components.append(Lifespan(lifespan))
    components.append(Position(*occupied_tiles))
    components.append(Identity(terrain_data.name, terrain_data.description))
    components.append(Physicality(terrain_data.blocks_movement, terrain_data.height))

    # add aesthetic N.B. translation to screen coordinates is handled by the camera
    sprites = build_sprites_from_paths([terrain_data.sprite_paths], (TILE_SIZE, TILE_SIZE))
    components.append(Aesthetic(sprites.idle, sprites, [terrain_data.sprite_paths], RenderLayer.TERRAIN, (x, y)))

    # add reactions
    components.append(Reaction(terrain_data.reactions))

    # add light
    if terrain_data.light:
        _light = terrain_data.light
        light_id = create_light(spawn_pos, _light.radius, _light.colour, _light.alpha)
        components.append(LightSource(light_id, _light.radius))

    # create the entity
    entity = create_entity(components)

    logging.debug(f"Terrain Entity, '{terrain_data.name}', created.")

    return entity


def create_projectile(creating_entity: EntityID, tile_pos: Tuple[int, int], data: ProjectileData) -> EntityID:
    """
    Create an entity with all of the components to be a projectile. Returns entity ID.
    """
    skill_name = data.skill_name
    projectile: List[Component] = []
    x, y = tile_pos

    name = get_name(creating_entity)
    projectile_name = f"{name}`s {skill_name}`s projectile"
    desc = f"{skill_name} on its way."
    projectile.append(Identity(projectile_name, desc))

    sprites = build_sprites_from_paths([data.sprite_paths], (TILE_SIZE, TILE_SIZE))

    projectile.append(Aesthetic(sprites.move, sprites, [data.sprite_paths], RenderLayer.ACTOR, (x, y)))
    projectile.append(Tracked(chronicle.get_time_of_last_turn()))  # allocate time to ensure they act next
    projectile.append(Position((x, y)))
    projectile.append(Resources(999, 999))  # TODO - remove need to have Resources
    projectile.append(Afflictions())  # TODO - remove need to have Afflictions
    projectile.append(IsActive())

    # set up light
    radius = 1  # TODO - pull radius and colour from external data
    colour = (68, 174, 235)
    alpha = 240
    light_id = create_light((x, y), radius, colour, alpha)
    projectile.append(LightSource(light_id, radius))

    entity = create_entity(projectile)

    # add post-creation components
    behaviour = store.behaviour_registry["Projectile"]
    thought = Thought(behaviour(entity))
    from scripts.engine.internal.action import Projectile
    assert isinstance(thought.behaviour, Projectile)
    thought.behaviour.data = data  # projectile is a  special case and requires the data set
    add_component(entity, thought)

    move = store.skill_registry["Move"]
    known_skills = [move]
    add_component(entity, Knowledge(known_skills))

    logging.debug(f"{projectile_name}`s created at ({x},{y}) heading {data.direction}.")

    return entity


def create_delayed_skill(creating_entity: EntityID, tile_pos: Tuple[int, int], data: DelayedSkillData) -> EntityID:
    """
    Create an entity with all of the components to be a delayed skill. Returns Entity ID.
    """
    skill_name = data.skill_name
    delayed_skill: List[Component] = []
    x, y = tile_pos

    name = get_name(creating_entity)
    delayed_skill_name = f"{name}`s {skill_name}`s delayed skill"
    desc = f"{skill_name} incoming."
    delayed_skill.append(Identity(delayed_skill_name, desc))

    sprites = build_sprites_from_paths([data.sprite_paths], (TILE_SIZE, TILE_SIZE))

    delayed_skill.append(Aesthetic(sprites.idle, sprites, [data.sprite_paths], RenderLayer.TERRAIN, (x, y)))
    delayed_skill.append(Tracked(chronicle.get_time_of_last_turn() - 1))  # allocate time to ensure they act next
    delayed_skill.append(Position((x, y)))
    delayed_skill.append(IsActive())

    entity = create_entity(delayed_skill)

    # add post-creation components
    behaviour = store.behaviour_registry["DelayedSkill"]
    thought = Thought(behaviour(entity))
    from scripts.engine.internal.action import DelayedSkill
    assert isinstance(thought.behaviour, DelayedSkill)
    thought.behaviour.data = data
    thought.behaviour.remaining_duration = data.duration
    add_component(entity, thought)

    logging.debug(f"{delayed_skill_name}`s created at ({x},{y}) and will trigger in {data.duration} " f"turns.")

    return entity


def create_affliction(name: str, creator: EntityID, target: EntityID, duration: int) -> Affliction:
    """
    Creates an instance of an Affliction provided the name
    """
    affliction = store.affliction_registry[name](creator, target, duration)
    return affliction


def create_combat_stats(entity: EntityID) -> CombatStats:
    """
    Create and return a stat object  for an entity.
    """
    stats = CombatStats(entity)
    return stats


def create_light(pos: Tuple[int, int], radius: int, colour: Tuple[int, int, int], alpha: int) -> str:
    """
    Create a Light and add it to the current GameMap's Lightbox. Pos is the world position - the light will handle
    scaling to screen.
    Returns the light_id of the Light.
    """
    light_img = utility.get_image("world/light_mask.png", ((radius * 2) * TILE_SIZE, (radius * 2) * TILE_SIZE))
    light_box = get_game_map().light_box
    light = lighting.Light([pos[0] * TILE_SIZE, pos[1] * TILE_SIZE], radius * TILE_SIZE, light_img)
    light.set_alpha(alpha)
    light.set_colour(colour)
    light_id = light_box.add_light(light)

    return light_id


def create_pathfinder() -> tcod.path.Pathfinder:
    """
    Create an empty pathfinder using the current game map
    """
    game_map = get_game_map()

    # combine entity blocking and tile blocking maps
    cost_map = game_map.block_movement_map | get_entity_blocking_movement_map()

    # create graph to represent the map and a pathfinder to navigate
    graph = tcod.path.SimpleGraph(cost=np.asarray(cost_map, dtype=np.int8), cardinal=2, diagonal=0)
    pathfinder = tcod.path.Pathfinder(graph)

    return pathfinder


def create_effect(origin: EntityID, target: EntityID, data: EffectData) -> Effect:
    """
    Create an effect from effect data.
    """
    effect_type = data.effect_type

    if effect_type == EffectType.APPLY_AFFLICTION:
        assert isinstance(data, ApplyAfflictionEffectData)
        return _create_apply_affliction_effect(origin, target, data)

    elif effect_type == EffectType.DAMAGE:
        assert isinstance(data, DamageEffectData)
        return _create_damage_effect(origin, target, data)

    elif effect_type == EffectType.MOVE:
        assert isinstance(data, MoveActorEffectData)
        return _create_move_actor_effect(origin, target, data)

    elif effect_type == EffectType.AFFECT_STAT:
        assert isinstance(data, AffectStatEffectData)
        return _create_affect_stat_effect(origin, target, data)

    elif effect_type == EffectType.AFFECT_COOLDOWN:
        assert isinstance(data, AffectCooldownEffectData)
        return _create_affect_cooldown_effect(origin, target, data)

    elif effect_type == EffectType.ALTER_TERRAIN:
        assert isinstance(data, AlterTerrainEffectData)
        return _create_alter_terrain_effect(origin, target, data)

    else:
        raise KeyError(f"Create effect: Effect provided ({effect_type}) was not handled.")


def _create_apply_affliction_effect(
    origin: EntityID, target: EntityID, data: ApplyAfflictionEffectData
) -> ApplyAfflictionEffect:
    effect = ApplyAfflictionEffect(
        origin=origin,
        target=target,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        affliction_name=data.affliction_name,
        duration=data.duration,
    )
    return effect


def _create_damage_effect(origin: EntityID, target: EntityID, data: DamageEffectData) -> DamageEffect:
    effect = DamageEffect(
        origin=origin,
        target=target,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        stat_to_target=data.stat_to_target,
        accuracy=data.accuracy,
        damage=data.damage,
        damage_type=data.damage_type,
        mod_stat=data.mod_stat,
        mod_amount=data.mod_amount,
        potency=data.potency,
    )

    return effect


def _create_move_actor_effect(origin: EntityID, target: EntityID, data: MoveActorEffectData) -> MoveActorEffect:
    effect = MoveActorEffect(
        origin=origin,
        target=target,
        direction=data.direction,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        move_amount=data.move_amount,
    )

    return effect


def _create_affect_stat_effect(origin: EntityID, target: EntityID, data: AffectStatEffectData) -> AffectStatEffect:
    effect = AffectStatEffect(
        origin=origin,
        target=target,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        cause_name=data.cause_name,
        stat_to_target=data.stat_to_target,
        affect_amount=data.affect_amount,
    )

    return effect


def _create_affect_cooldown_effect(
    origin: EntityID, target: EntityID, data: AffectCooldownEffectData
) -> AffectCooldownEffect:
    effect = AffectCooldownEffect(
        origin=origin,
        target=target,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        skill_name=data.skill_name,
        affect_amount=data.affect_amount,
    )

    return effect


def _create_alter_terrain_effect(
    origin: EntityID, target: EntityID, data: AlterTerrainEffectData
) -> AlterTerrainEffect:
    effect = AlterTerrainEffect(
        origin=origin,
        target=target,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        terrain_name=data.terrain_name,
        affect_amount=data.affect_amount,
    )

    return effect


############################# GET - RETURN AN EXISTING SOMETHING ###########################


def get_game_map() -> GameMap:
    """
    Get current game_map. Raises AttributeError if game_map doesnt exist.
    """
    if store.current_game_map:
        game_map = store.current_game_map
    else:
        raise AttributeError("get_game_map: Tried to get the game_map but there isnt one.")
    return game_map


def get_tile(tile_pos: Tuple[int, int]) -> Tile:
    """
    Get the tile at the specified location. Raises exception if out of bounds or doesnt exist.
    """
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


def get_entity_blocking_movement_map() -> np.array:
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
    raise ValueError("Player not found.")


def get_entitys_component(entity: EntityID, component: Type[_C]) -> _C:
    """
    Get an entity's component. Will raise exception if entity does not have the component.  Use entity_has_component
    to check.
    """
    if entity_has_component(entity, component):
        return snecs.entity_component(entity, component)
    else:
        name = get_name(entity)
        raise AttributeError(
            f"get_entitys_component:'{name}'({entity}) tried to get {component.__name__}, " f"but it was not found."
        )


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

    if entity_has_component(entity, Traits):
        trait = get_entitys_component(entity, Traits)
        for name in trait.names:
            data = library.TRAITS[name]
            value += getattr(data, stat)

    if entity_has_component(entity, Afflictions):
        afflictions = get_entitys_component(entity, Afflictions)
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
    # FIXME - this doesnt work for sight range
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
    if entity_has_component(entity, Afflictions):
        afflictions = get_entitys_component(entity, Afflictions)
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
        return knowledge.skills[skill_name]
    except KeyError:
        raise KeyError(
            f"get_known_skill: '{get_name(entity)}' tried to use a skill, '{skill_name}', they dont  " f"know."
        )


def get_affected_entities(
    target_pos: Tuple[int, int], shape: ShapeType, shape_size: int, shape_direction: Optional[Tuple[int, int]] = None
):
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


def get_entities_on_tile(tile: Tile) -> List[EntityID]:
    """
    Return a list of all the entities in that tile
    """
    x = tile.x
    y = tile.y
    entities = []
    from scripts.engine.core import query

    for entity, (position,) in query.position:
        assert isinstance(position, Position)
        if (x, y) in position:
            entities.append(entity)
    return entities


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
    game_map = store.current_game_map  # not using get_game_map for performance
    assert isinstance(game_map, GameMap)

    # before we even check tags, lets confirm it is in bounds
    if not _is_tile_in_bounds(tile, game_map):
        return False

    if tag == TileTag.OPEN_SPACE:
        # if nothing is blocking movement
        if not tile.blocks_movement and not _tile_has_entity_blocking_movement(tile):
            return True
    elif tag == TileTag.BLOCKED_MOVEMENT:
        # if anything is blocking
        if tile.blocks_movement or _tile_has_entity_blocking_movement(tile):
            return True
    elif tag == TileTag.SELF:
        # if entity on tile is same as active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            return _tile_has_specific_entity(tile, active_entity)
        else:
            logging.warning("Tried to get TileTag.SELF but gave no active_entity.")
    elif tag == TileTag.OTHER_ENTITY:
        # if entity on tile is not active entity
        if active_entity:
            assert isinstance(active_entity, EntityID)
            # check both possibilities. either the tile containing the active entity or not
            return _tile_has_other_entities(tile, active_entity)
        else:
            logging.warning("Tried to get TileTag.OTHER_ENTITY but gave no active_entity.")
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

    # If we've hit here it must be false!
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
    fov_map = get_entitys_component(entity, FOV).map
    light_map = game_map.light_map

    # combine maps
    visible_map = fov_map & light_map

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
    return len(get_entities_on_tile(tile)) > 0


def _tile_has_other_entities(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile has other entities apart from the provided active entity
    """
    entities_on_tile = get_entities_on_tile(tile)
    active_entity_is_on_tile = active_entity in entities_on_tile
    return (len(entities_on_tile) > 0 and not active_entity_is_on_tile) or (
        len(entities_on_tile) > 1 and active_entity_is_on_tile
    )


def _tile_has_specific_entity(tile: Tile, active_entity: EntityID) -> bool:
    """
    Check if the specified tile  has the specified entity on it
    """
    return active_entity in get_entities_on_tile(tile)


def _tile_has_entity_blocking_movement(tile: Tile) -> bool:
    x = tile.x
    y = tile.y

    # Any entities that block movement?
    for entity, (position, physicality) in get_components([Position, Physicality]):
        assert isinstance(position, Position)
        assert isinstance(physicality, Physicality)

        if (x, y) in position and physicality.blocks_movement:
            return True
    return False


def _tile_has_entity_blocking_sight(tile: Tile, active_entity: EntityID) -> bool:
    x = tile.x
    y = tile.y

    if entity_has_component(active_entity, Physicality):
        viewer_height = get_entitys_component(active_entity, Physicality).height
    else:
        # viewer has no height, assume everything blocks
        return True

    # Any entities that block sight?
    for entity, (position, physicality) in get_components([Position, Physicality]):
        assert isinstance(position, Position)
        assert isinstance(physicality, Physicality)

        if (x, y) in position and physicality.height > viewer_height:
            return True
    return False


def _can_afford_cost(entity: EntityID, resource: ResourceType, cost: int) -> bool:
    """
    Check if entity can afford the resource cost
    """
    resources = get_entitys_component(entity, Resources)

    # Check if cost can be paid
    value = getattr(resources, resource.lower())
    if value - cost >= 0:
        return True
    else:
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
    not_on_cooldown = False
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
            event_hub.post(MessageEvent("I cannot afford to do that."))
        else:
            logging.warning(
                f"can_use_skill: '{get_name(entity)}' tried to use {skill_name}, which they can`t" f"afford."
            )

    # log/inform on cooldown
    if not not_on_cooldown:
        # is it the player that's can't afford it?
        if entity == player:
            event_hub.post(MessageEvent("I'm not ready to do that, yet."))
        else:
            if cooldown == INFINITE:
                cooldown_msg = "unknown"
            else:
                cooldown_msg = str(cooldown)
            logging.warning(
                f"can_use_skill: '{get_name(entity)}' tried to use {skill_name}, but needs to wait "
                f" {cooldown_msg} more rounds."
            )

    # we've reached the end; no good.
    return False


def entity_has_immunity(entity: EntityID, name: str) -> bool:
    """
    Check if an entity has immunity to the named Action.
    """
    try:
        immunity = get_entitys_component(entity, Immunities)
        if name in immunity.active:
            return True
        else:
            return False

    except AttributeError:
        logging.info(f"entity_has_immunity: `{get_name(entity)}`, ({entity}), does not have Immunities Component.")
        return False


def add_immunity(entity: EntityID, immunity_name: str, duration: int):
    """
    Add an immunity to an Entity's Immunities Component. If entity has no Immunities Component one will be added.
    """
    try:
        immunity = get_entitys_component(entity, Immunities)
        immunity.active[immunity_name] = duration

    except AttributeError:
        add_component(entity, Immunities({immunity_name: duration}))

    logging.debug(f"'{get_name(entity)}' is now immune to {immunity_name} for {duration} rounds.")


################################ CONDITIONAL ACTIONS - CHANGE STATE - RETURN SUCCESS STATE  #############


def pay_resource_cost(entity: EntityID, resource: ResourceType, cost: int) -> bool:
    """
    Remove the resource cost from the using entity
    """
    resources = get_entitys_component(entity, Resources)
    name = get_name(entity)

    try:
        resource_value = getattr(resources, resource.lower())

        if resource_value != INFINITE:
            resource_left = resource_value - cost
            setattr(resources, resource.lower(), resource_left)

            logging.info(f"'{name}' paid {cost} {resource} and has {resource_left} left.")
            return True
        else:
            logging.info(f"'{name}' paid nothing as they have infinite {resource}.")
    except AttributeError:
        logging.warning(f"pay_resource_cost: '{name}' tried to pay {cost} {resource} but Resources component not "
                        f"found.")

    return False


def use_skill(user: EntityID, skill: Type[Skill], target_tile: Tile, direction: DirectionType) -> bool:
    """
    Use the specified skill on the target tile, usually creating a projectile. Returns True is successful if
    criteria to use skill was met, False if not.
    """
    # we init so that any overrides of the Skill.init are applied
    skill_cast = skill(user, target_tile, direction)

    # ensure they are the right target type
    if tile_has_tags(user, skill_cast.target_tile, skill_cast.cast_tags):
        result = skill_cast.use()
        return result
    else:
        logging.info(f"Could not use skill, target tile does not have required tags ({skill_cast.cast_tags}).")

    return False


def apply_skill(skill: Skill) -> bool:
    """
    Resolve the skill's effects. Returns True is successful if criteria to apply skill was met, False if not.
    """
    success = None

    # ensure they are the right target type
    if tile_has_tags(skill.user, skill.target_tile, skill.target_tags):
        for entity, effects in skill.apply():
            if entity not in skill.ignore_entities:
                effect_queue = list(effects)
                while effect_queue:
                    effect = effect_queue.pop()
                    result, new_effects = effect.evaluate()
                    effect_queue.extend(new_effects)

                    # only take result of initial effect
                    if not success:
                        success = result
        if success:
            logging.debug(f"'{get_name(skill.user)}' successfully applied {skill.name} to ({skill.target_tile.x},"
                          f"{skill.target_tile.y}).")
            return True
        else:
            logging.debug(f"'{get_name(skill.user)}' unsuccessfully applied {skill.name} to ({skill.target_tile.x},"
                          f"{skill.target_tile.y}).")
            return False
    else:
        logging.info(
            f"Could not apply skill '{skill.__class__.__name__}', target tile does not have required "
            f"tags ({skill.target_tags})."
        )

    return False


def set_skill_on_cooldown(entity: EntityID, skill_name: str, cooldown_duration: int):
    """
    Sets an entity's skill on cooldown.
    """
    knowledge = get_entitys_component(entity, Knowledge)
    knowledge.set_skill_cooldown(skill_name, cooldown_duration)


def apply_affliction(affliction: Affliction) -> bool:
    """
    Apply the affliction's effects. Returns True is successful if criteria to trigger the affliction was met,
    False if not.
    """
    target = affliction.affected_entity
    position = get_entitys_component(target, Position)
    target_tile = get_tile((position.x, position.y))

    # ensure they are the right target type
    if tile_has_tags(affliction.origin, target_tile, affliction.target_tags):
        for entity, effects in affliction.apply():
            effect_queue = list(effects)
            while effect_queue:
                effect = effect_queue.pop()
                effect_queue.extend(effect.evaluate()[1])
        return True
    else:
        logging.info(
            f'Could not apply affliction "{affliction.name}", target tile does not have required '
            f"tags ({affliction.target_tags})."
            )

    return False


def trigger_affliction(affliction: Affliction):
    """
    Trigger the affliction on the affected entity.
    """
    for entity, effects in affliction.trigger():
        effect_queue = list(effects)
        while effect_queue:
            effect = effect_queue.pop()
            effect_queue.extend(effect.evaluate()[1])


def take_turn(entity: EntityID) -> bool:
    """
    Process the entity's Thought component. If no component found then EndTurn event is fired.
    """
    logging.debug(f"'{get_name(entity)}' is beginning their turn.")

    try:
        behaviour = get_entitys_component(entity, Thought)
        behaviour.behaviour.act()
        return True
    except AttributeError:
        logging.critical(f"'{get_name(entity)}' has no behaviour to use.")

    return False


def apply_damage(entity: EntityID, damage: int) -> bool:
    """
    Remove damage from entity's health. Return True is damage was applied.
    """
    if damage <= 0:
        logging.info(f"Damage was {damage} and therefore nothing was done.")
        return False

    try:
        resource = get_entitys_component(entity, Resources)
        resource.health -= damage
        logging.info(f"'{get_name(entity)}' takes {damage} and has {resource.health} health remaining.")
        return True
    except AttributeError:
        logging.warning(f"apply_damage: '{get_name(entity)}' has no resource so couldn`t apply damage.")

    return False


def spend_time(entity: EntityID, time_spent: int) -> bool:
    """
    Add time_spent to the entity's total time spent.
    """

    try:
        tracked = get_entitys_component(entity, Tracked)
        tracked.time_spent += time_spent
        return True
    except AttributeError:
        logging.warning(f"spend_time: '{get_name(entity)}' has no tracked to spend time.")

    return False


def choose_target(entity: EntityID) -> Optional[EntityID]:
    """
    Choose an appropriate target for the entity.
    FIXME - CURRENTLY JUST RETURNS PLAYER
    """
    return get_player()


################################ DEFINITE ACTIONS - CHANGE STATE - RETURN NOTHING  #############


def kill_entity(entity: EntityID):
    """
    Add entity to the deletion stack and removes them from the turn queue.
    """
    # if not player
    if entity != get_player():
        # delete from world
        delete_entity(entity)

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
        event_hub.post(MessageEvent("I should have died just then."))


def delete_entity(entity: EntityID):
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


def remove_component(entity: EntityID, component: Type[Component]):
    """
    Remove a component from the entity
    """
    snecs.remove_component(entity, component)


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
        logging.warning(f"{get_name(entity)} has no Knowledge component and cannot learn {skill_name}.")
        return

    knowledge = get_entitys_component(entity, Knowledge)
    skill_class = store.skill_registry[skill_name]
    knowledge.add(skill_class)


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

    # never less than 1
    if int_modified_damage <= 0:
        logging.debug(f"-> Damage ended at {int_modified_damage} so replaced with minimum damage value of 1.")
        int_modified_damage = 1

    # log the info
    logging.debug(
        f"-> Initial:{base_damage}, Mitigated: {format(mitigated_damage, '.2f')},  Modified"
        f":{format(modified_damage, '.2f')}, Final: {int_modified_damage}"
    )

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
