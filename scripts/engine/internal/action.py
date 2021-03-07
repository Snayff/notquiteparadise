from __future__ import annotations

import logging
import os
import random
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Set, TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core import hourglass, matter, world
from scripts.engine.core.component import Aesthetic, Knowledge, Position
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


__all__ = ["Skill", "Affliction", "Behaviour", "SkillModifier", "register_action"]


# used by skill modifiers
import scripts.engine.core.effect

_EFFECTS = {k: getattr(scripts.engine.core.effect, k) for k in dir(scripts.engine.core.effect)}


class Action(ABC):
    """
    Action taken during the game. A container for Effects.
    """

    # details to be overwritten by external data
    name: str  # name of the class
    description: str
    icon_path: str

    # details to be overwritten in subclass
    target_tags: List[TileTagType]
    shape: ShapeType
    shape_size: int

    # set by instance
    effects: List[Effect]

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

    # core data, to be overwritten by external data
    resource_type: ResourceType
    resource_cost: int
    time_cost: int
    base_cooldown: int

    # targeting details, to be overwritten in subclass
    targeting_method: TargetingMethodType  # Tile, Direction, Auto
    cast_tags: List[TileTagType]
    target_directions: List[DirectionType]  # needed for Direction
    range: int  # needed for Tile, Auto

    # delivery methods, to be overwritten in subclass
    uses_projectile: bool  # usable by for Tile, Direction, Auto
    projectile_data: Optional[ProjectileData]
    is_delayed: bool  # usable by Tile, Auto  - Doesnt make sense for Direction to have a delayed cast.
    delayed_skill_data: Optional[DelayedSkillData]

    # blessing related attributes
    blessings: List[SkillModifier]
    types: List[str]

    def __init__(self, user: EntityID, target_tile: Tile, direction: DirectionType):
        self.user: EntityID = user
        self.target_tile: Tile = target_tile
        self.direction: DirectionType = direction
        self.projectile: Optional[EntityID] = None
        self.delayed_skill: Optional[EntityID] = None

        # vars needed to keep track of changes
        self.ignore_entities: List[EntityID] = []  # to ensure entity not hit more than once

        self.inactive_effects: List[str] = []

    def _post_build_effects(self, entity: EntityID, potency: float = 1.0, skill_stack=None) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. This function will be used to apply any dynamic tweaks to the effects stack after the subclass generates its stack.
        """
        # handle mutable default
        if skill_stack is None:
            skill_stack = []
        skill_blessings = matter.get_entitys_component(self.user, Knowledge).skill_blessings
        relevant_blessings: List[SkillModifier] = []
        if self.__class__.__name__ in skill_blessings:
            relevant_blessings = skill_blessings[self.__class__.__name__]
        for blessing in relevant_blessings:
            blessing.apply(skill_stack, self.user, entity)
        return skill_stack

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the skill from the class key
        """
        from scripts.engine.internal import library

        cls.data = library.SKILLS[cls.__name__]
        cls.name = cls.__name__
        cls.description = cls.data.description
        cls.base_cooldown = cls.data.cooldown
        cls.time_cost = cls.data.time_cost
        cls.icon_path = cls.data.icon_path
        cls.resource_type = cls.data.resource_type
        cls.resource_cost = cls.data.resource_cost
        cls.types = cls.data.types

    def apply(self) -> Iterator[Tuple[EntityID, List[Effect]]]:
        """
        An iterator over pairs of (affected entity, [effects]). Uses target tile. Can apply to an entity multiple
        times.
        """
        entity_names = []
        for entity in matter.get_affected_entities(
            (self.target_tile.x, self.target_tile.y), self.shape, self.shape_size, self.direction
        ):
            yield entity, [
                effect
                for effect in self._build_effects(entity)
                if effect.__class__.__name__ not in self.inactive_effects
            ]
            entity_names.append(matter.get_name(entity))

    def use(self) -> bool:
        """
        If uses_projectile then create a projectile to carry the skill effects. Otherwise call self.apply
        """
        logging.debug(f"'{matter.get_name(self.user)}' used '{self.__class__.__name__}'.")

        # handle the delivery method of the skill
        if self.uses_projectile:
            self._create_projectile()
            is_successful = True
        elif self.is_delayed:
            self._create_delayed_skill()
            is_successful = True
        else:
            is_successful = matter.apply_skill(self)

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
        projectile = matter.create_projectile(self.user, (self.target_tile.x, self.target_tile.y), projectile_data)

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
        delayed_skill = matter.create_delayed_skill(
            self.user, (self.target_tile.x, self.target_tile.y), delayed_skill_data
        )

        # add to ignore list
        self.ignore_entities.append(delayed_skill)

        # save reference
        self.delayed_skill = delayed_skill

    @abstractmethod
    def _build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        """
        Build the effects of this skill applying to a single entity. Must be overridden in subclass.
        """
        pass


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
        cls.description = cls.data.description
        cls.icon_path = cls.data.icon_path
        cls.category = cls.data.category
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
        position = matter.get_entitys_component(self.affected_entity, Position)

        for coordinate in position.coordinates:
            for entity in matter.get_affected_entities(coordinate, self.shape, self.shape_size):
                if entity not in entities:
                    entities.add(entity)
                    yield entity, self._build_effects(entity)
                    entity_names.append(matter.get_name(entity))

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


