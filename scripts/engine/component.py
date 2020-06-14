from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Any
from snecs import RegisteredComponent
from scripts.engine.core.constants import InteractionCauseType, Effect

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict, Optional
    from scripts.engine.thought import AIBehaviour
    import tcod.map
    from snecs.typedefs import EntityID
    from scripts.engine.core.definitions import CharacteristicSpritesData, InteractionData
    from scripts.nqp.skills import Skill


##########################################################
# Components are to hold data that is subject to change.
#########################################################

########################### FLAGS ##############################

class IsPlayer(RegisteredComponent):
    """
    Whether the entity is the player.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class IsGod(RegisteredComponent):
    """
    Whether the entity is a god.
    """
    __slots__ = ()


class IsProjectile(RegisteredComponent):
    """
    Whether the entity is a projectile.
    """

    def __init__(self, creator: EntityID):
        self.creator = creator


class IsActor(RegisteredComponent):
    """
    Whether the entity is an actor.
    """
    __slots__ = ()


class HasCombatStats(RegisteredComponent):
    """
    A flag to show if an entity has stats used for combat.
    """
    __slots__ = ()


#################### OTHERS #########################


class Position(RegisteredComponent):
    """
    An entity's position on the map.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Aesthetic(RegisteredComponent):
    """
    An entity's sprite.
    """

    def __init__(self, current_sprite: pygame.Surface, sprites: CharacteristicSpritesData, screen_x: float,
            screen_y: float):
        # TODO - add render layer/order
        self.current_sprite = current_sprite
        self.sprites = sprites

        self.screen_x: float = screen_x
        self.screen_y: float = screen_y
        self.target_screen_x: float = screen_x
        self.target_screen_y: float = screen_y
        self.current_sprite_duration: float = 0


class Tracked(RegisteredComponent):
    """
    A component to hold info on activities of an entity
    """

    def __init__(self, time_spent: int = 0):
        self.time_spent: int = time_spent


class Resources(RegisteredComponent):
    """
    An entity's resources. Members align to Resource constants.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health: int = health
        self.stamina: int = stamina


class Blocking(RegisteredComponent):
    """
    An entity's blocking of other objects.
    """

    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement: bool = blocks_movement
        self.blocks_sight: bool = blocks_sight


class Identity(RegisteredComponent):
    """
    An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description


class People(RegisteredComponent):
    # TODO - inherit from str and add name directly
    """
    An entity's people.
    """

    def __init__(self, people_name: str):
        self.name: str = people_name


class Savvy(RegisteredComponent):
    # TODO - inherit from str and add name directly
    """
    An entity's savvy.
    """

    def __init__(self, savvy_name: str):
        self.name: str = savvy_name


class Homeland(RegisteredComponent):
    # TODO - inherit from str and add name directly
    """
    An entity's homeland.
    """

    def __init__(self, homeland_name: str):
        self.name: str = homeland_name


class Behaviour(RegisteredComponent):
    """
    An ai behaviour to control an entity.
    """

    # TODO - inherit from AIBehaviour
    def __init__(self, behaviour: AIBehaviour):
        self.behaviour = behaviour


class Knowledge(RegisteredComponent):
    """
    An entity's knowledge, including skills.
    """

    def __init__(self, skills: Dict[str, Dict[str, Any]] = None, skill_order: List[str] = None):
        if skills is None:
            skills = {}
        if skill_order is None:
            skill_order = []

        self.skill_order = skill_order  # list of skill names, to allow access by index
        self.skills: Dict[str, Dict[str, Any]] = skills  # skill_name : {Skill, cooldown}


class Afflictions(Dict[str, int], RegisteredComponent):
    """
    An entity's Boons and Banes. held in dict as {affliction_name: duration}
    """
    pass


class Aspect(RegisteredComponent):
    # TODO - inherit from dict and add to that
    """
    An entity's aspects. A static tile modifier. Held in a dict as {aspect_name: duration}
    """

    def __init__(self, aspects: Optional[Dict[str, int]] = None):
        if aspects is None:
            aspects = {}
        self.aspects: Dict[str, int] = aspects


class Opinion(RegisteredComponent):
    # TODO - inherit from dict and add to that
    """
    An entity's views on other entities. {entity, opinion}
    """

    def __init__(self):
        self.opinions: Dict[int, int] = {}


class FOV(RegisteredComponent):
    """
    An entities field of view.
    """

    def __init__(self, fov_map: tcod.map.Map):
        self.map: tcod.map.Map = fov_map


class Interactions(Dict[InteractionCauseType, List[Effect]], RegisteredComponent):
    """
    The effects triggered when a specific criteria is met.
    """
    pass
