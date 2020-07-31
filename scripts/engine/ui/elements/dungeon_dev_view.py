
import pygame
import pygame_gui
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui import UIManager
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UIWindow
from scripts.engine.core.constants import RenderLayer
from typing import List, Tuple


class DungeonDevView(UIWindow):
    """
    UI component that renders the construction of a dungeon as a separate window, step by step.
    """

    SLEEP_PER_ROOM = 1.0
    SCALE_FACTOR = 20.0
    ROOM_COLOR = (216, 216, 216, 255)
    ROOM_WALL_COLOR = (64, 64, 64, 255)
    TUNNEL_COLOR = ROOM_COLOR

    def __init__(self, rect: Rect, manager: pygame_gui.ui_manager.UIManager):

        super().__init__(rect, manager, element_id="dungeon_dev_view")

        rect = pygame.Rect((0, 0), (self.rect.width, self.rect.height))
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.room_view = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                               container=self.get_container(), object_id="#roomview")
        self.tunnel_view = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                                    container=self.get_container(), object_id="#tunnelview")

        self.timer = 0
        self.current_room = 0
        self.current_tunnel = 0
        self.room_surfaces = []
        self.tunnel_surfaces = []
        self.rooms = None
        self.tunnels = None

    def update_view(self):
        """
        Updates the view of the dungeon
        """
        self._update_surface(self.room_view, self.room_surfaces)
        self._update_surface(self.tunnel_view, self.tunnel_surfaces)

    def _update_surface(self, ui: UIImage, surfaces: List[Tuple[Tuple[int, int], pygame.Surface]]):
        """
        Updates a single surface
        :param ui: UIImage to update
        :param surfaces: List of surfaces to blit
        """
        surf = Surface((ui.rect.width, ui.rect.height), SRCALPHA)

        for position, surface in surfaces:
            surf.blit(surface, position)

        ui.set_image(surf)

    def set_data(self, rooms, tunnels):
        """
        Sets the data for the dev view to use
        :param rooms: List of rooms in order
        :param tunnels: List of tunnels in order
        """
        self.rooms = rooms
        self.tunnels = tunnels
        self.reset()

    @staticmethod
    def _create_room_surf(room: Tuple[Tuple[int, int], List[List[int]]]) -> Tuple[Tuple[float, float], Surface]:
        """
        Create a surface for a room
        :param room: Room to model after
        :return: A Surf object and its position
        """
        position, cells = room
        width = len(cells)
        height = len(cells[0])
        scale = DungeonDevView.SCALE_FACTOR

        room_surf = Surface((width * scale, height * scale), SRCALPHA)
        for x in range(width):
            for y in range(height):
                if cells[x][y] == 0:
                    room_surf.fill(DungeonDevView.ROOM_COLOR, rect=Rect((x * scale, y * scale), (scale, scale)))
                #elif (x > 0 and cells[x-1][y] == 0) or (x < width-1 and cells[x+1][y] == 0) or (y > 0 and cells[x][y-1] == 0) or (y < height-1 and cells[x][y+1] == 0):
                #    room_surf.fill(DungeonDevView.ROOM_WALL_COLOR, rect=Rect((x * scale, y * scale), (scale, scale)))

        p_x, p_y = position
        return (p_x * scale, p_y * scale), room_surf

    @staticmethod
    def _create_tunnel_surf(tunnel: Tuple[Tuple[int, int], Tuple[int, int], int]) -> Tuple[Tuple[float, float], Surface]:
        """
        Create a surface for a tunnel
        :return: A Surf object and its position
        """
        origin, direction, length = tunnel
        x, y = origin
        d_x, d_y = direction
        scale = DungeonDevView.SCALE_FACTOR

        width, height = (int(max(1, d_x * length) * scale), int(max(1, d_y * length) * scale))
        tunnel_surf = Surface((width, height), SRCALPHA)
        tunnel_surf.fill(DungeonDevView.TUNNEL_COLOR)

        return (x * scale, y * scale), tunnel_surf

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        if self.visible:
            self.timer += time_delta
            if self.timer > DungeonDevView.SLEEP_PER_ROOM:

                if self.current_room < len(self.rooms):
                    self.room_surfaces.append(self._create_room_surf(self.rooms[self.current_room]))
                    self.current_room += 1

                if self.current_tunnel < len(self.tunnels):
                    self.tunnel_surfaces.append(self._create_tunnel_surf(self.tunnels[self.current_tunnel]))
                    self.current_tunnel += 1

                self.update_view()
                self.timer = 0

    def reset(self):
        """
        Resets the state of the dungeon view object
        """
        self.current_room = 0
        self.current_tunnel = 0
        self.timer = DungeonDevView.SLEEP_PER_ROOM
        self.room_surfaces = []
        self.tunnel_surfaces = []

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass