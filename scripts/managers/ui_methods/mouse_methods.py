
import pygame
from scripts.core.constants import UIElements


class MouseMethods:
    """
    Methods for handling ui interactions

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

    def get_scaled_mouse_pos(self):
        """
        Get the scaled mouse position

        Returns(tuple): Returns mouse position scaled to screen size
        """
        mouse_pos = pygame.mouse.get_pos()
        mod_x, mod_y = self.manager.Display.get_screen_scaling_mod()
        scaled_mouse_pos = mouse_pos[0] // mod_x, mouse_pos[1] // mod_y
        return scaled_mouse_pos

    def get_relative_scaled_mouse_pos(self, mouse_x=-1, mouse_y=-1):
        """
        Get the scaled mouse position relative to the ui element it is colliding with. Current position of mouse
        used if one not provided.

        Args:
            mouse_x(int): Optional. Mouses x coord
            mouse_y(int):  Optional. Mouses y coord.

        Returns:
            tuple: Returns mouse position scaled to screen size
        """
        # if mouse pos was provided use it, else get it
        if mouse_x != -1 and mouse_y != -1:
            mouse_pos = (mouse_x, mouse_y)
        else:
            mouse_pos = self.get_scaled_mouse_pos()

        ui_object = self.get_colliding_panel(mouse_pos[0], mouse_pos[1])

        relative_mouse_pos = mouse_pos[0] - ui_object.x, mouse_pos[1] - ui_object.y

        return relative_mouse_pos

    def get_colliding_panel(self, mouse_x=-1, mouse_y=-1):
        """
        Determine which panel is colliding with  mouse position. Current position used if one not provided.

        Args:
            mouse_x(int): Optional. Mouses x coord
            mouse_y(int):  Optional. Mouses y coord.

        Returns:
            rect: ui_element's panel
        """
        colliding_panel = None

        # if mouse pos was provided use it, else get it
        if mouse_x != -1 and mouse_y != -1:
            mouse_pos = (mouse_x, mouse_y)
        else:
            mouse_pos = self.get_scaled_mouse_pos()

        ui_elements = self.manager.Element.get_ui_elements()
        for key, ui_object in ui_elements.items():
            if hasattr(ui_object, "panel"):
                if ui_object.panel.rect.collidepoint(mouse_pos):
                    colliding_panel = ui_object.panel

        return colliding_panel

    def get_colliding_ui_element_type(self, mouse_x=-1, mouse_y=-1):
        """
        Determine which ui element type is colliding with mouse position. Current position used if one not provided.

        Args:
            mouse_x(int): Optional. Mouses x coord
            mouse_y(int):  Optional. Mouses y coord.

        Returns:
            UIElements: ui_element type
        """
        ui_element_type = None

        # if mouse pos was provided use it, else get it
        if mouse_x != -1 and mouse_y != -1:
            mouse_pos = (mouse_x, mouse_y)
        else:
            mouse_pos = self.get_scaled_mouse_pos()

        ui_elements = self.manager.Element.get_ui_elements()
        for key, ui_object in ui_elements.items():
            if hasattr(ui_object, "panel"):
                if ui_object.panel.rect.collidepoint(mouse_pos):
                    ui_element_type = key

        return ui_element_type

    def get_skill_index_from_skill_clicked(self, relative_x, relative_y):
        """
        Return the index of the skill clicked in the skill bar

        Args:
            relative_x (int):
            relative_y (int):

        Returns:
            int: -1 if nothing, else 0+.

        Notes:
            The skills in the skill bar are pulled, in order, from the player`s known skills.
        """
        skill_bar = self.manager.Element.get_ui_element(UIElements.SKILL_BAR)

        for container in skill_bar.skill_containers:
            if container.rect.collidepoint(relative_x, relative_y):
                skill_index = skill_bar.skill_containers.index(container)
                return skill_index

        return -1
