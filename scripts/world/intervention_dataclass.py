
from dataclasses import dataclass, field
from typing import List
from scripts.skills.effects.effect_dataclass import EffectData


@dataclass()
class InterventionData:
    """
    Data class for a god's intervention
    """
    name: str = "None"
    required_opinion: int = 0
    effects: List[EffectData] = field(default_factory=list)