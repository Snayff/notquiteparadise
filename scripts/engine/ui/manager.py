from __future__ import annotations

import logging
import pygame
from typing import TYPE_CHECKING, Union
from pygame_gui import UIManager
from pygame_gui.core import UIElement as PygameGuiElement
from snecs.typedefs import EntityID
from scripts.engine import debug, utility
from scripts.engine.core.constants import (GAP_SIZE, MAX_SKILLS, SKILL_SIZE,
                                           Direction, MessageType,
                                           MessageTypeType, UIElement,
                                           UIElementType, VisualInfo)
from scripts.engine.library import library
from scripts.engine.ui.multi_instance_elements.screen_message import \
    ScreenMessage
from scripts.engine.ui.single_instance_elements.actor_info import ActorInfo
from scripts.engine.ui.single_instance_elements.camera import Camera
from scripts.engine.ui.single_instance_elements.data_editor import DataEditor
from scripts.engine.ui.single_instance_elements.message_log import MessageLog
from scripts.engine.ui.single_instance_elements.skill_bar import SkillBar
from scripts.engine.ui.single_instance_elements.tile_info import TileInfo
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Dict, Tuple

_ui_element_union = Union[MessageLog, ActorInfo, SkillBar, Camera, DataEditor, TileInfo]


class _UIManager:
    """
    Manage the UI, such as windows, resource bars etc
    """

    def __init__(self):
        self.debug_font = None

        # first action needs to be to init pygame.
        pygame.init()
        pygame.font.init()

        #  set the display
        self._desired_width = VisualInfo.BASE_WINDOW_WIDTH
        self._desired_height = VisualInfo.BASE_WINDOW_HEIGHT
        self._screen_scaling_mod_x = self._desired_width // VisualInfo.BASE_WINDOW_WIDTH
        self._screen_scaling_mod_y = self._desired_height // VisualInfo.BASE_WINDOW_HEIGHT
        self._window: pygame.display = pygame.display.set_mode((self._desired_width, self._desired_height))
        self._main_surface: pygame.Surface = pygame.Surface((VisualInfo.BASE_WINDOW_WIDTH,
                                                            VisualInfo.BASE_WINDOW_HEIGHT), pygame.SRCALPHA)

        # now that the display is configured  init the pygame_gui
        self._gui = UIManager((VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT), "data/ui/themes.json")

        # elements info
        self._elements = {}  # dict of all init'd ui_manager elements
        self._element_details: Dict[UIElementType, Tuple[PygameGuiElement, pygame.Rect]] = {}

        # process config
        self._load_display_config()
        self._load_fonts()
        self._load_element_layout()

        logging.info(f"UIManager initialised.")

    ################ CORE METHODS ########################

    def update(self, delta_time: float):
        """
        Update all ui_manager elements
        """
        self._gui.update(delta_time)

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

        self._gui.draw_ui(main_surface)

        self._draw_debug()

        # resize the surface to the desired resolution
        scaled_surface = pygame.transform.scale(main_surface, (self._desired_width, self._desired_height))
        self._window.blit(scaled_surface, (0, 0))

        # update the display
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
            return self.create_element(element_type)

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
        pygame.display.set_icon(utility.get_image("assets/ui/nqp_icon.png"))

    def _load_fonts(self):
        self._gui.add_font_paths("barlow", "assets/fonts/Barlow-Light.otf")
        self.debug_font = pygame.font.Font("assets/fonts/Kenney Future Narrow.ttf", 12)

        fonts = [
            {'name': 'barlow', 'point_size': 24, 'style': 'regular'}
            ]

        self._gui.preload_fonts(fonts)

    def _load_element_layout(self):
        # Message Log
        message_width = 400
        message_height = 200
        message_x = 0
        message_y = -message_height

        # Skill Bar
        skill_width = MAX_SKILLS * (SKILL_SIZE + GAP_SIZE)
        skill_height = SKILL_SIZE
        skill_x = (VisualInfo.BASE_WINDOW_WIDTH // 2) - (skill_width // 2)
        skill_y = -SKILL_SIZE

        # Camera
        camera_width = VisualInfo.BASE_WINDOW_WIDTH
        camera_height = VisualInfo.BASE_WINDOW_HEIGHT
        camera_x = 0
        camera_y = 0

        # Tile Info
        tile_info_width = 240
        tile_info_height = 160
        tile_info_x = -tile_info_width
        tile_info_y = -tile_info_height

        # Data Editor
        data_width = VisualInfo.BASE_WINDOW_WIDTH
        data_height = VisualInfo.BASE_WINDOW_HEIGHT
        data_x = 5
        data_y = 10

        # Npc info
        npc_info_width = VisualInfo.BASE_WINDOW_WIDTH / 2
        npc_info_height = VisualInfo.BASE_WINDOW_HEIGHT - (VisualInfo.BASE_WINDOW_HEIGHT / 4)
        npc_info_x = 5
        npc_info_y = 10

        layout = {
            UIElement.MESSAGE_LOG: (MessageLog, pygame.Rect((message_x, message_y), (message_width, message_height))),
            UIElement.TILE_INFO: (TileInfo, pygame.Rect((tile_info_x, tile_info_y),
                                                        (tile_info_width, tile_info_height))),
            UIElement.SKILL_BAR: (SkillBar, pygame.Rect((skill_x, skill_y), (skill_width, skill_height))),
            UIElement.CAMERA: (Camera, pygame.Rect((camera_x, camera_y), (camera_width, camera_height))),
            UIElement.DATA_EDITOR: (DataEditor, pygame.Rect((data_x, data_y), (data_width, data_height))),
            UIElement.ACTOR_INFO: (ActorInfo, pygame.Rect((npc_info_x, npc_info_y), (npc_info_width, npc_info_height)))
        }
        self._element_details = layout

    def init_all_ui_elements(self, visible: bool = False):
        """
        Initialise the game's UI elements with specified visibility.
        """
        for element_type in utility.get_class_members(UIElement):
            _element_type = getattr(UIElement, element_type)

            # in case we add an element to the UIElement class before creating the object and adding to load
            if _element_type in self._element_details:
                self.create_element(_element_type)
                self.set_element_visibility(_element_type, visible)

    def create_element(self, element_type: UIElementType) -> _ui_element_union:
        """
        Create the specified UI element. Object is returned for convenience, it is already held and can be returned
        with get_element at a later date. If it already exists current instance will be overwritten.
        """
        # if it already exists, log is being overwritten
        # N.B. do not use get_element to check as it will create a circular reference
        if element_type in self._elements:
            element_name = utility.value_to_member(element_type, UIElement)
            logging.warning(f"Created new {element_name} ui element, overwriting previous instance.")

        # create the element from the details held in element layout
        element_class, rect = self._element_details.get(element_type)  # type: ignore  # mypy thinks will return none
        element = element_class(rect, self.get_gui_manager())
        self._elements[element_type] = element

        return element

    def create_screen_message(self, message: str, colour, size: int):
        """
        Create a message on the screen.
        """
        col = "#531B75"
        text = f"<font face=barlow color={col} size={size}>{message}</font>"
        screen_message = ScreenMessage(text, self.get_gui_manager())

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
        logging.warning("Tried to get screen position but camera not init`d. Likely to draw in wrong place, "
                        "if it draws at all.")
        return 0, 0

    def update_targeting_overlay(self, is_visible: bool, skill_name: str = None):
        """
        Show or hide targeting overlay, using Direction possible in the skill.
        """
        camera = self.get_element(UIElement.CAMERA)
        if camera:
            # update directions to either clear or use info from skill
            if is_visible and skill_name:
                data = library.get_skill_data(skill_name)
                _directions = data.target_directions
            else:
                _directions = []

            # ensure all directions are of type Direction
            directions = []
            for direction in _directions:
                directions.append(getattr(Direction, direction.upper()))  # type: ignore  # direction has string

            camera.set_overlay_directions(directions)
            camera.set_overlay_visibility(is_visible)
            camera.update_grid()

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

    def _add_to_message_log(self, message: str):
        """
        Add a text to the message log. Includes processing of the text.
        """
        try:
            message_log = self.get_element(UIElement.MESSAGE_LOG)
            message_log.add_message(message)

        except AttributeError:
            logging.warning(f"Tried to add text to MessageLog but key not found. Is it init`d?")

    def log_message(self, message_type: MessageTypeType,  message: str, colour: str = None, size: int = 4,
            entity: EntityID = None):
        if message_type == MessageType.LOG:
            self._add_to_message_log(message)

        elif message_type == MessageType.SCREEN:
            self.create_screen_message(message, colour, size)

        elif message_type == MessageType.ENTITY:
            pass

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


ui = _UIManager()
