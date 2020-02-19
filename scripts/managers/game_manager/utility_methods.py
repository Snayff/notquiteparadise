from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pygame

from scripts.core.constants import IMAGE_NOT_FOUND_PATH

if TYPE_CHECKING:
    from scripts.managers.game_manager.game_manager import GameManager
    from typing import Tuple


class UtilityMethods:
    """
    Methods for general utility
    """

    def __init__(self, manager):
        self._manager = manager  # type: GameManager

    def get_image(self, img_path: str, desired_dimensions: Tuple[int, int] = None) -> pygame.Surface:
        """
        Get the specified image and resize if dimensions provided. Dimensions are in (width, height) format.
        """
        # try and get the image
        try:
            image = pygame.image.load(img_path).convert_alpha()
        except:
            image = pygame.image.load(IMAGE_NOT_FOUND_PATH).convert_alpha()

        # resize if needed
        if desired_dimensions:
            width, height = desired_dimensions
            image = pygame.transform.smoothscale(image, (width, height))

        return image