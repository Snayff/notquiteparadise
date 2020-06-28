from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Iterator, TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import world
from scripts.engine.component import Position
from scripts.engine.core.constants import BASE_ACCURACY, BASE_DAMAGE, BASE_MOVE_COST, DamageType, Direction, \
    DirectionType, PrimaryStat, ProjectileExpiry, ProjectileExpiryType, ProjectileSpeed, \
    ProjectileSpeedType, Resource, ResourceType, Shape, ShapeType, TargetTag, TargetTagType, \
    TargetingMethod, TargetingMethodType, TerrainCollision, TerrainCollisionType, TravelMethod, TravelMethodType
from scripts.engine.effect import DamageEffect, Effect, MoveActorEffect
from scripts.engine.library import library
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Optional, Tuple, List


class Skill(ABC):
    """
    A subclass of Skill represents a skill and holds all the data that is
    not dependent on the individual cast - stuff like shape, base accuracy, etc.

    An instance of Skill represents an individual use of that skill,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass
    name: str = ""
    description: str = ""
    icon_path: str = ""
    resource_type: ResourceType = Resource.STAMINA
    resource_cost: int = 0
    time_cost: int = 0
    base_cooldown: int = 0
    targeting_method: TargetingMethodType = TargetingMethod.TARGET
    target_directions: List[DirectionType] = []
    shape: ShapeType = Shape.TARGET
    shape_size: int = 1
    required_tags: List[TargetTagType] = [TargetTag.OTHER_ENTITY]
    uses_projectile: bool = False
    projectile_speed: ProjectileSpeedType = ProjectileSpeed.SLOW
    travel_method: TravelMethodType = TravelMethod.STANDARD
    range: int = 1
    terrain_collision: TerrainCollisionType = TerrainCollision.FIZZLE
    expiry_type: ProjectileExpiryType = ProjectileExpiry.FIZZLE

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction

    def use(self):
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        logging.debug(f"'{world.get_name(self.user)}' used '{self.name}'.")
        if self.uses_projectile:
            from scripts.engine.core.definitions import ProjectileData
            projectile_data = ProjectileData(
                creator=self.user,
                skill_name=self.name,
                skill_instance=self,
                required_tags=self.required_tags,
                direction=self.direction,
                speed=self.projectile_speed,
                travel_method=self.travel_method,
                range=self.range,
                terrain_collision=self.terrain_collision,
                expiry_type=self.expiry_type
            )
            world.create_projectile(self.user, self.target_tile.x, self.target_tile.y, projectile_data)
        else:
            world.apply_skill(self)

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        entity_names = []

        for entity in world.get_affected_entities((self.target_tile.x, self.target_tile.y), self.shape,
                                                  self.shape_size):
            yield entity, self.build_effects(entity)
            entity_names.append(world.get_name(entity))

        logging.debug(f"'{world.get_name(self.user)}' applied '{self.name}' to {entity_names}.")

    @abstractmethod
    def build_effects(self, entity):
        """
        Build the effects of this skill applying to a single entity. Must be overridden by subclass.
        """
        pass


class Move(Skill):
    """
    Basic move for an entity.
    """
    # Move's definitions are not defined in the json. They are set here and only here.
    name = "move"
    required_tags = [TargetTag.SELF]
    description = "this is the normal movement."
    icon_path = ""
    resource_type = Resource.STAMINA
    resource_cost = 0
    time_cost = BASE_MOVE_COST
    base_cooldown = 0
    targeting_method = TargetingMethod.TARGET
    target_directions = [
        Direction.UP_LEFT,
        Direction.UP,
        Direction.UP_RIGHT,
        Direction.LEFT,
        Direction.CENTRE,
        Direction.RIGHT,
        Direction.DOWN_LEFT,
        Direction.DOWN,
        Direction.DOWN_RIGHT
    ]
    shape = Shape.TARGET
    shape_size = 1
    uses_projectile = False

    def __init__(self, user: EntityID, target_tile: Tile, direction):
        """
        Only Move needs an init as it overrides the target tile
        """
        # override target
        position = world.get_entitys_component(user, Position)
        tile = world.get_tile((position.x, position.y))

        super().__init__(user, tile, direction)

    def build_effects(self, entity: EntityID) -> List[MoveActorEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """

        move_effect = MoveActorEffect(
            origin=self.user,
            target=entity,
            success_effects=[],
            failure_effects=[],
            direction=self.direction,
            move_amount=1
        )

        return [move_effect]


class BasicAttack(Skill):
    data = library.get_skill_data("basic_attack")
    name = data.name
    required_tags = data.required_tags
    description = data.description
    icon_path = data.icon
    resource_type = data.resource_type
    resource_cost = data.resource_cost
    time_cost = data.time_cost
    base_cooldown = data.cooldown
    targeting_method = data.targeting_method
    target_directions = data.target_directions
    shape = data.shape
    shape_size = data.shape_size
    uses_projectile = data.uses_projectile
    projectile_speed = getattr(ProjectileSpeed, data.projectile_speed.upper())
    travel_method = data.travel_method
    range = data.range
    terrain_collision = data.terrain_collision
    expiry_type = data.expiry_type

    def build_effects(self, entity: EntityID) -> List[DamageEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """
        # TODO - externalise effect data to allow specifying in json
        damage_effect = DamageEffect(
            origin=self.user,
            success_effects=[],
            failure_effects=[],
            target=entity,
            stat_to_target=PrimaryStat.VIGOUR,
            accuracy=BASE_ACCURACY,
            damage=BASE_DAMAGE,
            damage_type=DamageType.MUNDANE,
            mod_stat=PrimaryStat.CLOUT,
            mod_amount=0.1
        )

        return [damage_effect]
