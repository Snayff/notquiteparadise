from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

import pygame
from snecs.typedefs import EntityID

from scripts.engine.core.constants import AfflictionCategoryType, DamageTypeType, Direction, DirectionType, \
    EffectType, \
    EffectTypeType, PrimaryStatType, ProjectileExpiry, ProjectileExpiryType, ProjectileSpeed, ProjectileSpeedType, \
    Resource, ResourceType, SecondaryStatType, Shape, ShapeType, TargetTag, TargetTagType, TargetingMethod, \
    TargetingMethodType, TerrainCollision, TerrainCollisionType, TravelMethod, TravelMethodType
from scripts.engine.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    from scripts.nqp.actions.skills import Skill


######################### SKILLS ##################################

@register_dataclass_with_json
@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """
    # TODO - rename relevant sections to indicate they are base values
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


####################### EFFECTS ######################################

@register_dataclass_with_json
@dataclass
class EffectData(ABC):
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
    icon: str = field(default="none")
    idle: str = field(default="none")
    attack: str = field(default="none")
    hit: str = field(default="none")
    dead: str = field(default="none")
    move: str = field(default="none")


@register_dataclass_with_json
@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = field(default="none")
    description: str = field(default="none")
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=CharacteristicSpritePathsData)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)
    permanent_afflictions: List[str] = field(default_factory=list)