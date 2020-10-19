import logging
from typing import Iterable, List, Optional, Tuple, cast

import pygame
import pygame_gui
import pytweening
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui import UIManager
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UIPanel

from scripts.engine import utility, world
from scripts.engine.component import Aesthetic, Position
from scripts.engine.core.constants import TILE_SIZE, DirectionType, InputEvent, RenderLayer, UIElement
from scripts.engine.utility import clamp, convert_tile_string_to_xy
from scripts.engine.world_objects.tile import Tile


class Camera(UIPanel):
    """
    UI element to display the GameMap.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        # FIXME - grid doesnt stay aligned to player movement/position

        # flags
        self.ignore_fov = False
        self.is_dirty = True

        # determine how many tiles to show
        self.rows = rect.height // TILE_SIZE
        self.columns = rect.width // TILE_SIZE

        # store this now so we can refer to it later
        game_map = world.get_game_map()
        self.map_width = game_map.width
        self.map_height = game_map.height

        # to hold the last stored end values
        self._end_x = 0
        self._end_y = 0

        # duration of the animation - only used when animating the camera move
        self.move_duration = 0.0
        self.max_move_duration = 40  # in ms

        # start col, row are floats - the decimal representing the proportion of offset
        self.start_x = 0.0
        self.start_y = 0.0
        self.target_x = 0.0
        self.target_y = 0.0

        # number of tiles around the edge that trigger camera movement
        self.edge_size = 3

        self._tiles_in_view: List[Tile] = []

        # overlay info
        self.is_overlay_visible = False
        self.overlay_directions: List[DirectionType] = []  # list of tuples

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="camera")

        # create game map
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.game_map = UIImage(
            relative_rect=Rect((0, 0), rect.size),
            image_surface=blank_surf,
            manager=manager,
            container=self.get_container(),
            object_id="#game_map",
        )

        # create grid
        self.grid = UIContainer(
            relative_rect=Rect((0, 0), rect.size), manager=manager, container=self.get_container(), object_id="#grid"
        )

        # update everything
        self.update(0)

        # confirm init complete
        logging.debug(f"Camera initialised.")

    @property
    def end_x(self) -> int:
        if self.is_dirty:
            self._end_x = min(round(self.start_x + self.columns), self.map_width)

        return self._end_x

    @property
    def end_y(self) -> int:
        if self.is_dirty:
            self._end_y = min(round(self.start_y + self.rows), self.map_height)

        return self._end_y

    @property
    def current_tiles(self):
        """
        Return current tiles. Updates if is dirty.
        """
        if self.is_dirty:
            tiles = []
            # ensure all values are ints and clamped. + 2 to end to have tiles to roll onto (no black borders)
            start_x = int(clamp(self.start_x, 0, self.map_width - self.columns))
            start_y = int(clamp(self.start_y, 0, self.map_height - self.rows))
            end_x = int(clamp(self.end_x + 2, self.columns, self.map_width))
            end_y = int(clamp(self.end_y + 2, self.rows, self.map_height))

            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    tile = world.get_tile((x, y))
                    if tile.is_visible or self.ignore_fov:
                        tiles.append(tile)
            self._tiles_in_view = tiles
        return self._tiles_in_view

    ############### EVENTS ###########################

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        ui_object_id = event.ui_object_id

        # For tiles
        if "#tile" in ui_object_id:

            # get the row, col of the UI element
            x, y = self.get_tile_col_row(ui_object_id)

            # convert x,y to tile position
            x = x + int(self.start_x)
            y = y + int(self.start_y)

            # clicking a tile
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                event = pygame.event.Event(InputEvent.TILE_CLICK, tile_pos=(x, y))
                pygame.event.post(event)

            # hovering a tile
            elif event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                updated_tile_info = False
                from scripts.engine.ui.manager import ui
                from scripts.engine.core import queries

                for entity, (position,) in queries.position:
                    position: Position
                    if (x, y) in position:
                        ui.set_selected_tile_pos((x, y))
                        ui.set_element_visibility(UIElement.TILE_INFO, True)
                        updated_tile_info = True
                # entity not found at location so hide
                if not updated_tile_info:
                    if ui.element_is_visible(UIElement.TILE_INFO):
                        ui.set_element_visibility(UIElement.TILE_INFO, False)

    ############### UPDATE ###########################

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

        # move camera if not at target
        if not self.has_reached_target() or self.is_dirty:
            self._update_camera_position(time_delta)
            self._update_grid()

        # update entities in game map every frame
        self._draw_game_map()
        self._update_ui_element_pos()

        # all updates have been processed
        self.is_dirty = False

    def _update_camera_position(self, time_delta):
        """
        Update realtime camera timers, such as the camera scrolling to reveal new tiles.
        """
        # increment time
        self.move_duration += time_delta

        # if still moving
        if not self.has_reached_target():
            # time for animation exceeded
            time_exceeded = self.move_duration > self.max_move_duration

            # time for animation exceeded or animation very close to end
            if time_exceeded or utility.is_close((self.start_x, self.start_y), (self.target_x, self.target_y)):

                # set start_tile to target
                self.start_x = self.target_x
                self.start_y = self.target_y

            # keep moving
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, self.move_duration / self.max_move_duration))
                self.start_x = utility.lerp(self.start_x, self.target_x, lerp_amount)
                self.start_y = utility.lerp(self.start_y, self.target_y, lerp_amount)

        # not moving
        else:
            self.move_duration = 0
            self.start_x = int(self.target_x)
            self.start_y = int(self.target_y)

        self.is_dirty = True

    def _update_grid(self):
        """
        Update the tile grid to only have options in line with the tiles set OR the overlay
        """
        return
        # FIXME - update to work with new position. COnsider moving out of camera.
        # if self.is_overlay_visible:
        #
        #     # player column and row
        #     p_col = self.player_tile.x
        #     p_row = self.player_tile.y
        #
        #     # offset center column and center row
        #     cx = p_col - int(self.start_tile_col)
        #     cy = p_row - int(self.start_tile_row)
        #
        #     # set to contain all the tile positions in the overlay_directions
        #     tile_positions = {(cx + dir_x, cy + dir_y) for dir_x, dir_y in self.overlay_directions}
        #
        # else:
        #     tile_positions = []
        #
        #     # tile positions generator - contains 1 layer of padding to ensure smooth rollover
        #     for x in range(-1, self.columns + 1):
        #         for y in range(-1, self.rows + 1):
        #             # FIXME - this falls out of line with FOV being drawn by
        #             # check is in fov
        #             tile = world.get_tile((x, y))
        #             if tile.is_visible:
        #                 tile_positions.append((x, y))
        #
        # self._draw_grid(tile_positions)

    def _update_ui_element_pos(self):
        """
        Updates the ui element positions of the grid. Useful when moving the grid.
        """
        if len(self.grid.elements) == 0:
            return

        # get the decimal offsets of start tile
        dx = int(self.start_x) - self.start_x
        dy = int(self.start_y) - self.start_y

        ## Checking whether an update is necessary
        # get the first element
        element0 = self.grid.elements[0]

        # cast for typing
        element0 = cast(UIButton, element0)

        # get the (x,y) position of the element
        x, y, _, _ = element0.get_relative_rect()

        # get the updated position of the tile
        col, row = self.get_tile_col_row(element0.object_ids[-1])
        updated_pos = self._grid_to_draw_position((col + dx, row + dy))

        # update only if the current and updated position don't match
        should_update = updated_pos != (x, y)

        if should_update:
            for element in self.grid.elements:

                # cast for typing
                element = cast(UIButton, element)

                # get the updated position
                col, row = self.get_tile_col_row(element.object_ids[-1])
                updated_pos = self._grid_to_draw_position((col + dx, row + dy))

                # set updated position
                element.set_relative_position(updated_pos)

    ############### DRAW ###########################

    def _draw_game_map(self):
        """
        Update the game map to show the current tiles and entities
        """
        # create new surface for the game map
        map_width = self.game_map.rect.width
        map_height = self.game_map.rect.height
        map_surf = Surface((map_width, map_height), SRCALPHA)

        # draw tiles
        for tile in self.current_tiles:
            self._draw_surface(tile.sprite, map_surf, (tile.x, tile.y))

        # draw entities
        from scripts.engine.core import queries
        for entity, (pos, aesthetic) in queries.position_and_aesthetic:
            # if part of entity in camera view
            for offset in pos.offsets:
                src_area = Rect(offset[0] * TILE_SIZE, offset[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                position = (pos.x + offset[0], pos.y + offset[1])
                draw_position = (aesthetic.draw_x + offset[0], aesthetic.draw_y + offset[1])
                if self.is_in_camera_view(position):
                    tile = world.get_tile(position)
                    if tile.is_visible or self.ignore_fov:
                        self._draw_surface(aesthetic.current_sprite, map_surf, draw_position, src_area)

        # draw lighting
        light_box = world.get_game_map().light_box
        light_box.render(map_surf, )

        self.game_map.set_image(map_surf)

    def _draw_grid(self, tile_positions: Iterable):
        """
        Clears and redraws a grid of the tiles provided
        """
        manager = self.ui_manager
        grid = self.grid

        # clear the current grid
        grid.clear()

        # for all the tile positions provided
        for col, row in tile_positions:
            # find the screen position
            start_x, start_y = self._grid_to_draw_position((col, row))

            # create a rect
            tile_rect = Rect(start_x, start_y, TILE_SIZE, TILE_SIZE)

            # draw a button
            UIButton(
                relative_rect=tile_rect,
                manager=manager,
                text="",
                container=grid,
                parent_element=grid,
                object_id=f"#tile{col},{row}",
            )

    def _draw_surface(
        self, sprite: Surface, map_surface: Surface, col_row: Tuple[float, float], src_area: Optional[Rect] = None
    ):
        """
        Draw a surface on the surface map. The function handles coordinates transformation to the screen
        """
        pos = self.world_to_draw_position(col_row)
        map_surface.blit(sprite, pos, area=src_area)

    ############## SET #########################

    def set_target(self, position: Tuple[int, int], recentre: bool = False):
        """
        Set the target position.
        """
        x, y = position

        if self.is_in_camera_edge(position) or recentre:
            # centre the target
            half_width = int((self.rect.width / TILE_SIZE) / 2)
            half_height = int((self.rect.height / TILE_SIZE) / 2)

            if recentre:
                self.start_x = x
                self.start_y = y
                self.target_x = x
                self.target_y = y
                offset_x = -half_width
                offset_y = -half_height
            else:
                offset_x, offset_y = self.get_edge_offset(position)

            new_x = self.target_x + offset_x
            new_y = self.target_y + offset_y

            self.target_x = int(clamp(new_x, 0 + half_width, self.map_width - half_width))
            self.target_y = int(clamp(new_y, 0 + half_height, self.map_height - half_height))

        self.is_dirty = True

    def set_overlay_visibility(self, is_visible: bool):
        """
        Set whether the targeting overlay is visible or now.
        """
        self.is_overlay_visible = is_visible

    def set_overlay_directions(self, directions: List[DirectionType]):
        """
        Set the overlay with possible targeting directions.
        """
        self.overlay_directions = directions

    ################## GET ######################

    @staticmethod
    def get_tile_col_row(id_string: str):
        """
        Get the (col, row) from the object_id string
        """
        prefix = "#tile"
        index = id_string.index(prefix)
        tile_string = id_string[index + len(prefix) :]
        return convert_tile_string_to_xy(tile_string)

    ############# UTILITY #########################

    def world_to_draw_position(self, pos: Tuple[float, float]) -> Tuple[int, int]:
        """
        Convert from the tile position to the screen position
        """
        start_x = int((pos[0] - self.start_x) * TILE_SIZE)
        start_y = int((pos[1] - self.start_y) * TILE_SIZE)

        return start_x, start_y

    def draw_to_world_position(self, pos: Tuple[float, float]) -> Tuple[int, int]:
        """
        Convert from a draw position to a tile position, rounding down.
        """
        x = int(clamp(pos[0] // TILE_SIZE, 0, self.map_width))
        y = int(clamp(pos[1] // TILE_SIZE, 0, self.map_height))

        return x, y

    def _grid_to_draw_position(self, pos: Tuple[float, float]) -> Tuple[int, int]:
        """
        Converts grid positions to screen positions
        """
        x, y = pos
        draw_x = int(x * TILE_SIZE)
        draw_y = int(y * TILE_SIZE)
        return draw_x, draw_y

    ############# QUERIES #########################

    def has_reached_target(self) -> bool:
        """
        returns True if target equals start tile
        """
        return self.start_x == self.target_x and self.start_y == self.target_y

    def is_in_camera_view(self, pos: Tuple[float, float]) -> bool:
        """
        is the position inside the current camera view
        """
        x, y = pos
        in_view = self.start_x <= x < self.end_x and self.start_y <= y < self.end_y

        return in_view

    def is_in_camera_edge(self, target_pos: Tuple[int, int]) -> bool:
        """
        Determine if target position is within the edge of the camera. N.B. they are tile positions.
        """
        in_edge = False

        if self.get_edge_offset(target_pos) != 0:
            in_edge = True

        return in_edge

    def get_edge_offset(self, target_pos: Tuple[int, int]) -> Tuple[int, int]:
        """
        Determine how far the player is into the edge of the camera
        """
        x, y = target_pos
        edge_size = self.edge_size
        dir_x = 0
        dir_y = 0
        start_x = int(self.start_x)
        start_y = int(self.start_y)
        end_x = self.end_x
        end_y = self.end_y

        # check left and right edges
        if x < start_x + edge_size:
            dir_x = x - (start_x + edge_size)

        elif x > end_x - edge_size:
            dir_x = x - (end_x - edge_size)

        # check top and bottom edges
        if y < start_y + edge_size:
            dir_y = y - (start_y + edge_size)

        elif y > end_y - edge_size:
            dir_y = y - (end_y - edge_size)

        return dir_x, dir_y
