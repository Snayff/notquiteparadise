from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Dict, TYPE_CHECKING, Iterator, Type

from snecs.typedefs import EntityID

from scripts.engine.component import Aesthetic, Position
from scripts.engine.core.constants import (
    AfflictionCategoryType,
    AfflictionTriggerType,
    Direction,
    DirectionType,
    EffectTypeType,
    Resource,
    ResourceType,
    Shape,
    ShapeType,
    TargetingMethod,
    TargetingMethodType,
    TargetTag,
    TargetTagType,
)
from scripts.engine.core.definitions import ProjectileData
from scripts.engine.effect import Effect, MoveActorEffect
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Tuple, List

__all__ = ["Skill", "Affliction", "properties_set_by_data", "register_action", "skill_registry",
    "affliction_registry"]

skill_registry: Dict[str, Type[Skill]] = {}
affliction_registry: Dict[str, Type[Affliction]] = {}


class Skill(ABC):
    """
    A subclass of Skill represents a skill and holds all the data that is
    not dependent on the individual cast - stuff like shape, base accuracy, etc.

    An instance of Skill represents an individual use of that skill,
    and additionally holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass, including being set by external data
    key: str
    description: str
    icon_path: str
    resource_type: ResourceType
    resource_cost: int
    time_cost: int
    base_cooldown: int
    targeting_method: TargetingMethodType
    target_directions: List[DirectionType]
    shape: ShapeType
    shape_size: int
    required_tags: List[TargetTagType]
    uses_projectile: bool
    projectile_data: ProjectileData

    # vars needed to keep track of changes
    ignore_entities: List[int] = []

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction
        self.projectile = None

    def use(self):
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        from scripts.engine import world
        logging.debug(f"'{world.get_name(self.user)}' used '{self.key}'.")

        # animate the skill user
        self._play_animation()

        # set the skill on cooldown
        world.set_skill_on_cooldown(self)

        # create the projectile
        if self.uses_projectile:
            # update projectile values
            projectile_data = self.projectile_data
            projectile_data.creator = self.user
            projectile_data.skill_name = self.key
            projectile_data.skill_instance = self
            projectile_data.direction = self.direction

            # create the projectile
            projectile = world.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)

            # save the reference to the projectile entity
            self.projectile = projectile
        else:
            world.apply_skill(self)

    def _play_animation(self):
        """
        Play the provided animation on the entity's aesthetic component
        """
        from scripts.engine import world
        aesthetic = world.get_entitys_component(self.user, Aesthetic)
        animation = self.get_animation(aesthetic)
        if aesthetic and animation:
            aesthetic.current_sprite = animation
            aesthetic.current_sprite_duration = 0

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        entity_names = []
        from scripts.engine import world
        for entity in world.get_affected_entities((self.target_tile.x, self.target_tile.y), self.shape,
                                                  self.shape_size, self.direction):
            yield entity, self.build_effects(entity)
            entity_names.append(world.get_name(entity))

        logging.debug(f"'{world.get_name(self.user)}' applied '{self.key}' to {entity_names}.")

    @abstractmethod
    def get_animation(self, aesthetic: Aesthetic):
        """
        Return the animation to play when executing the skill
        """
        pass

    @abstractmethod
    def build_effects(self, entity: EntityID, effect_strength: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden by subclass.
        """
        pass

    @classmethod
    def set_properties(cls):
        """
        Sets the class properties of the skill from a skill name
        """
        from scripts.engine import library
        cls.data = library.SKILLS[cls.key]
        cls.required_tags = cls.data.required_tags
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon_path
        cls.resource_type = cls.data.resource_type
        cls.resource_cost = cls.data.resource_cost
        cls.time_cost = cls.data.time_cost
        cls.base_cooldown = cls.data.cooldown
        cls.targeting_method = cls.data.targeting_method
        cls.target_directions = cls.data.target_directions
        cls.shape = cls.data.shape
        cls.shape_size = cls.data.shape_size
        cls.uses_projectile = cls.data.uses_projectile
        cls.projectile_data = cls.data.projectile_data


class Affliction(ABC):
    """
    A subclass of Affliction represents an affliction (a semi-permanent modifier) and holds all the data that is
    not dependent on the individual instances -  stuff like applicable targets etc.

    An instance of Affliction represents an individual application of that affliction,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass, including being set by external data
    key: str = ""
    description: str = ""
    icon_path: str = ""
    required_tags: List[TargetTagType]
    identity_tags: List[EffectTypeType]
    triggers: List[AfflictionTriggerType]
    category: AfflictionCategoryType
    shape: ShapeType
    shape_size: int

    def __init__(self, creator: EntityID, affected_entity: EntityID, duration: int):
        self.creator = creator
        self.affected_entity = affected_entity
        self.duration = duration

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        from scripts.engine import world
        entities = set()
        position = world.get_entitys_component(self.affected_entity, Position)
        if position:
            for coordinate in position.coordinates:
                for entity in world.get_affected_entities(coordinate, self.shape, self.shape_size):
                    if entity not in entities:
                        entities.add(entity)
                        yield entity, self.build_effects(entity)

    @abstractmethod
    def build_effects(self, entity: EntityID):
        """
        Build the effects of this affliction applying to a single entity. Must be overridden by subclass.
        """
        pass

    @classmethod
    def set_properties(cls):
        """
        Sets the class properties of the skill from a skill name
        """
        from scripts.engine import library

        cls.data = library.AFFLICTIONS[cls.key]
        cls.key = cls.data.name
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon_path
        cls.category = cls.data.category
        cls.shape = cls.data.shape
        cls.shape_size = cls.data.shape_size
        cls.required_tags = cls.data.required_tags
        cls.identity_tags = cls.data.identity_tags
        cls.triggers = cls.data.triggers


def properties_set_by_data(cls):
    """
    Class decorator used for initializing class with a  set properties method so as to avoid repeating code.
    """
    cls.set_properties()
    return cls


def register_action(cls):
    """
    Class decorator used to register an action with the engine.
    """
    if issubclass(cls, Skill):
        skill_registry[cls.key] = cls
    elif issubclass(cls, Affliction):
        affliction_registry[cls.key] = cls

    return cls
