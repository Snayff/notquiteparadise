from __future__ import annotations

import pygame
from typing import TYPE_CHECKING
from scripts.engine.core.constants import VisualInfo


if TYPE_CHECKING:
    from typing import Tuple
    from scripts.managers.ui_manager.ui_manager import UIManager


class DisplayMethods:
    """
    Methods for handling display

    Attributes:
        manager ():
    """

    def __init__(self, manager):

        self._manager = manager  # type: UIManager

        self.init_pygame()

        self.desired_width = VisualInfo.BASE_WINDOW_WIDTH
        self.desired_height = VisualInfo.BASE_WINDOW_HEIGHT
        # TODO - allow for selection by player but only multiples of base (16:9)
        self.screen_scaling_mod_x = self.desired_width // VisualInfo.BASE_WINDOW_WIDTH
        self.screen_scaling_mod_y = self.desired_height // VisualInfo.BASE_WINDOW_HEIGHT
        self.window = pygame.display.set_mode((self.desired_width, self.desired_height))
        self.main_surface = pygame.Surface((VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT),
                                           pygame.SRCALPHA)

        self.init_display_config()

    ############# INIT ###############################

    @staticmethod
    def init_pygame():
        """
        Init pygame
        """
        pygame.init()

    @staticmethod
    def init_display_config():
        """
        Initialise display settings.
        """
        pygame.display.set_caption("Not Quite Paradise")
        # pygame.display.set_icon() # TODO - add window icon

    ############# GET ##############################

    def get_screen_scaling_mod(self) -> Tuple[int, int]:
        """
        Get the screen scaling modifier
        """
        return self.screen_scaling_mod_x, self.screen_scaling_mod_y

    def get_main_surface(self) -> pygame.Surface:
        """
        Get the main surface where all draws eventually go.
        """
        return self.main_surface

    def get_desired_resolution(self) -> Tuple[int, int]:
        """
        Get the desired resolution as (width, height)
        """
        return self.desired_width, self.desired_height

    def get_window(self) -> pygame.display:
        """
        Get the window
        """
        return self.window