from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame
    from typing import List, Dict

##########################################################
# Components are to hold data that is subject to change.
#########################################################


class IsPlayer:
    """
    [Component] Whether the entity is the player.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Position:
    """
    [Component] An entity's position on the map.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Aesthetic:
    """
    [Component] An entity's sprite.
    """

    def __init__(self, sprite: pygame.Surface, icon: pygame.Surface):
        self.icon = icon
        self.sprite = sprite
        # TODO - add screen pos here and use that in drawing


class Resources:
    """
    [Component] An entity's resources.
    """

    def __init__(self, health: int = 1, stamina: int = 1):
        self.health = health
        self.stamina = stamina
        self.time_spent = 0


class Blocking:
    """
    [Component] An entity's blocking of other objects.
    """

    def __init__(self, blocks_movement: bool = False, blocks_sight: bool = False):
        self.blocks_movement = blocks_movement
        self.blocks_sight = blocks_sight


class Identity:
    """
    [Component] An entity's identity, such as name and description.
    """

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description


class Race:
    """
    [Component] An entity's people.
    """

    def __init__(self, people_name: str):
        self.name = people_name


class Savvy:
    """
    [Component] An entity's savvy.
    """

    def __init__(self, savvy_name: str):
        self.name = savvy_name


class Homeland:
    """
    [Component] An entity's homeland.
    """

    def __init__(self, homeland_name: str):
        self.name = homeland_name


class AIBasic:
    """
    [Component] An ai to control an entity.
    """


class HasCombatStats:
    """[Component] A flag to show if an entity has stats used for combat."""
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance

class Knowledge:
    """[Component] An entity's knowledge, including skills."""
    def __init__(self, skills: List[str] = None):
        if skills is None:
            skills = []
        self.skills = skills


class Affliction:
    """[Component] An entity's Boons and Banes. e.g. {boon_name: duration}"""
    def __init__(self, boons: Dict = None, banes: Dict = None):
        if banes is None:
            banes = {}
        if boons is None:
            boons = {}
        self.boons = boons
        self.banes = banes


class Aspect:
    """[Component] An entity's aspects. A static tile modifier. e.g. {aspect_name: duration} """
    def __init__(self, aspects: Dict = None):
        if aspects is None:
            aspects = {}
        self.aspects = aspects


class IsGod:
    """
    [Component] Whether the entity is a god.
    """
    __slots__ = ()  # reduces memory footprint as it prevents the creation of __dict__ and __weakref__ per instance


class Opinion:
    """
    [Component] An entity's views on other entities.
    """
    def __init__(self):
        self.opinions = {}