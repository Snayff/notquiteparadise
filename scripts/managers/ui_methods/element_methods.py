import logging
import pygame
from typing import Tuple
from scripts.core.constants import UIElementTypes, TILE_SIZE, VisualInfo
from scripts.core.data_library import library
from scripts.managers.world_manager import world
from scripts.ui.ui_elements.entity_info import EntityInfo
from scripts.ui.ui_elements.message_log import MessageLog
from scripts.ui.ui_elements.entity_queue import EntityQueue
from scripts.ui.ui_elements.camera import Camera
from scripts.ui.ui_elements.pgui_camera import PguiCamera
from scripts.ui.ui_elements.pgui_skill_bar import PguiSkillBar
from scripts.ui.ui_elements.skill_bar import SkillBar
from scripts.ui.ui_elements.targeting_overlay import TargetingOverlay
from scripts.world.entity import Entity


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

    def init_pgui_skill_bar(self):
        """
        Initialise the skill bar.
        """
        width = 80
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = 2
        rect = pygame.Rect((x, y), (width, height))
        self.pgui_elements[UIElementTypes.SKILL_BAR.name] = PguiSkillBar(rect, self.manager.Gui)

    def init_pgui_camera(self):
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
        self.pgui_elements[UIElementTypes.CAMERA.name] = PguiCamera(rect, self.manager.Gui, rows, cols)

    def init_skill_bar(self):
        """
        Initialise the skill bar
        """
        self.elements[UIElementTypes.SKILL_BAR.name] = SkillBar()

    def init_entity_queue(self):
        """
        Initialise the entity queue
        """
        self.elements[UIElementTypes.ENTITY_QUEUE.name] = EntityQueue()

        from scripts.managers.turn_manager import turn
        if turn:
            self.update_entity_queue()

    def init_camera(self):
        """
        Initialise the camera
        """
        self.elements[UIElementTypes.CAMERA.name] = Camera()

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

    def get_selected_tile_pos(self) -> Tuple:
        """
        Get the selected tile pos

        Returns:
            Tuple: tile x,y
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        return camera.selected_tile_pos

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

    def set_skill_being_targeted(self, skill):
        """
        Set the skill that the player is currently targeting

        Args:
            skill (Skill):
        """
        self.elements[UIElementTypes.TARGETING_OVERLAY.name].skill_being_targeted = skill

    def set_selected_tile(self, tile):
        """
        Update the tile currently selected in the targeting overlay. Must be in the highlighted range.

        Args:
            tile(Tile):
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        if tile in targeting_overlay.tiles_in_range_and_fov:
            targeting_overlay.selected_tile = tile

    def set_tiles_in_targeting_overlay(self, tiles):
        """
        Set the tiles to be shown in the targeting overlay

        Args:
            tiles (list[Tiles]):
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)
        targeting_overlay.tiles_in_range_and_fov = tiles

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

    def get_skill_being_targeted(self):
        """
        Get the skill being targeted (held in targeting overlay).

        Returns:
            Skill:
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)
        return targeting_overlay.skill_being_targeted

    def update_targeting_overlays_tiles_in_range_and_fov(self):
        """
        Update list of valid tiles within range based on currently selected skill's range.
        """
        skill_being_targeted = self.get_skill_being_targeted()

        # if there is a skill being targeted
        if skill_being_targeted:

            skill_data = library.get_skill_data(skill_being_targeted.skill_tree_name, skill_being_targeted.name)
            skill_range = skill_data.range

            from scripts.managers.world_manager import world
            tiles = world.FOV.get_tiles_in_range_and_fov_of_player(skill_range)

            self.set_tiles_in_targeting_overlay(tiles)

    def update_targeting_overlays_tiles_in_skill_effect_range(self):
        """
        Update the list of Tiles for those effected by the skill effect range. Based on selected skill.
        """
        # TODO - convert to a set method and set via an event
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        # if there is a skill being targeted
        if targeting_overlay.skill_being_targeted:

            # clear current tiles
            targeting_overlay.tiles_in_skill_effect_range = []

            # get the skill data
            data = library.get_skill_data(targeting_overlay.skill_being_targeted.skill_tree_name,
                                          targeting_overlay.skill_being_targeted.name)

            from scripts.managers.world_manager import world
            coords = world.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world.Map.get_tiles(targeting_overlay.selected_tile.x,
                                                         targeting_overlay.selected_tile.y, coords)

            targeting_overlay.tiles_in_skill_effect_range = effected_tiles

    def update_skill_bars_icons(self):
        """
        Get the player`s known skills to show in the skill bar.
        """
        # TODO - convert to a set and set via an event
        skill_bar = self.get_ui_element(UIElementTypes.SKILL_BAR)

        # update info
        from scripts.managers.world_manager import world
        player = world.player

        # if the player and the skill bar have been init'd update skill bar
        if player and skill_bar:
            for counter, skill in enumerate(player.actor.known_skills):
                skill_bar.set_skill(counter, skill)

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
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.update_game_map()

    def set_player_pos_in_camera(self, x, y):
        """
        Use xy within camera to set the player's position within the camera.

        Args:
            x ():
            y ():
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        camera.set_player_cell(x, y)

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