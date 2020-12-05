from __future__ import annotations

import logging
import os
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.internal.component import Aesthetic, Position
from scripts.engine.internal.constant import (
    AfflictionCategoryType,
    DirectionType,
    EffectTypeType,
    ReactionTriggerType,
    ResourceType,
    ShapeType,
    TargetingMethodType,
    TargetTagType,
)
from scripts.engine.internal.definition import ProjectileData
from scripts.engine.internal.effect import Effect
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Iterator, List, Optional, Tuple, Type, TYPE_CHECKING, Union

__all__ = ["Skill", "Affliction", "Behaviour", "register_action"]


class Action(ABC):
    """
    Action taken during the game. A container for Effects.
    """

    name: str  # name of the class
    f_name: str  # friendly name, can include spaces, slashes etc.
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
    range: int
    uses_projectile: bool
    projectile_data: Optional[ProjectileData]

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user = user
        self.target_tile = target_tile
        self.direction = direction
        self.projectile = None

        # vars needed to keep track of changes
        self.ignore_entities: List[EntityID] = []  # to ensure entity not hit more than once

    @abstractmethod
    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass

    def get_animation(self, aesthetic: Aesthetic):
        """
        Return the animation to play when executing the skill. Defaults to attack sprite. Override in subclass if
        another is needed.
        """
        return aesthetic.sprites.attack

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the skill from the class key
        """
        from scripts.engine.internal import library

        cls.data = library.SKILLS[cls.__name__]
        cls.name = cls.__name__
        cls.f_name = cls.data.name
        cls.target_tags = cls.data.target_tags
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon_path
        cls.resource_type = cls.data.resource_type
        cls.resource_cost = cls.data.resource_cost
        cls.range = cls.data.range
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
        An iterator over pairs of (affected entity, [effects]). Uses target tile. Can apply to an entity multiple
        times.
        """
        entity_names = []
        from scripts.engine.core import world

        for entity in world.get_affected_entities(
            (self.target_tile.x, self.target_tile.y), self.shape, self.shape_size, self.direction
        ):
            yield entity, self.build_effects(entity)
            entity_names.append(world.get_name(entity))

    def use(self) -> bool:
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        from scripts.engine.core import world

        logging.debug(f"'{world.get_name(self.user)}' used '{self.__class__.__name__}'.")

        # animate the skill user
        self._play_animation()

        # create the projectile
        if self.uses_projectile:
            self._create_projectile()
            is_successful = True
        else:
            is_successful = world.apply_skill(self)

        return is_successful

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
        from scripts.engine.core import world

        projectile = world.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)

        # add projectile to ignore list
        self.ignore_entities.append(projectile)

        # save the reference to the projectile entity
        self.projectile = projectile

    def _play_animation(self):
        """
        Play the provided animation on the entity's aesthetic component
        """
        from scripts.engine.core import world

        if world.entity_has_component(self.user, Aesthetic):
            aesthetic = world.get_entitys_component(self.user, Aesthetic)
            animation = self.get_animation(aesthetic)
            if animation:
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
    triggers: List[ReactionTriggerType]
    category: AfflictionCategoryType

    def __init__(self, origin: EntityID, affected_entity: EntityID, duration: int):
        self.origin = origin
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
        from scripts.engine.internal import library

        cls.data = library.AFFLICTIONS[cls.__name__]
        cls.name = cls.__name__
        cls.f_name = cls.data.name
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
        Apply the affliction to the affected entity.
        An iterator over pairs of (affected entity, [effects]). Use affected entity position.  Applies to each
        entity only once.
        """
        from scripts.engine.core import world

        entity_names = []
        entities = set()
        position = world.get_entitys_component(self.affected_entity, Position)
        if position:
            for coordinate in position.coordinates:
                for entity in world.get_affected_entities(coordinate, self.shape, self.shape_size):
                    if entity not in entities:
                        entities.add(entity)
                        yield entity, self.build_effects(entity)
                        entity_names.append(world.get_name(entity))

    def trigger(self):
        """
        Trigger the affliction on the affected entity
        """
        yield self.affected_entity, self.build_effects(self.affected_entity)


class Behaviour(ABC):
    """
    Base class for AI behaviours. Not really an Action, as such, more of a super class that determines when npcs
    will use Actions.
    """

    def __init__(self, attached_entity: EntityID):
        self.entity = attached_entity

    @abstractmethod
    def act(self):
        """
        Perform the behaviour
        """
        pass


def register_action(cls: Type[Union[Action, Behaviour]]):
    """
    Initialises the class properties set by external data, if appropriate, and adds to the action registry for use
    by the engine.
    """
    if "GENERATING_SPHINX_DOCS" in os.environ:  # when building in CI these fail
        return

    from scripts.engine.internal.data import store

    if issubclass(cls, Skill):
        cls._init_properties()
        store.skill_registry[cls.__name__] = cls
    elif issubclass(cls, Affliction):
        cls._init_properties()
        store.affliction_registry[cls.__name__] = cls
    elif issubclass(cls, Behaviour):
        store.behaviour_registry[cls.__name__] = cls
