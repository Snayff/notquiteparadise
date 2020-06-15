from __future__ import annotations

import logging
import pygame
from typing import TYPE_CHECKING, cast
from pygame_gui import UIManager
from snecs.typedefs import EntityID
from scripts.engine import debug
from scripts.engine.core.constants import Direction, GAP_SIZE, ICON_SIZE, MAX_SKILLS, MessageType, MessageTypeType, \
    SKILL_SIZE, \
    VisualInfo, UIElement, UIElementType, DirectionType
from scripts.engine.library import library
from scripts.engine.ui.basic.fonts import Font
from scripts.engine.ui.elements.camera import Camera
from scripts.engine.ui.elements.data_editor import DataEditor
from scripts.engine.ui.elements.entity_info import EntityInfo
from scripts.engine.ui.elements.message_log import MessageLog
from scripts.engine.ui.elements.screen_message import ScreenMessage
from scripts.engine.ui.elements.skill_bar import SkillBar
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Type, Dict, Tuple, List


class _UIManager:
    """
    Manage the UI, such as windows, resource bars etc
    """

    def __init__(self):
        self.debug_font = None

        # first action needs to be to init pygame.
        pygame.init()

        #  set the display
        # TODO - allow for selection by player but only multiples of base (16:9)
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
        self._element_layout: Dict[UIElementType, Tuple[object, pygame.Rect]] = {}

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
        Process input events
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
        values = debug.get_visible_values()
        y = 10
        debug_font = self.debug_font

        for value in values:
            text, rect = debug_font.render(value, (255, 255, 255))
            self._main_surface.blit(text, (0, y))
            y += 10

    def add_element(self, element_type: UIElementType, element: object):
        """
        Add ui_manager element to the list of all elements.
        """
        self._elements[element_type] = element

    ##################### GET ############################

    def get_element(self, element_type: UIElementType):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.
        """
        try:
            return self._elements[element_type]
        except KeyError:
            logging.warning(f"Tried to get {element_type} ui element but key not found, is it init`d?")
            return None

    def get_gui_manager(self) -> UIManager:
        """
        Return the pygame_gui UI Manager
        """
        return self._gui

    def get_elements(self) -> Dict:
        """
        Get all the ui_manager elements
        """
        return self._elements

    ##################### INIT, LOAD AND CREATE ############################

    @staticmethod
    def _load_display_config():
        """
        Initialise display settings.
        """
        pygame.display.set_caption("Not Quite Paradise")
        # pygame.display.set_icon() # TODO - add window icon

    def _load_fonts(self):
        self._gui.add_font_paths("barlow", "assets/fonts/Barlow-Light.otf")
        self.debug_font = Font().debug

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

        # Entity Info
        entity_info_width = 240
        entity_info_height = 200
        entity_info_x = -entity_info_width
        entity_info_y = -entity_info_height

        # Data Editor
        data_width = 1200
        data_height = 600
        data_x = 5
        data_y = 10

        layout = {
            UIElement.MESSAGE_LOG: (MessageLog, pygame.Rect((message_x, message_y), (message_width, message_height))),
            UIElement.ENTITY_INFO: (EntityInfo, pygame.Rect((entity_info_x, entity_info_y),
                                                            (entity_info_width, entity_info_height))),
            UIElement.SKILL_BAR: (SkillBar, pygame.Rect((skill_x, skill_y), (skill_width, skill_height))),
            UIElement.CAMERA: (Camera, pygame.Rect((camera_x, camera_y), (camera_width, camera_height))),
            UIElement.DATA_EDITOR: (DataEditor, pygame.Rect((data_x, data_y), (data_width, data_height)))
        }
        self._element_layout = layout

    def init_game_ui(self):
        """
        Initialise the game's UI elements. Helper function to run kill_element on relevant elements.
        """
        self.create_element(UIElement.CAMERA)
        self.create_element(UIElement.SKILL_BAR)
        self.create_element(UIElement.MESSAGE_LOG)
        self.create_element(UIElement.ENTITY_INFO)

    def create_element(self, element_type: UIElementType) -> object:
        """
        Create the specified UI element. Object is returned for convenience, it is already held and can be returned
        with get_element at a later date.
        """
        # if it already exists, kill it
        if self.get_element(element_type):
            self.kill_element(element_type)

        # create the element from the details held in element layout
        element_class, rect = self._element_layout.get(element_type)
        element = element_class(rect, self.get_gui_manager())
        self.add_element(element_type, element)

        return element

    def create_screen_message(self, message: str, colour, size: int):
        """
        Create a message on the screen.
        """
        # TODO - respect colour chosen. Use colour mapping to go from RGB to Hex.
        col = "#531B75"
        text = f"<font face=barlow color={col} size={size}>{message}</font>"
        screen_message = ScreenMessage(text, self.get_gui_manager())

    ######################## KILL ###############################################

    def kill_game_ui(self):
        """
        Close and kill the game's UI elements. Helper function to run kill_element on relevant elements.
        """
        self.kill_element(UIElement.CAMERA)
        self.kill_element(UIElement.SKILL_BAR)
        self.kill_element(UIElement.MESSAGE_LOG)
        self.kill_element(UIElement.ENTITY_INFO)

    def kill_element(self, element_type: UIElementType):
        """
        Remove any reference to the element
        """
        element = self.get_element(element_type)

        if element:
            del self._elements[element_type]
            element.kill()
        else:
            logging.warning(f"Tried to remove {element_type} element but key not found.")

    ######################## CAMERA ###############################################

    def set_player_tile(self, tile: Tile):
        """
        Set the player tile in the Camera ui_manager element.
        """
        camera = self.get_element(UIElement.CAMERA)

        if camera:
            camera.set_player_tile(tile)
        else:
            logging.warning(f"Tried to set player tile in Camera but key not found. Is it init`d?")

    def set_overlay_directions(self, directions: List[DirectionType]):
        """
        Set the overlay with possible targeting directions.
        """
        camera = self.get_element(UIElement.CAMERA)
        if camera:
            camera.set_overlay_directions(directions)
        else:
            logging.warning(f"Tried to set Camera overlay directions but key not found. Is it init`d?")

    def world_to_screen_position(self, pos: Tuple[int, int]):
        """
        Convert from the world_objects position to the screen position. 0, 0 if camera not init'd.
        """
        # TODO - this shouldnt rely on UI, if possible.
        camera = self.get_element(UIElement.CAMERA)

        # if camera has been init'd
        if camera:
            return camera.world_to_screen_position(pos)
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
                if not isinstance(direction, Direction):
                    directions.append(getattr(Direction, direction.upper()))
                else:
                    directions.append(direction)

            camera.set_overlay_directions(directions)
            camera.set_overlay_visibility(is_visible)
            camera.update_camera_grid()

    ######################## ENTITY INFO ###############################################

    def set_selected_entity(self, entity: EntityID):
        """
        Set the selected entity and show it.
        """
        entity_info = self.get_element(UIElement.ENTITY_INFO)

        if entity_info:
            if entity:
                entity_info.set_entity(entity)
                entity_info.show()
            else:
                entity_info.cleanse()
        else:
            logging.warning(f"Tried to set selected entity in EntityInfo but key not found. Is it init`d?")

    ######################## MESSAGES #################################

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
            # TODO - create message over entity
            #  can we reuse screen message but provide xy?
            pass


ui = _UIManager()
