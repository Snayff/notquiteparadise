from __future__ import annotations

from dataclasses import dataclass
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass
class InterventionData:
    """
    Data class for a god's intervention
    """
    skill_key: str = "None"
    required_opinion: int = 0