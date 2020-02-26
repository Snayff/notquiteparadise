from __future__ import annotations

from dataclasses import dataclass
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass
class AttitudeData:
    """
    Data class for  a god's attitude
    """
    action: str = "None"
    opinion_change: int = 0