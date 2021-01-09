from __future__ import annotations

from snecs import Query

from scripts.engine.core.component import (
    Aesthetic,
    Afflictions,
    Exists,
    FOV,
    HasCombatStats,
    Identity,
    Immunities,
    IsActive,
    Knowledge,
    Lifespan,
    LightSource,
    Opinion,
    Physicality,
    Position,
    Reaction,
    Tracked,
    Traits, WinCondition,
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
    "active_and_position_and_fov_and_combat_stats_and_physicality",
    "position_and_physicality",
    "position_and_aesthetic",
    "position_and_identity_and_aesthetic",
    "position_and_win_condition",
    "active_and_tracked",
    "light_source_and_aesthetic",
    "position_and_identity_and_lifespan",
    "active_and_position_and_physicality",
]


get_components = Query  # import directly from snecs to avoid issues with importing from world

################### SINGLE QUERIES #######################

tracked = get_components([Tracked]).compile()

aesthetic = get_components([Aesthetic]).compile()

knowledge = get_components([Knowledge]).compile()

afflictions = get_components([Afflictions]).compile()

position = get_components([Position]).compile()

active = get_components([IsActive]).compile()

lifespan = get_components([Lifespan]).compile()

opinion = get_components([Opinion]).compile()

reaction = get_components([Reaction]).compile()

immunities = get_components([Immunities]).compile()


################## MULTI QUERIES ##########################

position_and_light_source = get_components([Position, LightSource]).compile()

position_and_physicality = get_components([Position, Physicality]).compile()

position_and_aesthetic = get_components([Position, Aesthetic]).compile()

position_and_win_condition = get_components([Position, WinCondition]).compile()

position_and_reaction = get_components([Position, Reaction]).compile()

active_and_tracked = get_components([IsActive, Tracked]).compile()

position_and_identity_and_lifespan = get_components([Position, Identity, Lifespan]).compile()

position_and_identity_and_aesthetic = get_components([Position, Identity, Aesthetic]).compile()

active_and_light_source_and_position = get_components([IsActive, LightSource, Position]).compile()

light_source_and_aesthetic = get_components([LightSource, Aesthetic]).compile()

active_and_position_and_physicality = get_components([IsActive, Position, Physicality]).compile()

active_and_position_and_fov_and_combat_stats_and_physicality = get_components(
    [IsActive, Position, FOV, HasCombatStats, Physicality]
).compile()


################## TYPE OF ENTITY QUERIES ##########################
# N.B. these are based on what components are used during the creation methods

actors = get_components([Position, Physicality, Identity, HasCombatStats, Traits, FOV, Tracked, Immunities])


##################### FILTERS ###############################
# .filter((DOT & StatusEffect) | (~DOT & Poison & ~Antidote))
# would be "return HPComponents where (if entity has DamageOverTimeComponent it also must have
# StatusEffectComponent, otherwise it has PoisonComponent and not AntidoteComponent)

not_position = get_components([Exists]).filter(~Position).compile()
