from __future__ import annotations
from dataclasses import dataclass


@dataclass
class InteractionData:
    """
    Data class for an interaction
    """
    cause: str = "None"
    change_to: str = "None"