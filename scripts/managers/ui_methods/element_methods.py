import logging
import pygame

from scripts.core.constants import UIElementTypes
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

    def update_element_visibility(self, element_type, visible):
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

        for key, element in self.manager.elements:
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

