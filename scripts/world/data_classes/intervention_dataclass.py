
from dataclasses import dataclass


@dataclass()
class InterventionData:
    """
    Data class for a god's intervention
    """
    name: str = "None"
    required_opinion: int = 0