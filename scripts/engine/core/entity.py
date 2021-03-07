from __future__ import annotations

import logging
import random
from typing import List, Optional, Tuple, Type, TypeVar

import numpy as np
import snecs
import tcod
from snecs import Component, new_entity, Query
from snecs.typedefs import EntityID

from scripts.engine.core import hourglass, utility
from scripts.engine.core.component import (
    Aesthetic,
    Afflictions,
    CombatStats,
    Exists,
    FOV,
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
    Sight,
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
    MoveOtherEffect,
    MoveSelfEffect,
)
from scripts.engine.core.utility import build_sprites_from_paths
from scripts.engine.internal import library
from scripts.engine.internal.action import Affliction, Skill
from scripts.engine.internal.constant import (
    DirectionType,
    EffectType,
    HitType,
    HitTypeType,
    INFINITE,
    PrimaryStat,
    RenderLayer,
    ResourceType,
    SecondaryStat,
    ShapeType,
    TILE_SIZE,
    TraitGroup,
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
    MoveEffectData,
    ProjectileData,
    TerrainData,
)
from scripts.engine.internal.event import event_hub, LoseConditionMetEvent, MessageEvent
from scripts.engine.world_objects import lighting
from scripts.engine.world_objects.tile import Tile

__all__ = ["create_entity"]

############################# LOCAL DEFINITIONS #############################

_C = TypeVar("_C", bound=Component)  # to represent components where we don't know which is being used
get_entitys_components = snecs.all_components
get_components = Query
entity_has_component = snecs.has_component


############################# CREATE - RETURN OBJECT #############################


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
    components.append(Physicality(True, actor_data.height))
    components.append(Traits(actor_data.trait_names))
    components.append(FOV())
    components.append(Tracked(hourglass.get_time()))
    components.append(Immunities())

    # combat stats
    base_stats = {}
    base_values = library.GAME_CONFIG.base_values
    for primary_stat in [
        PrimaryStat.VIGOUR,
        PrimaryStat.CLOUT,
        PrimaryStat.SKULLDUGGERY,
        PrimaryStat.BUSTLE,
        PrimaryStat.EXACTITUDE,
    ]:
        # apply primary base value
        value = getattr(base_values, primary_stat)

        # loop traits and get values for stats
        for name in actor_data.trait_names:
            data = library.TRAITS[name]
            value += getattr(data, primary_stat)
        base_stats[primary_stat] = value
    stats = CombatStats(**base_stats)  # type: ignore

    # apply base values to secondary
    for secondary_stat in [
        SecondaryStat.MAX_HEALTH,
        SecondaryStat.MAX_STAMINA,
        SecondaryStat.ACCURACY,
        SecondaryStat.RESIST_BURN,
        SecondaryStat.RESIST_CHEMICAL,
        SecondaryStat.RESIST_ASTRAL,
        SecondaryStat.RESIST_COLD,
        SecondaryStat.RESIST_MUNDANE,
        SecondaryStat.RUSH,
    ]:
        stats.amend_base_value(secondary_stat, getattr(library.GAME_CONFIG.base_values, secondary_stat))
    components.append(stats)  # type: ignore

    # sight range
    sight_range = 0
    for name in actor_data.trait_names:
        data = library.TRAITS[name]
        if data.sight_range > sight_range:
            sight_range = data.sight_range
    components.append(Sight(sight_range))

    # set up light
    radius = 2
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
    components.append(Aesthetic(sprites, traits_paths, RenderLayer.ACTOR, (x, y)))

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
    components.append(Aesthetic(sprites, [terrain_data.sprite_paths], RenderLayer.TERRAIN, (x, y)))

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

    projectile.append(Aesthetic(sprites, [data.sprite_paths], RenderLayer.ACTOR, (x, y)))
    projectile.append(Tracked(hourglass.get_time_of_last_turn()))  # allocate time to ensure they act next
    projectile.append(Position((x, y)))
    projectile.append(Resources(999, 999))
    projectile.append(Afflictions())
    projectile.append(IsActive())

    # set up light
    radius = 1
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

    delayed_skill.append(Aesthetic(sprites, [data.sprite_paths], RenderLayer.TERRAIN, (x, y)))
    delayed_skill.append(Tracked(hourglass.get_time_of_last_turn() - 1))  # allocate time to ensure they act next
    delayed_skill.append(Position((x, y)))
    delayed_skill.append(IsActive())

    entity = create_entity(delayed_skill)

    # add post-creation components
    behaviour = store.behaviour_registry["DelayedSkill"]
    thought = Thought(behaviour(entity))
    from scripts.engine.internal.action import DelayedSkill

    assert isinstance(thought.behaviour, DelayedSkill)
    thought.behaviour.data = data
    add_component(entity, thought)

    logging.debug(f"{delayed_skill_name}`s created at ({x},{y}) and will trigger in {data.duration} rounds.")

    return entity


def create_affliction(name: str, creator: EntityID, target: EntityID, duration: int) -> Affliction:
    """
    Creates an instance of an Affliction provided the name
    """
    affliction = store.affliction_registry[name](creator, target, duration)
    return affliction