class SkillModifier(ABC):
    """
    The base class for blessings. Blessings modify skills through the effects applied.
    """

    name: str
    description: str

    level: str
    removable: bool
    conflicts: List[str]
    skill_types: List[str]

    # remove/add are applied when the blessing is applied
    remove_effects: List[str]
    add_effects: List[Dict[str, Any]]

    # modifications are applied when the effects are built
    modify_effects_set: List[Dict[str, Any]]
    modify_effects_tweak_flat: List[Dict[str, Any]]
    modify_effects_tweak_percent: List[Dict[str, Any]]

    # custom args (set by child if JSON doesn't cover the argument needs)
    custom_args: Dict[str, Any] = {}

    def __init__(self, owner):
        self.owner = owner

    @classmethod
    def _init_properties(cls):
        """
        Sets the class properties of the blessing from the class key
        """
        from scripts.engine.internal import library

        cls.data = library.BLESSINGS[cls.__name__]
        cls.name = cls.__name__
        cls.description = cls.data["description"]
        cls.level = "Base"  # assume common exists for now
        cls.removable = cls.data["removable"]
        cls.conflicts = cls.data["conflicts"]
        cls.skill_types = cls.data["skill_types"]

        cls.remove_effects = cls.data["base_effects"]["remove_effects"]
        cls.add_effects = cls.data["base_effects"]["add_effects"]
        cls.modify_effects_set = cls.data["base_effects"]["modify_effects_set"]
        cls.modify_effects_tweak_flat = cls.data["base_effects"]["modify_effects_tweak_flat"]
        cls.modify_effects_tweak_percent = cls.data["base_effects"]["modify_effects_tweak_percent"]

    @property
    def involved_effects(self) -> Set[str]:
        """
        Get the set of effects involved in the blessing.
        """
        return set([v["effect_id"] for v in self.add_effects + self.modify_effects_set] + self.remove_effects)

    def roll_level(self):
        """
        Runs the level selection algorithm and updates attributes with the applied level.
        """
        levels = []
        level_chances = []
        total = 0

        for level in self.data["levels"]:
            levels.append(level)
            total += self.data["levels"][level]["rarity"]
            level_chances.append(total)

        random_float = random.random()
        for i, chance in enumerate(level_chances):
            if random_float <= chance:
                break

        self.set_level(levels[i])

    def set_level(self, level):
        """
        Refreshes the class attributes with the data for the specific blessing level.
        """
        self.level = level
        if "remove_effects" in self.data["levels"][self.level]["effects"]:
            self.remove_effects = self.data["levels"][self.level]["effects"]["remove_effects"]
        if "add_effects" in self.data["levels"][self.level]["effects"]:
            self.add_effects = self.data["levels"][self.level]["effects"]["add_effects"]
        if "modify_effects_set" in self.data["levels"][self.level]["effects"]:
            self.modify_effects_set = self.data["levels"][self.level]["effects"]["modify_effects_set"]
        if "modify_effects_tweak_flat" in self.data["levels"][self.level]["effects"]:
            self.modify_effects_tweak_flat = self.data["levels"][self.level]["effects"]["modify_effects_tweak_flat"]
        if "modify_effects_tweak_percent" in self.data["levels"][self.level]["effects"]:
            self.modify_effects_tweak_percent = self.data["levels"][self.level]["effects"][
                "modify_effects_tweak_percent"
            ]

    def apply(self, effects: List[Effect], owner, target):
        """
        This is the core function of the blessing. It takes the effect stack and modifies it with the blessing.
        """

        # go through the effects backwards so that the .remove() doesn't mess up indexing
        for effect in effects[::-1]:
            effect_name = effect.__class__.__name__

            # flat config change
            for mod in self.modify_effects_tweak_flat:
                if mod["effect_id"] == effect_name:
                    for value in mod["values"]:
                        current_value = getattr(effect, value)
                        setattr(effect, value, current_value + mod["values"][value])

            # set config change
            for mod in self.modify_effects_set:
                if mod["effect_id"] == effect_name:
                    for value in mod["values"]:
                        setattr(effect, value, mod["values"][value])

            # percent config change
            for mod in self.modify_effects_tweak_percent:
                if mod["effect_id"] == effect_name:
                    for value in mod["values"]:
                        current_value = getattr(effect, value)
                        setattr(effect, value, current_value * mod["values"][value])

            # remove effects from the stack if applicable
            if effect_name in self.remove_effects:
                effects.remove(effect)

        # add effects to the stack
        for add_effect in self.add_effects:
            # build the effect creation arguments from the config
            args = {"origin": owner, "target": target, "success_effects": [], "failure_effects": []}
            args.update(add_effect["args"])
            if add_effect["effect_id"] in self.custom_args:
                args.update(self.custom_args)
            effects.append(_EFFECTS[add_effect["effect_id"]](**args))


