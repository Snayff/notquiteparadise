from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass
class GodData:
    """
    Data class for a god
    """
    name: str = "None"
    description: str = "None"
    sprite: str = "None"
    attitudes: Dict = field(default_factory=dict)
    interventions: Dict = field(default_factory=dict)