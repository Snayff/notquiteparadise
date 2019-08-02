
from dataclasses import dataclass


@dataclass()
class RaceData:
    """
    Data class for an aspect
    """
    name: str = "None"
    description: str = "None"
    sprite: str = "None"
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