def register_action(cls: Type[Union[Action, Behaviour, SkillModifier]]):
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
    elif issubclass(cls, SkillModifier):
        cls._init_properties()
        store.blessing_registry[cls.__name__] = cls
    elif issubclass(cls, Affliction):
        cls._init_properties()
        store.affliction_registry[cls.__name__] = cls
    elif issubclass(cls, Behaviour):
        store.behaviour_registry[cls.__name__] = cls


######################### REQUIRED ACTION SUBCLASSES ##########################


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
        pos = matter.get_entitys_component(entity, Position)
        current_tile = world.get_tile((pos.x, pos.y))
        dir_x, dir_y = self.data.direction[0], self.data.direction[1]
        target_tile = world.get_tile((current_tile.x + dir_x, current_tile.y + dir_y))

        # check if already on top of an entity before moving in case something move into the projectile or the projectile was created on top of an entity
        player_pos = matter.get_entitys_component(matter.get_player(), Position)
        if world.tile_has_tag(entity, current_tile, TileTag.OTHER_ENTITY):
            self.data.skill_instance.target_tile = current_tile
            should_activate = True
            logging.debug(f"'{matter.get_name(entity)}' collided with an entity on cast at ({pos.x},{pos.y}).")

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
                matter.kill_entity(entity)

        if should_activate:
            logging.debug(f"'{matter.get_name(entity)}' is going to activate at ({pos.x},{pos.y}).")

            # apply skill, rather than using it, as the instance already exists and we are just using the effects
            matter.apply_skill(self.data.skill_instance)

            # die after activating
            matter.kill_entity(entity)

        elif should_move:
            logging.debug(
                f"'{matter.get_name(entity)}' has {self.data.range - self.distance_travelled} range left and"
                f" is going to move from ({pos.x},{pos.y}) to "
                f"({pos.x + dir_x},{pos.y + dir_y})."
            )

            move = matter.get_known_skill(entity, "Move")
            matter.use_skill(entity, move, current_tile, self.data.direction)

            self.distance_travelled += 1
            hourglass.end_turn(entity, self.data.speed)

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
                matter.kill_entity(self.entity)

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
            time_left_in_round = hourglass.get_time_left_in_round()
            from scripts.engine.internal import library

            time_per_round = library.GAME_CONFIG.default_values.time_per_round

            # align to round time and add number of rounds as a delay
            time_delay = (time_per_round * self.data.duration) + time_left_in_round
            hourglass.end_turn(self.entity, time_delay)

            # set flag
            self.delayed = True

            logging.debug(f"{matter.get_name(self.entity)} will trigger in {self.data.duration} rounds.")

            return

        # apply skill, rather than using it, as the instance already exists and we are just using the effects
        matter.apply_skill(self.data.skill_instance)

        # die after activating
        matter.kill_entity(self.entity)
