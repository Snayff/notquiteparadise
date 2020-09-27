from __future__ import annotations

import logging
from typing import List, Tuple

import pygame
from pygame_gui import UIManager
from pygame_gui.core import UIElement
from pygame_gui.elements import UIImage, UIPanel, UITextBox

from scripts.engine import world
from scripts.engine.component import Aesthetic, Aspect, Identity, Position, Resources, Traits
from scripts.engine.core.constants import GAP_SIZE, ICON_IN_TEXT_SIZE, RenderLayer


class TileInfo(UIPanel):
    """
    Hold text relating to the game's events, to display to the player.
    """

    def __init__(self, rect: pygame.Rect, manager: UIManager):

        self.selected_tile_pos: Tuple[int, int] = (0, 0)
        self.sections: List[UIElement] = []

        # complete base class init
        super().__init__(
            rect,
            RenderLayer.UI_BASE,
            manager,
            element_id="tile_info",
            anchors={"left": "right", "right": "right", "top": "bottom", "bottom": "bottom"},
        )

        # show self
        self.show()

        # confirm init complete
        logging.debug(f"Tile Info initialised.")

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

    def set_selected_tile_pos(self, tile_pos: Tuple[int, int]):
        """
        Set the selected tile position to show the info for that tile.
        """
        self.selected_tile_pos = tile_pos

    ############### ACTIONS #########################

    def show(self):
        """
        Show the tile info. Builds the sections required, after clearing any existing. Also triggers base class show
        method.
        """
        super().show()

        # clear to refresh first
        self.cleanse()

        if self.selected_tile_pos:

            images = []
            info = []

            # get entities at selected position
            from scripts.engine.core import queries

            for entity, (position, identity, aesthetic) in queries.position_and_identity_and_aesthetic:
                if self.selected_tile_pos in position:

                    # get universal info
                    images.append(aesthetic.sprites.icon)
                    current_info = [identity.name]

                    ## is it an entity with more useful info?
                    # get resources
                    resources = world.get_entitys_component(entity, Resources)
                    if resources:
                        current_info.append(f"Health: {resources.health}")
                        current_info.append(f"Stamina: {resources.stamina}")

                    #  get traits
                    traits = world.get_entitys_component(entity, Traits)
                    if traits:
                        names = ""
                        for name in traits.names:
                            # if more than one trait add a separator
                            if len(names) > 1:
                                names += ", "
                            names += f"{name}"
                        current_info.append(names)

                    # get aspects
                    aspect = world.get_entitys_component(entity, Aspect)
                    if aspect:
                        details = ""
                        for name, duration in aspect.aspects.items():
                            # if more than one aspect add a separator
                            if len(details) > 1:
                                details += ", "
                            details += f"{name}:{duration}"
                        current_info.append(details)

                    # add collected info to main info
                    info.append(current_info)

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

    def _create_sections(self, images: List[pygame.surface], info: List[List[str]]):
        """
        Create sections for the information about the tile
        """
        sections = []
        current_y = 0
        section_number = 0

        # draw info
        centre_draw_x = int((self.rect.width / 2) - (ICON_IN_TEXT_SIZE / 2))
        image_rect = pygame.Rect((centre_draw_x, 0), (ICON_IN_TEXT_SIZE, ICON_IN_TEXT_SIZE))
        x = 0
        width = self.rect.width
        text_height = 0  # box will resize height anyway

        # loop each image provided and use as header for each group of info
        # FIXME - hovering projectile breaks it due to not havign a surface (missing icon_path?)
        for image in images:
            #  create image
            _image = pygame.transform.scale(image, (ICON_IN_TEXT_SIZE, ICON_IN_TEXT_SIZE))
            ui_image = UIImage(
                relative_rect=image_rect, image_surface=_image, manager=self.ui_manager, container=self.get_container()
            )
            sections.append(ui_image)
            ui_image = None  # clear to prevent any carry over

            # update position
            current_y += ICON_IN_TEXT_SIZE + GAP_SIZE

            # collect text for the section
            text = ""
            for line in info[section_number]:
                text += line + "<br>"

            # create textbox
            rect = pygame.Rect((x, current_y), (width, text_height))
            ui_text = UITextBox(
                html_text=text,
                relative_rect=rect,
                manager=self.ui_manager,
                wrap_to_height=True,
                layer_starting_height=1,
                container=self.get_container(),
            )
            sections.append(ui_text)
            ui_text = None  # clear to prevent any carry over

            # increment section
            section_number += 1

        # update main sections list
        self.sections = sections
