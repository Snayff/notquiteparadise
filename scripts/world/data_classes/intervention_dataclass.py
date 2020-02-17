from __future__ import annotations
from dataclasses import dataclass


@dataclass
class InterventionData:
    """
    Data class for a god's intervention
    """
    skill_key: str = "None"
    required_opinion: int = 0