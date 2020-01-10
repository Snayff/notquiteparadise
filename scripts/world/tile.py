from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.managers.world_manager import world
from scripts.world.components import Position, Blocking

if TYPE_CHECKING:
    import pygame


class Tile:
    """
    A Tile on the GameMap. Can contain an Entity, a Terrain and an Effect.

    Attributes:
        x(int): tile_x
        y(int): tile_y
        is_visible(bool): if tile is visible to player
        sprite(pygame.Surface): the sprite of the floor.
    """

    def __init__(self, x: int, y: int, sprite: pygame.Surface, blocks_sight: bool = False, blocks_movement: bool =
    False):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.is_visible = False
        self._blocks_sight = blocks_sight
        self._blocks_movement = blocks_movement

    @property
    def has_entity(self):
        """
        Check if the tag is applicable

        Returns:
            bool: True if tag is applicable
        """
        entities = world.Entity.get_entities(Position)
        for entity in entities:
            pos = world.Entity.get_entitys_component(entity, Position)
            if pos.x == self.x and pos.y == self.y:
                return True

        return False

    @property
    def blocks_movement(self):
        """
        If anything on tile blocks ability to move

        Returns:
            bool: True if movement is blocked.
        """
        if self._blocks_movement:
            return True

        entities = world.Entity.get_entities(Position, Blocking)
        for entity in entities:
            pos = world.Entity.get_entitys_component(entity, Position)
            blocking = world.Entity.get_entitys_component(entity, Blocking)
            if pos.x == self.x and pos.y == self.y and blocking.blocks_movement:
                return True

        return False

    @property
    def blocks_sight(self):
        """
        If anything on tile blocks ability to see

        Returns:
            bool: True if sight is blocked.
        """
        if self._blocks_sight:
            return True

        entities = world.Entity.get_entities(Position, Blocking)
        for entity in entities:
            pos = world.Entity.get_entitys_component(entity, Position)
            blocking = world.Entity.get_entitys_component(entity, Blocking)
            if pos.x == self.x and pos.y == self.y and blocking.blocks_sight:
                return True

        return False



