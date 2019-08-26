
from dataclasses import dataclass


@dataclass()
class AttitudeData:
    """
    Data class for  a god's attitude
    """
    action: str = "None"
    opinion_change: int = 0