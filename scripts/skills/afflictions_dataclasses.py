from dataclasses import dataclass, field
from typing import Dict

from scripts.core.constants import AfflictionTriggers, AfflictionCategory


@dataclass()
class AfflictionData:
    """
    Data class for a skill
    """
    name: str
    description: str
    icon: str
    trigger_event: AfflictionTriggers
    category: AfflictionCategory
    effects: Dict = field(default_factory=list)