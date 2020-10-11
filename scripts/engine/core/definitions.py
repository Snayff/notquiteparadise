from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, cast

import pygame
from snecs.typedefs import EntityID

from scripts.engine.core.constants import (
    AfflictionCategory,
    AfflictionCategoryType,
    AfflictionTriggerType,
    Direction,
    DirectionType,
    EffectType,
    EffectTypeType,
    PrimaryStatType,
    ProjectileExpiry,
    ProjectileExpiryType,
    ProjectileSpeed,
    ProjectileSpeedType,
    RenderLayer,
    RenderLayerType,
    Resource,
    ResourceType,
    SecondaryStatType,
    Shape,
    ShapeType,
    TargetingMethod,
    TargetingMethodType,
    TargetTagType,
    TerrainCollision,
    TerrainCollisionType,
    TraitGroup,
    TraitGroupType,
    TravelMethod,
    TravelMethodType,
)
from scripts.engine.core.extend_json import register_dataclass_with_json

if TYPE_CHECKING:
    from scripts.engine.action import Skill


######################### Aesthetics ##################################


@register_dataclass_with_json
@dataclass
class TraitSpritesData:
    """
    Possible sprites.
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

    render_order: RenderLayerType = field(default=RenderLayer.BOTTOM)
    icon: str = field(default="none")
    idle: str = field(default="none")
    attack: str = field(default="none")
    hit: str = field(default="none")
    dead: str = field(default="none")
    move: str = field(default="none")


##################### ACTORS #################################


@register_dataclass_with_json
@dataclass
class ActorData:
    """
    Data class for an actor
    """

    key: str = "none"
    possible_names: List[str] = field(default_factory=list)
    description: str = "none"
    position_offsets: List[Tuple[int, int]] = field(default_factory=list)
    trait_names: List[str] = field(default_factory=list)
    behaviour_name: str = "none"


@register_dataclass_with_json
@dataclass
class TraitData:
    """
    Data class for a trait.
    """

    name: str = "none"
    group: TraitGroupType = TraitGroup.NPC
    description: str = "none"
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
        # FIXME - this should be handled prior to coming to the dataclass
        trait_render_order = {"npc": 0, "people": 1, "homeland": 2, "savvy": 3}
        self.sprite_paths.render_order = trait_render_order.get(self.group)


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


####################### NON-ACTOR ENTITIES ######################


@register_dataclass_with_json
@dataclass
class ProjectileData:
    """
    Data class for a projectile
    """

    # what created it?
    creator: EntityID = cast(EntityID, 0)  # this will be overwritten or will break, but need defaults to allow passing
    skill_name: str = "none"
    skill_instance: Optional[Skill] = None
    name: str = "none"
    description: str = "none"

    # who are we targeting?
    target_tags: List[TargetTagType] = field(default_factory=list)

    # where are we going?
    direction: Optional[DirectionType] = None

    # what does it look like?
    sprite_paths: TraitSpritePathsData = field(default_factory=TraitSpritePathsData)

    # how does it travel?
    speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    travel_method: TravelMethodType = TravelMethod.STANDARD
    range: int = 1

    # how does it interact?
    terrain_collision: Optional[TerrainCollisionType] = None
    expiry_type: Optional[ProjectileExpiryType] = None

    def __post_init__(self):
        self.speed = getattr(ProjectileSpeed, self.speed.upper())


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
    attitudes: Dict[str, AttitudeData] = field(default_factory=dict)
    interventions: Dict[str, InterventionData] = field(default_factory=dict)


####################### WORLD ######################


@register_dataclass_with_json
@dataclass
class MapData:
    """
    Data class for a Map, specifically for generation. A map is a collection of rooms. Defines the rooms on
    the map, how they are placed and joined up (tunnels).
    """

    name: str = "none"
    key: str = "none"

    # map size
    width: int = 0
    height: int = 0

    # map gen rules
    min_rooms: int = 0
    max_rooms: int = 0
    max_tunnel_length: int = 0
    min_path_distance_for_shortcut: int = 0
    max_room_entrances: int = 0
    extra_entrance_chance: int = 0
    chance_of_tunnel_winding: int = 0

    rooms: Dict[str, float] = field(default_factory=dict)  # room name, room weight

    # aesthetics
    sprite_paths: Dict[str, str] = field(default_factory=dict)  # sprite name, sprite path


@register_dataclass_with_json
@dataclass
class RoomConceptData:
    """
    Data class for a RoomConcept. Only used in generation.
    """

    name: str = "none"
    key: str = "none"

    # sizes
    min_width: int = 0
    min_height: int = 0
    max_width: int = 0
    max_height: int = 0

    # room parameters
    design: str = ""
    max_neighbouring_walls_in_room: int = 0
    chance_of_spawning_wall: float = 0.0

    # actor generation
    actors: Dict[str, float] = field(default_factory=dict)  # actor name, actor weight
    min_actors: int = 0
    max_actors: int = 0

    # aesthetics
    sprite_paths: Dict[str, str] = field(default_factory=dict)  # sprite name, sprite path


######################### ACTIONS ##################################


@register_dataclass_with_json
@dataclass
class SkillData:
    """
    Data class for a skill. Used by the library to load from json.
    """

    # how do we know it?
    name: str = "none"
    description: str = "none"
    icon_path: str = "none"

    # when do we use it?
    target_tags: List[TargetTagType] = field(default_factory=list)

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
    projectile_data: Optional[ProjectileData] = None

    def __post_init__(self):
        # convert directions to their constant values
        _mapped_directions = []

        for _direction in self.target_directions:
            _mapped_directions.append(getattr(Direction, _direction.upper()))

        self.target_directions = _mapped_directions


@register_dataclass_with_json
@dataclass()
class AfflictionData:
    """
    Data class for an Afflictions
    """

    name: str = "none"
    description: str = "none"
    icon_path: str = "none"
    category: AfflictionCategoryType = AfflictionCategory.BANE
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1
    target_tags: List[TargetTagType] = field(default_factory=list)
    identity_tags: List[EffectTypeType] = field(default_factory=list)
    triggers: List[AfflictionTriggerType] = field(default_factory=list)


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
    target_tags: List[TargetTagType] = field(default_factory=list)

    # how are we targeting?
    stat_to_target: Optional[PrimaryStatType] = None
    accuracy: int = 0

    # what is the area of effect?
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1

    # what next?
    success_effects: List[EffectData] = field(default_factory=list)
    fail_effects: List[EffectData] = field(default_factory=list)


################### CONFIG ###################################################


@register_dataclass_with_json
@dataclass
class Dimensions:
    height: int
    width: int


@register_dataclass_with_json
@dataclass
class VideoConfigData:
    base_window: Dimensions
    desired_window: Dimensions
    fps_limit: int


@register_dataclass_with_json
@dataclass
class HitInfoData:
    value: int
    modifier: float


@register_dataclass_with_json
@dataclass
class HitTypeData:
    graze: HitInfoData
    hit: HitInfoData
    crit: HitInfoData


@register_dataclass_with_json
@dataclass
class BaseValueData:
    move_cost: int
    accuracy: int
    damage: int


@register_dataclass_with_json
@dataclass
class DefaultValueData:
    time_per_round: int
    entity_blocks_sight: bool
    reduced_effectiveness_multi_tile_modifier: float


@register_dataclass_with_json
@dataclass
class GameConfigData:
    hit_types: HitTypeData
    base_values: BaseValueData
    default_values: DefaultValueData
