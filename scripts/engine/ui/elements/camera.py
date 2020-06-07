import logging
from typing import List, Tuple, cast, Iterable

import pygame_gui
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame_gui import UIManager
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UIPanel, UIWindow
from scripts.engine import world
from scripts.engine.core.constants import LAYER_CAMERA, DirectionType, TILE_SIZE
from scripts.engine.core.event_core import publisher
from scripts.engine.utility import clamp, convert_tile_string
from scripts.engine.event import ClickTile
from scripts.engine.component import Position, Aesthetic
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
        self.x_bounds = None
        self.y_bounds = None

        self.edge_size = 5  # number of tiles to control camera movement

        # game map info
        pos = world.get_entitys_component(world.get_player(), Position)
        tile = world.get_tile((pos.x, pos.y))
        self.player_tile = tile  # the tile in which the player resides
        self.tiles: List[Tile] = []

        # overlay info
        self.is_overlay_visible = False
        self.overlay_directions: List[DirectionType] = []  # list of tuples

        # grid info
        self.selected_tile = None  # the tile in the grid currently being selected

        # complete base class init
        super().__init__(rect, LAYER_CAMERA, manager, element_id="camera")

        # create game map
        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.game_map = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                                container=self.get_container(), object_id="#game_map")

        # create grid
        self.grid = UIContainer(relative_rect=Rect((0, 0), rect.size), manager=manager, container=self.get_container(),
                                object_id="#grid")

        self.update_tile_properties()

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
            tile_pos = (x, y)

            # clicking a tile
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # get the required tile and publish click event
                tile = world.get_tile(tile_pos)
                publisher.publish(ClickTile(tile))

            # hovering a tile
            elif event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                self.selected_tile = world.get_tile(tile_pos)

    ############### UPDATE ###########################

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        self.update_tile_properties()
        self.update_game_map()
        self._update_ui_element_pos()

    def update_tile_properties(self):
        """
        Refresh tile dimensions and the map bounds.
        """
        self.x_bounds, self.y_bounds = self.get_tile_bounds()

    def update_game_map(self):
        """
        Update the game map to show the current tiles and entities
        """
        # create new surface for the game map
        map_width = self.game_map.rect.width
        map_height = self.game_map.rect.height
        map_surf = Surface((map_width, map_height), SRCALPHA)

        # draw tiles
        for tile in self._current_tiles():
            # if in player fov
            if tile.is_visible:
                self.draw_surface(tile.sprite, map_surf, (tile.x, tile.y))

        # draw entities
        for entity, (pos, aesthetic) in world.get_components([Position, Aesthetic]):
            # if in camera view
            if self.is_in_camera_view((pos.x, pos.y)):
                tile = world.get_tile((pos.x, pos.y))
                if tile.is_visible:
                    self.draw_surface(aesthetic.current_sprite, map_surf, (aesthetic.screen_x, aesthetic.screen_y))

        self.game_map.set_image(map_surf)

    def update_grid(self):
        """
        Update the tile grid to only have options in line with the tiles set OR the overlay
        """
        should_update = False

        if self.is_overlay_visible:

            # player column and row
            p_col = self.player_tile.x
            p_row = self.player_tile.y

            # offset center column and center row
            cx = p_col - int(self.start_tile_col)
            cy = p_row - int(self.start_tile_row)

            # set to contain all the tile positions in the overlay_directions
            tile_positions = {(cx + dir_x, cy + dir_y) for dir_x, dir_y in self.overlay_directions}

            # set to contain all the tile positions in the current grid
            current_positions = {self.get_tile_col_row(element.object_ids[-1]) for element in self.grid.elements}

            # have to redraw only if the tile positions are different
            should_update = tile_positions != current_positions

        else:
            # tile positions generator - contains 1 layer of padding to ensure smooth rollover
            tile_positions = ((x, y) for x in range(-1, self.columns + 1) for y in range(-1, self.rows + 1))

            # number of tiles
            no_of_tiles = (self.columns + 2) * (self.rows + 2)

            # redraw necessary if the amount of tiles doesn't match
            should_update = no_of_tiles != len(self.grid.elements)

        if should_update:
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
        updated_pos = self._grid_to_screen_position((col + dx, row + dy))

        # update only if the current and updated position don't match
        should_update = updated_pos != (x, y)

        if should_update:
            for element in self.grid.elements:

                # cast for typing
                element = cast(UIButton, element)

                # get the updated position
                col, row = self.get_tile_col_row(element.object_ids[-1])
                updated_pos = self._grid_to_screen_position((col + dx, row + dy))

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
            # FIXME - this tanks FPS - why?
            # check in fov
            # tile = world.get_tile((col, row))
            # if tile.is_visible:

                # find the screen position
                screen_x, screen_y = self._grid_to_screen_position((col, row))

                # create a rect
                tile_rect = Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE)

                # draw a button
                UIButton(relative_rect=tile_rect, manager=manager, text="", container=grid, parent_element=grid,
                         object_id=f"#tile{col},{row}")

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
        self.player_tile = tile

    def set_overlay_visibility(self, is_visible: bool):
        """
        Set whether the targeting overlay is visible or now.
        """
        self.is_overlay_visible = is_visible

    def set_overlay_directions(self, directions: List):
        """
        Set the overlay with possible targeting directions.
        """
        self.overlay_directions = directions

    ################## GET ######################

    def get_tile_bounds(self):
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

    ############# ACTIONS #########################

    def draw_surface(self, sprite: Surface, map_surface: Surface, col_row: Tuple[float, float]):
        """
        Draw a surface on the surface map. The function handles coordinate transformation to the screen
        """
        pos = self.world_to_screen_position(col_row)
        map_surface.blit(sprite, pos)

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

    def world_to_screen_position(self, pos: Tuple[float, float]):
        """
        Convert from the world_objects position to the screen position
        """
        screen_x = int((pos[0] - self.start_tile_col) * TILE_SIZE)
        screen_y = int((pos[1] - self.start_tile_row) * TILE_SIZE)

        return screen_x, screen_y

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
        x_start, x_max = self.x_bounds
        y_start, y_max = self.y_bounds

        return x_start <= x < x_max and y_start <= y < y_max

    def _grid_to_screen_position(self, pos: Tuple[float, float]) -> Tuple[int, int]:
        """
        Converts grid positions to screen positions
        """
        x, y = pos
        screen_x = int(x * TILE_SIZE)
        screen_y = int(y * TILE_SIZE)
        return screen_x, screen_y

    def _current_tiles(self):
        """
        Current tiles as a generator
        """
        tile_generator = (world.get_tile((x, y)) for x in range(*self.x_bounds) for y in range(*self.y_bounds))
        return tile_generator
