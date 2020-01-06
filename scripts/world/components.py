from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame


class Position:
    """
    An entity's position on the map.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Aesthetic:
    """
    An entity's sprite.
    """
    def __init__(self, sprite: pygame.Surface):
        self.sprite = sprite