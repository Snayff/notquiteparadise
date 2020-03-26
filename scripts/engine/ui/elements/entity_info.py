import logging
from typing import Optional

import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIImage, UITextBox
from scripts.engine import existence, utility
from scripts.engine.core.constants import PrimaryStat, SecondaryStat, IMAGE_NOT_FOUND_PATH, INFINITE
from scripts.engine.utility import get_class_members
from scripts.engine.component import Aesthetic, Identity, Resources, Afflictions


class EntityInfo(UIWindow):
    """
    Hold text relating to the game's events, to display to the player.
    """

    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager):
        self.gui_manager = manager

        # FIXME - entity info  doesn't update when entity info changes.

        # sections
        self.selected_entity: Optional[int] = None
        self.entity_image: Optional[pygame.Surface] = None
        self.info_section: Optional[UITextBox] = None

        # data
        self.gap_between_sections = 2
        self.indent = 3
        self.entity_image_height = 32
        self.entity_image_width = 32
        self.core_info_height = 300

        # complete base class init
        super().__init__(rect, manager, ["entity_info"])

        # confirm init complete
        logging.debug(f"Entity Info initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass

    def set_entity(self, ent: int):
        """
        Set the selected entity to show the info for that entity.
        """
        self.selected_entity = ent

    def show(self):
        """
        Show the entity info. Builds the sections required, after clearing any existing.
        """
        if self.selected_entity:
            # clear to refresh first
            self.cleanse()

            # create the various boxes for the info
            self.entity_image = self.create_entity_image_section()
            self.info_section = self.create_info_section()

    def cleanse(self):
        """
        Cleanse existing section info.
        """
        # kill the boxes and clear the references
        if self.entity_image:
            self.entity_image.kill()
            self.entity_image = None
        if self.info_section:
            self.info_section.kill()
            self.info_section = None

    def create_entity_image_section(self):
        """
        Create the image section.

        Returns:
            UIImage:
        """
        image_width = self.entity_image_width
        image_height = self.entity_image_height
        centre_draw_x = int((self.rect.width / 2) - (image_width / 2))
        rect = pygame.Rect((centre_draw_x, self.indent), (image_width, image_height))

        aesthetic = existence.get_entitys_component(self.selected_entity, Aesthetic)
        if aesthetic:
            image = pygame.transform.scale(aesthetic.sprites.icon, (image_width, image_height))
        else:
            image = utility.get_image(IMAGE_NOT_FOUND_PATH)

        entity_image = UIImage(relative_rect=rect, image_surface=image, manager=self.gui_manager,
                               container=self.get_container(), object_id="#entity_image")
        return entity_image

    def create_info_section(self) -> UITextBox:
        """
        Create the core info section.
        """
        ent = self.selected_entity
        gap = "|-----------------------| <br>"

        if ent:
            text = ""

            # basic info
            identity = existence.get_entitys_component(ent, Identity)
            if identity:
                text += f"{identity.name.capitalize()}" + "<br>"
            resources = existence.get_entitys_component(ent, Resources)
            if resources:
                text += f"Current Health: {resources.health}" + "<br>"
                text += f"Current Stamina: {resources.stamina}" + "<br>"

            # add gap
            text += gap

            # afflictions
            afflictions = existence.get_entitys_component(ent, Afflictions)
            if afflictions:
                for affliction, duration in afflictions.items():
                    if duration == INFINITE:
                        duration = "∞"
                    text += f"{affliction} : {duration}" + "<br>"

            # add gap
            text += gap

            # stats info
            stats = existence.get_combat_stats(self.selected_entity)
            primary_stats = utility.get_class_members(PrimaryStat)
            for name in primary_stats:
                try:
                    stat_value = getattr(stats, name.lower())

                    name = name.title()
                    name = name.replace("_", " ")
                    text += f"{name}: {stat_value}" + "<br>"

                # in case it fails to pull expected attribute
                except AttributeError:
                    logging.warning(f"Attribute {name} not found for EntityInfo.")

            # add gap
            text += gap

            secondary_stats = get_class_members(SecondaryStat)
            for name in secondary_stats:
                try:
                    stat_value = getattr(stats, name.lower())

                    name = name.title()
                    name = name.replace("_", " ")
                    text += f"{name}: {stat_value}" + "<br>"

                # in case it fails to pull expected attribute
                except AttributeError:
                    logging.warning(f"Attribute {name} not found for EntityInfo.")

        else:
            text = ""

        x = self.indent
        y = (self.gap_between_sections * 2) + self.indent + self.entity_image_height
        width = self.rect.width - (self.indent * 2)
        height = self.core_info_height

        rect = pygame.Rect((x, y), (width, height))
        core_info = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#info_section",
                              container=self.get_container())
        return core_info

