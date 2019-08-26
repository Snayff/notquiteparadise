
from dataclasses import dataclass, field
from typing import List

from scripts.world.attitude_dataclass import AttitudeData
from scripts.world.intervention_dataclass import InterventionData


@dataclass()
class GodData:
    """
    Data class for a god
    """
    name: str = "None"
    description: str = "None"
    sprite: str = "None"
    attitudes: List[AttitudeData] = field(default_factory=list)
    interventions: List[InterventionData] = field(default_factory=list)