from __future__ import annotations

import logging
import pygame
from typing import TYPE_CHECKING
from pygame_gui import UIManager
from snecs.typedefs import EntityID
from scripts.engine import debug, world
from scripts.engine.component import Position
from scripts.engine.core.constants import VisualInfo, UIElement, TILE_SIZE, UIElementType, DirectionType
from scripts.engine.ui.basic.fonts import Font
from scripts.engine.ui.elements.camera import Camera
from scripts.engine.ui.elements.data_editor import DataEditor
from scripts.engine.ui.elements.entity_info import EntityInfo
from scripts.engine.ui.elements.message_log import MessageLog
from scripts.engine.ui.elements.screen_message import ScreenMessage
from scripts.engine.ui.elements.skill_bar import SkillBar
from scripts.engine.utility import is_coordinate_in_bounds
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

        # process config
        self._load_display_config()
        self._load_fonts()

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

    def add_ui_element(self, element_type: UIElementType, element: object):
        """
        Add ui_manager element to the list of all elements.
        """
        self._elements[element_type] = element

    def kill_element(self, element_type: UIElementType):
        """
        Remove any reference to the element
        """
        element = self.get_ui_element(element_type)

        if element:
            del self._elements[element_type]
            element.kill()
        else:
            logging.warning(f"Tried to remove {element_type} element but key not found.")

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

    @staticmethod
    def get_gui_manager() -> UIManager:
        """
        Return the pygame_gui UI Manager
        """
        return ui._gui

    def get_ui_element(self, element_type: UIElementType):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.
        """
        try:
            return self._elements[element_type]
        except KeyError:
            return None

    def get_ui_elements(self) -> Dict:
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

    def init_message_log(self):
        """
        Initialise the text log ui_manager element.
        """
        # TODO - convert to create and move details to nqp
        width = 400
        height = 100
        x = VisualInfo.BASE_WINDOW_WIDTH - width - 5
        y = VisualInfo.BASE_WINDOW_HEIGHT - height - 5
        rect = pygame.Rect((x, y), (width, height))
        message_log = MessageLog(rect, self.get_gui_manager())
        self.add_ui_element(UIElement.MESSAGE_LOG, message_log)

    def init_entity_info(self):
        """
        Initialise the selected entity info ui_manager element.
        """
        # TODO - convert to create and move details to nqp
        width = 240
        height = 200
        x = -width
        y = -height
        rect = pygame.Rect((x, y), (width, height))
        info = EntityInfo(rect, self.get_gui_manager())
        self.add_ui_element(UIElement.ENTITY_INFO, info)

    def init_skill_bar(self):
        """
        Initialise the skill bar.
        """
        # TODO - convert to create and move details to nqp
        width = 80
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = 2
        rect = pygame.Rect((x, y), (width, height))
        skill_bar = SkillBar(rect, self.get_gui_manager())
        self.add_ui_element(UIElement.SKILL_BAR, skill_bar)

    def init_camera(self):
        """
        Initialise the camera.
        """
        # TODO - convert to create and move details to nqp

        width = VisualInfo.BASE_WINDOW_WIDTH  # cols * TILE_SIZE
        height = VisualInfo.BASE_WINDOW_HEIGHT  # rows * TILE_SIZE
        x = 0
        y = 0
        rows = height // TILE_SIZE
        cols = width // TILE_SIZE
        rect = pygame.Rect((x, y), (width, height))
        pos = world.get_entitys_component(world.get_player(), Position)
        tile = world.get_tile((pos.x, pos.y))

        camera = Camera(rect, self.get_gui_manager(), rows, cols, tile)
        self.add_ui_element(UIElement.CAMERA, camera)

        # initialize grid
        camera.update_grid()

    def init_skill_editor(self):
        """
        Initialise the skill editor ui_manager element.
        """
        # TODO - convert to create and move details to nqp
        width = 1200
        height = 600
        x = 5
        y = 10
        rect = pygame.Rect((x, y), (width, height))
        editor = DataEditor(rect, self.get_gui_manager())
        self.add_ui_element(UIElement.DATA_EDITOR, editor)

    def create_screen_message(self, message: str, colour, size: int):
        """
        Create a message on the screen.
        """
        # TODO - respect colour chosen. Use colour mapping to go from RGB to Hex.
        col = "#531B75"
        text = f"<font face=barlow color={col} size={size}>{message}</font>"
        screen_message = ScreenMessage(text, self.get_gui_manager())

    ######################## CAMERA ###############################################

    def is_target_pos_in_camera_edge(self, target_pos: Tuple) -> bool:
        """
        Determine if target position is within the edge of the camera
        """
        camera = self.get_ui_element(UIElement.CAMERA)

        if camera:
            player_x, player_y = target_pos
            x_bounds, y_bounds = camera.get_tile_bounds()

            x_in_camera_edge = is_coordinate_in_bounds(coordinate=player_x, bounds=x_bounds, edge=camera.edge_size)
            y_in_camera_edge = is_coordinate_in_bounds(coordinate=player_y, bounds=y_bounds, edge=camera.edge_size)

            return not x_in_camera_edge or not y_in_camera_edge

        else:
            logging.warning(f"Tried to check target pos in Camera but key not found. Is it init`d?")
            return False

    def move_camera(self, num_cols: int, num_rows: int):
        """
        Increment camera's drawn tiles in the given direction. N.B. Physical position on screen does not change.
        """
        camera = self.get_ui_element(UIElement.CAMERA)

        if camera:
            camera.move_camera(num_cols, num_rows)
        else:
            logging.warning(f"Tried to move Camera but key not found. Is it init`d?")

    def update_cameras_tiles(self):
        """
        Retrieve the tiles to draw within view of the camera and provide them to the camera. Checks FOV.
        """
        camera = self.get_ui_element(UIElement.CAMERA)

        if camera:
            pass
            # camera.update_camera_tiles(num_cols, num_rows)
        else:
            logging.warning(f"Tried to set camera tiles in Camera but key not found. Is it init`d?")

    def update_camera_game_map(self):
        """
        Update the camera game map to show what is in the tiles held by the camera.
        """
        camera = self.get_ui_element(UIElement.CAMERA)

        if camera:
            camera.update_game_map()

    def update_camera_grid(self):
        """
        Update the camera's grid. Controls tile hover highlighting.
        """
        camera = self.get_ui_element(UIElement.CAMERA)
        if camera:
            camera.update_grid()
        else:
            logging.warning(f"Tried to update camera grid in Camera move but key not found. Is it init`d?")

    def set_player_tile(self, tile: Tile):
        """
        Set the player tile in the Camera ui_manager element.

        Args:
            tile ():
        """
        camera = self.get_ui_element(UIElement.CAMERA)

        if camera:
            camera.set_player_tile(tile)
        else:
            logging.warning(f"Tried to set player tile in Camera but key not found. Is it init`d?")

    def set_overlay_visibility(self, is_visible: bool):
        """
        Set the visibility of the targeting overlay in the Camera.

        Args:
            is_visible ():
        """
        camera = self.get_ui_element(UIElement.CAMERA)
        if camera:
            camera.set_overlay_visibility(is_visible)
        else:
            logging.warning(f"Tried to set Camera overlay but key not found. Is it init`d?")

    def set_overlay_directions(self, directions: List[DirectionType]):
        """
        Set the overlay with possible targeting directions.
        """
        camera = self.get_ui_element(UIElement.CAMERA)
        if camera:
            camera.set_overlay_directions(directions)
        else:
            logging.warning(f"Tried to set Camera overlay directions but key not found. Is it init`d?")

    def should_camera_move(self, start_pos: Tuple, target_pos: Tuple) -> bool:
        """
        Determine if camera should move based on start and target pos and intersecting the edge of the screen.
        pos is x, y.
        """
        start_x, start_y = start_pos
        target_x, target_y = target_pos
        camera = self.get_ui_element(UIElement.CAMERA)

        # if camera has been init'd
        if camera:
            edge_start_x = camera.start_tile_col
            edge_end_x = camera.start_tile_col + camera.columns
            edge_start_y = camera.start_tile_row
            edge_end_y = camera.start_tile_row + camera.rows

            start_pos_in_edge = self.is_target_pos_in_camera_edge(start_pos)
            target_pos_in_edge = self.is_target_pos_in_camera_edge(target_pos)

            # are we currently in the edge (e.g. edge of world)
            if start_pos_in_edge:

                # will we still be in the edge after we move?
                if target_pos_in_edge:
                    dir_x = target_x - start_x
                    dir_y = target_y - start_y

                    # are we moving to a worse position?
                    if edge_start_x <= start_x < edge_start_x + camera.edge_size + 1:
                        # player is on the left side, are we moving left?
                        if dir_x < 0:
                            return True
                    if edge_end_x > start_x >= edge_end_x - camera.edge_size - 2:
                        # player is on the right side, are we moving right?
                        if 0 < dir_x:
                            return True
                    if edge_start_y <= start_y < edge_start_y + camera.edge_size + 1:
                        # player is on the up side, are we moving up?
                        if dir_y < 0:
                            return True
                    if edge_end_y > start_y >= edge_end_y - camera.edge_size - 2:
                        # player is on the down side, are we moving down?
                        if 0 < dir_y:
                            return True

            elif target_pos_in_edge:
                # we are moving into the edge
                return True
        else:
            logging.warning(f"Tried to check if Camera should move but key not found. Is it init`d?")

        return False

    def world_to_screen_position(self, pos: Tuple[int, int]):
        """
        Convert from the world_objects position to the screen position. -1, -1 if camera not init'd.
        """
        # TODO - this shouldnt rely on UI, if possible.
        camera = self.get_ui_element(UIElement.CAMERA)

        # if camera has been init'd
        if camera:
            return camera.world_to_screen_position(pos)
        logging.warning("Tried to get screen position but camera not init`d. Likely to draw in wrong place, "
                        "if it draws at all.")
        return 0, 0

        ############## ENTITY INFO ###################

    def set_selected_entity(self, entity: EntityID):
        """
        Set the selected entity and show it.
        """
        entity_info = self.get_ui_element(UIElement.ENTITY_INFO)

        if entity_info:
            if entity:
                entity_info.set_entity(entity)
                entity_info.show()
            else:
                entity_info.cleanse()
        else:
            logging.warning(f"Tried to set selected entity in EntityInfo but key not found. Is it init`d?")

    ################## ENTITY INFO ####################################

    def hide_entity_info(self):
        """
        Hide the entity info ui_manager element.
        """
        entity_info = self.get_ui_element(UIElement.ENTITY_INFO)

        if entity_info:
            entity_info.cleanse()
        else:
            logging.warning(f"Tried to kill EntityInfo but key not found. Is it init`d?")

    ######################## MESSAGES #################################

    def add_to_message_log(self, message: str):
        """
        Add a text to the message log. Includes processing of the text.
        """
        try:
            message_log = self.get_ui_element(UIElement.MESSAGE_LOG)
            message_log.add_message(message)

        except AttributeError:
            logging.warning(f"Tried to add text to MessageLog but key not found. Is it init`d?")


ui = _UIManager()
