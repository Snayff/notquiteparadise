from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict
from scripts.core.constants import PrimaryStatTypes, SecondaryStatTypes
from scripts.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    pass


@register_dataclass_with_json
@dataclass
class BaseStatData:
    """
    Data class to contain primary and secondary stats
    """
    primary: Dict = field(default_factory=dict)
    secondary: Dict = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class BasePrimaryStatData:
    """
    Data class for primary  stats
    """
    name: str = "None"
    primary_stat_type: PrimaryStatTypes = None
    base_value: int = 0


@register_dataclass_with_json
@dataclass
class BaseSecondaryStatData:
    """
    Data class for secondary stats
    """
    name: str = "None"
    secondary_stat_type: SecondaryStatTypes = None
    base_value: int = 0
    vigour_mod: int = 0
    clout_mod: int = 0
    skullduggery_mod: int = 0
    bustle_mod: int = 0
    exactitude_mod: int = 0