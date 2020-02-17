from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    sprite: str = "None"
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    skills: Dict = field(default_factory=dict)
