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

    def recursive_replace(self, obj, key, value_to_replace, new_value):
        """
        Check through any number of nested dicts or lists for the specified key->value pair and replace the value.

        Args:
            obj (object): dict, list, string, or anything else to be checked.
            key (str): The key to look for in the object
            value_to_replace (): The value to look for, stored against the key.
            new_value (): The value to set.
        """
        if isinstance(obj, dict):
            # Break the dict out and run recursively against the elements
            for k, v in obj.items():
                if k == key:
                    # The value may be a list so handle it if so
                    if isinstance(v, list):
                        # Loop the list and replace the required value
                        for index, item in enumerate(v):
                            if item == value_to_replace:
                                v[index] = new_value
                    elif v == value_to_replace:
                        obj[key] = new_value
                else:
                    self.recursive_replace(v, key, value_to_replace, new_value)

        elif isinstance(obj, list):
            # Break the list out and run recursively against the elements
            for element in obj:
                self.recursive_replace(element, key, value_to_replace, new_value)