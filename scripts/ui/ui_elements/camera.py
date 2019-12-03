import logging
import pygame
from typing import List
from scripts.core.constants import VisualInfo, InputStates, TILE_SIZE, Directions, UIElementTypes
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.grid import Grid
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class Camera(UIElement):
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):

        self.rows = 10
        self.columns = 10
        self.start_tile_col = 0
        self.start_tile_row = 0
        self.edge_size = 3  # # of tiles to control camera movement
        self.is_overlay_visible = False
        self.selected_child = None  # the child widget currently being selected
        self.player_cell = None  # the child widget in which the player resides
        self.selected_tile_pos = (0, 0)  # tile x,y
        self.overlay_directions = []  # hold list of cardinal directions to show in the overlay

        # size and position
        width = TILE_SIZE * self.columns
        height = TILE_SIZE * self.rows
        x = 10
        y = 10

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
        selected_tile = self.create_selected_tile_widget()
        camera_children.append(game_map)
        camera_children.append(overlay)
        camera_children.append(selected_tile)

        # complete base class init
        super().__init__(UIElementTypes.CAMERA, base_style, x, y, width, height, camera_children)

        # confirm init complete
        logging.debug(f"Camera initialised.")

    def update(self):
        """
        Ensure all the children update in response to changes. Update the overlay to be positioned over the player.
        """
        if self.is_dirty:
            # update overlay position to match player's
            if self.player_cell:
                overlay = self.get_child("overlay")
                overlay.rect.x = self.player_cell.rect.x
                overlay.rect.y = self.player_cell.rect.y
                print(f"player:{self.player_cell.rect};  new overlay:{overlay.rect}")

        super().update()

    def draw(self, main_surface):
        """
        Draw the camera. Overrides super.

        Args:
            main_surface ():
        """
        adjusted_rect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.base_style.draw(self.surface, adjusted_rect)

        # draw map
        game_map = self.get_child("map")
        game_map.draw(self.surface)

        # draw overlay
        if self.is_overlay_visible:
            overlay = self.get_child("overlay")
            overlay.draw(self.surface)

            # only draw desired directions
            for direction in self.overlay_directions:
                # TODO - don't draw centre tile
                direction_frame = self.get_child(f"{direction}")
                direction_frame.draw(self.surface)

        # draw selected tile
        selected_tile = self.get_child("selected_child")
        selected_tile.draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """
        if input_key == pygame.MOUSEMOTION:
            from scripts.managers.ui_manager import ui
            rel_x, rel_y = ui.Mouse.get_relative_scaled_mouse_pos()
            self.set_selected_tile(rel_x, rel_y)

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
        """
        Check what tile collides with the xy given and set the selected tile to that

        Args:
            x (int): x inside the ui element
            y (int): y inside the ui element
        """
        if not self.selected_child or not self.selected_child.rect.collidepoint((x, y)):
            # check which cell we're over
            for child in self.all_children():
                if child.rect.collidepoint((x, y)) and child.name.startswith("cell"):
                    self.selected_child = child

                    # move position of selected tile widget
                    selected_widget = self.get_child("selected_child")
                    selected_widget.rect.x = child.rect.x
                    selected_widget.rect.y = child.rect.y

                    # update selected tile info
                    child_name = child.name.replace(",", " ")
                    child_name = child_name.replace("cell", "")
                    split_name = [int(num) for num in child_name.split()]
                    row, col = split_name[0], split_name[1]
                    self.selected_tile_pos = (self.start_tile_col + row, self.start_tile_row + col)

                    # TODO - have ui get the selected tile and set the entity info

                    break

    def set_player_cell(self, tile_x, tile_y):
        """
        Check what tile collides with the xy given and set the player pos to that

        Args:
            tile_x (int): x of player on the game map
            tile_y (int): y of player on the game map
        """
        # get the cell player is in
        row = tile_x - self.start_tile_col
        col = tile_y - self.start_tile_row
        child = self.get_child(f"cell{row},{col}")
        self.player_cell = child
        self.is_dirty = True

    def create_map_widget(self) -> Grid:
        """
        Create the map widget

        Returns:
            Grid: Grid widget

        """
        # create map style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        # size and position
        cell_gap = 0
        edge = 5
        width = ((TILE_SIZE + cell_gap) * self.columns) + ((border_size + edge) * 2)
        height = ((TILE_SIZE + cell_gap) * self.rows) + ((border_size + edge) * 2)

        # create maps' children
        grid_rows = self.rows
        grid_columns = self.columns
        map_children = []

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

    @staticmethod
    def create_overlay_widget() -> Grid:
        """
        Create the target overlay widget

        Returns:
            Grid: grid widget

        """
        # size and position
        grid_rows = 3
        grid_columns = 3
        border_size = 2
        edge = 5
        cell_gap = 0
        width = ((TILE_SIZE + cell_gap) * grid_columns) + ((border_size + edge) * 2)
        height = ((TILE_SIZE + cell_gap) * grid_rows) + ((border_size + edge) * 2)

        # create overlay  style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default

        bg_colour = palette.overlay
        border_colour = palette.overlay_border
        number_of_directions = 9  # 8 cardinal directions + centre

        # create maps' children
        overlay_children = []

        # create a frame for each of the directions
        for direction_number in range(0, number_of_directions):
            base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                     font_colour=font_colour, border_size=border_size)
            direction_label = Directions(direction_number)
            frame = Frame(base_style=base_style, name=f"{direction_label}")
            overlay_children.append(frame)

        base_style = WidgetStyle(font=font, font_colour=font_colour, border_size=border_size)

        # create overlay
        # TODO - set the correct position, 1 tile up and left, from player
        overlay = Grid(base_style, edge, edge, width - (edge * 2), height - (edge * 2), overlay_children, "overlay",
                       grid_rows, grid_columns, cell_gap)

        return overlay

    @staticmethod
    def create_selected_tile_widget() -> Frame:
        """
        Create the widget for the selected tile

        Returns:
            Frame: frame widget

        """
        # create selected tile  style
        palette = Palette().camera
        font = Font().camera
        font_colour = palette.text_default
        border_size = 4
        border_colour = palette.selected_tile_border

        base_style = WidgetStyle(font=font, border_colour=border_colour, font_colour=font_colour,
                                 border_size=border_size)

        frame = Frame(base_style=base_style, name=f"selected_child", width=TILE_SIZE, height=TILE_SIZE)

        return frame
