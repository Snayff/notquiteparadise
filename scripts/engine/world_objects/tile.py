from __future__ import annotations

import logging
from typing import Any, Dict, TYPE_CHECKING

from scripts.engine.core.constants import TILE_SIZE

if TYPE_CHECKING:
    import pygame


class Tile:
    """
    A Tile on the GameMap.
    """

    def __init__(self, x: int, y: int, sprite: pygame.Surface, sprite_path: str, blocks_sight: bool = False,
            blocks_movement: bool = False):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite_path = sprite_path
        self.is_visible = False
        self.blocks_sight = blocks_sight
        self.blocks_movement = blocks_movement

    def serialise(self) -> Dict[str, Any]:
        """
        Serialise the Tile
        """
        _dict = {
            "x": self.x,
            "y": self.y,
            "sprite_path": self.sprite_path,
            "is_visible": self.is_visible,
            "blocks_sight": self.blocks_sight,
            "blocks_movement": self.blocks_movement
        }
        return _dict

    def deserialise(self, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the Tile.
        """
        try:
            self.x = serialised["x"]
            self.y = serialised["y"]
            self.sprite_path = serialised["sprite_path"]
            from scripts.engine import utility
            self.sprite = utility.get_image(self.sprite_path, (TILE_SIZE, TILE_SIZE))
            self.is_visible = serialised["is_visible"]
            self.blocks_sight = serialised["blocks_sight"]
            self.blocks_movement = serialised["blocks_movement"]

        except KeyError:
            logging.error(f"Tile:Deserialise: Incorrect key given. Data not loaded correctly.")
