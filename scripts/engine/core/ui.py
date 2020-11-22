from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING

import pygame
from pygame_gui import UIManager

from scripts.engine.core import utility
from scripts.engine.internal import debug, library
from scripts.engine.internal.constant import ASSET_PATH, DATA_PATH, UIElement, UIElementType
from scripts.engine.widgets.screen_message import ScreenMessage

if TYPE_CHECKING:
    from typing import Dict, Optional, Tuple, TYPE_CHECKING, Union

    from scripts.engine.widgets.panel import Panel
    from scripts.engine.widgets.window import Window

__all__ = ["ui"]


class UI:
    """
    Manage the UI, such as windows, resource bars etc
    """

    def __init__(self):
        self.debug_font = None

        # first action needs to be to init pygame.
        pygame.init()
        pygame.font.init()

        # get config info
        base_window_data = library.VIDEO_CONFIG.base_window
        desired_window_data = library.VIDEO_CONFIG.desired_window

        # pull out to reduce use of accessor
        base_width = base_window_data.width
        base_height = base_window_data.height
        desired_width = desired_window_data.width
        desired_height = desired_window_data.height

        ##  set the display
        # base values
        self.base_width = base_width
        self.base_height = base_height
        self._main_surface: pygame.Surface = pygame.Surface((desired_width, desired_height), pygame.SRCALPHA)

        # values to scale to
        self.desired_width = desired_width
        self.desired_height = desired_height
        self._window: pygame.display = pygame.display.set_mode((desired_width, desired_height))

        # now that the display is configured  init the pygame_gui
        self._gui = UIManager((desired_width, desired_height), DATA_PATH / "ui/themes.json")

        # elements info
        self._elements: Dict[UIElementType, Union[Panel, Window]] = {}  # dict of all init'd ui_manager elements

        # process config
        self._load_display_config()
        self._load_fonts()

        logging.info(f"UIManager initialised.")

    ################ CORE METHODS ########################

    def update(self, time_delta: float):
        """
        Update all ui_manager elements
        """
        self._gui.update(time_delta)

    def process_ui_events(self, event):
        """
        Pass event to the gui manager.
        """
        self._gui.process_events(event)

    def draw(self):
        """
        Draw the UI.
        """
        main_surface = self._main_surface

        # clear previous frame
        main_surface.fill((0, 0, 0))

        # draw everything
        self._draw_debug()
        self._gui.draw_ui(main_surface)

        # update the display
        self._window.blit(main_surface, (0, 0))
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def _draw_debug(self):
        """
        Draw debug information, based on visible values in debug.
        """
        values = debug.get_visible_values()
        y = 10
        debug_font = self.debug_font

        for value in values:
            surface = debug_font.render(value, False, (255, 255, 255))
            self._main_surface.blit(surface, (0, y))
            y += 10

    ##################### GET ############################

    def get_element(self, element_type: UIElementType) -> Union[Panel, Window]:
        """
        Get UI element.
        """
        if element_type in self._elements:
            return self._elements[element_type]

        element_name = utility.value_to_member(element_type, UIElement)
        raise KeyError(f"Tried to get {element_name} ui element but key not found.")

    def get_gui_manager(self) -> UIManager:
        """
        Return the pygame_gui UI Manager
        """
        return self._gui

    ##################### INIT, LOAD AND CREATE ############################

    @staticmethod
    def _load_display_config():
        """
        Initialise display settings.
        """
        pygame.display.set_caption("Not Quite Paradise")
        pygame.display.set_icon(utility.get_image("ui/nqp_icon.png"))

    def _load_fonts(self):
        self._gui.add_font_paths("barlow", str(ASSET_PATH / "fonts/Barlow-Light.otf"))
        self.debug_font = pygame.font.Font(str(ASSET_PATH / "fonts/Kenney Future Narrow.ttf"), 6)

        fonts = [
            {"name": "barlow", "point_size": 12, "style": "regular"},
        ]

        self._gui.preload_fonts(fonts)

    def register_element(self, element_type: UIElementType, element: Union[Panel, Window]):
        """
        Register the specified UI element. Can be returned with get_element at a later date. If it already exists
        current instance will be overwritten.
        """
        # if it already exists, log that is being overwritten
        # N.B. do not use get_element to check as it will create a circular reference
        if element_type in self._elements:
            element_name = utility.value_to_member(element_type, UIElement)
            logging.warning(f"Created new {element_name} ui element, overwriting previous instance.")

        self._elements[element_type] = element

    def create_screen_message(self, message: str, colour: str = "#531B75", size: int = 4):
        """
        Create a message on the screen.
        """
        text = f"<font face=barlow color={colour} size={size}>{message}</font>"
        rect = pygame.Rect((self.base_width / 4, self.base_height / 4), (self.base_width / 2, -1))
        screen_message = ScreenMessage(rect, text, self.get_gui_manager())

    ######################## KILL ###############################################

    def kill_all_elements(self):
        """
        Close and kill the game's UI elements. Helper function to run kill_element on all elements.
        """
        for element_type in self._elements.keys():
            self.kill_element(element_type)

    def kill_element(self, element_type: UIElementType):
        """
        Remove any reference to the element.
        """
        element = self.get_element(element_type)
        del self._elements[element_type]
        element.kill()

    ################################ QUERIES #################################################################

    def element_is_visible(self, element_type: UIElementType) -> bool:
        """
        Check if an element is visible.
        """
        if self.has_element(element_type):
            element = self.get_element(element_type)
            return element.visible
        else:
            return False

    def element_is_active(self, element_type: UIElementType) -> bool:
        """
        Check if an element has been created and is visible
        """
        if element_type in self._elements:
            return self.element_is_visible(element_type)
        else:
            return False

    def has_element(self, element_type: UIElementType) -> bool:
        """
        Check if an element exists
        """
        if element_type in self._elements:
            return True
        else:
            return False

    ################################ UNIVERSAL ACTIONS #############################################

    def set_element_visibility(self, element_type: UIElementType, visible: bool) -> bool:
        """
        Set whether the element is visible or not. Returns true if successful, false if element not found.
        """
        if not self.has_element(element_type):
            return False

        element = self.get_element(element_type)
        element.visible = visible
        element_name = utility.value_to_member(element_type, UIElement)

        if visible:
            element.show()
            logging.debug(f"Showed {element_name} ui element.")
        else:
            element.hide()
            logging.debug(f"Hid {element_name} ui element.")

        return True


if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    ui = UI()
else:
    ui = ""  # type: ignore
