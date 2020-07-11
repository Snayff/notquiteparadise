from __future__ import annotations

from typing import Any, TYPE_CHECKING, Tuple

from snecs import RegisteredComponent

from scripts.engine.core.constants import PrimaryStatType

if TYPE_CHECKING:
    import pygame
    import tcod.map
    from typing import List, Dict, Optional
    from scripts.engine.thought import AIBehaviour
    from snecs.typedefs import EntityID
    from scripts.engine.core.definitions import TraitSpritesData
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


class IsGod(RegisteredComponent):
    """
    Whether the entity is a god.
    """
    # TODO - replace need for this with the appropriate AI
    __slots__ = ()


class HasCombatStats(RegisteredComponent):
    """
    A flag to show if an entity has stats used for combat.
    """
    __slots__ = ()
    # TODO - move stats to here, set base stats on init then hold modification value


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

    def __init__(self, current_sprite: pygame.Surface, sprites: TraitSpritesData, draw_x: float, draw_y: float):
        # TODO - add render layer/order
        self.current_sprite = current_sprite
        self.sprites = sprites

        self.draw_x: float = draw_x
        self.draw_y: float = draw_y
        self.target_draw_x: float = draw_x
        self.target_draw_y: float = draw_y
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


class Trait(RegisteredComponent):
    """
    An entity's traits. Class, archetype, skill set or otherwise defining group.
    """

    def __init__(self, trait_names: List[str]):
        self.names: List[str] = trait_names


class Behaviour(RegisteredComponent):
    """
    An ai behaviour to control an entity.
    """

    # TODO - inherit from AIBehaviour
    def __init__(self, behaviour: AIBehaviour):
        self.behaviour = behaviour


class Knowledge(RegisteredComponent):
    """
    An entity's knowledge, including skills. Skills are held as skill_name : {Skill, cooldown}.
    """

    def __init__(self, skills: Dict[str, Dict[str, Any]] = None, skill_order: List[str] = None):
        if skills is None:
            skills = {}
        if skill_order is None:
            skill_order = []

        self.skill_order = skill_order  # list of skill names, to allow access by index
        self.skills: Dict[str, Dict[str, Any]] = skills  # skill_name : {Skill, cooldown}
            # FIXME - how is it str and Skill? Can't be both


class Afflictions(RegisteredComponent):
    """
    An entity's Boons and Banes. held in .active as {affliction_name: affliction_instance}.
    """
    def __init__(self, active: List[Affliction] = None):
        if active is None:
            active = []
        for a in active:
            if type(a) == int:
                raise Exception('asda')
        self.active: List[Affliction] = active
        self.stat_modifiers: Dict[str, Tuple[PrimaryStatType, int]] = {}


class Aspect(RegisteredComponent):
    # TODO - inherit from dict and add to that
    # TODO - combine aspect and terrain
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
    An entity's field of view.
    """

    def __init__(self, fov_map: tcod.map.Map):
        self.map: tcod.map.Map = fov_map
