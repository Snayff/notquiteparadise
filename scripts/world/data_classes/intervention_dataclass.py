
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
    description: str = "None"
    icon: str = "None"
    required_opinion: int = 0
    shape: SkillShapes = None
    shape_size: int = 1
    cooldown: int = 0
    required_tags: List[TargetTags] = field(default_factory=list)
    effects: Dict = field(default_factory=dict)