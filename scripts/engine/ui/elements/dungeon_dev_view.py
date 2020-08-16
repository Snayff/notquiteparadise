
import pygame
import pygame_gui
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui import UIManager
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UIWindow
from scripts.engine.core.constants import RenderLayer
from scripts.engine.world_objects.world_gen import DungeonGeneration
from typing import List, Tuple, Optional, Iterator


class DungeonDevView(UIWindow):
    """
    UI component that renders the construction of a dungeon as a separate window, step by step.
    """

    SLEEP_PER_ROOM = 1.0
    SCALE_FACTOR = 20.0
    ROOM_COLOR = (216, 216, 216, 255)
    ROOM_WALL_COLOR = (64, 64, 64, 255)

    def __init__(self, rect: Rect, manager: pygame_gui.ui_manager.UIManager):

        super().__init__(rect, manager, element_id="dungeon_dev_view")

        rect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.view = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                               container=self.get_container(), object_id="#roomview")

        self.timer: float = 0.0
        self.level = None
        self.iterator: Optional[Iterator] = None

    def update_view(self):
        """
        Updates the view of the dungeon
        """
        surf = Surface((self.view.rect.width, self.view.rect.height), SRCALPHA)
        scale = DungeonDevView.SCALE_FACTOR

        for x in range(len(self.level)):
            for y in range(len(self.level[x])):
                color = DungeonDevView.ROOM_COLOR if self.level[x][y] == 0 else DungeonDevView.ROOM_WALL_COLOR
                surf.fill(color, rect=Rect((x * scale, y * scale), (scale, scale)))

        self.view.set_image(surf)

    def set_data(self, world_gen: DungeonGeneration):
        """
        Sets the data for the viewer
        :param world_gen: The world gen used
        """
        self.iterator = world_gen.generate_steps()
        self.reset()

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        if self.visible:
            self.timer += time_delta
            if self.timer > DungeonDevView.SLEEP_PER_ROOM:
                self.level = next(self.iterator, None)  # type: ignore
                if self.level:
                    self.update_view()  # type: ignore
                self.timer = 0

    def reset(self):
        """
        Resets the state of the dungeon view object
        """
        self.timer = DungeonDevView.SLEEP_PER_ROOM

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass