import pygame

from scripts.core.constants import UIElementTypes


class MouseMethods:
    """
    Methods for handling ui interactions

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

    @staticmethod
    def get_scaled_mouse_pos(screen_scaling_mod_x, screen_scaling_mod_y):
        """
        Get the scaled mouse position

        Returns(tuple): Returns mouse position scaled to screen size

        """
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = mouse_pos[0] // screen_scaling_mod_x, mouse_pos[1] // screen_scaling_mod_y
        return scaled_mouse_pos

    def get_relative_scaled_mouse_pos(self, screen_scaling_mod_x, screen_scaling_mod_y, ui_element, mouse_x=-1,
            mouse_y=-1):
        """
        Get the scaled mouse position relative to the ui element. Current position used if one not provided.

        Args:
            screen_scaling_mod_x (int):
            screen_scaling_mod_y (int):
            ui_element (UIElementTypes):
            mouse_x(int): Optional. Mouses x coord
            mouse_y(int):  Optional. Mouses y coord.

        Returns:
            tuple: Returns mouse position scaled to screen size
        """
        # if mouse pos was provided use it, else get it
        if mouse_x != -1 and mouse_y != -1:
            mouse_pos = (mouse_x, mouse_y)
        else:
            mouse_pos = self.get_scaled_mouse_pos(screen_scaling_mod_x, screen_scaling_mod_y)

        ui_object = self.manager.Element.get_ui_element(ui_element)

        relative_mouse_pos = mouse_pos[0] - ui_object.x, mouse_pos[1] - ui_object.y

        return relative_mouse_pos

    def get_clicked_panels_rect(self, screen_scaling_mod_x, screen_scaling_mod_y, mouse_x=-1, mouse_y=-1):
        """
        Determine which panel has been clicked based on mouse position. Current position used if one not provided.

        Args:
            screen_scaling_mod_y ():
            screen_scaling_mod_x ():
            mouse_x(int): Optional. Mouses x coord
            mouse_y(int):  Optional. Mouses y coord.

        Returns:
            rect: ui_element
        """
        clicked_rect = None

        # if mouse pos was provided use it, else get it
        if mouse_x != -1 and mouse_y != -1:
            mouse_pos = (mouse_x, mouse_y)
        else:
            mouse_pos = self.get_scaled_mouse_pos(screen_scaling_mod_x, screen_scaling_mod_y)

        for key, ui_object in self.manager.elements.items():
            if hasattr(ui_object, "panel"):
                if ui_object.panel.rect.collidepoint(mouse_pos):
                    clicked_rect = key

        return clicked_rect

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
        skill_bar = self.manager.Element.get_ui_element(UIElementTypes.SKILL_BAR)

        for container in skill_bar.skill_containers:
            if container.rect.collidepoint(relative_x, relative_y):
                skill_index = skill_bar.skill_containers.index(container)
                return skill_index

        return -1
