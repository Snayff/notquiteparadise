from __future__ import annotations
from typing import List, Tuple, Optional, Iterator

import pygame
import pygame_gui

from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui.elements import UIImage, UIWindow
from scripts.engine.core.constants import TileCategory


class DungenViewer(UIWindow):
    """
    UI component that renders the construction of a dungeon as a separate window, step by step.
    """

    def __init__(self, rect: Rect, manager: pygame_gui.ui_manager.UIManager):
        super().__init__(rect, manager, element_id="dungeon_dev_view")

        # config of view
        self.sleep_per_room = 0.2
        self.scale_factor = 20.0
        self.floor_colour = (214, 211, 191, 255)
        self.wall_colour = (51, 39, 18, 255)

        # create the image to hold the rooms
        rect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.view = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                               container=self.get_container(), object_id="#roomview")

        self.timer: float = 0.0
        self.level = None
        self.iterator: Optional[Iterator] = None

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        if self.visible:
            self.timer += time_delta
            if self.timer > self.sleep_per_room:
                self.level = next(self.iterator, None)  # type: ignore
                if self.level:
                    self._update_view()  # type: ignore
                self.timer = 0

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass

    def _update_view(self):
        """
        Updates the view of the dungeon
        """
        surf = Surface((self.view.rect.width, self.view.rect.height), SRCALPHA)
        scale = self.scale_factor

        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                color = self.floor_colour if self.level[x][y] == TileCategory.FLOOR else self.wall_colour
                surf.fill(color, rect=Rect((x * scale, y * scale), (scale, scale)))

        self.view.set_image(surf)

    def init_viewer(self):
        """
        Gets the data for the viewer
        """
        from scripts.engine import dungen
        self.iterator = dungen.generate_steps("cave")
        self._reset()

    def _reset(self):
        """
        Resets the state of the dungeon view object
        """
        self.timer = self.sleep_per_room


