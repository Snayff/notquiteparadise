from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING

import numpy as np
from snecs import RegisteredComponent

from scripts.engine.core.constants import EffectType, PrimaryStatType, RenderLayerType

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict, Optional, Type, Tuple
    from scripts.engine.action import Affliction, Behaviour, Skill
    from scripts.engine.core.definitions import TraitSpritePathsData, TraitSpritesData


##########################################################
# Components are to hold data that is subject to change.
#########################################################

########################### FLAGS ##############################


class IsPlayer(RegisteredComponent):
    """
    Whether the entity is the player.
    """

    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return IsPlayer()


class IsActor(RegisteredComponent):
    """
    Whether the entity is an actor.
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return IsActor()


class IsGod(RegisteredComponent):
    """
    Whether the entity is a god.
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return IsGod()


class HasCombatStats(RegisteredComponent):
    """
    A flag to show if an entity has stats used for combat.
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return HasCombatStats()


class WinCondition(RegisteredComponent):
    """
    A flag to show that an entity is a win objective
    """

    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialised):
        return WinCondition()


#################### OTHERS #########################


class Position(RegisteredComponent):
    """
    An entity's position on the map. At initiation provide all positions the entity holds. After initiation only need
     to set the top left, or reference position as the other coordinates are held as offsets.
    """

    def __init__(self, *positions: Tuple[int, int]):
        # Sort the positions from top-left to down-right
        if not positions:
            raise ValueError("Must provide at least 1 coordinate for the entity.")

        sorted_positions = sorted(positions, key=lambda x: (x[0] ** 2 + x[1] ** 2))
        top_left = sorted_positions[0]
        self.offsets = [(x - top_left[0], y - top_left[1]) for x, y in sorted_positions]
        self.reference_position = top_left

    def serialize(self):
        return self.coordinates

    @classmethod
    def deserialize(cls, serialised):
        return Position(*serialised)

    def set(self, x: int, y: int):
        self.reference_position = (x, y)

    def get_outermost(self, direction: Tuple[int, int]) -> Tuple[int, int]:
        """
        Calculate the outermost tile in the direction provided
        :param direction: Direction to use
        :return: The position of the outermost tile
        """
        coordinates = self.coordinates
        # Calculate center
        center = (sum(c[0] for c in coordinates), sum(c[1] for c in coordinates))
        transformed = [np.dot((c[0], c[1]), direction) for c in coordinates]
        # Find the coordinate that is nearest the direction
        arg_max = np.argwhere(transformed == np.amax(transformed))
        # From all the nearest coordinates find the one nearest to the center of the entity
        arg_min = np.argmin(
            np.sqrt((center[0] - transformed[i[0]][0]) ** 2 + (center[1] - transformed[i[0]][1]) ** 2) for i in arg_max
        )
        return coordinates[arg_max[arg_min][0]][0], coordinates[arg_max[arg_min][0]][1]

    @property
    def x(self) -> int:
        """
        :return: The x component of the top-left position
        """
        return self.reference_position[0]

    @property
    def y(self) -> int:
        """
        :return: The y component of the top-left position
        """
        return self.reference_position[1]

    @property
    def coordinates(self) -> List[Tuple[int, int]]:
        """
        :return: The list of coordinates that this Position represents
        """
        return [(self.x + x, self.y + y) for x, y in self.offsets]

    def __contains__(self, key: Tuple[int, int]):
        """
        :param key: Coordinate to test against
        :return: A bool that represents if the Position contains the provided coordinates
        """
        for coordinate in self.coordinates:
            if coordinate == key:
                return True
        return False


class Aesthetic(RegisteredComponent):
    """
    An entity's sprite.
    """

    def __init__(
        self,
        current_sprite: pygame.Surface,
        sprites: TraitSpritesData,
        sprite_paths: List[TraitSpritePathsData],
        render_layer: RenderLayerType,
        draw_pos: Tuple[float, float],
    ):
        self._sprite_paths: List[TraitSpritePathsData] = sprite_paths
        self.current_sprite: pygame.Surface = current_sprite
        self.sprites: TraitSpritesData = sprites
        self.render_layer = render_layer

        draw_x, draw_y = draw_pos
        self.draw_x: float = draw_x
        self.draw_y: float = draw_y

        self.target_draw_x: float = draw_x
        self.target_draw_y: float = draw_y
        self.current_sprite_duration: float = 0

    def serialize(self):

        # loop all sprite paths and convert to dict
        sprite_paths = []
        for sprite_path in self._sprite_paths:
            sprite_paths.append(asdict(sprite_path))

        _dict = {
            "draw_pos": (self.draw_x, self.draw_y),
            "render_layer": self.render_layer,
            "sprite_paths": sprite_paths,
        }
        return _dict

    @classmethod
    def deserialize(cls, serialised):

        x, y = serialised["draw_pos"]
        render_layer = serialised["render_layer"]
        _sprite_paths = serialised["sprite_paths"]

        # unpack sprite paths
        sprite_paths = []
        from scripts.engine.core.definitions import TraitSpritePathsData

        for sprite_path in _sprite_paths:
            sprite_paths.append(TraitSpritePathsData(**sprite_path))

        # convert sprite paths to sprites
        from scripts.engine import utility

        sprites = utility.build_sprites_from_paths(sprite_paths)

        return Aesthetic(sprites.idle, sprites, sprite_paths, render_layer, (x, y))


class Tracked(RegisteredComponent):
    """
    A component to hold info on activities of an entity
    """

    def __init__(self, time_spent: int = 0):
        self.time_spent: int = time_spent

    def serialize(self):
        return self.time_spent

    @classmethod
    def deserialize(cls, serialised):
        return Tracked(serialised)


class Resources(RegisteredComponent):
    """
    An entity's resources. Members align to Resource constants.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health: int = health
        self.stamina: int = stamina

    def serialize(self):
        return self.health, self.stamina

    @classmethod
    def deserialize(cls, serialised):
        return Resources(*serialised)


