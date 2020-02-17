from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from scripts.world.data_classes.interaction_dataclass import InteractionData


@dataclass
class AspectData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    duration: int = None
    sprite: str = "None"
    blocks_sight: bool = False
    blocks_movement: bool = False
    effects: Dict = field(default_factory=list)
    interactions: List[InteractionData] = field(default_factory=list)  # TODO - convert to dict