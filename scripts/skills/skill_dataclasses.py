
from dataclasses import dataclass, field
from typing import List, Dict
from scripts.core.constants import TargetTags, SkillShapes


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
    effects: Dict = field(default_factory=dict)


@dataclass()
class SkillTreeData:
    """
    Data class for a skill tree
    """
    name: str
    skill: Dict = field(default_factory=dict)