class Blocking(RegisteredComponent):
    """
    An entity's blocking of other objects.
    """

    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement: bool = blocks_movement
        self.blocks_sight: bool = blocks_sight

    def serialize(self):
        return self.blocks_movement, self.blocks_sight

    @classmethod
    def deserialize(cls, serialised):
        return Blocking(*serialised)


class Identity(RegisteredComponent):
    """
    An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description

    def serialize(self):
        return self.name, self.description

    @classmethod
    def deserialize(cls, serialised):
        return cls(*serialised)


class Traits(RegisteredComponent):
    """
    An entity's traits. Class, archetype, skill set or otherwise defining group.
    """

    def __init__(self, trait_names: List[str]):
        self.names: List[str] = trait_names

    def serialize(self):
        return self.names

    @classmethod
    def deserialize(cls, serialised):
        return Traits(serialised)


class Thought(RegisteredComponent):
    """
    An ai behaviour to control an entity.
    """

    def __init__(self, behaviour: Behaviour):
        self.behaviour = behaviour

    def serialize(self):
        _dict = {"behaviour_name": self.behaviour.__class__.__name__, "entity": self.behaviour.entity}

        return _dict

    @classmethod
    def deserialize(cls, serialised):
        from scripts.engine import action

        behaviour = action.behaviour_registry[serialised["behaviour_name"]]

        return Thought(behaviour(serialised["entity"]))


class Knowledge(RegisteredComponent):
    """
    An entity's knowledge, including skills.
    """

    def __init__(
        self,
        skills: List[Type[Skill]],
        skill_order: Optional[List[str]] = None,
        cooldowns: Optional[Dict[str, int]] = None,
    ):
        skills = skills or []
        skill_order = skill_order or []
        cooldowns = cooldowns or {}

        # determine if we need to add cooldowns or not - must be before setting self
        if cooldowns:
            _set_cooldown = False
        else:
            _set_cooldown = True

        # dont override skill order if it has been provided
        if skill_order:
            _add_to_order = False
        else:
            _add_to_order = True

        self.skill_order: List[str] = skill_order
        self.cooldowns: Dict[str, int] = cooldowns
        self.skill_names: List[str] = []
        self.skills: Dict[str, Type[Skill]] = {}  # dont set skills here, use learn skill

        for skill_class in skills:
            self.learn_skill(skill_class, _add_to_order, _set_cooldown)

    def set_skill_cooldown(self, name: str, value: int):
        """
        Sets the cooldown of a skill
        """
        self.cooldowns[name] = max(0, value)

    def learn_skill(self, skill: Type[Skill], add_to_order: bool = True, set_cooldown: bool = True):
        """
        Learn a new skill.
        """
        self.skill_names.append(skill.__name__)
        self.skills[skill.__name__] = skill
        if add_to_order:
            self.skill_order.append(skill.__name__)
        if set_cooldown:
            self.cooldowns[skill.__name__] = 0

    def serialize(self):
        _dict = {"skill_names": self.skill_names, "cooldowns": self.cooldowns, "skill_order": self.skill_order}
        return _dict

    @classmethod
    def deserialize(cls, serialised):
        skill_names = serialised["skill_names"]
        cooldowns = serialised["cooldowns"]
        skill_order = serialised["skill_order"]

        skills = []
        from scripts.engine import action

        for name in skill_names:
            skills.append(action.skill_registry[name])

        return Knowledge(skills, skill_order, cooldowns)


class Afflictions(RegisteredComponent):
    """
    An entity's Boons and Banes. held in .active as a list of Affliction.
    """

    def __init__(
        self,
        active: Optional[List[Affliction]] = None,
        stat_modifiers: Optional[Dict[str, Tuple[PrimaryStatType, int]]] = None,
    ):
        active = active or []
        stat_modifiers = stat_modifiers or {}

        self.active: List[Affliction] = active
        self.stat_modifiers: Dict[str, Tuple[PrimaryStatType, int]] = stat_modifiers

    def serialize(self):
        active = {}
        for affliction in self.active:
            active[affliction.__class__.__name__] = (
                affliction.origin,
                affliction.affected_entity,
                affliction.duration,
            )

        _dict = {"active": active, "stat_modifiers": self.stat_modifiers}

        return _dict

    @classmethod
    def deserialize(cls, serialised):
        active_dict = serialised["active"]

        active_instances = []
        from scripts.engine import action

        for name, value_tuple in active_dict.items():
            _affliction = action.affliction_registry[name]
            affliction = _affliction(value_tuple[0], value_tuple[1], value_tuple[2])
            active_instances.append(affliction)

        return Afflictions(active_instances, serialised["stat_modifiers"])

    def add(self, affliction: Affliction):
        self.active.append(affliction)

    def remove(self, affliction: Affliction):
        if affliction in self.active:
            # if it is affect_stat remove the affect
            if EffectType.AFFECT_STAT in affliction.identity_tags:
                self.stat_modifiers.pop(affliction.__class__.__name__)

            # remove from active list
            self.active.remove(affliction)


class Aspect(RegisteredComponent):
    """
    An entity's aspects. A static tile modifier. Held in a dict as {aspect_name: duration}
    """

    def __init__(self, aspects: Optional[Dict[str, int]] = None):
        aspects = aspects or {}
        self.aspects: Dict[str, int] = aspects

    def serialize(self):
        return self.aspects

    @classmethod
    def deserialize(cls, serialised):
        return Aspect(*serialised)


class Opinion(RegisteredComponent):
    """
    An entity's views on other entities. {entity, opinion}
    """

    def __init__(self, opinions: Optional[Dict[int, int]] = None):
        opinions = opinions or {}
        self.opinions: Dict[int, int] = opinions

    def serialize(self):
        return self.opinions

    @classmethod
    def deserialize(cls, serialised):
        return Opinion(*serialised)


class FOV(RegisteredComponent):
    """
    An entity's field of view. Always starts blank.
    """

    def __init__(self):
        from scripts.engine import world

        game_map = world.get_game_map()
        self.map: np.array = game_map.block_sight_map

    def serialize(self):
        fov_map = self.map.tolist()
        return fov_map

    @classmethod
    def deserialize(cls, serialised):
        fov = FOV()
        fov.map = np.array(serialised)
        return fov


class LightSource(RegisteredComponent):
    """
    An emitter of light. Takes the light_id from a Light. The Light must be added to the Lightbox of the
    Gamemap separately.
    """

    def __init__(self, light_id: str, radius: int):
        self.light_id: str = light_id
        self.radius: int = radius

    def serialize(self):
        return self.light_id

    @classmethod
    def deserialize(cls, serialised):
        return LightSource(*serialised)
