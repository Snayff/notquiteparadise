from __future__ import annotations

import logging
from typing import Callable, Optional, TYPE_CHECKING, Union

import pygame
import pygame_gui
from pygame import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UIDropDownMenu, UIImage, UIPanel

__all__ = ["CharacterSelector"]

from scripts.engine import library
from scripts.engine.core.constants import GAP_SIZE, RenderLayer, TILE_SIZE, TraitGroup
from scripts.engine.utility import build_sprites_from_paths

if TYPE_CHECKING:
    from typing import Dict, List


class CharacterSelector(UIPanel):
    """
    A menu widget. Used to hold a collection of text, images, buttons etc. Expects to have buttons and provides
    functionality to handle the clicks
    """

    def __init__(self, rect: Rect, manager: UIManager):

        self.button_events: Dict[str, Union[pygame.event.Event, Callable]] = {}

        # containers for created widgets
        self.buttons: List[UIButton] = []
        self.drop_downs: List[UIDropDownMenu] = []
        self.ui_image: Optional[UIImage] = None

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="character_selector")

        self._init_buttons()
        self._init_drop_downs()
        self._refresh_image()

        # confirm init complete
        logging.debug(f"CharacterSelector initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        # handle button presses
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

            # Find out which button we are clicking
            button = event.ui_element

            # post the new event
            if button in self.buttons:
                # get the id
                ids = event.ui_object_id.split(".")
                button_id = ids[-1]  # get last element
                new_event = self.button_events[button_id]

                if isinstance(new_event, pygame.event.Event):
                    pygame.event.post(new_event)
                else:
                    new_event()

                logging.debug(f"CharacterSelector button '{button_id}' pressed.")

        # handle new selection in drop downs
        if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            self._refresh_image()

    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        pass

    def _init_drop_downs(self):
        """
        Initialise the drop downs for the menu
        """
        people = []
        savvy = []
        homeland = []

        manager = self.ui_manager
        max_width = self.rect.width
        max_height = self.rect.height
        num_drop_downs = 3
        gap = GAP_SIZE
        width = int((max_width / num_drop_downs) - (gap * num_drop_downs + 2))
        height = int(max_height / 12)
        start_x = 0
        start_y = int((max_height / 3) * 2)  # anchored to the bottom left
        max_expansion = int(start_y - height)

        # get traits
        for key, trait in library.TRAITS.items():
            if trait.group == TraitGroup.PEOPLE:
                people.append(key)
            elif trait.group == TraitGroup.SAVVY:
                savvy.append(key)
            elif trait.group == TraitGroup.HOMELAND:
                homeland.append(key)

        # bundle trait lists with group name
        all_traits = [
            (people, TraitGroup.PEOPLE),
            (savvy, TraitGroup.SAVVY),
            (homeland, TraitGroup.SAVVY)
        ]

        # create drop downs
        count = 0
        for traits, trait_group in all_traits:
            x = start_x + (count * (width + gap))
            rect = Rect((x, start_y), (width, height))
            drop_down = UIDropDownMenu(
                options_list=traits,
                starting_option=traits[0],
                relative_rect=rect,
                manager=manager,
                container=self.get_container(),
                object_id=trait_group,
                expansion_height_limit=max_expansion
            )

            count += 1
            self.drop_downs.append(drop_down)

    def _refresh_image(self):
        """
        Update the image in line with drop down selections
        """
        width = TILE_SIZE * 4
        height = TILE_SIZE * 4
        x = int((self.rect.width / 2) - (width / 2))
        y = int(self.rect.height / 10)
        rect = Rect((x, y), (width, height))

        # clear ui image if it exists
        if self.ui_image:
            self.ui_image.kill()
            self.ui_image = None

        # get sprite paths from traits
        sprite_paths = []
        for drop_down in self.drop_downs:
            trait = library.TRAITS[drop_down.selected_option]
            sprite_paths.append(trait.sprite_paths)

        # sort and build into sprites
        sprite_paths.sort(key=lambda path: path.render_order, reverse=True)
        sprites = build_sprites_from_paths(sprite_paths, (width, height))

        # create UI image
        ui_image = UIImage(
            relative_rect=rect,
            image_surface=sprites.idle,
            manager=self.ui_manager,
            container=self.get_container()
        )

        self.ui_image = ui_image
