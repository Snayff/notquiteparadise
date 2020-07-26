import logging
from typing import Iterable, List, Optional, Tuple, cast

import pygame
import pygame_gui
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui import UIManager
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UIPanel

from scripts.engine import world
from scripts.engine.component import Aesthetic, IsActor, Position
from scripts.engine.core.constants import (
    TILE_SIZE, DirectionType, EventType, RenderLayer, UIElement)
from scripts.engine.utility import (clamp, convert_tile_string,
                                    is_coordinate_in_bounds)
from scripts.engine.world_objects.tile import Tile


class Camera(UIPanel):
    """
    Hold the visual info for the game Map
    """

    def __init__(self, rect: Rect, manager: UIManager):

        # general info
        self.rows = rect.height // TILE_SIZE
        self.columns = rect.width // TILE_SIZE

        # duration of the animation - only used when animating the camera move
        self.current_sprite_duration = 0.0

        # start col, row are floats - the decimal representing the proportion of offset
        self.start_tile_col = 0.0
        self.start_tile_row = 0.0

        # target same as the start
        self.target_tile_col = 0.0
        self.target_tile_row = 0.0

        # initialize these variables from self.update_tile_properties()
        self.x_bounds: Optional[Tuple[int, int]] = None
        self.y_bounds: Optional[Tuple[int, int]] = None

        self.edge_size = 5  # number of tiles to control camera movement

        # game map info
        pos = world.get_entitys_component(world.get_player(), Position)
        if pos:
            tile = world.get_tile((pos.x, pos.y))
        else:
            tile = world.get_tile((0, 0))  # player should always have Position but just in case
        self.player_tile = tile  # the tile in which the player resides
        self.last_updated_player_tile = tile  # the tile the player was in when camera last updated movement
        self.tiles: List[Tile] = []

        # overlay info
        self.is_overlay_visible = False
        self.overlay_directions: List[DirectionType] = []  # list of tuples

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="camera")

        # create game map
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.gamemap = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                                container=self.get_container(), object_id="#gamemap")

        # create grid
        self.grid = UIContainer(relative_rect=Rect((0, 0), rect.size), manager=manager, container=self.get_container(),
                                object_id="#grid")

        # update everything
        self.update_tile_properties()
        self.update_gamemap()
        self.update_grid()


        # confirm init complete
        logging.debug(f"Camera initialised.")

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        ui_object_id = event.ui_object_id

        # For tiles
        if '#tile' in ui_object_id:

            # get the row, col of the UI element
            x, y = self.get_tile_col_row(ui_object_id)

            # convert x,y to tile position
            x = x + int(self.start_tile_col)
            y = y + int(self.start_tile_row)

            # clicking a tile
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                event = pygame.event.Event(EventType.TILE_CLICK, tile_pos=(x, y))
                pygame.event.post(event)

            # hovering a tile
            elif event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                updated_tile_info = False
                from scripts.engine.ui.manager import ui
                for entity, (position, ) in world.get_components([Position]):
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
        
        if self.last_updated_player_tile != self.player_tile:
            start_pos = (self.last_updated_player_tile.x, self.last_updated_player_tile.y)
            target_pos = (self.player_tile.x, self.player_tile.y)
            if self.should_camera_move(start_pos, target_pos):
                move_x = target_pos[0] - start_pos[0]
                move_y = target_pos[1] - start_pos[1]
                self.move_camera(move_x, move_y)
                self.update_tile_properties()  # update if camera moved as it used start row and col

            self.update_grid()

            # set last updated to current
            self.last_updated_player_tile = self.player_tile

        # update entities in game map every frame
        self.update_gamemap()
        self._update_ui_element_pos()

    def update_tile_properties(self):
        """
        Refresh tile dimensions and the map bounds.
        """
        self.x_bounds, self.y_bounds = self.get_tile_bounds()

    def update_gamemap(self):
        """
        Update the game map to show the current tiles and entities
        """
        # create new surface for the game map
        map_width = self.gamemap.rect.width
        map_height = self.gamemap.rect.height
        map_surf = Surface((map_width, map_height), SRCALPHA)

        # draw tiles
        for tile in self._get_current_tiles():
            # if in player fov
            if tile.is_visible:
                self.draw_surface(tile.sprite, map_surf, (tile.x, tile.y))

        # draw entities
        for entity, (pos, aesthetic) in world.get_components([Position, Aesthetic]):
            # if in camera view
            for offset in pos.offsets:
                src_area = Rect(offset[0] * TILE_SIZE, offset[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                position = (pos.x + offset[0], pos.y + offset[1])
                draw_position = (aesthetic.draw_x + offset[0], aesthetic.draw_y + offset[1])
                if self.is_in_camera_view(position):
                    tile = world.get_tile(position)
                    if tile.is_visible:
                        self.draw_surface(aesthetic.current_sprite, map_surf, draw_position, src_area)

        self.gamemap.set_image(map_surf)

    def update_grid(self):
        """
        Update the tile grid to only have options in line with the tiles set OR the overlay
        """
        if self.is_overlay_visible:

            # player column and row
            p_col = self.player_tile.x
            p_row = self.player_tile.y

            # offset center column and center row
            cx = p_col - int(self.start_tile_col)
            cy = p_row - int(self.start_tile_row)

            # set to contain all the tile positions in the overlay_directions
            tile_positions = {(cx + dir_x, cy + dir_y) for dir_x, dir_y in self.overlay_directions}

        else:
            tile_positions = []

            # tile positions generator - contains 1 layer of padding to ensure smooth rollover
            for x in range(-1, self.columns + 1):
                for y in range(-1, self.rows + 1):
                    # FIXME - this falls out of line with FOV being drawn by
                    # check is in fov
                    tile = world.get_tile((x, y))
                    if tile.is_visible:
                        tile_positions.append((x, y))

        self._draw_grid(tile_positions)

    def _update_ui_element_pos(self):
        """
        Updates the ui element positions of the grid. Useful when moving the grid.
        """
        if len(self.grid.elements) == 0:
            return

        # get the decimal offsets of start tile
        dx = int(self.start_tile_col) - self.start_tile_col
        dy = int(self.start_tile_row) - self.start_tile_row

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
            draw_x, draw_y = self._grid_to_draw_position((col, row))

            # create a rect
            tile_rect = Rect(draw_x, draw_y, TILE_SIZE, TILE_SIZE)

            # draw a button
            UIButton(relative_rect=tile_rect, manager=manager, text="", container=grid, parent_element=grid,
                     object_id=f"#tile{col},{row}")

    def draw_surface(self, sprite: Surface, map_surface: Surface, col_row: Tuple[float, float], src_area: Optional[Rect] = None):
        """
        Draw a surface on the surface map. The function handles coordinates transformation to the screen
        """
        pos = self.world_to_draw_position(col_row)
        map_surface.blit(sprite, pos, area=src_area)

    ############## SET #########################

    def set_start_col_row(self, offset: Tuple[float, float]):
        """
        Set the Start column and row
        """
        self.start_tile_col, self.start_tile_row = offset

    def set_start_to_target(self):
        """
        Set the current start tile to the target tile
        """
        self.start_tile_col = self.target_tile_col
        self.start_tile_row = self.target_tile_row

    def set_player_tile(self, tile):
        """
        Set the player tile
        """
        self.last_updated_player_tile = self.player_tile
        self.player_tile = tile

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

    def get_tile_bounds(self) -> List[Tuple[int, int]]:
        """
        Get the (col, row) bounds
        """
        return [(int(self.start_tile_col), round(self.start_tile_col + self.columns)),
                (int(self.start_tile_row), round(self.start_tile_row + self.rows))]

    @staticmethod
    def get_tile_col_row(id_string: str):
        """
        Get the (col, row) from the object_id string
        """
        prefix = '#tile'
        index = id_string.index(prefix)
        tile_string = id_string[index + len(prefix):]
        return convert_tile_string(tile_string)

    def _get_current_tiles(self):
        """
        Current tiles as a generator
        """
        tile_generator = (world.get_tile((x, y)) for x in range(*self.x_bounds) for y in range(*self.y_bounds))
        return tile_generator

    ############# ACTIONS #########################

    def move_camera(self, num_cols: int, num_rows: int):
        """
        Adjust the camera position by the number of columns and rows
        """
        # calculate new start col, rows
        new_start_col = round(clamp(self.target_tile_col + num_cols, 0.0, self.columns))
        new_start_row = round(clamp(self.target_tile_row + num_rows, 0.0, self.rows))

        # set them as target
        self.target_tile_col = new_start_col
        self.target_tile_row = new_start_row

        # reset animation time
        self.current_sprite_duration = 0

    def world_to_draw_position(self, pos: Tuple[float, float]):
        """
        Convert from the world_objects position to the screen position
        """
        draw_x = int((pos[0] - self.start_tile_col) * TILE_SIZE)
        draw_y = int((pos[1] - self.start_tile_row) * TILE_SIZE)

        return draw_x, draw_y

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
        return self.target_tile_col == self.start_tile_col and self.target_tile_row == self.start_tile_row

    def is_in_camera_view(self, pos: Tuple[float, float]) -> bool:
        """
        is the position inside the current camera view
        """
        x, y = pos
        if self.x_bounds and self.y_bounds:
            x_start, x_max = self.x_bounds
            y_start, y_max = self.y_bounds

            in_view = x_start <= x < x_max and y_start <= y < y_max
        else:
            in_view = False

        return in_view
    
    def should_camera_move(self, start_pos: Tuple, target_pos: Tuple) -> bool:
        """
        Determine if camera should move based on start and target pos and intersecting the edge of the screen.
        pos is x, y.
        """
        # FIXME - camera moves when player walks into a wall and does not move
        start_x, start_y = start_pos
        target_x, target_y = target_pos


        edge_start_x = self.start_tile_col
        edge_end_x = self.start_tile_col + self.columns
        edge_start_y = self.start_tile_row
        edge_end_y = self.start_tile_row + self.rows

        start_pos_in_edge = self.is_target_pos_in_camera_edge(start_pos)
        target_pos_in_edge = self.is_target_pos_in_camera_edge(target_pos)

        # are we currently in the edge (e.g. edge of world)
        if start_pos_in_edge:

            # will we still be in the edge after we move?
            if target_pos_in_edge:
                dir_x = target_x - start_x
                dir_y = target_y - start_y

                # are we moving to a worse position?
                if edge_start_x <= start_x < edge_start_x + self.edge_size + 1:
                    # player is on the left side, are we moving left?
                    if dir_x < 0:
                        return True
                if edge_end_x > start_x >= edge_end_x - self.edge_size - 2:
                    # player is on the right side, are we moving right?
                    if 0 < dir_x:
                        return True
                if edge_start_y <= start_y < edge_start_y + self.edge_size + 1:
                    # player is on the up side, are we moving up?
                    if dir_y < 0:
                        return True
                if edge_end_y > start_y >= edge_end_y - self.edge_size - 2:
                    # player is on the down side, are we moving down?
                    if 0 < dir_y:
                        return True

        elif target_pos_in_edge:
            # we are moving into the edge
            return True

        return False

    def is_target_pos_in_camera_edge(self, target_pos: Tuple) -> bool:
        """
        Determine if target position is within the edge of the camera
        """
        player_x, player_y = target_pos
        x_bounds, y_bounds = self.get_tile_bounds()

        x_in_camera_edge = is_coordinate_in_bounds(coordinate=player_x, bounds=x_bounds, edge=self.edge_size)
        y_in_camera_edge = is_coordinate_in_bounds(coordinate=player_y, bounds=y_bounds, edge=self.edge_size)

        return not x_in_camera_edge or not y_in_camera_edge
