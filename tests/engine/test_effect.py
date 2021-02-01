import pytest
import snecs
from snecs.typedefs import EntityID

from scripts.engine.core import query, state, world
from scripts.engine.internal import library
from scripts.engine.core.component import Afflictions, CombatStats, Knowledge, Position, Resources
from scripts.engine.internal.constant import DamageType, Direction, PrimaryStat
from scripts.engine.internal.data import store
from scripts.engine.internal.definition import ActorData
from scripts.engine.core.effect import (
    AffectCooldownEffect,
    AffectStatEffect,
    AlterTerrainEffect,
    ApplyAfflictionEffect,
    DamageEffect,
    MoveActorEffect,
)
from scripts.engine.world_objects.game_map import GameMap
from scripts.nqp.command import register_actions

##############################################################
#
# !IMPORTANT! Using pytest-benchmark causes the damage effect test to hang indefinitely and the others to fail
#
###############################################################



# register all actions with engine
register_actions()


def _create_scenario() -> EntityID:

    # new world
    empty_world = snecs.World()
    world.move_world(empty_world)

    # new gamemap
    game_map = GameMap("debug", 10)
    store.current_game_map = game_map
    actor_data = ActorData(
        key="test",
        possible_names=["test_name"],
        description="test_desc",
        position_offsets=[(0, 0)],
        trait_names=["shoom", "soft_tops", "dandy"],
    )
    game_map.generate_new_map(actor_data)

    return world.get_player()


test_damage_effect_parameters = [
    # stat to target
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.CLOUT, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.SKULLDUGGERY, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.BUSTLE, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.EXACTITUDE, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),

    # accuracy
    (PrimaryStat.VIGOUR, 100, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, -1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),

    # damage
    (PrimaryStat.VIGOUR, 1, 100, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, -1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, 0, DamageType.BURN, PrimaryStat.VIGOUR, 1, 1),

    # damage type
    (PrimaryStat.VIGOUR, 1, 1, DamageType.CHEMICAL, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.ASTRAL, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.COLD, PrimaryStat.VIGOUR, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.MUNDANE, PrimaryStat.VIGOUR, 1, 1),

    # mod stats
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.CLOUT, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.SKULLDUGGERY, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.BUSTLE, 1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.EXACTITUDE, 1, 1),

    # mod amount
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 100, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, -1, 1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 0, 1),

    # potency
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 100),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, -1),
    (PrimaryStat.VIGOUR, 1, 1, DamageType.BURN, PrimaryStat.VIGOUR, 1, 0),
]


@pytest.mark.parametrize(["stat_to_target", "accuracy", "damage", "damage_type", "mod_stat", "mod_amount",
                             "potency"], test_damage_effect_parameters)
def test_damage_effect(
        stat_to_target,
        accuracy,
        damage,
        damage_type,
        mod_stat,
        mod_amount,
        potency,
):
    entity = _create_scenario()

    effect = DamageEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        stat_to_target=stat_to_target,
        accuracy=accuracy,
        damage=damage,
        damage_type=damage_type,
        mod_stat=mod_stat,
        mod_amount=mod_amount,
        potency=potency
    )

    start_hp = world.get_entitys_component(entity, Resources).health
    effect.evaluate()
    end_hp = world.get_entitys_component(entity, Resources).health

    # assess results
    # We are just testing damage can be applied, not the damage formula and as such this is simplified, otherwise
    # would need to consider  potency, stats etc.
    if damage > 0:
        assert start_hp != end_hp
    elif damage <= 0:
        assert start_hp == end_hp


test_move_actor_effect_parameters = [
    Direction.UP,
    Direction.UP_RIGHT,
    Direction.UP_LEFT,
    Direction.DOWN,
    Direction.DOWN_RIGHT,
    Direction.DOWN_LEFT
]


@pytest.mark.parametrize(["x", "y"], test_move_actor_effect_parameters)
def test_move_actor_effect(
        x,
        y
):
    entity = _create_scenario()
    direction = (x, y)  # type:ignore

    effect = MoveActorEffect(
        origin=entity,
        target=entity,
        direction=direction,
        success_effects=[],
        failure_effects=[],
        move_amount=1
    )

    position = world.get_entitys_component(entity, Position)
    start_pos = (position.x, position.y)
    success = effect.evaluate()[0]
    end_pos = (position.x, position.y)

    # assess results
    if success:
        assert start_pos[0] != end_pos[0] or start_pos[1] != end_pos[1]
    else:
        assert start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]


test_affect_stat_parameters = [
    # stats
    ("foo", PrimaryStat.VIGOUR, 1),
    ("foo", PrimaryStat.CLOUT, 1),
    ("foo", PrimaryStat.EXACTITUDE, 1),
    ("foo", PrimaryStat.BUSTLE, 1),
    ("foo", PrimaryStat.SKULLDUGGERY, 1),

    # amounts
    ("foo", PrimaryStat.VIGOUR, -1),
    ("foo", PrimaryStat.VIGOUR, 100),
    ("foo", PrimaryStat.VIGOUR, -100),
]


