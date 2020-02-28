from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from scripts.core.constants import CharacteristicSprites
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    sprites: Dict[str, CharacteristicSprites] = field(default_factory=dict)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)
