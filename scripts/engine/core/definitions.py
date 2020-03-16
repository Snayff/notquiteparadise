from __future__ import annotations

from abc import ABC

import pygame
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional, Union
from scripts.engine.core.constants import PrimaryStatType, TargetTagType, EffectType, DamageTypeType, \
    AfflictionCategoryType, InteractionCauseType, ShapeType, TerrainCollisionType, TravelMethodType, \
    ProjectileExpiryType, DirectionType, SecondaryStatType, ProjectileSpeedType, ProjectileSpeed, Effect
from scripts.engine.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    pass


######################### SKILLS ##################################

@register_dataclass_with_json
@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """
    # how do we know it?
    name: str = field(default="None")
    description: str = field(default="None")
    icon: str = field(default="None")

    # what does it cost?
    resource_type: Optional[SecondaryStatType] = None
    resource_cost: int = 0
    time_cost: int = 0
    cooldown: int = 0

    # how does it travel from the user?
    target_directions: List[DirectionType] = field(default_factory=list)
    projectile: ProjectileData = field(default_factory=dict)

    # how does it interact?
    interactions: Dict[InteractionCauseType, InteractionData] = field(default_factory=dict)


@register_dataclass_with_json
@dataclass
class ProjectileData:
    """
    Data class for a projectile
    """
    # what created it?
    skill_name: str = field(default="None")

    # what does it look like?
    sprite: str = field(default="None")

    # how does it travel?
    direction: Optional[DirectionType] = None
    speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    travel_type: Optional[TravelMethodType] = None
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
    effect_type: Optional[EffectType] = None

    # who are we targeting?
    required_tags: List[TargetTagType] = field(default_factory=list)

    # how are we targeting?
    stat_to_target: Optional[PrimaryStatType] = None
    accuracy: int = 0

    # what is the area of effect?
    shape: Optional[ShapeType] = None
    shape_size: int = 1


@register_dataclass_with_json
@dataclass
class ApplyAfflictionEffectData(EffectData):
    """
    Data for the Apply Affliction effect.
    """
    effect_type = Effect.APPLY_AFFLICTION

    duration: int = 0
    affliction_name: str = field(default="None")


@register_dataclass_with_json
@dataclass
class DamageEffectData(EffectData):
    """
    Data for the Damage effect.
    """
    effect_type = Effect.DAMAGE

    damage: int = 0
    damage_type: Optional[DamageTypeType] = None
    mod_stat: Optional[PrimaryStatType] = None
    mod_amount: int = 0


@register_dataclass_with_json
@dataclass
class AffectStatEffectData(EffectData):
    """
    Data for the Affect Stat effect.
    """
    effect_type = Effect.AFFECT_STAT

    stat_to_affect: Optional[PrimaryStatType] = None
    affect_stat_amount: int = 0


@register_dataclass_with_json
@dataclass
class AddAspectEffectData(EffectData):
    """
    Data for the Add Aspect effect.
    """
    effect_type = Effect.ADD_ASPECT

    aspect_name: str = field(default="None")


@register_dataclass_with_json
@dataclass
class RemoveAspectEffectData(EffectData):
    """
    Data for the Remove Aspect effect.
    """
    effect_type = Effect.REMOVE_ASPECT

    aspect_name: str = field(default="None")


@register_dataclass_with_json
@dataclass
class TriggerSkillEffectData(EffectData):
    """
    Data for the  Trigger Skill effect.
    """
    effect_type = Effect.TRIGGER_SKILL

    skill_name: str = field(default="None")


##################### ACTORS #################################

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
    name: str = field(default="None")
    primary_stat_type: Optional[PrimaryStatType] = None
    base_value: int = 0


@register_dataclass_with_json
@dataclass
class BaseSecondaryStatData:
    """
    Data class for secondary stats
    """
    name: str = field(default="None")
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
    icon: str = field(default="None")
    idle: str = field(default="None")
    attack: str = field(default="None")
    hit: str = field(default="None")
    dead: str = field(default="None")
    move: str = field(default="None")


@register_dataclass_with_json
@dataclass
class InteractionData:
    """
    Data class for an interaction
    """
    cause: Optional[InteractionCauseType] = None
    apply_affliction: Optional[ApplyAfflictionEffectData] = None
    damage: Optional[DamageEffectData] = None
    affect_stat: Optional[AffectStatEffectData] = None
    add_aspect: Optional[AddAspectEffectData] = None
    remove_aspect: Optional[RemoveAspectEffectData] = None
    trigger_skill: Optional[TriggerSkillEffectData] = None


@register_dataclass_with_json
@dataclass
class CharacteristicData:
    """
    Data class for an aspects
    """
    name: str = field(default="None")
    description: str = field(default="None")
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=CharacteristicSpritePathsData)
    sight_range: int = 0
    vigour: int = 0
    clout: int = 0
    skullduggery: int = 0
    bustle: int = 0
    exactitude: int = 0
    known_skills: List[str] = field(default_factory=list)


@register_dataclass_with_json
@dataclass()
class AfflictionData:
    """
    Data class for an Affliction
    """
    name: str = field(default="None")
    description: str = field(default="None")
    icon: str = field(default="None")
    category: Optional[AfflictionCategoryType] = None
    interactions: Dict[InteractionCauseType, InteractionData] = field(default_factory=dict)


########################## WORLD #########################################

@register_dataclass_with_json
@dataclass
class AspectData:
    """
    Data class for an aspects
    """
    name: str = field(default="None")
    description: str = field(default="None")
    duration: int = 0
    sprite: str = field(default="None")
    blocks_sight: bool = False
    blocks_movement: bool = False
    interactions: Dict[InteractionCauseType, InteractionData] = field(default_factory=dict)


#################### GODS ###################################################


@register_dataclass_with_json
@dataclass
class AttitudeData:
    """
    Data class for  a god's attitude
    """
    action: str = field(default="None")
    opinion_change: int = 0


@register_dataclass_with_json
@dataclass
class InterventionData:
    """
    Data class for a god's intervention
    """
    skill_key: str = field(default="None")
    required_opinion: int = 0


@register_dataclass_with_json
@dataclass
class GodData:
    """
    Data class for a god
    """
    name: str = field(default="None")
    description: str = field(default="None")
    sprite_paths: CharacteristicSpritePathsData = field(default_factory=CharacteristicSpritePathsData)
    attitudes: Dict[int, AttitudeData] = field(default_factory=dict)
    interventions: Dict[int, InterventionData] = field(default_factory=dict)

######################### VALIDATORS ####################################
#
# def _validate_effect_type(s):
#     if s is not None and not hasattr(Effect, s):
#         raise ValidationError(f"{s} is not a valid effect type")