def create_light(pos: Tuple[int, int], radius: int, colour: Tuple[int, int, int], alpha: int) -> str:
    """
    Create a Light and add it to the current GameMap's Lightbox. Pos is the world position - the light will handle
    scaling to screen.
    Returns the light_id of the Light.
    """
    light_img = utility.get_image("world/light_mask.png", ((radius * 2) * TILE_SIZE, (radius * 2) * TILE_SIZE))
    from scripts.engine.core.world import get_game_map
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
    from scripts.engine.core.world import get_game_map
    game_map = get_game_map()

    # combine entity blocking and tile blocking maps
    from scripts.engine.core.world import get_entity_blocking_movement_map
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
        assert isinstance(data, MoveEffectData)
        return _create_move_self_effect(origin, target, data)

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


def _create_move_self_effect(origin: EntityID, target: EntityID, data: MoveEffectData) -> MoveSelfEffect:
    effect = MoveSelfEffect(
        origin=origin,
        target=target,
        direction=data.direction,
        success_effects=data.success_effects,
        failure_effects=data.failure_effects,
        move_amount=data.move_amount,
    )

    return effect


def _create_move_other_effect(origin: EntityID, target: EntityID, data: MoveEffectData) -> MoveOtherEffect:
    effect = MoveOtherEffect(
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


############################# GET - RETURN AN EXISTING SOMETHING  #############################

def get_player() -> EntityID:
    """
    Get the player.
    """
    for entity, (_,) in get_components([IsPlayer]):
        return entity
    raise ValueError("Player not found.")


def get_entitys_component(entity: EntityID, component: Type[_C]) -> _C:
    """
    Get an entity's component. Will raise exception if entity does not have the component.  Use entity_has_component
    to check.
    """
    if entity_has_component(entity, component):
        return snecs.entity_component(entity, component)
    elif entity_has_component(entity, Identity):
        name = get_name(entity)
        raise AttributeError(
            f"get_entitys_component:'{name}'({entity}) tried to get {component.__name__}, " f"but it was not found."
        )
    else:
        raise AttributeError(
            f"get_entitys_component:'unknown'({entity}) tried to get {component.__name__}, " f"but it was not found."
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


############################# QUERIES #############################

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


############################# AMEND STATE #############################

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
        logging.warning(
            f"pay_resource_cost: '{name}' tried to pay {cost} {resource} but Resources component not " f"found."
        )

    return False


def use_skill(user: EntityID, skill: Type[Skill], target_tile: Tile, direction: DirectionType) -> bool:
    """
    Use the specified skill on the target tile, usually creating a projectile. Returns True is successful if
    criteria to use skill was met, False if not.
    """
    # we init so that any overrides of the Skill.init are applied
    skill_cast = skill(user, target_tile, direction)

    # ensure they are the right target type
    from scripts.engine.core.world import tile_has_tags
    if tile_has_tags(user, skill_cast.target_tile, skill_cast.cast_tags):
        result = skill_cast.use()
        return result
    else:
        logging.info(
            f"Could not use skill, ({target_tile.x},{target_tile.y}) does not have required tags "
            f"({skill_cast.cast_tags})."
        )

    return False


def apply_skill(skill: Skill) -> bool:
    """
    Resolve the skill's effects. Returns True is successful if criteria to apply skill was met, False if not.
    """
    success = None

    # ensure they are the right target type
    from scripts.engine.core.world import tile_has_tags
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
            logging.debug(
                f"'{get_name(skill.user)}' successfully applied {skill.name} to ({skill.target_tile.x},"
                f"{skill.target_tile.y})."
            )
            return True
        else:
            logging.debug(
                f"'{get_name(skill.user)}' unsuccessfully applied {skill.name} to ({skill.target_tile.x},"
                f"{skill.target_tile.y})."
            )
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
    from scripts.engine.core.world import get_tile
    target_tile = get_tile((position.x, position.y))

    # ensure they are the right target type
    from scripts.engine.core.world import tile_has_tags
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
    N.B. CURRENTLY JUST RETURNS PLAYER
    """
    return get_player()


def kill_entity(entity: EntityID):
    """
    Add entity to the deletion stack and removes them from the turn queue.
    """
    # if not player
    if entity != get_player():
        # delete from world
        delete_entity(entity)

        turn_queue = hourglass.get_turn_queue()

        # if turn holder create new queue without them
        if entity == hourglass.get_turn_holder():

            # ensure the game state reflects the new queue
            hourglass.next_turn(entity)

        elif entity in turn_queue:
            # remove from turn queue
            turn_queue.pop(entity)

    else:
        event_hub.post(LoseConditionMetEvent())


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

        # remove stat modification
        if EffectType.AFFECT_STAT in affliction.identity_tags and entity_has_component(entity, CombatStats):
            stats = get_entitys_component(entity, CombatStats)
            stats.remove_mod(affliction.name)


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


############################# CALCULATIONS #############################

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
        hit_mod = hit_types_data.crit.modifier
    elif hit_type == HitType.HIT:
        hit_mod = hit_types_data.hit.modifier
    else:
        hit_mod = hit_types_data.graze.modifier
    modified_damage = mitigated_damage * hit_mod

    # round down the dmg
    int_modified_damage = int(modified_damage)

    # never less than 1
    if int_modified_damage <= 0:
        logging.debug(f"-> Damage ended at {int_modified_damage} so replaced with minimum damage value of 1.")
        int_modified_damage = 1

    # log the info
    logging.debug(
        f"-> Base Damage:{base_damage}, +Damage Mod:{damage_mod_amount} ({base_damage + damage_mod_amount}), "
        f"-Resistance:{resist_value} ({format(mitigated_damage, '.2f')}), "
        f"*Hit Mod:{hit_mod} ({format(modified_damage, '.2f')}), "
        f"Result (rounded): {int_modified_damage}"
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