@pytest.mark.parametrize(["cause_name", "stat_to_target", "affect_amount"], test_affect_stat_parameters)
def test_affect_stat_effect(
        cause_name,
        stat_to_target,
        affect_amount,
):
    entity = _create_scenario()

    effect = AffectStatEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        cause_name=cause_name,
        stat_to_target=stat_to_target,
        affect_amount=affect_amount,
    )

    stats = world.get_entitys_component(entity, CombatStats)
    start_stat = getattr(stats, stat_to_target)
    success = effect.evaluate()[0]
    end_stat = getattr(stats, stat_to_target)

    if success:
        # N.B. should never be less than 1
        assert max(start_stat + affect_amount, 1) == end_stat
    else:
        assert start_stat == end_stat


_affliction_names = []
for name in library.AFFLICTIONS.keys():
    _affliction_names.append(name)


@pytest.fixture(params=_affliction_names)
def affliction_name(request):
    return request.param


def test_apply_affliction_effect(
        affliction_name,
):
    entity = _create_scenario()

    effect = ApplyAfflictionEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        affliction_name=affliction_name,
        duration=1,
    )

    success = effect.evaluate()[0]
    end_afflictions = world.get_entitys_component(entity, Afflictions)

    names = []
    for affliction in end_afflictions.active:
        names.append(affliction.name)

    if success:
        assert affliction_name in names
    else:
        assert affliction_name not in names


_skill_names = []
for name in library.SKILLS.keys():
    _skill_names.append(name)


@pytest.fixture(params=_skill_names)
def skill_name(request):
    return request.param


@pytest.fixture(params=[-100, -1, 0, 1, 100])
def affect_cooldown_amount(request):
    return request.param


def test_affect_cooldown_effect(
        skill_name,
        affect_cooldown_amount
):
    entity = _create_scenario()

    # assign skill
    world.learn_skill(entity, skill_name)

    effect = AffectCooldownEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        skill_name=skill_name,
        affect_amount=affect_cooldown_amount,
    )

    cooldown = 99
    knowledge = world.get_entitys_component(entity, Knowledge)
    knowledge.set_skill_cooldown(skill_name, cooldown)
    success = effect.evaluate()[0]
    end_cooldown = knowledge.cooldowns[skill_name]

    if success:
        assert max(cooldown - affect_cooldown_amount, 0) == end_cooldown
    else:
        assert cooldown == end_cooldown


_terrain_names = []
for name in library.TERRAIN.keys():
    _terrain_names.append(name)


@pytest.fixture(params=_terrain_names)
def terrain_name(request):
    return request.param


@pytest.fixture(params=[1, 100])
def affect_terrain_amount(request):
    return request.param


def test_alter_terrain_effect_create(
        terrain_name,
        affect_terrain_amount
):
    entity = _create_scenario()

    effect = AlterTerrainEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        terrain_name=terrain_name,
        affect_amount=affect_terrain_amount,
    )

    success = effect.evaluate()[0]
    target_pos = world.get_entitys_component(entity, Position)

    if success:
        confirmed = False
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                confirmed = True
        assert confirmed
    else:
        confirmed = False
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                confirmed = True
        assert not confirmed


@pytest.fixture(params=[0, -1, -100])
def affect_terrain_negative_amount(request):
    return request.param


def test_alter_terrain_effect_reduce_duration(
        terrain_name,
        affect_terrain_negative_amount
):
    entity = _create_scenario()

    # create terrain on the spot
    base_duration = 10
    effect = AlterTerrainEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        terrain_name=terrain_name,
        affect_amount=base_duration,
    )
    effect.evaluate()

    effect = AlterTerrainEffect(
        origin=entity,
        target=entity,
        success_effects=[],
        failure_effects=[],
        terrain_name=terrain_name,
        affect_amount=affect_terrain_negative_amount,
    )

    success = effect.evaluate()[0]
    target_pos = world.get_entitys_component(entity, Position)

    if success and (base_duration > affect_terrain_negative_amount):
        # test case: reduced duration but still exists
        still_exists = False
        duration_remaining = None
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                still_exists = True
                duration_remaining = lifespan.duration
        assert still_exists
        assert duration_remaining == base_duration - affect_terrain_negative_amount

    elif success and (base_duration < affect_terrain_negative_amount):
        # test case: duration sufficient to remove
        still_exists = False
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                still_exists = True
        assert not still_exists

    else:
        # test case: failed to create terrain; check valid reason
        data = library.TERRAIN[terrain_name]
        if data.blocks_movement:
            assert True
        else:
            assert False



