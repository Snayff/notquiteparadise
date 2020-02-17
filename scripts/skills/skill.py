from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict
from scripts.core.constants import SkillExpiryTypes, Directions, SkillTravelTypes, TargetTags, \
    SkillTerrainCollisions, SkillShapes


@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """
    # how do we know it?
    name: str = "None"
    description: str = "None"
    icon: str = "None"

    # what does it cost?
    resource_type: str = "None"
    resource_cost: int = 0
    time_cost: int = 0
    cooldown: int = 0

    # how does it travel from the user?
    target_directions: List[Directions] = field(default_factory=list)
    range: int = 1
    terrain_collision: SkillTerrainCollisions = None
    travel_type: SkillTravelTypes = None

    # when does it interact?
    expiry_type: SkillExpiryTypes = None
    required_tags: List[TargetTags] = field(default_factory=list)

    # how does it interact?
    shape: SkillShapes = None
    shape_size: int = 1
    effects: Dict = field(default_factory=dict)