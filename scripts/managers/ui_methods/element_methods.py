import logging
from typing import Tuple

import pygame

from scripts.core.constants import UIElements
from scripts.global_singletons.data_library import library
from scripts.ui.ui_elements.camera import Camera
from scripts.ui.ui_elements.entity_info import SelectedEntityInfo
from scripts.ui.ui_elements.entity_queue import EntityQueue
from scripts.ui.ui_elements.message_log import MessageLog
from scripts.ui.ui_elements.skill_bar import SkillBar
from scripts.ui.ui_elements.targeting_overlay import TargetingOverlay


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

        ###########################################################
        from scripts.ui.templates.frame import Frame
        from scripts.ui.templates.widget_style import WidgetStyle
        from scripts.ui.templates.text_box import TextBox
        from scripts.ui.basic.fonts import Font
        font = Font().default
        from scripts.ui.basic.colours import Colour
        text_box_style = WidgetStyle(font, background_colour=Colour().green, border_colour=Colour().red, border_size=1)
        text_box = TextBox(5, 5, 90, 90, text_box_style, "this is a text box and has text over several lines")
        widgets = [text_box]
        frame_style = WidgetStyle(font, background_colour=Colour().blue, border_colour=Colour().red, border_size=1)
        frame = Frame(200, 200, 100, 100, frame_style, widgets)

        from scripts.ui.ui_elements.another_message_log import AnotherMessageLog
        msg_log = AnotherMessageLog(frame)
        msg_log.is_visible = True
        self.elements["new_msg_log"] = msg_log
        #############################################################

    def init_message_log(self):
        """
        Initialise the message log ui element.
        """
        self.elements[UIElements.MESSAGE_LOG.name] = MessageLog()

    def init_entity_info(self):
        """
        Initialise the selected entity info ui element
        """
        self.elements[UIElements.ENTITY_INFO.name] = SelectedEntityInfo()

    def init_targeting_overlay(self):
        """
        Initialise the targeting_overlay
        """
        self.elements[UIElements.TARGETING_OVERLAY.name] = TargetingOverlay()

    def init_skill_bar(self):
        """
        Initialise the skill bar
        """
        self.elements[UIElements.SKILL_BAR.name] = SkillBar()

    def init_entity_queue(self):
        """
        Initialise the entity queue
        """
        self.elements[UIElements.ENTITY_QUEUE.name] = EntityQueue()

        from scripts.global_singletons.managers import turn_manager
        if turn_manager:
            self.update_entity_queue()

    def init_camera(self):
        """
        Initialise the camera
        """
        self.elements[UIElements.CAMERA.name] = Camera()

    def set_element_visibility(self, element_type, visible):
        """
        Update whether an element is visible.

        Args:
            element_type (UIElements): 
            visible (bool):
        """
        try:
            element = self.elements[element_type.name]
            element.is_visible = visible
        except KeyError:
            logging.debug(f"Tried to set {element_type.name} to {visible} but key doesn't exist.")

    def draw_visible_elements(self):
        """
        Draw the visible ui elements based on is_visible attribute of the element
        """
        # TODO - add handling for dirty

        surface = self.manager.Display.get_main_surface()

        for key, element in self.elements.items():
            if element.is_visible:
                element.draw(surface)

        # resize the surface to the desired resolution
        scaled_surface = pygame.transform.scale(surface, self.manager.Display.get_desired_resolution())
        window = self.manager.Display.get_window()
        window.blit(scaled_surface, (0, 0))

        # update the display
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def set_selected_entity(self, entity):
        """
        Set the selected entity

        Args:
            entity(Entity):
        """
        self.elements[UIElements.ENTITY_INFO.name].selected_entity = entity

    def set_skill_being_targeted(self, skill):
        """
        Set the skill that the player is currently targeting

        Args:
            skill (Skill):
        """
        self.elements[UIElements.TARGETING_OVERLAY.name].skill_being_targeted = skill

    def set_selected_tile(self, tile):
        """
        Update the tile currently selected in the targeting overlay. Must be in the highlighted range.

        Args:
            tile(Tile):
        """
        targeting_overlay = self.get_ui_element(UIElements.TARGETING_OVERLAY)

        if tile in targeting_overlay.tiles_in_range_and_fov:
            targeting_overlay.selected_tile = tile

    def set_tiles_in_targeting_overlay(self, tiles):
        """
        Set the tiles to be shown in the targeting overlay

        Args:
            tiles (list[Tiles]):
        """
        targeting_overlay = self.get_ui_element(UIElements.TARGETING_OVERLAY)
        targeting_overlay.tiles_in_range_and_fov = tiles

    def get_ui_element(self, element_type):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.

        Args:
            element_type (UIElements):

        Returns:
            any: ui element
        """
        try:
            return self.elements[element_type.name]
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
        targeting_overlay = self.get_ui_element(UIElements.TARGETING_OVERLAY)
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

            from scripts.global_singletons.managers import world_manager
            tiles = world_manager.FOV.get_tiles_in_range_and_fov_of_player(skill_range)

            self.set_tiles_in_targeting_overlay(tiles)

    def update_targeting_overlays_tiles_in_skill_effect_range(self):
        """
        Update the list of Tiles for those effected by the skill effect range. Based on selected skill.
        """
        # TODO - convert to a set method and set via an event
        targeting_overlay = self.get_ui_element(UIElements.TARGETING_OVERLAY)

        # if there is a skill being targeted
        if targeting_overlay.skill_being_targeted:

            # clear current tiles
            targeting_overlay.tiles_in_skill_effect_range = []

            # get the skill data
            data = library.get_skill_data(targeting_overlay.skill_being_targeted.skill_tree_name,
                                          targeting_overlay.skill_being_targeted.name)

            from scripts.global_singletons.managers import world_manager
            coords = world_manager.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world_manager.Map.get_tiles(targeting_overlay.selected_tile.x,
                                                         targeting_overlay.selected_tile.y, coords)

            targeting_overlay.tiles_in_skill_effect_range = effected_tiles

    def update_skill_bars_icons(self):
        """
        Get the player`s known skills to show in the skill bar.
        """
        # TODO - convert to a set and set via an event
        skill_bar = self.get_ui_element(UIElements.SKILL_BAR)

        # update info
        from scripts.global_singletons.managers import world_manager
        player = world_manager.player

        # if the player and the skill bar have been init'd update skill bar
        if player and skill_bar:
            for counter, skill in enumerate(player.actor.known_skills):

                skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)
                skill_icon = pygame.image.load("assets/skills/" + skill_data.icon).convert_alpha()

                # catch any images not the right size and resize them
                if skill_icon.get_size() != (skill_bar.skill_icon_size, skill_bar.skill_icon_size):
                    icon = pygame.transform.smoothscale(skill_icon, (skill_bar.skill_icon_size,
                            skill_bar.skill_icon_size))
                else:
                    icon = skill_icon

                skill_bar.skill_containers[counter].skill_icon = icon

    def update_entity_queue(self):
        """
        Get info from the turn_manager and update the entity queue to be displayed
        """
        # TODO - convert to a set and set via en event
        entity_queue = self.get_ui_element(UIElements.ENTITY_QUEUE)

        # if entity queue has been init'd
        if entity_queue:
            # clear current queue
            entity_queue.entity_queue.clear()

            counter = 0

            # loop entities in turn queue, up to max to show
            from scripts.global_singletons.managers import turn_manager
            for entity, time in turn_manager.turn_queue.items():
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

    def set_tiles_in_camera(self, tiles):
        """
        Set the tiles to be drawn by the camera based on the camera size.

        Args:
            tiles (list[Tile]): all of the tiles to draw.
        """
        camera = self.get_ui_element(UIElements.CAMERA)

        camera.tiles_to_draw = tiles

    def is_target_pos_in_camera_edge(self, target_pos: Tuple):
        """
        Determine if target position is within the edge of the camera

        Args:
            target_pos (): x,y

        Returns:
            bool:
        """
        camera = self.get_ui_element(UIElements.CAMERA)
        player_x, player_y = target_pos

        edge_start_x = camera.x
        edge_end_x = camera.x + camera.width
        edge_start_y = camera.y
        edge_end_y = camera.y + camera.height

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
        camera = self.get_ui_element(UIElements.CAMERA)

        # if camera has been init'd
        if camera:
            edge_start_x = camera.x
            edge_end_x = camera.x + camera.width
            edge_start_y = camera.y
            edge_end_y = camera.y + camera.height

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
                            print("moving left")
                            return True
                    if edge_end_x > start_x >= edge_end_x - camera.edge_size:
                        # player is on the right side, are we moving right?
                        if 0 < dir_x:
                            print("moving right")
                            return True
                    if edge_start_y <= start_y < edge_start_y + camera.edge_size:
                        # player is on the up side, are we moving up?
                        if dir_y < 0:
                            print("moving up")
                            return True
                    if edge_end_y > start_y >= edge_end_y - camera.edge_size:
                        # player is on the down side, are we moving down?
                        if 0 < dir_y:
                            print("moving down")
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
        camera = self.get_ui_element(UIElements.CAMERA)

        from scripts.global_singletons.managers import world_manager
        game_map = world_manager.Map.get_game_map()

        # clamp function: max(low, min(n, high))
        camera.x = max(0, min(camera.x + move_x, game_map.width))
        camera.y = max(0, min(camera.y + move_y, game_map.height))

    def update_cameras_tiles_to_draw(self):
        """
        Retrieve the tiles to draw within view of the camera
        """
        camera = self.get_ui_element(UIElements.CAMERA)
        coords = []

        # if camera has been init'd
        if camera:
            for x in range(camera.x, camera.x + camera.width):
                for y in range(camera.y, camera.y + camera.height):
                    coords.append((x, y))

            from scripts.global_singletons.managers import world_manager
            # use 0,0 to stop the camera double jumping due to converting back and forth from world and physical space
            tiles = world_manager.Map.get_tiles(0, 0, coords)
            self.set_tiles_in_camera(tiles)