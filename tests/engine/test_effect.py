from snecs.typedefs import EntityID

from scripts.engine import library, utility, world
from scripts.engine.component import Afflictions, Position, Resources
from scripts.engine.core.constants import Direction, PrimaryStat, DamageType
from scripts.engine.core.data import store
from scripts.engine.core.definitions import ActorData
from scripts.engine.effect import AffectStatEffect, ApplyAfflictionEffect, DamageEffect, MoveActorEffect
from scripts.engine.world_objects.game_map import GameMap
import pytest
from scripts.nqp.actions import afflictions, behaviours, skills  # must import to register in engine


def _create_scenario() -> EntityID:
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
        benchmark,
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
    benchmark(effect.evaluate)
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
        benchmark,
        x,
        y
):
    entity = _create_scenario()
    direction = (x, y)

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
    success = benchmark(effect.evaluate)[0]
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
        benchmark,
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

    stats = world.create_combat_stats(entity)
    start_stat = getattr(stats, stat_to_target)
    success = benchmark(effect.evaluate)[0]
    stats = world.create_combat_stats(entity)
    end_stat = getattr(stats, stat_to_target)

    if success:
        assert start_stat + affect_amount == end_stat
    else:
        assert start_stat == end_stat


_affliction_names = []
for name in library.AFFLICTIONS.keys():
    _affliction_names.append(name)


@pytest.fixture(params=_affliction_names)
def affliction_name(request):
    return request.param


def test_apply_affliction_effect(
        benchmark,
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

    # start_afflictions = world.get_entitys_component(entity, Afflictions)
    success = benchmark(effect.evaluate)[0]
    end_afflictions = world.get_entitys_component(entity, Afflictions)

    names = []
    for affliction in end_afflictions.active:
        names.append(affliction.name)

    if success:
        assert affliction_name in names
    else:
        assert affliction_name not in names
