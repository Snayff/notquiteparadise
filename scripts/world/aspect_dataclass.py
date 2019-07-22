from dataclasses import dataclass, field
from typing import Dict


@dataclass()
class AspectData:
    """
    Data class for an aspect
    """
    name: str = "None"
    description: str = "None"
    sprite: str = "None"
    blocks_sight: bool = False
    blocks_movement: bool = False
    effects: Dict = field(default_factory=list)