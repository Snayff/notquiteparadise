from snecs.typedefs import EntityID

from scripts.engine import utility, world
from scripts.engine.component import Resources
from scripts.engine.core.constants import PrimaryStat, DamageType
from scripts.engine.core.data import store
from scripts.engine.core.definitions import ActorData
from scripts.engine.effect import DamageEffect
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
    elif damage == 0:
        assert start_hp == end_hp
    elif damage < 0:
        assert start_hp == end_hp
