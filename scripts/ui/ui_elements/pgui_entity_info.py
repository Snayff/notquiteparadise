import logging
from typing import Union

import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIImage, UITextBox

from scripts.core.constants import PrimaryStatTypes, SecondaryStatTypes
from scripts.world.entity import Entity


class PGEntityInfo(UIWindow):
    """
    Hold text relating to the game's events, to display to the player.
    """

    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager):
        self.gui_manager = manager

        # sections
        self.selected_entity = None
        self.entity_image = None
        self.core_info = None
        self.primary_stats = None
        self.secondary_stats = None

        # data
        self.gap_between_sections = 2
        self.indent = 3
        self.entity_image_height = 32
        self.entity_image_width = 32
        self.core_info_height = 80
        self.primary_stats_height = 100
        self.secondary_stats_height = 100

        # complete base class init
        super().__init__(rect, manager, ["entity_info"])

        # confirm init complete
        logging.debug(f"Entity Info initialised.")

    def set_entity(self, entity: Union[Entity, None]):
        self.selected_entity = entity

    def show(self):
        if self.selected_entity:
            # create the various boxes for the info
            self.entity_image = self.create_entity_image_section()
            self.core_info = self.create_core_info_section()
            self.primary_stats = self.create_primary_stats_section()
            self.secondary_stats = self.create_secondary_stats_section()

    def hide(self):
        # kill the boxes
        self.entity_image = None
        self.core_info = None
        self.primary_stats = None
        self.secondary_stats = None

    def create_entity_image_section(self):
        image_width = self.entity_image_width
        image_height = self.entity_image_height
        centre_draw_x = int((self.rect.width / 2) - (image_width / 2))
        rect = pygame.Rect((centre_draw_x, self.indent), (image_width, image_height))
        image = pygame.transform.scale(self.selected_entity.icon, (image_width, image_height))

        entity_image = UIImage(relative_rect=rect, image_surface=image, manager=self.gui_manager,
                               container=self.get_container(), object_id="#entity_image")
        return entity_image

    def create_core_info_section(self):
        entity = self.selected_entity
        text = f"{entity.name.capitalize()}" + "<br>"
        text += f"Current Health: {entity.combatant.hp}" + "<br>"
        text += f"Current Stamina: {entity.combatant.stamina}" + "<br>"

        x = self.indent
        y = (self.gap_between_sections * 2) + self.indent + self.entity_image_height
        width = self.rect.width - (self.indent * 2)
        height = self.core_info_height

        rect = pygame.Rect((x, y), (width, height))
        core_info = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#core_info",
                              container=self.get_container())
        return core_info

    def create_primary_stats_section(self):
        text = ""
        stats = self.selected_entity.combatant.primary_stats

        for stat in PrimaryStatTypes:
            try:
                stat_value = getattr(stats, stat.name.lower())
                name = stat.name.title()
                name = name.replace("_", " ")

                text += f"{name}: {stat_value}" + "<br>"

            # in case it fails to pull expected attribute
            except AttributeError:
                logging.warning(f"Attribute {stat} not found for EntityInfo.")

        x = self.indent
        y = (self.gap_between_sections * 3) + self.indent + self.entity_image_height + self.core_info_height
        width = self.rect.width - (self.indent * 2)
        height = self.primary_stats_height
        rect = pygame.Rect((x, y), (width, height))
        primary_stats = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                                  wrap_to_height=False, layer_starting_height=1, object_id="#primary_stats",
                                  container=self.get_container())
        return primary_stats

    def create_secondary_stats_section(self):
        text = ""
        stats = self.selected_entity.combatant.secondary_stats

        for stat in SecondaryStatTypes:
            try:
                stat_value = getattr(stats, stat.name.lower())
                name = stat.name.title()
                name = name.replace("_", " ")

                text += f"{name}: {stat_value}" + "<br>"

            # in case it fails to pull expected attribute
            except AttributeError:
                logging.warning(f"Attribute {stat} not found for EntityInfo.")

        x = self.indent
        y = (self.gap_between_sections * 3) + self.indent + self.entity_image_height + self.core_info_height + \
            self.primary_stats_height
        width = self.rect.width - (self.indent * 2)
        height = self.secondary_stats_height
        rect = pygame.Rect((x, y), (width, height))
        secondary_stats = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#secondary_stats",
                              container=self.get_container())
        return secondary_stats