from __future__ import annotations

import logging

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING, Dict, Iterator, Type
from snecs.typedefs import EntityID
from scripts.engine.component import Aesthetic, Position
from scripts.engine.core.constants import (
    AfflictionCategoryType,
    AfflictionTriggerType,
    DirectionType,
    EffectTypeType,
    ResourceType,
    ShapeType,
    TargetingMethodType,
    TargetTagType,
)
from scripts.engine.core.definitions import ProjectileData
from scripts.engine.effect import Effect
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Tuple, List

__all__ = ["Skill", "Affliction", "init_action", "skill_registry", "affliction_registry"]

skill_registry: Dict[str, Type[Skill]] = {}
affliction_registry: Dict[str, Type[Affliction]] = {}


class Action(ABC):
    key: str
    name: str
    description: str
    icon_path: str
    target_tags: List[TargetTagType]
    effects: List[Effect]
    shape: ShapeType
    shape_size: int

    @abstractmethod
    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass


class Skill(Action):
    """
    A subclass of Skill represents a skill and holds all the data that is
    not dependent on the individual cast - stuff like shape, base accuracy, etc.

    An instance of Skill represents an individual use of that skill,
    and additionally holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass, including being set by external data
    resource_type: ResourceType
    resource_cost: int
    time_cost: int
    base_cooldown: int
    targeting_method: TargetingMethodType
    target_directions: List[DirectionType]
    uses_projectile: bool
    projectile_data: Optional[ProjectileData]

    # vars needed to keep track of changes
    ignore_entities: List[EntityID] = []  # to ensure entity not hit more than once

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction
        self.projectile = None

    @abstractmethod
    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass

    @abstractmethod
    def get_animation(self, aesthetic: Aesthetic):
        """
        Return the animation to play when executing the skill
        """
        pass

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the skill from the class key
        """
        from scripts.engine import library

        cls.data = library.SKILLS[cls.key]
        cls.name = cls.data.name
        cls.target_tags = cls.data.target_tags
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

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects])
        """
        entity_names = []
        from scripts.engine import world

        for entity in world.get_affected_entities(
            (self.target_tile.x, self.target_tile.y), self.shape, self.shape_size, self.direction
        ):
            yield entity, self.build_effects(entity)
            entity_names.append(world.get_name(entity))

        logging.debug(f"'{world.get_name(self.user)}' applied '{self.key}' to {entity_names}.")

    def use(self):
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        from scripts.engine import world

        logging.debug(f"'{world.get_name(self.user)}' used '{self.key}'.")

        # animate the skill user
        self._play_animation()

        # create the projectile
        if self.uses_projectile:
            self._create_projectile()
        else:
            world.apply_skill(self)

        # set the skill on cooldown
        world.set_skill_on_cooldown(self)

    def _create_projectile(self):
        """
        Create a projectile carrying the skill's effects
        """
        projectile_data = self.projectile_data

        # update projectile values
        projectile_data.creator = self.user
        projectile_data.skill_name = self.name
        projectile_data.skill_instance = self
        projectile_data.direction = self.direction

        # create the projectile
        from scripts.engine import world
        projectile = world.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)

        # save the reference to the projectile entity
        self.projectile = projectile

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


class Affliction(Action):
    """
    A subclass of Affliction represents an affliction (a semi-permanent modifier) and holds all the data that is
    not dependent on the individual instances -  stuff like applicable targets etc.

    An instance of Affliction represents an individual application of that affliction,
    and holds only the data that is tied to the individual use - stuff like
    the user and target.
    """

    # to be overwritten in subclass, including being set by external data
    identity_tags: List[EffectTypeType]
    triggers: List[AfflictionTriggerType]
    category: AfflictionCategoryType


    def __init__(self, creator: EntityID, affected_entity: EntityID, duration: int):
        self.creator = creator
        self.affected_entity = affected_entity
        self.duration = duration

    @abstractmethod
    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the affliction from the class key
        """
        from scripts.engine import library

        cls.data = library.AFFLICTIONS[cls.key]
        cls.name = cls.data.name
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon_path
        cls.category = cls.data.category
        cls.shape = cls.data.shape
        cls.shape_size = cls.data.shape_size
        cls.target_tags = cls.data.target_tags
        cls.identity_tags = cls.data.identity_tags
        cls.triggers = cls.data.triggers

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


def init_action(cls):
    """
    Class decorator used for initialising class with properties from external data and also add to the registry for
    use by the engine.
    """
    cls._init_properties()

    if issubclass(cls, Skill):
        skill_registry[cls.key] = cls
    elif issubclass(cls, Affliction):
        affliction_registry[cls.key] = cls



