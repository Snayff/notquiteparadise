from __future__ import annotations

from typing import TYPE_CHECKING, Type

from snecs import Query

from scripts.engine.component import (
    FOV,
    Aesthetic,
    Afflictions,
    Blocking,
    HasCombatStats,
    Identity,
    IsActor,
    Knowledge,
    LightSource,
    Position,
    Tracked,
    WinCondition,
)

if TYPE_CHECKING:
    pass

__all__ = [
    "tracked",
    "aesthetic",
    "knowledge",
    "affliction",
    "position",
    "light_source_and_position_and_aesthetic",
    "position_and_fov_and_combat_stats",
    "position_and_blocking",
    "position_and_aesthetic",
    "position_and_identity_and_aesthetic",
    "position_and_actor",
    "position_and_win_condition",
]


get_components = Query  # import from snecs to avoid issues with importing from world

################### SINGLE QUERIES #######################

tracked = get_components([Tracked]).compile()

aesthetic = get_components([Aesthetic]).compile()

knowledge = get_components([Knowledge]).compile()

affliction = get_components([Afflictions]).compile()

position = get_components([Position]).compile()

################## MULTI QUERIES ##########################

light_source_and_position_and_aesthetic = get_components([LightSource, Position, Aesthetic]).compile()

position_and_fov_and_combat_stats = get_components([FOV, Position, HasCombatStats]).compile()

position_and_blocking = get_components([Position, Blocking]).compile()

position_and_aesthetic = get_components([Position, Aesthetic]).compile()

position_and_actor = get_components([Position, IsActor]).compile()

position_and_win_condition = get_components([Position, WinCondition]).compile()

position_and_identity_and_aesthetic = get_components([Position, Identity, Aesthetic]).compile()
