from __future__ import annotations

from typing import TYPE_CHECKING

from snecs import Query

from scripts.engine.core.component import (
    Aesthetic,
    Afflictions,
    Blocking,
    Exists,
    FOV,
    HasCombatStats,
    Identity,
    IsActive,
    IsActor,
    Knowledge,
    Lifespan,
    LightSource,
    Position,
    Reaction,
    Tracked,
    WinCondition,
)

if TYPE_CHECKING:
    pass

__all__ = [
    "tracked",
    "aesthetic",
    "knowledge",
    "afflictions",
    "position",
    "active",
    "lifespan",
    "position_and_light_source",
    "position_and_reaction",
    "not_position",
    "active_and_light_source_and_position",
    "active_and_position_and_fov_and_combat_stats",
    "position_and_blocking",
    "position_and_aesthetic",
    "position_and_identity_and_aesthetic",
    "position_and_actor",
    "position_and_win_condition",
    "active_and_tracked",
    "light_source_and_aesthetic",
    "position_and_identity_and_lifespan",
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


################## MULTI QUERIES ##########################

position_and_light_source = get_components([Position, LightSource]).compile()

position_and_blocking = get_components([Position, Blocking]).compile()

position_and_aesthetic = get_components([Position, Aesthetic]).compile()

position_and_actor = get_components([Position, IsActor]).compile()

position_and_win_condition = get_components([Position, WinCondition]).compile()

position_and_reaction = get_components([Position, Reaction]).compile()

position_and_identity_and_lifespan = get_components([Position, Identity, Lifespan]).compile()

position_and_identity_and_aesthetic = get_components([Position, Identity, Aesthetic]).compile()

active_and_position_and_fov_and_combat_stats = get_components([IsActive, Position, FOV, HasCombatStats]).compile()

active_and_light_source_and_position = get_components([IsActive, LightSource, Position]).compile()

active_and_tracked = get_components([IsActive, Tracked]).compile()

light_source_and_aesthetic = get_components([LightSource, Aesthetic]).compile()

##################### FILTERS ###############################
# .filter((DOT & StatusEffect) | (~DOT & Poison & ~Antidote))
# would be "return HPComponents where (if entity has DamageOverTimeComponent it also must have
# StatusEffectComponent, otherwise it has PoisonComponent and not AntidoteComponent)

not_position = get_components([Exists]).filter(~Position).compile()
