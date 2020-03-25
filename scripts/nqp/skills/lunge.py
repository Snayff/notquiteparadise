from __future__ import annotations

from typing import TYPE_CHECKING, Type

from snecs.typedefs import EntityID

from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


def use():
    pass


def activate(causing_entity: EntityID, target_tiles: List[Tile]):
    # so we move forward 1 space

    # try to hit an enemy in the direction of movement

    # if we moved and hit refund half the resource cost and cooldown



    pass
