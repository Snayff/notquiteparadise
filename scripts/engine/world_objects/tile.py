from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame


class Tile:
    """
    A Tile on the GameMap.
    """

    def __init__(self, x: int, y: int, sprite: pygame.Surface, blocks_sight: bool = False,
            blocks_movement: bool = False):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.is_visible = False
        self.blocks_sight = blocks_sight
        self.blocks_movement = blocks_movement
