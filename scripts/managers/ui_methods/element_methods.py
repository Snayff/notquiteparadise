import logging
from typing import Tuple

import pygame

from scripts.core.constants import UIElementTypes, SkillShapes
from scripts.global_singletons.data_library import library
from scripts.ui_elements.camera import Camera
from scripts.ui_elements.entity_info import SelectedEntityInfo
from scripts.ui_elements.entity_queue import EntityQueue
from scripts.ui_elements.message_log import MessageLog
from scripts.ui_elements.skill_bar import SkillBar
from scripts.ui_elements.targeting_overlay import TargetingOverlay


class ElementMethods:
    """
    Methods for taking actions with ui elements

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

    def init_message_log(self):
        """
        Initialise the message log ui element.
        """
        self.manager.elements[UIElementTypes.MESSAGE_LOG.name] = MessageLog()

    def init_entity_info(self):
        """
        Initialise the selected entity info ui element
        """
        self.manager.elements[UIElementTypes.ENTITY_INFO.name] = SelectedEntityInfo()

    def init_targeting_overlay(self):
        """
        Initialise the targeting_overlay
        """
        self.manager.elements[UIElementTypes.TARGETING_OVERLAY.name] = TargetingOverlay()

    def init_skill_bar(self):
        """
        Initialise the skill bar
        """
        self.manager.elements[UIElementTypes.SKILL_BAR.name] = SkillBar()

    def init_entity_queue(self):
        """
        Initialise the entity queue
        """
        self.manager.elements[UIElementTypes.ENTITY_QUEUE.name] = EntityQueue()

    def init_camera(self):
        """
        Initialise the camera
        """
        self.manager.elements[UIElementTypes.CAMERA.name] = Camera()

    def set_element_visibility(self, element_type, visible):
        """
        Update whether an element is visible.

        Args:
            element_type (UIElementTypes): 
            visible (bool):
        """
        try:
            element = self.manager.elements[element_type.name]
            element.is_visible = visible
        except KeyError:
            logging.debug(f"Tried to set {element_type.name} to {visible} but key doesn't exist.")

    def draw_visible_elements(self):
        """
        Draw the visible ui elements based on is_visible attribute of the element
        """
        # TODO - add handling for dirty

        surface = self.manager.main_surface

        for key, element in self.manager.elements.items():
            if element.is_visible:
                element.draw(surface)

        # resize the surface to the desired resolution
        scaled_surface = pygame.transform.scale(surface, (self.manager.desired_width, self.manager.desired_height))
        self.manager.screen.blit(scaled_surface, (0, 0))

        # update the display
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def set_selected_entity(self, entity):
        """
        Set the selected entity

        Args:
            entity(Entity):
        """
        self.manager.elements[UIElementTypes.ENTITY_INFO.name].selected_entity = entity

    def set_skill_being_targeted(self, skill):
        """
        Set the skill that the player is currently targeting

        Args:
            skill (Skill):
        """
        self.manager.elements[UIElementTypes.TARGETING_OVERLAY.name].skill_being_targeted = skill

    def set_selected_tile(self, tile):
        """
        Update the tile currently selected. Must be in the highlighted range.

        Args:
            tile(Tile):
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        if tile in targeting_overlay.tiles_in_range_and_fov:
            targeting_overlay.selected_tile = tile

    def set_tiles_in_camera(self, tiles):
        """
        Set the tiles to be drawn by the camera based on the camera size.

        Args:
            tiles (list[Tile]): all of the tiles.
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        camera.tiles_to_draw = tiles

    def get_camera_view_size(self):
        """
        Get the size of the camera view

        Returns:
            Tuple[int,int]: (rows, cols)  in number of tiles
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        return camera.rows_in_view, camera.cols_in_view

    def get_ui_element(self, element_type):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.

        Args:
            element_type (UIElementTypes):

        Returns:
            any: ui element
        """
        return self.manager.elements[element_type.name]

    def update_targeting_overlays_tiles_in_range_and_fov(self):
        """
        Update list of valid tiles within range based on currently selected skill's range.
        """
        # TODO - convert to a set and set via en event
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        # clear current tiles
        targeting_overlay.tiles_in_range_and_fov = []

        # if there is a skill being targeted
        if targeting_overlay.skill_being_targeted:

            skill_data = library.get_skill_data(targeting_overlay.skill_being_targeted.skill_tree_name,
                                                targeting_overlay.skill_being_targeted.name)
            skill_range = skill_data.range

            from scripts.global_singletons.managers import world_manager
            tiles = world_manager.FOV.get_tiles_in_range_and_fov_of_player(skill_range)

            targeting_overlay.tiles_in_range_and_fov = tiles

    def update_targeting_overlays_tiles_in_skill_effect_range(self):
        """
        Update the list of Tiles for those effected by the skill effect range. Based on selected skill.
        """
        # TODO - convert to a set and set via en event
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

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
        # TODO - convert to a set and set via en event
        skill_bar = self.get_ui_element(UIElementTypes.SKILL_BAR)

        # update info
        from scripts.global_singletons.managers import world_manager
        player = world_manager.player

        # if the player has been init'd update skill bar
        if player:
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
        entity_queue = self.get_ui_element(UIElementTypes.ENTITY_QUEUE)

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