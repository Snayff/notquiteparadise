
import logging

from typing import Dict
from scripts.core.constants import VisualInfo
from scripts.ui.basic.fonts import Font
from scripts.ui.templates.panel import Panel


class MessageLog:
    """
    Store messages, and related functionality, to be shown in the text log.

    Attributes:
        message_list (List(Tuple(MessageEventTypes, string))):  list of messages and their type
        icons (Dict): Dictionary of icons to look for and the icon to show.
        is_dirty (bool): flag indicating need to draw
    """

    def __init__(self):
        # log setup
        self.message_list = []
        self.messages_to_draw = []
        self.keywords = {}
        self.icons = {}
        self.commands = {}
        self.is_dirty = True
        self.is_visible = False

        # panel info
        panel_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        panel_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        panel_x = VisualInfo.BASE_WINDOW_WIDTH - panel_width
        panel_y = VisualInfo.BASE_WINDOW_HEIGHT - panel_height
        panel_border = 2

        from scripts.global_singletons.managers import ui_manager
        palette = ui_manager.Palette.message_log
        panel_background_colour = palette.background
        panel_border_colour = palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # log info
        self.edge_size = 1
        self.message_indent = 5
        font_size = Font().message_log.size
        self.gap_between_lines = int(font_size / 3)
        self.first_message_index = 0
        self.number_of_messages_to_show = int((panel_height - 2 * self.edge_size) / (font_size +
                                                                                     self.gap_between_lines))

        logging.debug(f"MessageLog initialised.")

    def draw(self, surface):
        """
        Draw the text log and all included text and icons

        Args:
            surface(Surface): Main surface to draw to.
        """
        # get the surface to draw to
        panel_surface = self.panel.surface

        # panel background
        self.panel.draw_background()

        # init info for text render
        msg_x = self.edge_size + self.message_indent
        msg_y = self.edge_size
        from scripts.global_singletons.managers import ui_manager
        font = ui_manager.Font.message_log
        font_size = font.size
        line_count = 0

        # render the messages_to_draw
        for line_list in self.messages_to_draw:
            # reset offset
            x_offset = 0

            # get y position of line to write to
            adjusted_y = msg_y + (line_count * (font_size + self.gap_between_lines))

            # update  line count
            line_count += 1

            # pull each surface from each line_list and render to the panel surface
            for message in line_list:
                panel_surface.blit(message, (msg_x + x_offset, adjusted_y))
                message_width = message.get_width()
                x_offset += message_width + 2  # 2 for space between words

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))


