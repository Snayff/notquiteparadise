import logging
from typing import Iterable, List, Optional, Tuple
import os

import pygame
import pygame_gui
import pytweening
from pygame.rect import Rect
from pygame.surface import Surface

from scripts.engine.core import query, utility, world
from scripts.engine.core.utility import clamp, convert_tile_string_to_xy
from scripts.engine.internal import library
from scripts.engine.internal.component import Aesthetic, Position
from scripts.engine.internal.constant import TILE_SIZE, Height
from scripts.nqp import command


__all__ = ["camera"]


class Camera:
    """
    Management class for rendering the world onto the main display surface.
    """

    def __init__(self):

        base_window_data = library.VIDEO_CONFIG.base_window
        desired_window_data = library.VIDEO_CONFIG.desired_window

        self._base_width = base_window_data.width
        self._base_height = base_window_data.height

        self._desired_width = desired_window_data.width
        self._desired_height = desired_window_data.height

        self.show_all = False

        self.move_edge_size = 4

        rect = pygame.Rect(0, 0, self._base_width, self._base_height)

        # store this now so we can refer to it later
        #game_map = world.get_game_map()
        #self.map_width = game_map.width
        #self.map_height = game_map.height

        # determine how many tiles to show; max rows and cols in game map or max we can show based on size
        #self.rows = min(rect.width // TILE_SIZE, game_map.height - 1)
        #self.columns = min(rect.height // TILE_SIZE, game_map.width - 1)

        # duration of the animation - only used when animating the camera move
        self.move_duration = 0.0
        self.max_move_duration = 40  # in ms

        # confirm init complete
        logging.debug(f"Camera initialised.")

        self.start_x = 0.0
        self.start_y = 0.0
        self.target_x = 0.0
        self.target_y = 0.0

        self.move_duration = 0
        self.max_move_duration = 40

    ############### PROPERTIES ##################

    @property
    def on_target(self) -> bool:
        return (self.start_x == self.target_x) and (self.start_y == self.target_y)

    @property
    def end_x(self) -> int:
        return self.start_x + self._base_width / TILE_SIZE + 1

    @property
    def end_y(self) -> int:
        return self.start_y + self._base_height / TILE_SIZE + 1

    ############# UPDATE/RENDER #################

    def update(self, time_delta: float):
        """
        Apply logical updates to camera.
        """

        self._update_camera_position(time_delta)
        self.visible_tiles = self._get_visible_tiles()

    def _update_camera_position(self, time_delta: float):
        """
        Calculate and apply camera updates based on time based and the target position.
        """

        game_map = world.get_game_map()
        self.move_duration += time_delta

        if not self.on_target:
            time_exceeded = self.move_duration > self.max_move_duration
            if time_exceeded or utility.is_close((self.start_x, self.start_y), (self.target_x, self.target_y)):
                self.start_x = self.target_x
                self.start_y = self.target_y
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, self.move_duration / self.max_move_duration))
                self.start_x = utility.lerp(self.start_x, self.target_x, lerp_amount)
                self.start_y = utility.lerp(self.start_y, self.target_y, lerp_amount)
        else:
            self.move_duration = 0
            self.start_x = int(self.target_x)
            self.start_y = int(self.target_y)
        self.start_x = clamp(self.start_x, 0, game_map.width - self._base_height / TILE_SIZE)
        self.start_y = clamp(self.start_y, 0, game_map.height - self._base_height / TILE_SIZE)

    def render(self, target_surf: pygame.Surface):
        internal_surf = Surface((self._base_width, self._base_height))
        self._draw_floors(internal_surf)
        self._draw_entities(internal_surf)
        if not self.show_all:
            self._draw_lighting(internal_surf)
        self._draw_walls(internal_surf)
        target_surf.blit(pygame.transform.scale(internal_surf, target_surf.get_size()), (0, 0))

    def _get_visible_tiles(self):
        """
        Return visible tiles based on camera position and config.
        """

        tiles = []

        for x in range(int(self.start_x), int(self.end_x)):
            for y in range(int(self.start_y), int(self.end_y)):
                tile = world.get_tile((x, y))
                if tile.is_visible or self.show_all:
                    tiles.append(tile)

        return tiles

    ################ UTILITY ####################

    def is_in_camera_view(self, pos: Tuple[float, float]) -> bool:
        # TODO: implement this
        return 1

    def get_render_pos(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        """
        Converts world position to render position (in pixels) by applying the camera's position.
        """
        return [pos[0] - self.start_x * TILE_SIZE, pos[1] - self.start_y * TILE_SIZE]

    ############### RENDER CORE #################

    def _draw_floors(self, map_surf: pygame.Surface):
        for tile in self.visible_tiles:
            if tile.height == Height.MIN:
                map_surf.blit(tile.sprite, self.get_render_pos((tile.x * TILE_SIZE, tile.y * TILE_SIZE)))

    def _draw_entities(self, map_surf: pygame.Surface):
        from scripts.engine.core import query

        for entity, (pos, aesthetic) in query.position_and_aesthetic:
            assert isinstance(pos, Position)
            assert isinstance(aesthetic, Aesthetic)

            # if part of entity in camera view
            for offset in pos.offsets:
                src_area = Rect(offset[0] * TILE_SIZE, offset[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                position = (pos.x + offset[0], pos.y + offset[1])
                draw_position = (aesthetic.draw_x + offset[0], aesthetic.draw_y + offset[1])
                if self.is_in_camera_view(position):
                    tile = world.get_tile(position)
                    if tile.is_visible or self.show_all:
                        #self._draw_surface(aesthetic.current_sprite, map_surf, draw_position, src_area)
                        map_surf.blit(aesthetic.current_sprite, self.get_render_pos((draw_position[0] * TILE_SIZE, draw_position[1] * TILE_SIZE)), src_area)

    def _draw_lighting(self, map_surf: pygame.Surface):
        light_box = world.get_game_map().light_box
        light_box.render(map_surf, [int(self.start_x * TILE_SIZE), int(self.start_y * TILE_SIZE)])

    def _draw_walls(self, map_surf: pygame.Surface):
        for tile in self.visible_tiles:
            if tile.height == Height.MAX:
                map_surf.blit(tile.sprite, self.get_render_pos((tile.x * TILE_SIZE, tile.y * TILE_SIZE)))

    ################## SET ######################

    def set_target(self, pos: Tuple[float, float], recentre: bool = False):
        """
        Set a new target position for the camera. If recentre is False (the default),
        the camera will only move if the target position goes past the loose area defined
        by Camera.move_edge_size. It will also only move until the target position is within
        the loose area in the center. If recentre is True, the camera will center perfectly
        over the target position.
        """
        # TODO: find out why the -2s and the +1s are necessary
        if not recentre:
            if pos[0] < self.start_x + self.move_edge_size:
                self.target_x = pos[0] - self.move_edge_size
            if pos[0] > self.end_x - self.move_edge_size - 2:
                self.target_x = pos[0] + self.move_edge_size - self._base_width / TILE_SIZE + 1
            if pos[1] < self.start_y + self.move_edge_size:
                self.target_y = pos[1] - self.move_edge_size
            # this case is a bit scuffed because it's the only side of the view that doesn't perfectly align with the edge of a tile
            if pos[1] > self.end_y - self.move_edge_size - 2:
                self.target_y = int(pos[1] + self.move_edge_size - self._base_height / TILE_SIZE + 1)
        else:
            self.target_x = pos[0] - int((self._base_width / TILE_SIZE) / 2)
            self.target_y = pos[1] - int((self._base_height / TILE_SIZE) / 2)

if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    camera = Camera()
else:
    camera = ""  # type: ignore
