from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Union

import pygame
from pygame_gui import UIManager
from pygame_gui.core import UIElement as PygameGuiElement

from scripts.engine.core import utility
from scripts.engine.internal import debug, library
from scripts.engine.internal.constant import (
    ASSET_PATH,
    DATA_PATH,
    GAP_SIZE,
    MAX_SKILLS,
    SKILL_BUTTON_SIZE,
    UIElement,
    UIElementType,
)

from scripts.engine.widgets.screen_message import ScreenMessage
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Dict, Tuple, TYPE_CHECKING

_ui_element_union = Union[
    MessageLog, ActorInfo, SkillBar, Camera, DataEditor, TileInfo, DungenViewer, TitleScreen, CharacterSelector
]

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
        self._base_width = base_width
        self._base_height = base_height
        self._main_surface: pygame.Surface = pygame.Surface((desired_width, desired_height), pygame.SRCALPHA)

        # values to scale to
        self._desired_width = desired_width
        self._desired_height = desired_height
        self._screen_scaling_mod_x = desired_width // base_width
        self._screen_scaling_mod_y = desired_height // base_height
        self._window: pygame.display = pygame.display.set_mode((desired_width, desired_height))

        # now that the display is configured  init the pygame_gui
        self._gui = UIManager((desired_width, desired_height), DATA_PATH / "ui/themes.json")

        # elements info
        self._elements = {}  # dict of all init'd ui_manager elements
        self._element_details: Dict[UIElementType, Tuple[PygameGuiElement, pygame.Rect]] = {}

        # process config
        self._load_display_config()
        self._load_fonts()
        self._load_element_layout()

        logging.info(f"UIManager initialised.")

    ################ CORE METHODS ########################

    def update(self, time_delta: float):
        """
        Update all ui_manager elements
        """
        self._gui.update(time_delta)

    def process_ui_events(self, event):
        """
        Pass event to the gui manager and, if event type is USEREVENT, to all ui elements.
        """
        self._gui.process_events(event)

        # make sure it is a pgui event
        if event.type == pygame.USEREVENT:
            elements = self._elements

            for element in elements.values():
                element.handle_events(event)

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

    def get_element(self, element_type: UIElementType) -> _ui_element_union:
        """
        Get UI element. Creates instance if not found.
        """
        if element_type in self._elements:
            return self._elements[element_type]
        else:
            element_name = utility.value_to_member(element_type, UIElement)
            logging.info(f"Tried to get {element_name} ui element but key not found; new one created.")
            return self._create_element(element_type)

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
            {"name": "barlow", "point_size": 14, "style": "regular"},
        ]

        self._gui.preload_fonts(fonts)

    def _load_element_layout(self):
        base_width = self._desired_width
        base_height = self._desired_height

        # Message Log
        message_width = int(base_width * 0.31)
        message_height = int(base_height * 0.28)
        message_x = 0
        message_y = -message_height

        # Skill Bar
        skill_width = (MAX_SKILLS * (SKILL_BUTTON_SIZE + GAP_SIZE)) + (GAP_SIZE * 2)  # gap * 2 for borders
        skill_height = SKILL_BUTTON_SIZE + (GAP_SIZE * 2)
        skill_x = (base_width // 2) - (skill_width // 2)
        skill_y = -SKILL_BUTTON_SIZE

        # Camera
        camera_width = base_width
        camera_height = base_height
        camera_x = 0
        camera_y = 0

        # Title Screen
        title_screen_width = base_width
        title_screen_height = base_height
        title_screen_x = 0
        title_screen_y = 0

        # Dungeon dev view
        dungen_viewer_width = base_width
        dungen_viewer_height = base_height
        dungen_viewer_x = 0
        dungen_viewer_y = 0

        # Tile Info
        tile_info_width = int(base_width * 0.19)
        tile_info_height = int(base_height * 0.22)
        tile_info_x = -tile_info_width
        tile_info_y = -tile_info_height

        # Data Editor
        data_width = base_width
        data_height = base_height
        data_x = 0
        data_y = 0

        # Npc info
        npc_info_width = base_width / 2
        npc_info_height = base_height - (base_height / 4)
        npc_info_x = 5
        npc_info_y = 10

        # character selector
        char_selector_width = base_width
        char_selector_height = base_height
        char_selector_x = 0
        char_selector_y = 0

        layout = {
            UIElement.MESSAGE_LOG: (MessageLog, pygame.Rect((message_x, message_y), (message_width, message_height))),
            UIElement.TILE_INFO: (
                TileInfo,
                pygame.Rect((tile_info_x, tile_info_y), (tile_info_width, tile_info_height)),
            ),
            UIElement.SKILL_BAR: (SkillBar, pygame.Rect((skill_x, skill_y), (skill_width, skill_height))),
            UIElement.CAMERA: (Camera, pygame.Rect((camera_x, camera_y), (camera_width, camera_height))),
            UIElement.DATA_EDITOR: (DataEditor, pygame.Rect((data_x, data_y), (data_width, data_height))),
            UIElement.DUNGEN_VIEWER: (
                DungenViewer,
                pygame.Rect((dungen_viewer_x, dungen_viewer_y), (dungen_viewer_width, dungen_viewer_height)),
            ),
            UIElement.ACTOR_INFO: (ActorInfo, pygame.Rect((npc_info_x, npc_info_y), (npc_info_width, npc_info_height))),
            UIElement.TITLE_SCREEN: (
                TitleScreen,
                pygame.Rect((title_screen_x, title_screen_y), (title_screen_width, title_screen_height)),
            ),
            UIElement.CHARACTER_SELECTOR: (
                CharacterSelector,
                pygame.Rect((char_selector_x, char_selector_y), (char_selector_width, char_selector_height)),
            ),
        }
        self._element_details = layout

    def _create_element(self, element_type: UIElementType) -> _ui_element_union:
        """
        Create the specified UI element. Object is returned for convenience, it is already held and can be returned
        with get_element at a later date. If it already exists current instance will be overwritten.
        """
        # if it already exists, log that is being overwritten
        # N.B. do not use get_element to check as it will create a circular reference
        if element_type in self._elements:
            element_name = utility.value_to_member(element_type, UIElement)
            logging.warning(f"Created new {element_name} ui element, overwriting previous instance.")

        # create the element from the details held in element layout
        element_class, rect = self._element_details.get(element_type)  # type: ignore  # mypy thinks will return none
        element = element_class(rect, self.get_gui_manager())
        self._elements[element_type] = element

        return element

    def create_screen_message(self, message: str, colour: str = "#531B75", size: int = 4):
        """
        Create a message on the screen.
        """
        text = f"<font face=barlow color={colour} size={size}>{message}</font>"
        rect = pygame.Rect((self._base_width / 4, self._base_height / 4), (self._base_width / 2, -1))
        screen_message = ScreenMessage(rect, text, self.get_gui_manager())

    ######################## KILL ###############################################

    def kill_game_ui(self):
        """
        Close and kill the game's UI elements. Helper function to run kill_element on relevant elements.
        """
        for element_type in utility.get_class_members(UIElement):
            _element_type = getattr(UIElement, element_type)

            # in case we add an element to  the UIElement class before creating the object and adding to load
            if _element_type in self._element_details:
                self.kill_element(_element_type)

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
        element = self.get_element(element_type)
        return element.visible

    def element_is_active(self, element_type: UIElementType) -> bool:
        """
        Check if an element has been created and is visible
        """
        if element_type in self._elements:
            return self.element_is_visible(element_type)
        else:
            return False

    ######################## WRAPPED, FREQUENTLY-USED ELEMENT METHODS ############################################

    def set_player_tile(self, tile: Tile):
        """
        Set the player tile in the Camera ui_manager element.
        """
        camera = self.get_element(UIElement.CAMERA)

        if camera:
            camera.set_player_tile(tile)
        else:
            logging.warning(f"Tried to set player tile in Camera but key not found. Is it init`d?")

    def world_to_draw_position(self, pos: Tuple[int, int]):
        """
        Convert from the world_objects position to the draw position. 0, 0 if camera not init'd.
        """
        # FIXME - this shouldnt rely on UI, if possible.
        camera = self.get_element(UIElement.CAMERA)

        # if camera has been init'd
        if camera:
            return camera.world_to_draw_position(pos)
        logging.warning(
            "Tried to get screen position but camera not init`d. Likely to draw in wrong place, " "if it draws at all."
        )
        return 0, 0

    def update_targeting_overlay(self, is_visible: bool, skill_name: str = None):
        """
        Show or hide targeting overlay, using Direction possible in the skill.
        """
        camera = self.get_element(UIElement.CAMERA)
        if camera:
            # update directions to either clear or use info from skill
            if is_visible and skill_name:
                data = library.SKILLS[skill_name]
                directions = data.target_directions
            else:
                directions = []

            camera.set_overlay_directions(directions)
            camera.set_overlay_visibility(is_visible)
            camera._update_grid()

    def set_selected_tile_pos(self, tile_pos: Tuple[int, int]):
        """
        Set the selected entity and show it.
        """
        tile_info = self.get_element(UIElement.TILE_INFO)

        if tile_info:
            tile_info.set_selected_tile_pos(tile_pos)
            tile_info.show()
        else:
            logging.warning(f"Tried to update TileInfo but key not found. Is it init`d?")

    def log_message(self, message: str):
        """
        Add a text to the message log. Includes processing of the text.
        """
        try:
            message_log = self.get_element(UIElement.MESSAGE_LOG)
            message_log.add_message(message)

        except AttributeError:
            logging.warning(f"Tried to add text to MessageLog but key not found. Is it init`d?")

    def set_element_visibility(self, element_type: UIElementType, visible: bool):
        """
        Set whether the element is visible or not.
        """
        element = self.get_element(element_type)
        element.visible = visible
        element_name = utility.value_to_member(element_type, UIElement)

        if visible:
            element.show()
            logging.debug(f"Showed {element_name} ui element.")
        else:
            element.hide()
            logging.debug(f"Hid {element_name} ui element.")


if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    ui = UI()
else:
    ui = ""  # type: ignore
