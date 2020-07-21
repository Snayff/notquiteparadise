from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional

import pygame
from snecs.typedefs import EntityID

from scripts.engine.core.constants import (TRAIT_RENDER_ORDER,
                                           AfflictionCategoryType,
                                           AfflictionTriggerType,
                                           DamageTypeType, Direction,
                                           DirectionType, EffectType,
                                           EffectTypeType, PrimaryStatType,
                                           ProjectileExpiry,
                                           ProjectileExpiryType,
                                           ProjectileSpeed,
                                           ProjectileSpeedType, Resource,
                                           ResourceType, SecondaryStatType,
                                           Shape, ShapeType, TargetingMethod,
                                           TargetingMethodType, TargetTag,
                                           TargetTagType, TerrainCollision,
                                           TerrainCollisionType, TraitGroup,
                                           TravelMethod, TravelMethodType)
from scripts.engine.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    from scripts.nqp.actions.skills import Skill


######################### ACTIONS ##################################

@register_dataclass_with_json
@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """
    # how do we know it?
    name: str = field(default="none")
    description: str = field(default="none")
    icon: str = field(default="none")
    class_name: str = ""

    # when do we use it?
    required_tags: List[TargetTagType] = field(default_factory=list)

    # what does it cost?
    resource_type: ResourceType = Resource.STAMINA
    resource_cost: int = 0
    time_cost: int = 0
    cooldown: int = 0

    # how does it travel from the user?
    targeting_method: TargetingMethodType = TargetingMethod.TARGET
    target_directions: List[DirectionType] = field(default_factory=list)

    # what is the area of effect?
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1

    # projectile info
    uses_projectile: bool = True
    projectile_speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    travel_method: TravelMethodType = TravelMethod.STANDARD
    range: int = 1
    terrain_collision: TerrainCollisionType = TerrainCollision.FIZZLE
    expiry_type: ProjectileExpiryType = ProjectileExpiry.FIZZLE
    projectile_sprite: str = field(default="none")


@register_dataclass_with_json
@dataclass
class ProjectileData:
    """
    Data class for a projectile
    """
    # what created it?
    creator: EntityID
    skill_name: str = field(default="none")
    skill_instance: Skill = False
    name: str = ""
    description: str = ""

    # what does it look like?
    sprite: str = field(default="none")

    # who are we targeting?
    required_tags: List[TargetTagType] = field(default_factory=list)

    # how does it travel?
    direction: Optional[DirectionType] = None
    speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    travel_method: Optional[TravelMethodType] = None
    range: int = 1

    # how does it interact?
    terrain_collision: Optional[TerrainCollisionType] = None
    expiry_type: Optional[ProjectileExpiryType] = None


@register_dataclass_with_json
@dataclass()
class AfflictionData:
    """
    Data class for an Afflictions
    """
    name: str = field(default="none")
    class_name: str = field(default="none")
    description: str = field(default="none")
    icon: str = field(default="none")
    category: Optional[AfflictionCategoryType] = None
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1
    required_tags: List[TargetTagType] = field(default_factory=list(TargetTag.OTHER_ENTITY))
    identity_tags: List[EffectTypeType] = field(default_factory=list(EffectType.DAMAGE))
    triggers: List[AfflictionTriggerType] = field(default_factory=list())


@register_dataclass_with_json
@dataclass
class EffectData:
    """
    Base data class for an effect.
    """
    # who am I?
    originator: Optional[EntityID] = None  # actor
    creators_name: Optional[str] = None  # skill, projectile, etc.'s name
    effect_type = EffectType.MOVE

    # who are we targeting?
    required_tags: List[TargetTagType] = field(default_factory=list)

    # how are we targeting?
    stat_to_target: Optional[PrimaryStatType] = None
    accuracy: int = 0

    # what is the area of effect?
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1

    # what next?
    success_effects: List[Optional[EffectData]] = field(default_factory=list)
    fail_effects: List[Optional[EffectData]] = field(default_factory=list)


##################### ACTORS #################################

@register_dataclass_with_json
@dataclass
class TraitSpritesData:
    """
    Possible sprites for a trait
    """
    icon: Optional[pygame.Surface] = None
    idle: Optional[pygame.Surface] = None
    attack: Optional[pygame.Surface] = None
    hit: Optional[pygame.Surface] = None
    dead: Optional[pygame.Surface] = None
    move: Optional[pygame.Surface] = None


@register_dataclass_with_json
@dataclass
class TraitSpritePathsData:
    """
    Possible sprites paths for a trait
    """
    render_order: int = field(default=0)
    icon: str = field(default="none")
    idle: str = field(default="none")
    attack: str = field(default="none")
    hit: str = field(default="none")
    dead: str = field(default="none")
    move: str = field(default="none")


@register_dataclass_with_json
@dataclass
class TraitData:
    """
    Data class for an aspects
    """
    name: str = field(default="none")
    group: TraitGroup = field(default="none")
    behaviour_name: str = field(default="none")
    description: str = field(default="none")
    sprite_paths: TraitSpritePathsData = field(default_factory=TraitSpritePathsData)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)
    permanent_afflictions: List[str] = field(default_factory=list)

    def __post_init__(self):
        # update sprite path render order
        self.sprite_paths.render_order = TRAIT_RENDER_ORDER.get(self.group)


@register_dataclass_with_json
@dataclass
class BaseStatData:
    """
    Data class to contain primary and secondary stats
    """
    primary: Dict[str, BasePrimaryStatData] = field(default_factory=dict)
    secondary: Dict[str, BaseSecondaryStatData] = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class BasePrimaryStatData:
    """
    Data class for primary  stats
    """
    name: str = field(default="none")
    primary_stat_type: Optional[PrimaryStatType] = None
    base_value: int = 0


@register_dataclass_with_json
@dataclass
class BaseSecondaryStatData:
    """
    Data class for secondary stats
    """
    name: str = field(default="none")
    secondary_stat_type: Optional[SecondaryStatType] = None
    base_value: int = 0
    vigour_mod: int = 0
    clout_mod: int = 0
    skullduggery_mod: int = 0
    bustle_mod: int = 0
    exactitude_mod: int = 0


####################### WORLD ######################

@register_dataclass_with_json
@dataclass
class AspectData:
    """
    Data class for an aspects
    """
    name: str = field(default="none")
    description: str = field(default="none")
    duration: int = 0
    sprite: str = field(default="none")
    blocks_sight: bool = False
    blocks_movement: bool = False


################### GODS ###################################################

@register_dataclass_with_json
@dataclass
class AttitudeData:
    """
    Data class for  a god's attitude
    """
    action: str = field(default="none")
    opinion_change: int = 0


@register_dataclass_with_json
@dataclass
class InterventionData:
    """
    Data class for a god's intervention
    """
    skill_key: str = field(default="none")
    required_opinion: int = 0


@register_dataclass_with_json
@dataclass
class GodData:
    """
    Data class for a god
    """
    name: str = field(default="none")
    description: str = field(default="none")
    attitudes: Dict[int, AttitudeData] = field(default_factory=dict)
    interventions: Dict[int, InterventionData] = field(default_factory=dict)
