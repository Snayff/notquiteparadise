from __future__ import annotations

from typing import Iterator, Optional

import pygame
import pygame_gui
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui.elements import UIImage, UIPanel

from scripts.engine.internal import library
from scripts.engine.internal.constant import RenderLayer, TileCategory


class DungenViewer(UIPanel):
    """
    UI component that renders the construction of a dungeon as a separate window, step by step.
    """

    def __init__(self, rect: Rect, manager: pygame_gui.ui_manager.UIManager):
        super().__init__(rect, RenderLayer.UI_WINDOW, manager, object_id="dungen_viewer")

        # config of view
        self.sleep_per_room = 0.1
        self.scale_factor = 20.0
        self.category_colours = {
            TileCategory.FLOOR: (214, 211, 191, 255),
            TileCategory.WALL: (51, 39, 18, 255),
            TileCategory.ACTOR: (235, 172, 26, 255),
            TileCategory.PLAYER: (0, 255, 0, 255),
            TileCategory.DEBUG: (255, 0, 0, 255),
        }

        # create the image to hold the rooms
        rect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.view = UIImage(
            relative_rect=Rect((0, 0), rect.size),
            image_surface=blank_surf,
            manager=manager,
            container=self.get_container(),
            object_id="#roomview",
        )

        self.timer: float = 0.0
        self.map = None
        self.iterator: Optional[Iterator] = None

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        if self.visible:
            self.timer += time_delta
            if self.timer > self.sleep_per_room:
                self.map = next(self.iterator, None)  # type: ignore
                if self.map:
                    self._update_view()
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

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                tile_cat = self.map[x][y]
                if tile_cat in self.category_colours:
                    colour = self.category_colours[tile_cat]
                else:
                    colour = self.category_colours[TileCategory.DEBUG]
                surf.fill(colour, rect=Rect((x * scale, y * scale), (scale, scale)))

        self.view.set_image(surf)

    def refresh_viewer(self):
        """
        Gets the data for the viewer and runs generation again.
        """
        map_name = "cave"

        # set the scale so map always fits on screen
        map_data = library.MAPS[map_name]
        x_scale = self.rect.width // map_data.width
        y_scale = self.rect.height // map_data.height
        self.scale_factor = min(x_scale, y_scale)

        from scripts.engine.core import dungen

        self.iterator = dungen.generate_steps(map_name)
        self._reset()

    def _reset(self):
        """
        Resets the state of the dungeon view object
        """
        self.timer = self.sleep_per_room
