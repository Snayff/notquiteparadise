from __future__ import annotations

from dataclasses import dataclass, field
from scripts.core.extend_json import register_dataclass_with_json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scripts.world.data_classes.attitude_dataclass import AttitudeData
    from typing import Dict
    from scripts.world.data_classes.intervention_dataclass import InterventionData
    from scripts.world.data_classes.sprites_dataclass import CharacteristicSpritePathsData


@register_dataclass_with_json
@dataclass
class GodData:
    """
    Data class for a god
    """
    name: str = "None"
    description: str = "None"
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=dict)
    attitudes: AttitudeData = field(default_factory=dict)
    interventions: InterventionData = field(default_factory=dict)