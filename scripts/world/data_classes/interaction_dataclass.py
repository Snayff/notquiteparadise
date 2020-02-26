from __future__ import annotations

from dataclasses import dataclass
from scripts.core.extend_json import register_dataclass_with_json


@register_dataclass_with_json
@dataclass
class InteractionData:
    """
    Data class for an interaction
    """
    cause: str = "None"
    change_to: str = "None"