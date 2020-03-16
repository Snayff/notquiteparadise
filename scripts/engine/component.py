from __future__ import annotations

import tcod.map
from abc import ABC
from typing import TYPE_CHECKING
from scripts.engine.ai import AIBehaviour
from scripts.engine.core.constants import InteractionCauseType
from scripts.engine.core.definitions import CharacteristicSpritesData, InteractionData

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict, Optional

##########################################################
# Components are to hold data that is subject to change.
#########################################################


class Component(ABC):
    """
    Base component
    """
    pass


class IsPlayer(Component):
    """
    Whether the entity is the player.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Position(Component):
    """
    An entity's position on the map.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Aesthetic(Component):
    """
    An entity's sprite.
    """
    def __init__(self, current_sprite: pygame.Surface, sprites: CharacteristicSpritesData):
        self.current_sprite = current_sprite
        self.sprites = sprites

        self.screen_x: float = 0
        self.screen_y: float = 0
        self.target_screen_x: float = 0
        self.target_screen_y: float = 0
        self.current_sprite_duration: float = 0


class Resources(Component):
    """
    An entity's resources.
    """
    def __init__(self, health: int = 1, stamina: int = 1):
        self.health: int = health
        self.stamina: int = stamina
        self.time_spent: int = 0


class Blocking(Component):
    """
    An entity's blocking of other objects.
    """
    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement: bool = blocks_movement
        self.blocks_sight: bool = blocks_sight


class Identity(Component):
    """
    An entity's identity, such as name and description.
    """
    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description


class Race(Component):
    """
    An entity's people.
    """
    def __init__(self, people_name: str):
        self.name: str = people_name


class Savvy(Component):
    """
    An entity's savvy.
    """
    def __init__(self, savvy_name: str):
        self.name: str = savvy_name


class Homeland(Component):
    """
    An entity's homeland.
    """
    def __init__(self, homeland_name: str):
        self.name: str = homeland_name


class Behaviour(Component):
    """
    An ai behaviour to control an entity.
    """
    def __init__(self, behaviour: AIBehaviour):
        self.behaviour = behaviour


class HasCombatStats(Component):
    """
    A flag to show if an entity has stats used for combat.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Knowledge(Component):
    """"
    An entity's knowledge, including skills.
    """
    def __init__(self, skills: List[str] = None):
        if skills is None:
            skills = []
        self.skills: List[str] = skills


class Affliction(Component):
    """
    An entity's Boons and Banes. held in dict as {boon_name: duration}
    """
    def __init__(self, boons: Optional[Dict[str, int]] = None, banes: Optional[Dict[str, int]] = None):
        if banes is None:
            banes = {}
        if boons is None:
            boons = {}
        self.boons: Dict[str, int] = boons
        self.banes: Dict[str, int] = banes


class Aspect(Component):
    """
    An entity's aspects. A static tile modifier. Held in a dict as {aspect_name: duration}
    """
    def __init__(self, aspects: Optional[Dict[str, int]] = None):
        if aspects is None:
            aspects = {}
        self.aspects: Dict[str, int] = aspects


class IsGod(Component):
    """
    Whether the entity is a god.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Opinion(Component):
    """
    An entity's views on other entities. {entity, opinion}
    """
    def __init__(self):
        self.opinions: Dict[int, int] = {}


class FOV(Component):
    """
    An entities field of view.
    """
    def __init__(self, fov_map: tcod.map.Map):
        self.map: tcod.map.Map = fov_map


class Interaction(Component):
    """
    The effects triggered when a specific criteria is met
    """
    def __init__(self, interactions: Dict[InteractionCauseType, InteractionData]):
        self.interactions = interactions


class IsProjectile(Component):
    """
    Whether the entity is a projectile.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance