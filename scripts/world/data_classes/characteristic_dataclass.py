from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from scripts.core.extend_json import register_dataclass_with_json
from scripts.world.data_classes.sprites_dataclass import CharacteristicSpritePathsData

if TYPE_CHECKING:
    from typing import Dict, List


@register_dataclass_with_json
@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=dict)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)
