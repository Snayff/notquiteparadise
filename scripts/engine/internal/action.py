from __future__ import annotations

import logging
import os
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core import chronicle, world
from scripts.engine.core.component import Aesthetic, Position
from scripts.engine.core.effect import Effect
from scripts.engine.internal.constant import (
    AfflictionCategoryType,
    DirectionType,
    EffectTypeType,
    ProjectileExpiry,
    ReactionTriggerType,
    ResourceType,
    ShapeType,
    TargetingMethodType,
    TerrainCollision,
    TileTag,
    TileTagType,
)
from scripts.engine.internal.definition import DelayedSkillData, ProjectileData
from scripts.engine.internal.event import event_hub, UseSkillEvent
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
    target_tags: List[TileTagType]
    effects: List[Effect]
    shape: ShapeType
    shape_size: int

    @abstractmethod
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
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
    targeting_method: TargetingMethodType  # Tile, Direction, Auto

    # targeting details
    cast_tags: List[TileTagType]
    target_directions: List[DirectionType]  # needed for Direction
    range: int  # needed for Tile, Auto

    # delivery methods
    uses_projectile: bool  # usable by for Tile, Direction, Auto
    projectile_data: Optional[ProjectileData]
    is_delayed: bool  # usable by Tile, Auto  - Doesnt make sense for Direction to have a delayed cast.
    delayed_skill_data: Optional[DelayedSkillData]

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user: EntityID = user
        self.target_tile: Tile = target_tile
        self.direction: DirectionType = direction
        self.projectile: Optional[EntityID] = None
        self.delayed_skill: Optional[EntityID] = None

        # vars needed to keep track of changes
        self.ignore_entities: List[EntityID] = []  # to ensure entity not hit more than once

    @abstractmethod
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the skill from the class key
        """
        from scripts.engine.internal import library

        cls.data = library.SKILLS[cls.__name__]
        cls.name = cls.__name__
        cls.f_name = cls.data.name
        cls.cast_tags = cls.data.cast_tags
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
        cls.is_delayed = cls.data.is_delayed
        cls.delayed_skill_data = cls.data.delayed_skill_data

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects]). Uses target tile. Can apply to an entity multiple
        times.
        """
        entity_names = []
        for entity in world.get_affected_entities(
            (self.target_tile.x, self.target_tile.y), self.shape, self.shape_size, self.direction
        ):
            yield entity, self._build_effects(entity)
            entity_names.append(world.get_name(entity))

    def use(self) -> bool:
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        logging.debug(f"'{world.get_name(self.user)}' used '{self.__class__.__name__}'.")

        # handle the delivery method of the skill
        if self.uses_projectile:
            self._create_projectile()
            is_successful = True
        elif self.is_delayed:
            self._create_delayed_skill()
            is_successful = True
        else:
            is_successful = world.apply_skill(self)

        if is_successful:
            # post interaction event
            event = UseSkillEvent(origin=self.user, skill_name=self.__class__.__name__)
            event_hub.post(event)

        return is_successful

    def _create_projectile(self):
        """
        Create a projectile carrying the skill's effects
        """
        projectile_data = self.projectile_data

        # update projectile instance values
        projectile_data.creator = self.user
        projectile_data.skill_name = self.name
        projectile_data.skill_instance = self
        projectile_data.direction = self.direction

        # create the projectile
        projectile = world.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)

        # add projectile to ignore list
        self.ignore_entities.append(projectile)

        # save the reference to the projectile entity
        self.projectile = projectile

    def _create_delayed_skill(self):
        delayed_skill_data = self.delayed_skill_data

        # update delayed skill instance values
        delayed_skill_data.creator = self.user
        delayed_skill_data.skill_name = self.name
        delayed_skill_data.skill_instance = self

        # create the delayed skill
        delayed_skill = world.create_delayed_skill(
            self.user, (self.target_tile.x, self.target_tile.y), delayed_skill_data
        )

        # add to ignore list
        self.ignore_entities.append(delayed_skill)

        # save reference
        self.delayed_skill = delayed_skill


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
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
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

        for coordinate in position.coordinates:
            for entity in world.get_affected_entities(coordinate, self.shape, self.shape_size):
                if entity not in entities:
                    entities.add(entity)
                    yield entity, self._build_effects(entity)
                    entity_names.append(world.get_name(entity))

    def trigger(self):
        """
        Trigger the affliction on the affected entity
        """
        yield self.affected_entity, self._build_effects(self.affected_entity)


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


######################### ACTION SUBCLASSES ##########################


