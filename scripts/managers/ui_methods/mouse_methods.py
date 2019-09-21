import pygame


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

    def get_relative_scaled_mouse_pos(self, screen_scaling_mod_x, screen_scaling_mod_y, visible_elements,
            visible_panel_name, mouse_x=-1, mouse_y=-1):
        """
        Get the scaled mouse position relative to the visible panel. Current position used if one not provided.

        Args:
            screen_scaling_mod_x ():
            screen_scaling_mod_y ():
            visible_elements ():
            visible_panel_name (str): name of the visible panel
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

        ui_object = visible_elements.get(visible_panel_name).panel

        relative_mouse_pos = mouse_pos[0] - ui_object.x, mouse_pos[1] - ui_object.y

        return relative_mouse_pos

    def get_clicked_panels_rect(self, screen_scaling_mod_x, screen_scaling_mod_y, visible_elements, mouse_x=-1,
            mouse_y=-1):
        """
        Determine which panel has been clicked based on mouse position. Current position used if one not provided.

        Args:
            screen_scaling_mod_y ():
            visible_elements ():
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

        for key, ui_object in visible_elements.items():
            if hasattr(ui_object, "panel"):
                if ui_object.panel.rect.collidepoint(mouse_pos):
                    clicked_rect = key

        return clicked_rect
