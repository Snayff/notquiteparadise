from __future__ import annotations

import logging
import pygame
from typing import List, Optional
from pygame_gui import UIManager
from pygame_gui.core import UIElement
from pygame_gui.elements import UIImage, UIPanel, UITextBox, UIWindow
from snecs.typedefs import EntityID
from scripts.engine import utility, world
from scripts.engine.component import Aesthetic, Afflictions, Identity, Resources, Traits
from scripts.engine.core.constants import GAP_SIZE, ICON_SIZE, IMAGE_NOT_FOUND_PATH, INFINITE, LAYER_BASE_UI, \
    PrimaryStat, \
    SecondaryStat
from scripts.engine.utility import get_class_members


class ActorInfo(UIWindow):
    """
    Full detail about an npc entity.
    """
    # TODO - change to window
    # TODO  - change state when selected

    def __init__(self, rect: pygame.Rect, manager: UIManager):

        # sections
        self.selected_entity: Optional[EntityID] = None
        self.sections: List[UIElement] = []

        # complete base class init
        super().__init__(rect, manager, element_id="entity_info")

        # show self
        self.show()

        # confirm init complete
        logging.debug(f"Actor Info initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI element. Method must exist, even if stubbed.
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
        super().show()

        self.visible = True
        entity = self.selected_entity

        if entity:
            # clear to refresh first
            self.cleanse()

            images = []
            info = []
            # TODO - replace with non-placeholder image
            section_break_image = utility.get_image("assets/ui/menu_window_n_repeat.png", (13, self.rect.width))

            # get aesthetic
            aesthetic = world.get_entitys_component(entity, Aesthetic)
            images.append(aesthetic.sprites.icon)

            # get identity
            identity = world.get_entitys_component(entity, Identity)
            info.append(identity.name)

            # get resources
            resources = world.get_entitys_component(entity, Resources)
            if resources:
                info.append(f"Health: {resources.health}")
                info.append(f"Stamina: {resources.stamina}")
                images.append(section_break_image)

            # get stats
            stats = world.create_combat_stats(entity)
            if stats:
                primary_stats = utility.get_class_members(PrimaryStat)
                for name in primary_stats:
                    try:
                        stat_value = getattr(stats, name.lower())

                        name = name.title()
                        name = name.replace("_", " ")
                        info.append(f"{name}: {stat_value}")

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"NpcEntityInfo: attribute {name} not found in primary stats.")


                secondary_stats = get_class_members(SecondaryStat)
                for name in secondary_stats:
                    # FIXME - HEALTH and STAMINA not found
                    try:
                        stat_value = getattr(stats, name.lower())

                        name = name.title()
                        name = name.replace("_", " ")
                        info.append(f"{name}: {stat_value}")

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"NpcEntityInfo: attribute {name} not found in secondary stats.")

                images.append(section_break_image)

            #  get traits
            traits = world.get_entitys_component(entity, Traits)
            if traits:
                names = ""
                for name in traits.names:
                    # if more than one trait add a separator
                    if len(names) > 1:
                        names += ", "
                    names += f"{name}"
                info.append(names)
                images.append(section_break_image)

            # get afflictions
            afflictions = world.get_entitys_component(entity, Afflictions)
            if afflictions:
                names = ""
                for name, affliction in afflictions.active.items():
                    # if more than one affliction add a separator
                    if len(names) > 1:
                        names += ", "
                    # get duration
                    if affliction.duration == INFINITE:
                        duration = "∞"
                    else:
                        duration = affliction.duration
                    # add value
                    names += f"{name}: {duration}"
                # if no afflictions, say so
                if names:
                    names = "Not afflicted."
                info.append(names)

            # create the box for the info
            self._create_sections(images, info)

    def cleanse(self):
        """
        Cleanse existing section info.
        """
        # kill the box and clear the reference
        for element in self.sections:
            element.kill()
        self.sections = []

    ############## CREATE ########################

    def _create_sections(self, images: List[pygame.surface], info: List[str]):
        """
        Create sections for the information about the tile
        """
        sections = []
        current_y = 0
        section_number = 0

        # draw info
        centre_draw_x = int((self.rect.width / 2) - (ICON_SIZE / 2))
        image_rect = pygame.Rect((centre_draw_x, 0), (ICON_SIZE, ICON_SIZE))
        x = 0
        width = self.rect.width
        text_height = 0  # box will resize height anyway

        # loop each image provided and use as header for each group of info
        for image in images:
            #  create image
            _image = pygame.transform.scale(image, (ICON_SIZE, ICON_SIZE))
            ui_image = UIImage(relative_rect=image_rect, image_surface=image, manager=self.ui_manager,
                               container=self.get_container())
            sections.append(ui_image)
            ui_image = None  # clear to prevent any carry over

            # update position
            current_y += ICON_SIZE + GAP_SIZE

            # collect text for the section
            text = ""
            for line in info[section_number]:
                text += line + "<br>"

            # create textbox
            rect = pygame.Rect((x, current_y), (width, text_height))
            ui_text = UITextBox(html_text=text, relative_rect=rect, manager=self.ui_manager,
                              wrap_to_height=True, layer_starting_height=1,
                              container=self.get_container())
            sections.append(ui_text)
            ui_text = None  # clear to prevent any carry over

            # increment section
            section_number += 1

        # update main sections list
        self.sections = sections


