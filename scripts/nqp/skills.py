from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type
from snecs.typedefs import EntityID
from scripts.engine import utility, world
from scripts.engine.component import Position, Resources, HasCombatStats
from scripts.engine.core.constants import ResourceType, Resource, TargetingMethodType, TargetingMethod, DirectionType, \
    Shape, ShapeType, TargetTagType, TargetTag, Direction, Effect, PrimaryStat, BASE_ACCURACY, BASE_DAMAGE, DamageType, \
    BASE_MOVE_COST
from scripts.engine.effect import DamageEffect, MoveActorEffect
from scripts.engine.library import library
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class Skill(ABC):
    """
    A subclass of Skill represents a skill and holds all the data that is
    not dependent on the individual cast - stuff like shape, base accuracy,
    etc etc.

    An instance of Skill represents an individual use of that skill,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass
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

    def __init__(self, user: EntityID, target_tile: Tile, direction: Optional[DirectionType] = None):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction

    def get_affected_entities(self):
        """
        Return a list of entities that this particular cast affects.
        """
        affected_entities = []
        affected_positions = []
        target_x = self.target_tile.x
        target_y = self.target_tile.y

        # get affected tiles
        coords = utility.get_coords_from_shape(self.shape, self.shape_size)
        for coord in coords:
            affected_positions.append((coord[0] + target_x, coord[1] + target_y))

        # get relevant entities in target area
        for entity, (position, *others) in world.get_components([Position, Resources, HasCombatStats]):
            if (position.x, position.y) in affected_positions:
                affected_entities.append(entity)

        return affected_entities

    def apply(self) -> Tuple[EntityID, List[Effect]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        for entity in self.get_affected_entities():
            yield entity, self.build_effects(entity)

    @abstractmethod
    def build_effects(self, entity):
        """
        Build the effects of this skill applying to a single entity.
        """
        pass


class Move(Skill):
    """
    Basic move for an entity.
    """
    # These are not defined in the json. They are set here and only here.
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

    def build_effects(self, entity) -> List[MoveActorEffect]:
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

    def build_effects(self, entity) -> List[DamageEffect]:
        """
        Build the effects of this skill applying to a single entity.
        """
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