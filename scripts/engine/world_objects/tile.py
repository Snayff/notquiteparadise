from __future__ import annotations

import logging

from typing import TYPE_CHECKING, Any, Dict

from scripts.engine.core.constants import TILE_SIZE

if TYPE_CHECKING:
    import pygame


class Tile:
    """
    A Tile on the Gamemap.
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

    @classmethod
    def deserialise(cls, serialised: Dict[str, Any]):
        """
        Loads the details from the serialised data back into the Tile.
        """
        try:
            x = serialised["x"]
            y = serialised["y"]
            sprite_path = serialised["sprite_path"]
            from scripts.engine import utility
            sprite = utility.get_image(sprite_path)
            is_visible = serialised["is_visible"]
            blocks_sight = serialised["blocks_sight"]
            blocks_movement = serialised["blocks_movement"]

            tile = Tile(x, y, sprite, sprite_path, blocks_sight, blocks_movement)
            tile.is_visible = is_visible
            return tile

        except KeyError as e:
            logging.warning(f"Tile.Deserialise: Incorrect key ({e.args[0]}) given. Data not loaded correctly.")
            raise Exception  # throw exception to hit outer error handler and exit
