from dataclasses import dataclass, field
from typing import List, Dict

from scripts.core.constants import EffectTypes, TargetTags, DamageTypes, PrimaryStatTypes


@dataclass
class EffectData:
    """
    Data class for a skill effect
    """
    effect_type: EffectTypes
    required_tags: List[TargetTags] = field(default_factory=list)
    amount: int = 0
    damage: int = 0
    damage_type: DamageTypes = None
    accuracy: int = 0
    stat_to_target: PrimaryStatTypes = None
    new_terrain: TargetTags = None
    affliction_name: str = ""
    duration: int = 0
    stat_to_affect: PrimaryStatTypes = None


@dataclass()
class SkillData:
    """
    Data class for a skill
    """
    name: str
    description: str
    icon: str
    range: int
    resource_type: str
    resource_cost: int
    time_cost: int
    cooldown: int
    required_tags: List[TargetTags] = field(default_factory=list)
    effects: Dict = field(default_factory=list)


@dataclass()
class SkillTreeData:
    """
    Data class for a skill tree
    """
    name: str
    skill: Dict = field(default_factory=dict)