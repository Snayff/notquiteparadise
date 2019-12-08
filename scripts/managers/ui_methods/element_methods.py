import logging
import pygame
from typing import Tuple, List
from scripts.core.constants import UIElementTypes, TILE_SIZE, VisualInfo
from scripts.core.data_library import library
from scripts.managers.world_manager import world
from scripts.ui.ui_elements.entity_info import EntityInfo
from scripts.ui.ui_elements.message_log import MessageLog
from scripts.ui.ui_elements.entity_queue import EntityQueue
from scripts.ui.ui_elements.camera import Camera
from scripts.ui.ui_elements.skill_bar import SkillBar
from scripts.ui.ui_elements.targeting_overlay import TargetingOverlay
from scripts.world.entity import Entity
from scripts.world.tile import Tile


class ElementMethods:
    """
    Methods for taking actions with ui elements

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

        self.elements = {}  # list of all init'd ui elements
        self.pgui_elements = {}  # TODO - combine with above once resolved and there is no diff between the elements

    ############### INIT ################

    def init_message_log(self):
        """
        Initialise the text log ui element.
        """
        self.elements[UIElementTypes.MESSAGE_LOG.name] = MessageLog()

    def init_entity_info(self):
        """
        Initialise the selected entity info ui element
        """
        self.elements[UIElementTypes.ENTITY_INFO.name] = EntityInfo()

    def init_targeting_overlay(self):
        """
        Initialise the targeting_overlay
        """
        self.elements[UIElementTypes.TARGETING_OVERLAY.name] = TargetingOverlay()

    def init_skill_bar(self):
        """
        Initialise the skill bar.
        """
        width = 80
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = 2
        rect = pygame.Rect((x, y), (width, height))
        self.pgui_elements[UIElementTypes.SKILL_BAR.name] = SkillBar(rect, self.manager.Gui)

    def init_camera(self):
        """
        Initialise the camera.
        """
        rows = 10
        cols = 15
        width = cols * TILE_SIZE
        height = rows * TILE_SIZE
        x = 5
        y = 5
        rect = pygame.Rect((x, y), (width, height))
        self.pgui_elements[UIElementTypes.CAMERA.name] = Camera(rect, self.manager.Gui, rows, cols)

    def init_entity_queue(self):
        """
        Initialise the entity queue
        """
        self.elements[UIElementTypes.ENTITY_QUEUE.name] = EntityQueue()

        from scripts.managers.turn_manager import turn
        if turn:
            self.update_entity_queue()

    ################ ELEMENT ###################

    def set_element_visibility(self, element_type, visible):
        """
        Update whether an element is visible.

        Args:
            element_type (UIElementTypes): 
            visible (bool):
        """
        try:
            element = self.elements[element_type.name]
            element.is_visible = visible
        except KeyError:
            logging.warning(f"ui tried to set {element_type.name} to {visible} but key doesn`t exist.")

    def draw_visible_elements(self, main_surface):
        """
        Draw the visible ui elements. Checks is_visible.
        """
        # TODO - add handling for dirty

        for key, element in self.elements.items():
            if element.is_visible:
                element.draw(main_surface)

        # # resize the surface to the desired resolution
        # scaled_surface = pygame.transform.scale(main_surface, self.manager.Display.get_desired_resolution())
        # window = self.manager.Display.get_window()
        # window.blit(scaled_surface, (0, 0))
        #
        # # update the display
        # pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def update_elements(self):
        """
        Update the ui elements.
        """

        for key, element in self.elements.items():
            element.update()

    def get_ui_element(self, element_type):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.

        Args:
            element_type (UIElementTypes):

        Returns:
            any: ui element
        """
        try:
            return self.pgui_elements[element_type.name]
        except KeyError:
            return None

    def get_ui_elements(self):
        """
        Get all the ui elements

        Returns:
            list: list of ui_elements
        """
        return self.elements

    ############## CAMERA ###################

    def is_target_pos_in_camera_edge(self, target_pos: Tuple):
        """
        Determine if target position is within the edge of the camera

        Args:
            target_pos (): x,y

        Returns:
            bool:
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        player_x, player_y = target_pos

        edge_start_x = camera.start_tile_col
        edge_end_x = camera.start_tile_col + camera.columns
        edge_start_y = camera.start_tile_row
        edge_end_y = camera.start_tile_row + camera.rows

        if edge_start_x <= player_x < edge_start_x + camera.edge_size:
            return True
        elif edge_end_x >= player_x > edge_end_x - camera.edge_size:
            return True
        elif edge_start_y <= player_y < edge_start_y + camera.edge_size:
            return True
        elif edge_end_y >= player_y > edge_end_y - camera.edge_size:
            return True
        else:
            return False

    def move_camera(self, move_x, move_y):
        """
        Increment camera's drawn tiles in the given direction. N.B. Physical position on screen does not change.

        Args:
            move_x ():
            move_y ():
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        from scripts.managers.world_manager import world
        game_map = world.Map.get_game_map()

        # clamp function: max(low, min(n, high))
        camera.start_tile_col = max(0, min(camera.start_tile_col + move_x, game_map.width))
        camera.start_tile_row = max(0, min(camera.start_tile_row + move_y, game_map.height))

    def update_cameras_tiles(self):
        """
        Retrieve the tiles to draw within view of the camera and provide them to the camera. Checks FOV.
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        if camera:
            tiles = []

            for x in range(camera.start_tile_col, camera.start_tile_col + camera.columns):
                for y in range(camera.start_tile_row, camera.start_tile_row + camera.rows):
                    if world.FOV.is_tile_in_fov(x, y):
                        tiles.append(world.Map.get_tile(x, y))

            camera.set_tiles(tiles)

    def update_camera_game_map(self):
        """
        Update the camera game map to show what is in the tiles held by the camera.
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.update_game_map()

    def update_camera_grid(self):
        """
        Update the camera's grid. Controls tile hover highlighting.
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.update_grid()

    def set_player_tile(self, tile: Tile):
        """
        Set the player tile in the Camera ui element.

        Args:
            tile ():
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.set_player_tile(tile)

    def set_overlay_visibility(self, is_visible: bool):
        """
        Set the visibility of the targeting overlay in the Camera.

        Args:
            is_visible ():
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.set_overlay_visibility(is_visible)

    def set_overlay_directions(self, directions: List):
        """
        Set the overlay with possible targeting directions.

        Args:
            directions (): List of Directions
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.set_overlay(directions)

    def should_camera_move(self, start_pos: Tuple, target_pos: Tuple):
        """
        Determine if camera should move based on start and target pos and intersecting the edge of the screen.

        Args:
            start_pos (): x,y
            target_pos (): x,y

        Returns:
            bool:
        """
        start_x, start_y = start_pos
        target_x, target_y = target_pos
        camera = self.get_ui_element(UIElementTypes.CAMERA)

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
                    if edge_start_x <= start_x < edge_start_x + camera.edge_size:
                        # player is on the left side, are we moving left?
                        if dir_x < 0:
                            return True
                    if edge_end_x > start_x >= edge_end_x - camera.edge_size:
                        # player is on the right side, are we moving right?
                        if 0 < dir_x:
                            return True
                    if edge_start_y <= start_y < edge_start_y + camera.edge_size:
                        # player is on the up side, are we moving up?
                        if dir_y < 0:
                            return True
                    if edge_end_y > start_y >= edge_end_y - camera.edge_size:
                        # player is on the down side, are we moving down?
                        if 0 < dir_y:
                            return True

            elif target_pos_in_edge:
                # we are moving into the edge
                return True

            else:
                return False

    ############## OTHER ELEMENTS ###################

    def set_selected_entity(self, entity: Entity):
        """
        Set the selected entity

        Args:
            entity(Entity):
        """
        try:
            self.elements[UIElementTypes.ENTITY_INFO.name].set_selected_entity(entity)
        except KeyError:
            logging.warning(f"Tried to set selected entity in EntityInfo but key not found. Is it init'd?")

    def update_entity_queue(self):
        """
        Get info from the turn and update the entity queue to be displayed
        """
        # TODO - convert to a set and set via en event
        entity_queue = self.get_ui_element(UIElementTypes.ENTITY_QUEUE)

        # if entity queue has been init'd
        if entity_queue:
            # clear current queue
            entity_queue.entity_queue.clear()

            counter = 0

            # loop entities in turn queue, up to max to show
            from scripts.managers.turn_manager import turn
            for entity, time in turn.turn_queue.items():
                if counter < entity_queue.max_entities_to_show:
                    icon = entity.icon

                    # catch any images not the right size and resize them
                    if icon.get_size() != (entity_queue.entity_icon_size, entity_queue.entity_icon_size):
                        icon = pygame.transform.smoothscale(icon, (entity_queue.entity_icon_size,
                            entity_queue.entity_icon_size))

                    entity_queue.entity_queue.append((icon, entity.name))

                    counter += 1

                else:
                    break

    def add_to_message_log(self, message):
        """
        Add a text to the message log. Includes processing of the text.

        Args:
            message (str):
        """
        try:
            message_log = self.manager.Element.get_ui_element(UIElementTypes.MESSAGE_LOG)
            message_log.add_message(message)

        except AttributeError:
            logging.warning(f"Tried to add text to MessageLog but key not found. Is it init'd?")