from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

from scripts.core.constants import AfflictionTriggers, AfflictionCategory
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass()
class AfflictionData:
    """
    Data class for an Affliction
    """
    name: str = "None"
    description: str = "None"
    icon: str = "None"
    trigger_event: AfflictionTriggers = None
    category: AfflictionCategory = None
    effects: Dict = field(default_factory=dict)