from __future__ import annotations

from typing import TYPE_CHECKING
from scripts.engine.core.definitions import CharacteristicSpritesData

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict

##########################################################
# Components are to hold data that is subject to change.
#########################################################


class Component:
    """ Base component"""
    pass


class IsPlayer(Component):
    """
    [Component] Whether the entity is the player.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Position(Component):
    """
    [Component] An entity's position on the map.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Aesthetic(Component):
    """
    [Component] An entity's sprite.
    """

    def __init__(self, current_sprite: pygame.Surface, sprites: CharacteristicSpritesData):
        self.current_sprite = current_sprite
        self.sprites = sprites

        self.screen_x: float = 0
        self.screen_y: float = 0
        self.target_screen_x: float = 0
        self.target_screen_y: float = 0
        self.current_sprite_duration = 0


class Resources(Component):
    """
    [Component] An entity's resources.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health = health
        self.stamina = stamina
        self.time_spent = 0


class Blocking(Component):
    """
    [Component] An entity's blocking of other objects.
    """

    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight


class Identity(Component):
    """
    [Component] An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description


class Race(Component):
    """
    [Component] An entity's people.
    """

    def __init__(self, people_name: str):
        self.name = people_name


class Savvy(Component):
    """
    [Component] An entity's savvy.
    """

    def __init__(self, savvy_name: str):
        self.name = savvy_name


class Homeland(Component):
    """
    [Component] An entity's homeland.
    """

    def __init__(self, homeland_name: str):
        self.name = homeland_name


class AIBasic(Component):
    """
    [Component] An ai to control an entity.
    """


class HasCombatStats(Component):
    """[Component] A flag to show if an entity has stats used for combat."""
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Knowledge(Component):
    """[Component] An entity's knowledge, including skills."""
    def __init__(self, skills: List[str] = None):
        if skills is None:
            skills = []
        self.skills = skills


class Affliction(Component):
    """[Component] An entity's Boons and Banes. e.g. {boon_name: duration}"""
    def __init__(self, boons: Dict = None, banes: Dict = None):
        if banes is None:
            banes = {}
        if boons is None:
            boons = {}
        self.boons = boons
        self.banes = banes


class Aspect(Component):
    """[Component] An entity's aspects. A static tile modifier. e.g. {aspect_name: duration} """
    def __init__(self, aspects: Dict = None):
        if aspects is None:
            aspects = {}
        self.aspects = aspects


class IsGod(Component):
    """
    [Component] Whether the entity is a god.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Opinion(Component):
    """
    [Component] An entity's views on other entities.
    """
    def __init__(self):
        self.opinions = {}