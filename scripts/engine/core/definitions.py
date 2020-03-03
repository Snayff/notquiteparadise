from __future__ import annotations

import pygame  # type: ignore
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional
from scripts.engine.core.constants import PrimaryStatType, TargetTagType, EffectTypeType, DamageTypeType, \
    AfflictionCategoryType, AfflictionTriggerType, SkillShapeType, SkillTerrainCollisionType, SkillTravelType, \
    SkillExpiryType, DirectionType, SecondaryStatType
from scripts.engine.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    pass


@register_dataclass_with_json
@dataclass
class BaseStatData:
    """
    Data class to contain primary and secondary stats
    """
    primary: Dict = field(default_factory=dict)
    secondary: Dict = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class BasePrimaryStatData:
    """
    Data class for primary  stats
    """
    name: str = "None"
    primary_stat_type: Optional[PrimaryStatType] = None
    base_value: int = 0


@register_dataclass_with_json
@dataclass
class BaseSecondaryStatData:
    """
    Data class for secondary stats
    """
    name: str = "None"
    secondary_stat_type: Optional[SecondaryStatType] = None
    base_value: int = 0
    vigour_mod: int = 0
    clout_mod: int = 0
    skullduggery_mod: int = 0
    bustle_mod: int = 0
    exactitude_mod: int = 0


@register_dataclass_with_json
@dataclass
class CharacteristicSpritesData:
    """
    Possible sprites for a characteristic
    """
    icon: Optional[pygame.Surface] = None
    idle: Optional[pygame.Surface] = None
    attack: Optional[pygame.Surface] = None
    hit: Optional[pygame.Surface] = None
    dead: Optional[pygame.Surface] = None
    move: Optional[pygame.Surface] = None


@register_dataclass_with_json
@dataclass
class CharacteristicSpritePathsData:
    """
    Possible sprites paths for a characteristic
    """
    icon: str = "none"
    idle: str = "none"
    attack: str = "none"
    hit: str = "none"
    dead: str = "none"
    move: str = "none"


@register_dataclass_with_json
@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """
    # how do we know it?
    name: str = "None"
    description: str = "None"
    icon: str = "None"

    # what does it cost?
    resource_type: str = "None"
    resource_cost: int = 0
    time_cost: int = 0
    cooldown: int = 0

    # how does it travel from the user?
    target_directions: List[DirectionType] = field(default_factory=list)
    range: int = 1
    terrain_collision: Optional[SkillTerrainCollisionType] = None
    travel_type: Optional[SkillTravelType] = None

    # when does it interact?
    expiry_type: Optional[SkillExpiryType] = None
    required_tags: List[TargetTagType] = field(default_factory=list)

    # how does it interact?
    shape: Optional[SkillShapeType] = None
    shape_size: int = 1
    effects: Dict = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class InterventionData:
    """
    Data class for a god's intervention
    """
    skill_key: str = "None"
    required_opinion: int = 0


@register_dataclass_with_json
@dataclass
class InteractionData:
    """
    Data class for an interaction
    """
    cause: str = "None"
    change_to: str = "None"


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


@register_dataclass_with_json
@dataclass
class EffectData:
    """
    Data class for a skill effect
    """
    effect_type: Optional[EffectTypeType] = None
    required_tags: List[TargetTagType] = field(default_factory=list)
    damage: int = 0
    affect_stat_amount: int = 0
    mod_stat: Optional[PrimaryStatType] = None
    mod_amount: int = 0
    damage_type: Optional[DamageTypeType] = None
    accuracy: int = 0
    stat_to_target: Optional[PrimaryStatType] = None
    aspect_name: str = "None"
    affliction_name: str = "None"
    duration: int = 0
    stat_to_affect: Optional[PrimaryStatType] = None


@register_dataclass_with_json
@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=dict)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)


@register_dataclass_with_json
@dataclass
class AspectData:
    """
    Data class for an aspects
    """
    name: str = "None"
    description: str = "None"
    duration: Optional[int] = None
    sprite: str = "None"
    blocks_sight: bool = False
    blocks_movement: bool = False
    effects: Dict = field(default_factory=list)
    interactions: List[InteractionData] = field(default_factory=list)  # TODO - convert to dict


@register_dataclass_with_json
@dataclass
class AttitudeData:
    """
    Data class for  a god's attitude
    """
    action: str = "None"
    opinion_change: int = 0


@register_dataclass_with_json
@dataclass()
class AfflictionData:
    """
    Data class for an Affliction
    """
    name: str = "None"
    description: str = "None"
    icon: str = "None"
    trigger_event: Optional[AfflictionTriggerType] = None
    category: Optional[AfflictionCategoryType] = None
    effects: Dict = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class IntentsData:
    """
    Hold the input intents
    """
    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False
    up_right: bool = False
    up_left: bool = False
    down_right: bool = False
    down_left: bool = False
    confirm: bool = False
    cancel: bool = False
    exit_game: bool = False
    skill0: bool = False
    skill1: bool = False
    skill2: bool = False
    skill3: bool = False
    skill4: bool = False
    skill5: bool = False
    refresh_data: bool = False
    button_pressed: bool = False
    debug_toggle: bool = False
    dev_toggle: bool = False