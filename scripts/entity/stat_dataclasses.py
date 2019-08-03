
from dataclasses import dataclass, field
from typing import Dict

from scripts.core.constants import PrimaryStatTypes, SecondaryStatTypes


@dataclass
class StatData:
    """
    Data class to contain primary and secondary stats
    """
    primary: Dict = field(default_factory=dict)
    secondary: Dict = field(default_factory=dict)


@dataclass
class PrimaryStatData:
    """
    Data class for primary  stats
    """
    name: str = "None"
    primary_stat_type: PrimaryStatTypes = None
    base_value: int = 0


@dataclass
class SecondaryStatData:
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
