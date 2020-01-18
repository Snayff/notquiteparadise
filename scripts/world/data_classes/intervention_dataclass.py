
from dataclasses import dataclass, field
from typing import List, Dict

from scripts.core.constants import SkillShapes, TargetTags
from scripts.skills.effects.effect_dataclass import EffectData


@dataclass()
class InterventionData:
    """
    Data class for a god's intervention
    """
    name: str = "None"
    required_opinion: int = 0