class Projectile(Behaviour):
    """
    Move in direction, up to max_range (in tiles). Speed is time spent per tile moved.
    """

    def __init__(self, attached_entity: EntityID):
        super().__init__(attached_entity)

        self.data: ProjectileData = ProjectileData()
        self.distance_travelled = 0

    def act(self):
        # flags
        should_activate = False
        should_move = False

        # get info we definitely need
        entity = self.entity
        pos = world.get_entitys_component(entity, Position)
        current_tile = world.get_tile((pos.x, pos.y))
        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
        target_tile = world.get_tile((current_tile.x + dir_x, current_tile.y + dir_y))

        # if we havent moved check for collision in current tile (it might be cast on top of enemy)
        if self.distance_travelled == 0 and world.tile_has_tag(entity, current_tile, TileTag.OTHER_ENTITY):
            should_activate = True
            logging.debug(f"'{world.get_name(entity)}' collided with an entity on cast at ({pos.x},{pos.y}).")

        # if we havent travelled max distance or determined we should activate then move
        # N.b. not an elif because we want the precheck above to happen in isolation
        if self.distance_travelled < self.data.range and not should_activate:
            # can we move
            if world.tile_has_tag(entity, target_tile, TileTag.OPEN_SPACE):
                should_move = True

            else:
                should_activate, should_move = self._handle_collision(current_tile, target_tile)

        elif self.distance_travelled >= self.data.range:
            # we have reached the limit, process expiry and then die
            if self.data.expiry_type == ProjectileExpiry.ACTIVATE:
                should_activate = True

                # update skill instance to point to current position, for when it is applied
                self.data.skill_instance.target_tile = current_tile

            else:
                # at max range and not activating so kill attached entity
                world.kill_entity(entity)

        if should_activate:
            logging.debug(f"'{world.get_name(entity)}' is going to activate at ({pos.x},{pos.y}).")

            # apply skill, rather than using it, as the instance already exists and we are just using the effects
            world.apply_skill(self.data.skill_instance)

            # die after activating
            world.kill_entity(entity)

        elif should_move:
            logging.debug(
                f"'{world.get_name(entity)}' has {self.data.range - self.distance_travelled} range left and"
                f" is going to move from ({pos.x},{pos.y}) to "
                f"({pos.x + dir_x},{pos.y + dir_y})."
            )

            move = world.get_known_skill(entity, "Move")
            world.use_skill(entity, move, current_tile, self.data.direction)

            self.distance_travelled += 1
            chronicle.end_turn(entity, self.data.speed)

    def _handle_collision(self, current_tile: Tile, target_tile: Tile) -> Tuple[bool, bool]:
        """
        Handle collisions, returning should_activate, should_move and updating target tile and direction if needed
        """
        should_activate = should_move = False

        if world.tile_has_tags(self.entity, target_tile, [TileTag.BLOCKED_MOVEMENT, TileTag.NO_ENTITY]):
            collision_type = self.data.terrain_collision

            if collision_type == TerrainCollision.ACTIVATE:
                should_activate = True

                # update skill instance to new target
                assert isinstance(self.data.skill_instance, Skill)
                self.data.skill_instance.target_tile = target_tile

            elif collision_type == TerrainCollision.FIZZLE:
                # get rid of projectile
                world.kill_entity(self.entity)

            elif collision_type == TerrainCollision.REFLECT:
                should_move = True

                # change direction and move
                new_dir = world.get_reflected_direction(
                    self.entity, (current_tile.x, current_tile.y), (target_tile.x, target_tile.y)
                )
                self.data.direction = new_dir

        # blocked by entity
        elif world.tile_has_tag(self.entity, target_tile, TileTag.OTHER_ENTITY):
            should_activate = True

            # update skill instance to new target
            assert isinstance(self.data.skill_instance, Skill)
            self.data.skill_instance.target_tile = target_tile

        return should_activate, should_move


class DelayedSkill(Behaviour):
    """
    After duration ends trigger skill centred on self.
    """

    def __init__(self, attached_entity: EntityID):
        super().__init__(attached_entity)

        # N.B. both must be set after init
        self.data: DelayedSkillData = DelayedSkillData()
        self.delayed: bool = False

    def act(self):
        if not self.delayed:
            # get time left in round, to align first end of turn to round
            time_left_in_round = chronicle.get_time_left_in_round()
            from scripts.engine.internal import library

            time_per_round = library.GAME_CONFIG.default_values.time_per_round

            # align to round time and add number of rounds as a delay
            time_delay = (time_per_round * self.data.duration) + time_left_in_round
            chronicle.end_turn(self.entity, time_delay)

            # set flag
            self.delayed = True

            logging.debug(f"{world.get_name(self.entity)} will trigger in {self.data.duration} rounds.")

            return

        # apply skill, rather than using it, as the instance already exists and we are just using the effects
        world.apply_skill(self.data.skill_instance)

        # die after activating
        world.kill_entity(self.entity)
