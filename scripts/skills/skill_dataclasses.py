from dataclasses import dataclass, field
from typing import List, Dict

from scripts.core.constants import SkillEffectTypes, TargetTags, DamageTypes, PrimaryStatTypes, TargetTypes


@dataclass
class SkillEffectData:
    """
    Data class for a skill effect
    """
    effect_type: SkillEffectTypes
    required_tags: List[TargetTags] = field(default_factory=list)
    required_target_type: TargetTags = None
    damage: int = 0
    damage_type: DamageTypes = None
    accuracy: int = 0
    stat_to_target: PrimaryStatTypes = None
    new_terrain: TargetTags = None
    affliction_name: str = ""
    duration: int = 0


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
    required_target_type: TargetTypes
    required_tags: List[TargetTags] = field(default_factory=list)
    skill_effects: Dict = field(default_factory=list)


@dataclass()
class SkillTreeData:
    """
    Data class for a skill tree
    """
    name: str
    skill: Dict = field(default_factory=dict)