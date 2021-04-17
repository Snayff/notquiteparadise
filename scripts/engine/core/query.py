from __future__ import annotations

from snecs import Query

from scripts.engine.core.component import (
    Aesthetic,
    Afflictions,
    CombatStats,
    Exists,
    FOV,
    Identity,
    Immunities,
    IsActive,
    Knowledge,
    Lifespan,
    LightSource,
    MapCondition,
    Shrine,
    Opinion,
    Physicality,
    Position,
    Reaction,
    Tracked,
    Traits,
    WinCondition,
)

__all__ = [
    "tracked",
    "aesthetic",
    "knowledge",
    "afflictions",
    "position",
    "active",
    "lifespan",
    "opinion",
    "reaction",
    "immunities",
    "position_and_light_source",
    "position_and_reaction",
    "not_position",
    "active_actors",
    "position_and_physicality",
    "position_and_aesthetic",
    "position_and_identity_and_aesthetic",
    "position_and_win_condition",
    "position_and_map_condition",
    "active_and_tracked",
    "light_source_and_aesthetic",
    "position_and_identity_and_lifespan",
    "active_and_position_and_physicality",
]


_get_components = Query  # import directly from snecs to avoid issues with importing from world

################### SINGLE QUERIES #######################

tracked = _get_components([Tracked]).compile()

aesthetic = _get_components([Aesthetic]).compile()

knowledge = _get_components([Knowledge]).compile()

afflictions = _get_components([Afflictions]).compile()

position = _get_components([Position]).compile()

active = _get_components([IsActive]).compile()

lifespan = _get_components([Lifespan]).compile()

opinion = _get_components([Opinion]).compile()

reaction = _get_components([Reaction]).compile()

immunities = _get_components([Immunities]).compile()


################## MULTI QUERIES ##########################

position_and_light_source = _get_components([Position, LightSource]).compile()

position_and_physicality = _get_components([Position, Physicality]).compile()

position_and_aesthetic = _get_components([Position, Aesthetic]).compile()

position_and_win_condition = _get_components([Position, WinCondition]).compile()

position_and_map_condition = _get_components([Position, MapCondition]).compile()

position_and_shrine = _get_components([Position, Shrine]).compile()

position_and_reaction = _get_components([Position, Reaction]).compile()

active_and_tracked = _get_components([IsActive, Tracked]).compile()

active_and_aesthetic = _get_components([IsActive, Aesthetic]).compile()

position_and_identity_and_lifespan = _get_components([Position, Identity, Lifespan]).compile()

position_and_identity_and_aesthetic = _get_components([Position, Identity, Aesthetic]).compile()

active_and_light_source_and_position = _get_components([IsActive, LightSource, Position]).compile()

light_source_and_aesthetic = _get_components([LightSource, Aesthetic]).compile()

active_and_position_and_physicality = _get_components([IsActive, Position, Physicality]).compile()


################## TYPE OF ENTITY QUERIES ##########################
# N.B. these are based on what components are used during the creation methods

actors = _get_components([Position, Physicality, Identity, CombatStats, Traits, FOV, Tracked, Immunities])
active_actors = _get_components(
    [IsActive, Position, Physicality, Identity, CombatStats, Traits, FOV, Tracked, Immunities]
).compile()

##################### FILTERS ###############################
# .filter((DOT & StatusEffect) | (~DOT & Poison & ~Antidote))
# would be "return HPComponents where (if entity has DamageOverTimeComponent it also must have
# StatusEffectComponent, otherwise it has PoisonComponent and not AntidoteComponent)

not_position = _get_components([Exists]).filter(~Position).compile()
