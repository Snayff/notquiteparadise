
from scripts.core.colours import Palette, Colour
from scripts.core.fonts import Font


class DebugManager:
    def __init__(self):
        self.visible = False
        self.messages = []

        self.show_game_time = False
        self.show_fps = True
        self.show_mouse_pos = True

        self.font = Font().debug

    def update(self):
        """
        Update to run every frame
        """
        if self.visible:
            self.update_debug_message()

    def draw(self, surface):
        """
        Draw the debug info
        Args:
            surface:
        """
        font = self.font
        font_size = font.size

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
            from scripts.core.global_data import turn_manager
            msg = f"The game time is: {turn_manager.time}"
            self.messages.append(msg)

        if self.show_fps:
            from scripts.core.global_data import game_manager
            clock = game_manager.internal_clock
            fps = str(int(clock.get_fps()))
            msg = f"FPS : {fps}"
            self.messages.append(msg)

        if self.show_mouse_pos:
            from scripts.core.global_data import ui_manager
            pos = ui_manager.get_scaled_mouse_pos()
            msg = f"Abs mouse pos : {pos}"
            self.messages.append(msg)

            offset_x = 0
            offset_y = 0
            current_rect = ""

            for key, rect in ui_manager.visible_panels.items():
                if rect.collidepoint(pos):
                    offset_x = rect.x
                    offset_y = rect.y
                    current_rect = key
            relative_pos = pos[0] - offset_x, pos[1] - offset_y
            if current_rect:
                msg2 = f"Rel mouse pos in {current_rect} : {relative_pos} "
                self.messages.append(msg2)

    def set_visibility(self, visible):
        """
        Set whether the debug info is visible

        Args:
            visible (bool): Whether debug info is visible
        """
        self.visible = visible
