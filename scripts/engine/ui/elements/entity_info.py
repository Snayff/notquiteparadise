import logging
from typing import Optional

import pygame
from pygame_gui import UIManager
from pygame_gui.elements import UIImage, UIPanel, UITextBox, UIWindow
from snecs.typedefs import EntityID

from scripts.engine import utility, world
from scripts.engine.core.constants import GAP_SIZE, LAYER_BASE_UI, PrimaryStat, SecondaryStat, IMAGE_NOT_FOUND_PATH, \
    INFINITE
from scripts.engine.utility import get_class_members
from scripts.engine.component import Aesthetic, Identity, Resources, Afflictions


class EntityInfo(UIPanel):
    """
    Hold text relating to the game's events, to display to the player.
    """

    def __init__(self, rect: pygame.Rect, manager: UIManager):
        # TODO - create highlevel entity summary for info while on gamemap
        # TODO - create full summary as new window
        # FIXME - entity info  doesn't update when entity info changes.

        # sections
        self.selected_entity: Optional[EntityID] = None
        self.entity_image: Optional[pygame.Surface] = None
        self.info_section: Optional[UITextBox] = None

        # data
        self.indent = 3
        self.entity_image_height = 32
        self.entity_image_width = 32
        self.core_info_height = rect.height - self.entity_image_height

        # complete base class init
        super().__init__(rect, LAYER_BASE_UI, manager, element_id="entity_info",
                         anchors={"left": "right",
                             "right": "right",
                             "top": "bottom",
                             "bottom": "bottom"})

        # show self
        self.show()

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

    ############## GET / SET ########################

    def set_entity(self, entity: EntityID):
        """
        Set the selected entity to show the info for that entity.
        """
        self.selected_entity = entity

    ############### ACTIONS #########################

    def show(self):
        """
        Show the entity info. Builds the sections required, after clearing any existing.
        """
        if self.selected_entity:
            # clear to refresh first
            self.cleanse()

            # create the various boxes for the info
            self.entity_image = self._create_entity_image_section()
            self.info_section = self._create_info_section()

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

    ############## CREATE ########################

    def _create_entity_image_section(self) -> UIImage:
        """
        Create the image section.
        """
        image_width = self.entity_image_width
        image_height = self.entity_image_height
        centre_draw_x = int((self.rect.width / 2) - (image_width / 2))
        rect = pygame.Rect((centre_draw_x, 0), (image_width, image_height))
        entity = self.selected_entity

        # get the image for the entity
        if entity:
            aesthetic = world.get_entitys_component(entity, Aesthetic)
            if aesthetic:
                image = pygame.transform.scale(aesthetic.sprites.icon, (image_width, image_height))
            else:
                image = utility.get_image(IMAGE_NOT_FOUND_PATH)

        else:
            image = utility.get_image(IMAGE_NOT_FOUND_PATH)

        entity_image = UIImage(relative_rect=rect, image_surface=image, manager=self.ui_manager,
                               container=self.get_container(), object_id="#entity_image")

        return entity_image

    def _create_info_section(self) -> UITextBox:
        """
        Create the core info section.
        """
        entity = self.selected_entity
        section_break = "|-------------------| <br>"

        if entity:
            text = ""

            # basic info
            identity = world.get_entitys_component(entity, Identity)
            if identity:
                text += f"{identity.name.capitalize()}" + "<br>"
            resources = world.get_entitys_component(entity, Resources)
            if resources:
                text += f"Current Health: {resources.health}" + "<br>"
                text += f"Current Stamina: {resources.stamina}" + "<br>"

            # add section_break
            text += section_break

            # afflictions
            afflictions = world.get_entitys_component(entity, Afflictions)
            if afflictions:
                for affliction, duration in afflictions.items():
                    # overwrite duration with infinity string if needed
                    if duration == INFINITE:
                        duration = "∞"  # type: ignore
                    text += f"{affliction} : {duration}" + "<br>"
            else:
                text += "Not afflicted." + "<br>"

            # add section_break
            text += section_break

            # stats info
            stats = world.create_combat_stats(entity)
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

            # add section_break
            text += section_break

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

        x = 0
        y = (GAP_SIZE * 2) + self.indent + self.entity_image_height
        width = self.rect.width - (self.indent * 2)
        height = self.core_info_height

        rect = pygame.Rect((x, y), (width, height))
        core_info = UITextBox(html_text=text, relative_rect=rect, manager=self.ui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#info_section",
                              container=self.get_container())
        return core_info

