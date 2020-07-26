from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING, Any, Tuple

from snecs import RegisteredComponent
import numpy as np
from scripts.engine.core.constants import (EffectType, PrimaryStatType,
                                           RenderLayerType)

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict, Optional, Type, Tuple
    from scripts.engine.thought import AIBehaviour
    from snecs.typedefs import EntityID
    from scripts.nqp.actions.skills import Skill
    from scripts.engine.core.definitions import SpritePathsData, SpritesData
    from scripts.nqp.actions.afflictions import Affliction


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
    def deserialize(cls, serialized):
        return IsPlayer()


class IsActor(RegisteredComponent):
    """
    Whether the entity is an actor.
    """
    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialized):
        return IsActor()


class IsGod(RegisteredComponent):
    """
    Whether the entity is a god.
    """
    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialized):
        return IsGod()


class HasCombatStats(RegisteredComponent):
    """
    A flag to show if an entity has stats used for combat.
    """
    __slots__ = ()

    def serialize(self):
        return True

    @classmethod
    def deserialize(cls, serialized):
        return HasCombatStats()


#################### OTHERS #########################

class Position(RegisteredComponent):
    """
    An entity's position on the map. At initiation provide all positions the entity holds. After initiation only need
     to set the top left, or reference position as the other coordinates are held as offsets.
    """

    def __init__(self, *positions: Tuple[int, int]):
        # Sort the positions from top-left to down-right
        if not positions:
            raise ValueError('Must provide at least 1 coordinate for the entity.')

        sorted_positions = sorted(positions, key=lambda x: (x[0]**2 + x[1]**2))
        top_left = sorted_positions[0]
        self.offsets = [(x - top_left[0], y - top_left[1]) for x, y in sorted_positions]
        self.reference_position = top_left

    def serialize(self):
        return self.coordinates

    @classmethod
    def deserialize(cls, serialized):
        return Position(*serialized)

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
            np.sqrt((center[0] - transformed[i[0]][0])**2 + (center[1] - transformed[i[0]][1])**2) for i in arg_max
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

    def __init__(self, current_sprite: pygame.Surface, sprites: SpritesData,
            sprite_paths: List[SpritePathsData], render_layer: RenderLayerType, draw_pos: Tuple[float, float]):
        self._sprite_paths: List[SpritePathsData] = sprite_paths
        self.current_sprite: pygame.Surface = current_sprite
        self.sprites: SpritesData = sprites
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
            "sprite_paths": sprite_paths
        }
        return _dict

    @classmethod
    def deserialize(cls, serialized):

        x, y = serialized["draw_pos"]
        render_layer = serialized["render_layer"]
        _sprite_paths = serialized["sprite_paths"]

        # unpack sprite paths
        sprite_paths = []
        for sprite_path in _sprite_paths:
            sprite_paths.append(SpritePathsData(**sprite_path))

        # convert sprite paths to sprites
        from scripts.engine import world
        sprites = world.build_sprites_from_paths(sprite_paths)

        return Aesthetic(sprites.idle, sprites, sprite_paths, render_layer, (x, y))


class Tracked(RegisteredComponent):
    """
    A component to hold info on activities of an entity
    """

    def __init__(self, time_spent: int = 0):
        self.time_spent: int = time_spent

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Resources(RegisteredComponent):
    """
    An entity's resources. Members align to Resource constants.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health: int = health
        self.stamina: int = stamina

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Blocking(RegisteredComponent):
    """
    An entity's blocking of other objects.
    """

    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement: bool = blocks_movement
        self.blocks_sight: bool = blocks_sight

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Identity(RegisteredComponent):
    """
    An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Traits(RegisteredComponent):
    """
    An entity's traits. Class, archetype, skill set or otherwise defining group.
    """

    def __init__(self, trait_names: List[str]):
        self.names: List[str] = trait_names

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Behaviour(RegisteredComponent):
    """
    An ai behaviour to control an entity.
    """

    def __init__(self, behaviour: AIBehaviour):
        self.behaviour = behaviour

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Knowledge(RegisteredComponent):
    """
    An entity's knowledge, including skills. Skills are held as skill_name : {Skill, cooldown}.
    """

    def __init__(self, skills: List[Type[Skill]], skill_order: Optional[List[str]] = None):
        skills = skills or []
        skill_order = skill_order or []

        self.skill_order: List[str] = skill_order
        self.cooldowns: Dict[str, int] = {}
        self.skill_names: List[str] = []
        self.skills: Dict[str, Type[Skill]] = {}

        for skill_class in skills:
            self.learn_skill(skill_class, add_to_order=False)

    def set_skill_cooldown(self, name: str, value: int):
        """
        Sets the cooldown of a skill
        """
        self.cooldowns[name] = max(0, value)

    def learn_skill(self, skill_class, add_to_order=True):
        """
        Learn a new skill
        """
        self.cooldowns[skill_class.name] = 0
        self.skill_names.append(skill_class.name)
        if add_to_order:
            self.skill_order.append(skill_class.name)
        self.skills[skill_class.name] = skill_class

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Afflictions(RegisteredComponent):
    """
    An entity's Boons and Banes. held in .active as a list of Affliction.
    """
    def __init__(self, active: List[Affliction] = None):
        if active is None:
            active = []

        self.active: List[Affliction] = active
        self.stat_modifiers: Dict[str, Tuple[PrimaryStatType, int]] = {}

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)

    def add(self, affliction: Affliction):
        self.active.append(affliction)

    def remove(self, affliction: Affliction):
        if affliction in self.active:
            # if it is affect_stat remove the affect
            if EffectType.AFFECT_STAT in affliction.identity_tags:
                self.stat_modifiers.pop(affliction.name)

            # remove from active list
            self.active.remove(affliction)


class Aspect(RegisteredComponent):
    """
    An entity's aspects. A static tile modifier. Held in a dict as {aspect_name: duration}
    """

    def __init__(self, aspects: Optional[Dict[str, int]] = None):
        if aspects is None:
            aspects = {}
        self.aspects: Dict[str, int] = aspects

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class Opinion(RegisteredComponent):
    """
    An entity's views on other entities. {entity, opinion}
    """

    def __init__(self):
        self.opinions: Dict[int, int] = {}

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)


class FOV(RegisteredComponent):
    """
    An entity's field of view.
    """

    def __init__(self, fov_map: np.array):
        self.map: np.array = fov_map
        self.algorithm = 0
        self.light_walls = True

    def serialize(self):
        return (self.first, self.second)

    @classmethod
    def deserialize(cls, serialized):
        return cls(*serialized)
