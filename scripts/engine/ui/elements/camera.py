import logging
import pygame
import pygame_gui
from typing import List, Tuple

from pygame_gui import UIManager
from pygame_gui.core import UIWindow, UIContainer
from pygame_gui.elements import UIButton, UIImage

from scripts.engine import world, existence
from scripts.engine.core.constants import TILE_SIZE, DirectionType, Direction
from scripts.engine.core.event_core import publisher
from scripts.engine.utility import clamp
from scripts.engine.event import ClickTile
from scripts.engine.component import Position, Aesthetic
from scripts.engine.world_objects.tile import Tile


class Camera(UIWindow):
    """
    Hold the visual info for the game Map
    """

    def __init__(self, rect: pygame.Rect, manager: UIManager, rows: int, cols: int):
        # general info
        self.rows = rows
        self.columns = cols
        self.start_tile_col = 0
        self.start_tile_row = 0
        self.edge_size = 3  # # of tiles to control camera movement

        # game map info
        self.player_tile = None  # the tile in which the player resides
        self.tiles: List[Tile] = []

        # overlay info
        self.is_overlay_visible = False
        self.overlay_directions: List[DirectionType] = []  # list of tuples

        # grid info
        self.selected_tile = None  # the tile in the grid currently being selected

        # complete base class init
        super().__init__(rect, manager, ["camera"])

        # create game map
        blank_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        self.game_map = UIImage(relative_rect=rect, image_surface=blank_surf, manager=manager,
                                container=self.get_container(), object_id="#game_map")

        # create grid
        self.grid = UIContainer(relative_rect=rect, manager=manager,  container=self.get_container(),
                                object_id="#grid")

        # confirm init complete
        logging.debug(f"Camera initialised.")

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        ui_object_id = event.ui_object_id

        # clicking a tile
        tile_prefix = "#tile"
        if ui_object_id[:len(tile_prefix)] == tile_prefix:
            tile_pos = ui_object_id[len('#tile'):]
            publisher.publish(ClickTile(tile_pos_string=tile_pos))

    ############### UPDATE ###########################

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)
        self.update_game_map()

    def update_game_map(self):
        """
        Update the game map to show the current tiles and entities
        """
        # create new surface for the game map
        map_width = self.game_map.rect.width
        map_height = self.game_map.rect.height
        map_surf = pygame.Surface((map_width, map_height), pygame.SRCALPHA)

        # draw tiles
        for tile in self.tiles:
            # TODO - determine where this is using FOV
            screen_x, screen_y = self.world_to_screen_position((tile.x, tile.y))
            map_surf.blit(tile.sprite, (screen_x, screen_y))

        # draw entities
        for entity, (pos, aesthetic) in existence.get_components([Position, Aesthetic]):
            # TODO - use FOV
            # if in camera view
            if self.start_tile_col <= pos.x < self.start_tile_col + self.columns:
                if self.start_tile_row <= pos.y < self.start_tile_row + self.rows:
                    map_surf.blit(aesthetic.current_sprite, (aesthetic.screen_x, aesthetic.screen_y))

        self.game_map.image = map_surf

    def update_grid(self):
        """
        Update the tile grid to only have  options in line with the tiles set OR the overlay
        """
        # clear existing grid tiles
        self.grid.clear()

        manager = self.ui_manager
        start_col = self.start_tile_col
        start_row = self.start_tile_row

        if self.is_overlay_visible:
            if self.player_tile:
                player_tile_x = self.player_tile.x
                player_tile_y = self.player_tile.y
            else:
                player_tile_x = 0
                player_tile_y = 0

            directions = self.overlay_directions

            # draw the overlay
            for direction in directions:
                offset_tile_x, offset_tile_y = getattr(Direction, direction.upper())
                x = ((player_tile_x + offset_tile_x) - start_col) * TILE_SIZE
                y = ((player_tile_y + offset_tile_y) - start_row) * TILE_SIZE
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                # get current row and col
                if x == 0:
                    tile_x = 0
                else:
                    tile_x = max(0, int(x / TILE_SIZE))
                if y == 0:
                    tile_y = 0
                else:
                    tile_y = max(0, int(y / TILE_SIZE))

                tile = UIButton(relative_rect=tile_rect, manager=manager, text="", container=self.grid,
                                parent_element=self.grid, object_id=f"#tile{tile_x},{tile_y}")
        else:
            tiles = self.tiles

            # create a grid for the tiles needed
            for tile in tiles:
                x = (tile.x - start_col) * TILE_SIZE
                y = (tile.y - start_row) * TILE_SIZE
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                # get current row and col
                if x == 0:
                    tile_x = 0
                else:
                    tile_x = max(0, int(x / TILE_SIZE))
                if y == 0:
                    tile_y = 0
                else:
                    tile_y = max(0, int(y / TILE_SIZE))

                tile = UIButton(relative_rect=tile_rect, manager=manager, text="", container=self.grid,
                                parent_element=self.grid, object_id=f"#tile{tile_x},{tile_y}")
                
    def update_camera_tiles(self):
        """
        Retrieve the tiles to draw within view of the camera and provide them to the camera. Checks FOV.
        """
        if self:
            tiles = []

            for x in range(self.start_tile_col, self.start_tile_col + self.columns):
                for y in range(self.start_tile_row, self.start_tile_row + self.rows):
                    # TODO - readd FOV
                    tile = world.get_tile((x, y))
                    if tile:
                        tiles.append(tile)
    
            self.set_tiles(tiles)

    ############## SET #########################

    def set_tiles(self, tiles: List):
        """
        Set the tiles in the camera.

        Args:
            tiles (): List of Tiles
        """
        self.tiles = tiles

    def set_player_tile(self, tile):
        """
        Set the player tile

        Args:
            tile ():
        """
        self.player_tile = tile

    def set_overlay_visibility(self, is_visible: bool):
        """
        Set whether the targeting overlay is visible or now.

        Args:
            is_visible ():
        """
        self.is_overlay_visible = is_visible

    def set_overlay_directions(self, directions: List):
        """
        Set the overlay with possible targeting directions.
        """
        self.overlay_directions = directions

    ############# UTILITY #########################

    def move_camera(self, num_cols: int, num_rows: int):
        """
        Adjust the camera position by the number of columns and rows
        """
        new_start_col = clamp(self.start_tile_col + num_cols, 0, self.columns)
        new_start_row = clamp(self.start_tile_row + num_rows, 0, self.rows)

        self.start_tile_col = new_start_col
        self.start_tile_row = new_start_row
        
    def world_to_screen_position(self, pos: Tuple[int, int]):
        """
        Convert from the world_objects position to the screen position
        """
        tile_width = int(self.game_map.rect.width / self.columns)
        tile_height = int(self.game_map.rect.height / self.rows)
        screen_x = (pos[0] - self.start_tile_col) * tile_width
        screen_y = (pos[1] - self.start_tile_row) * tile_height

        return screen_x, screen_y

