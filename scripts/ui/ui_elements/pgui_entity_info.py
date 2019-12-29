import logging
from typing import Union

import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIImage

from scripts.world.entity import Entity


class PGEntityInfo(UIWindow):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager):
        self.selected_entity = None
        self.entity_image = None
        self.core_info = None
        self.primary_info = None
        self.secondary_info = None
        self.gui_manager = manager

        # complete base class init
        super().__init__(rect, manager, ["entity_info"])

        # confirm init complete
        logging.debug(f"Entity Info initialised.")

    def set_entity(self, entity: Union[Entity, None]):
        self.selected_entity = entity

    def show(self):
        if self.selected_entity:
            # create the various boxes for the info
            self.entity_image = self.create_entity_image_element()

    def create_entity_image_element(self):
        image_width = 32
        image_height = 32
        centre_draw_x = int((self.rect.width / 2) - (image_width / 2))
        rect = pygame.Rect((centre_draw_x, 5), (image_width, image_height))
        image = pygame.transform.scale(self.selected_entity.icon, (image_width, image_height))

        entity_image = UIImage(relative_rect=rect, image_surface=image, manager=self.gui_manager,
                                container=self.get_container(), object_id="#entity_image")
        return entity_image

    def hide(self):
        # kill the boxes
        self.entity_image = None
        self.core_info = None
        self.primary_info = None
        self.secondary_info = None