import logging
from typing import Iterable, List, Optional, Tuple
import os
import math

import pygame
import pygame_gui
import pytweening
from pygame.rect import Rect
from pygame.surface import Surface

from scripts.engine.core import query, utility, world, state
from scripts.engine.core.utility import clamp, convert_tile_string_to_xy
from scripts.engine.core.component import Aesthetic, Position
from scripts.engine.internal import library
from scripts.engine.internal.constant import (
    TILE_SIZE,
    Height,
    InputIntent,
    InputEventType,
    EventType,
    UIElement,
    GameState,
    TargetingMethod
)
from scripts.engine.core.ui import ui
from scripts.nqp.ui_elements.tile_info import TileInfo
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

        self.hovered_tile = None
        self.valid_line_of_sight = False
        self.possible_los_tiles = None

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
        self._process_events()

    def _process_events(self):
        """
        For processing entirely local events.
        Updates the current hovered tile based on mouse position and updates the TILE_INFO GUI element.
        """

        mx, my = pygame.mouse.get_pos()
        mx /= self._desired_width / self._base_width
        my /= self._desired_height / self._base_height

        hover_pos = (int(self.start_x + mx / TILE_SIZE), int(self.start_y + my / TILE_SIZE))
        try:
            new_hover = world.get_tile(hover_pos)
            if (new_hover is self.hovered_tile) == False:
                if new_hover.is_visible:
                    if not ui.has_element(UIElement.TILE_INFO):
                        tile_info: TileInfo = TileInfo(command.get_element_rect(UIElement.TILE_INFO), ui.get_gui_manager())
                        ui.register_element(UIElement.TILE_INFO, tile_info)

                    tile_info = ui.get_element(UIElement.TILE_INFO)
                    tile_info.set_selected_tile_pos(hover_pos)
                    tile_info.cleanse()
                    ui.set_element_visibility(UIElement.TILE_INFO, True)
                else:
                    ui.set_element_visibility(UIElement.TILE_INFO, False)
            self.hovered_tile = new_hover
        except IndexError:
            pass

    def process_click(self):
        """
        Process a click. This is currently just used during targeting to trigger the cast event since the camera tracks what tiles are targetable.
        TODO: Move targeting logic out of the camera.
        """

        if self.hovered_tile and self.hovered_tile.is_visible:
            if state.get_current() == GameState.TARGETING:
                active_skill_name = state.get_active_skill()
                player = world.get_player()
                skill = world.get_known_skill(player, active_skill_name)

                # set the skill target for the skill cast if the hovered tile is a valid target during line of sight targeting
                if (skill.targeting_method == TargetingMethod.LINE_OF_SIGHT) and self.valid_line_of_sight:
                    state.set_active_skill_target((self.hovered_tile.x, self.hovered_tile.y))

                # cancel event triggering if the hovered target is invalid in the target mode
                if (skill.targeting_method == TargetingMethod.TILE):
                    position = world.get_entitys_component(player, Position)
                    dif = (position.x - self.hovered_tile.x, position.y - self.hovered_tile.y)
                    if (dif not in skill.target_directions) or (not self.hovered_tile.is_visible) or (not world.tile_has_tags(player, self.hovered_tile, skill.target_tags)):
                        return

            event = pygame.event.Event(EventType.INPUT, subtype=InputEventType.TILE_CLICK, tile_pos=(self.hovered_tile.x, self.hovered_tile.y))
            pygame.event.post(event)

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
        # main rendering
        internal_surf = Surface((self._base_width, self._base_height))
        self._draw_floors(internal_surf)
        self._draw_entities(internal_surf)
        self._draw_walls(internal_surf)
        if not self.show_all:
            self._draw_lighting(internal_surf)

        # targeting mode related indicator rendering
        # this needs to be moved out of the camera (a ton of it is half update and half render)
        if state.get_current() == GameState.TARGETING:
            player = world.get_player()
            position = world.get_entitys_component(player, Position)
            active_skill_name = state.get_active_skill()
            skill = world.get_known_skill(player, active_skill_name)

            # if this is a directional attack
            if skill.targeting_method == TargetingMethod.TILE:
                for direction in skill.target_directions:
                    target_x = position.x + direction[0]
                    target_y = position.y + direction[1]
                    tile = world.get_tile((target_x, target_y))
                    if tile.is_visible and world.tile_has_tags(player, tile, skill.target_tags):
                        option_r = pygame.Rect((target_x - self.start_x) * TILE_SIZE, (target_y - self.start_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        pygame.draw.rect(internal_surf, (60, 70, 120), option_r, 1)

            # if this is a line of sight attack
            elif skill.targeting_method == TargetingMethod.LINE_OF_SIGHT:
                # regenerate possible targets if targeting mode was just entered
                if self.possible_los_tiles == None:
                    self.possible_los_tiles = []
                    state.set_active_skill_target(None)
                    for y in range(skill.range * 2 + 1):
                        for x in range(skill.range * 2 + 1):
                            test_pos = (position.x - skill.range + x, position.y - skill.range + y)
                            valid, _ = self.check_valid_line_of_sight(test_pos)
                            if valid:
                                self.possible_los_tiles.append(test_pos)

                # check if current hovered tile is a valid target
                self.valid_line_of_sight = False
                self.valid_line_of_sight, tile_path = self.check_valid_line_of_sight((self.hovered_tile.x, self.hovered_tile.y))

                # render indicators
                for tile_pos in self.possible_los_tiles:
                    highlight_r = pygame.Rect((tile_pos[0] - self.start_x) * TILE_SIZE, (tile_pos[1] - self.start_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(internal_surf, (60, 70, 120), highlight_r, 1)
                if self.valid_line_of_sight:
                    for tile_pos in tile_path:
                        highlight_r = pygame.Rect((tile_pos[0] - self.start_x) * TILE_SIZE, (tile_pos[1] - self.start_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        pygame.draw.rect(internal_surf, (50, 150, 200), highlight_r, 1)

        # empty targeting data if not in targeting mode
        else:
            self.possible_los_tiles = None

        if self.hovered_tile and self.hovered_tile.is_visible:
            hover_r = pygame.Rect((self.hovered_tile.x - self.start_x) * TILE_SIZE, (self.hovered_tile.y - self.start_y) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(internal_surf, (200, 200, 0), hover_r, 1)

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

    def check_valid_line_of_sight(self, pos: Tuple[int, int]) -> Tuple[bool, List]:
        '''
        Checks if a tile is in the line of sight from the player and returns the visible path to the target tile.
        '''
        # get base info and init
        player = world.get_player()
        position = world.get_entitys_component(player, Position)
        active_skill_name = state.get_active_skill()
        skill = world.get_known_skill(player, active_skill_name)
        valid_line_of_sight = False
        target_tile = world.get_tile(pos)
        tile_path = []

        # check if the endpoint is even valid
        if target_tile.is_visible and world.tile_has_tags(player, target_tile, skill.target_tags):

            # init some values for search
            current_pos = [position.x, position.y]
            tile_path = [current_pos.copy()]
            target_pos = list(pos)

            # get list of possible search directions
            directions_for_steps = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
            # this set is for distance calculations
            # the 0.81 reduces the weight of diagonal movement so it isn't chosen too often
            directions_for_math = [(-1, 0), (1, 0), (0, 1), (0, -1), (-0.81, -0.81), (0.81, 0.81), (0.81, -0.81), (-0.81, 0.81)]

            valid = True

            # iteratively search for the bordering tile that's closest to the target
            while current_pos != target_pos:
                closest = [current_pos.copy(), math.sqrt((target_pos[0] - current_pos[0]) ** 2 + (target_pos[1] - current_pos[1]) ** 2)]
                for i, direction in enumerate(directions_for_steps):
                    check_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
                    math_check_pos = [current_pos[0] + directions_for_math[i][0], current_pos[1] + directions_for_math[i][1]]
                    dis = math.sqrt((math_check_pos[0] - target_pos[0]) ** 2 + (math_check_pos[1] - target_pos[1]) ** 2)
                    if dis < closest[1]:
                        closest = [check_pos.copy(), dis]
                tile = world.get_tile(closest[0])

                # check if tile step meets targeting criteria
                if (not tile.is_visible) or (not world.tile_has_tags(player, tile, skill.target_tags)):
                    valid = False

                current_pos = closest[0].copy()
                tile_path.append(current_pos.copy())

            # determine if the final path was valid based on skill range and previous calculations
            if (len(tile_path) - 1 <= skill.range) and valid:
                valid_line_of_sight = True

        return (valid_line_of_sight, tile_path)

    def is_in_camera_view(self, pos: Tuple[float, float]) -> bool:
        """
        is the position inside the current camera view
        """
        x, y = pos
        in_view = (self.start_x <= x < self.end_x) and (self.start_y <= y < self.end_y)

        return in_view

    def get_render_pos(self, pos: Tuple[float, float]) -> Tuple[float, float]:
        """
        Converts world position to render position (in pixels) by applying the camera's position.
        """
        return (pos[0] - self.start_x * TILE_SIZE, pos[1] - self.start_y * TILE_SIZE)

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
