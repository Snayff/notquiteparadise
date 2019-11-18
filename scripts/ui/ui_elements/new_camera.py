import logging
import pygame
from typing import List
from scripts.core.constants import VisualInfo, InputStates, TILE_SIZE, Directions
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class NewCamera(UIElement):
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):

        self.rows = 10
        self.columns = 10
        self.start_tile_x = 0
        self.start_tile_y = 0
        self.edge_size = 3  # # of tiles to control camera movement
        self.is_overlay_visible = False
        self.selected_tile = None
        self.overlay_directions = []  # hold list of cardinal directions to show in the overlay

        # size and position
        width = TILE_SIZE * self.columns
        height = TILE_SIZE * self.rows
        x = 2
        y = 2

        # style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2
        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create children
        camera_children = []
        game_map = self.create_map_widget()
        overlay = self.create_overlay_widget()
        camera_children.append(game_map)
        camera_children.append(overlay)

        # complete base class init
        super().__init__(base_style, x, y, width, height, camera_children)

        # confirm init complete
        logging.debug(f"Camera initialised.")

    def update(self):
        """
        Ensure all the children update in response to changes.
        """
        super().update()

        params = []
        for child in self.all_children():
            params.append(f"{child.name}:({child.rect.x},{child.rect.y})")
        print(f"{params}")
        pass

    def draw(self, main_surface):
        """
        Draw the camera. Overrides super.

        Args:
            main_surface ():
        """
        adjusted_rect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.base_style.draw(main_surface, adjusted_rect)

        # draw map
        game_map = self.get_child("map")
        if not game_map.is_dirty:
            game_map.draw(self.surface)

        # draw overlay
        if self.is_overlay_visible:
            overlay = self.get_child("overlay")
            overlay.draw(self.surface)

            # only draw desired directions
            for direction in self.overlay_directions:
                direction_frame = self.get_child(f"{direction}")
                direction_frame.draw(self.surface)

            # draw selected tile
            # TODO - add selected tile

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """

        pass

    def set_cell_background_image(self, row: int, col: int, image: pygame.Surface):
        """
        Set the background image of a cell in the camera

        Args:
            row ():
            col ():
            image ():
        """
        cell = self.get_child(f"cell{row},{col}")

        if cell:
            cell.base_style.background_image = image
            cell.is_dirty = True

    def set_targeting_overlay_visibility(self, visible: bool, possible_directions: List):
        """
        Set the targeting overlay's visibility.

        Args:
            possible_directions ():
            visible ():
        """
        self.is_overlay_visible = visible
        self.overlay_directions = possible_directions


    def set_selected_tile(self, x, y):
        self.selected_tile = (x, y)

        # move position of selected tile widget
        # TODO - add selected tile widget

    def create_map_widget(self) -> Grid:
        # size and position
        width = TILE_SIZE * self.columns
        height = TILE_SIZE * self.rows
        cell_gap = 2
        edge = 5

        # create map style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        # create maps' children
        grid_rows = self.rows
        grid_columns = self.columns
        map_children = []

        # TODO - fix the square drawing in the top left, above the grid.
        for row in range(0, grid_rows):
            for col in range(0, grid_columns):
                base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                         font_colour=font_colour, border_size=border_size)
                frame = Frame(base_style=base_style, name=f"cell{row},{col}")
                # use textbox for debugging, to show cell pos. It is VERY slow.
                # frame = TextBox(base_style=base_style, name=f"cell{row},{col}", text=f"{row},{col}",
                #                 width=TILE_SIZE, height=TILE_SIZE)
                map_children.append(frame)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create map
        game_map = Grid(base_style=base_style, x=edge, y=edge, width=width - (edge * 2), height=height - (edge * 2),
                        children=map_children, name="map", rows=grid_rows, columns=grid_columns,
                        gap_between_cells=cell_gap)

        return game_map

    def create_overlay_widget(self) -> Grid:
        # size and position
        grid_rows = 3
        grid_columns = 3
        width = TILE_SIZE * grid_columns
        height = TILE_SIZE * grid_rows
        cell_gap = 1
        edge = 5

        # create overlay  style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        border_size = 2
        alpha = 127
        bg_colour = palette.overlay + (alpha, )  # create new tuple from colour and alpha
        border_colour = palette.overlay_border + (alpha, )
        number_of_directions = 8  # 8 cardinal directions

        # create maps' children
        overlay_children = []

        # create a frame for each of the directions
        for direction_number in range(0, number_of_directions):
            base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                     font_colour=font_colour, border_size=border_size)
            direction_label = Directions(direction_number)
            frame = Frame(base_style=base_style, name=f"{direction_label}")
            overlay_children.append(frame)

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create overlay
        # TODO - set the correct position, 1 tile up and left, from player
        overlay = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), overlay_children, "overlay",
                       grid_rows, grid_columns, cell_gap)

        return overlay