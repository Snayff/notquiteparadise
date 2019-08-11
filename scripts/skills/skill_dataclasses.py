from dataclasses import dataclass, field
from typing import List, Dict

from scripts.core.constants import EffectTypes, TargetTags, DamageTypes, PrimaryStatTypes, SkillShapes


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
    affliction_name: str = "None"
    duration: int = 0
    stat_to_affect: PrimaryStatTypes = None


@dataclass()
class SkillData:
    """
    Data class for a skill
    """
    name: str = "None"
    description: str = "None"
    icon: str = "None"
    range: int = 1
    shape: SkillShapes = None
    shape_size: int = 1
    resource_type: str = "None"
    resource_cost: int = 0
    time_cost: int = 0
    cooldown: int = 0
    required_tags: List[TargetTags] = field(default_factory=list)
    effects: Dict = field(default_factory=list)


@dataclass()
class SkillTreeData:
    """
    Data class for a skill tree
    """
    name: str
    skill: Dict = field(default_factory=dict)