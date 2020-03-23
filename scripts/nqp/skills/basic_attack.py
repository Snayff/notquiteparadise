from __future__ import annotations

from typing import TYPE_CHECKING, Type
from snecs.typedefs import EntityID
from scripts.engine import skill, utility, world
from scripts.engine.core.constants import PrimaryStat, Shape, TargetTag, DamageType, BASE_ACCURACY, BASE_DAMAGE
from scripts.engine.core.definitions import DamageEffectData
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


def use():
    pass


def activate(causing_entity: EntityID, target_tiles: List[Tile]):
    # create damage effect
    effect_dict = {
        "creator": "basic_attack",
        "accuracy": BASE_ACCURACY + 5,
        "stat_to_target": PrimaryStat.VIGOUR,
        "shape": Shape.TARGET,
        "shape_size": 1,
        "required_tags": [
            TargetTag.OTHER_ENTITY
        ],
        "damage": BASE_DAMAGE + 20,
        "damage_type": DamageType.MUNDANE,
        "mod_amount": 0.1,
        "mod_stat": PrimaryStat.CLOUT
    }
    effect = DamageEffectData(**effect_dict)

    for tile in target_tiles:
        coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
        effected_tiles = world.get_tiles(tile.x, tile.y, coords)
        skill.process_effect(effect, effected_tiles, causing_entity)



