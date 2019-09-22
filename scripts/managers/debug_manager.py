
import logging

from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.core.constants import TILE_SIZE
from scripts.core.fonts import Font


class DebugManager:
    """
    Manager of Debug Functions
    """
    def __init__(self):
        self.visible = False
        self.messages = []

        self.show_game_time = True
        self.show_fps = True
        self.show_mouse_pos = False
        self.show_game_state = True
        self.show_tile_xy = False

        self.font = Font().debug

        logging.info( f"DebugManager initialised.")

    def update(self):
        """
        Update to run every frame
        """
        if self.visible:
            self.update_debug_message()

    def draw(self):
        """
        Draw the debug info
        """
        from scripts.global_singletons.managers import ui_manager
        surface = ui_manager.Display.get_main_surface()

        font = self.font
        font_size = font.size

        # render tile coords
        if self.show_tile_xy:
            from scripts.global_singletons.managers import world_manager
            panel = world_manager.game_map.panel

            for tile_x in range(0, panel.width, TILE_SIZE):
                for tile_y in range(0, panel.height, TILE_SIZE):
                    tile_row = int(tile_x / TILE_SIZE)
                    tile_col = int(tile_y / TILE_SIZE)
                    font.render_to(surface, (tile_x, tile_y), f"{tile_row},{tile_col}", Palette().debug_font_colour)

        # render debug messages
        # loop all lines in message and use line index to amend msg position
        for line in range(len(self.messages)):
            y_pos = 0 + (line * font_size)  # 0 is starting y coord
            font.render_to(surface, (0, y_pos), self.messages[line], Palette().debug_font_colour,
                           Colour().black)

    def update_debug_message(self):
        """
        Populate the debug messages/info
        """

        self.messages = []

        if self.show_game_time:
            from scripts.global_singletons.managers import turn_manager
            msg = f"Game time is: {turn_manager.time}, Round: {turn_manager.round}, time in round: " \
                  f" {turn_manager.round_time}"
            self.messages.append(msg)

        if self.show_fps:
            from scripts.global_singletons.managers import game_manager
            clock = game_manager.internal_clock
            fps = str(int(clock.get_fps()))
            msg = f"FPS : {fps}"
            self.messages.append(msg)

        if self.show_mouse_pos:
            from scripts.global_singletons.managers import ui_manager
            pos = ui_manager.Mouse.get_scaled_mouse_pos()
            msg = f"Abs mouse pos : {pos}, "

            offset_x = 0
            offset_y = 0
            current_rect = ""

            for key, ui_object in ui_manager.visible_elements.items():
                if hasattr(ui_object, "panel"):
                    if ui_object.panel.rect.collidepoint(pos):
                        offset_x = ui_object.panel.x
                        offset_y = ui_object.panel.y
                        current_rect = key
            relative_pos = pos[0] - offset_x, pos[1] - offset_y
            if current_rect:
                msg += f"Rel mouse pos in {current_rect} : {relative_pos} "
                self.messages.append(msg)

        if self.show_game_state:
            from scripts.global_singletons.managers import game_manager
            msg = f"Game state: {game_manager.game_state}"
            self.messages.append(msg)

    def set_visibility(self, visible):
        """
        Set whether the debug info is visible

        Args:
            visible (bool): Whether debug info is visible
        """
        self.visible = visible
