from __future__ import annotations
from typing import TYPE_CHECKING, Type

from scripts.engine import world
from scripts.engine.component import (
    Aesthetic,
    Afflictions,
    Blocking,
    FOV,
    HasCombatStats,
    Identity,
    IsActor,
    Knowledge,
    LightSource,
    Position,
    Tracked,
)

if TYPE_CHECKING:
    pass

__all__ = ["tracked", "aesthetic", "knowledge", "affliction", "position", "light_source_and_position",
    "position_and_fov_and_combat_stats", "position_and_blocking", "position_and_aesthetic",
    "position_and_identity_and_aesthetic", "position_and_actor"]


################### SINGLE QUERIES #######################

tracked = world.get_components([Tracked]).compile()

aesthetic = world.get_components([Aesthetic]).compile()

knowledge = world.get_components([Knowledge]).compile()

affliction = world.get_components([Afflictions]).compile()

position = world.get_components([Position]).compile()

################## MULTI QUERIES ##########################

light_source_and_position = world.get_components([LightSource, Position]).compile()

position_and_fov_and_combat_stats = world.get_components([FOV, Position, HasCombatStats]).compile()

position_and_blocking = world.get_components([Position, Blocking]).compile()

position_and_aesthetic = world.get_components([Position, Aesthetic]).compile()

position_and_actor = world.get_components([Position, IsActor]).compile()

position_and_identity_and_aesthetic = world.get_components([Position, Identity, Aesthetic]).compile()

