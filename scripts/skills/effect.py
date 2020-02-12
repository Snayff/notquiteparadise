from dataclasses import dataclass, field
from typing import List

from scripts.core.constants import EffectTypes, TargetTags, DamageTypes, PrimaryStatTypes


@dataclass
class EffectData:
    """
    Data class for a skill effect
    """
    effect_type: EffectTypes
    required_tags: List[TargetTags] = field(default_factory=list)
    damage: int = 0
    affect_stat_amount: int = 0
    mod_stat: PrimaryStatTypes = None
    mod_amount: int = 0
    damage_type: DamageTypes = None
    accuracy: int = 0
    stat_to_target: PrimaryStatTypes = None
    aspect_name: str = "None"
    affliction_name: str = "None"
    duration: int = 0
    stat_to_affect: PrimaryStatTypes = None