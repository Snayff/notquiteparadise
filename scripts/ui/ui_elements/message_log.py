import logging

from scripts.core.constants import VisualInfo, InputStates, MouseButtons
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class MessageLog(UIElement):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self):

        # size and position
        width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = VisualInfo.BASE_WINDOW_HEIGHT - height

        # create style
        palette = Palette().message_log
        font = Font().message_log
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        base_style = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)

        # create child text box and style
        children = []
        edge = 5
        text_box_base_style = WidgetStyle(font=font, background_colour=bg_colour, font_colour=font_colour)
        text_box = TextBox(edge, edge, width - (edge * 2), height - (edge * 2), text_box_base_style, [],
                           "message_box")
        children.append(text_box)

        # complete base class init
        super().__init__(x, y, width, height, base_style, children)

        # confirm init complete
        logging.debug(f"MessageLog initialised.")

    def draw(self, main_surface):
        """
        Draw the message log.

        Args:
            main_surface ():
        """
        super().draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """
        if input_key == MouseButtons.WHEEL_UP:
            for child in self.children:
                if child.name == "message_box":
                    child.first_line_index = max(child.first_line_index - 1, 0)
                    child.update_text_shown()
        elif input_key == MouseButtons.WHEEL_DOWN:
            for child in self.children:
                if child.name == "message_box":
                    max_index = max(len(child.text_list) - child.max_lines, 0)
                    child.first_line_index = min(child.first_line_index + 1, max_index)
                    child.update_text_shown()

    def add_message(self, message: str):
        """
        Add a message to the message log

        Args:
            message ():
        """
        for child in self.children:
            if child.name == "message_box":
                child.add_text(message)
                child.update_text_shown()



################################################
# LEFT AS REFERENCE FOR TOOL TIP
################################################
#
# import logging
# import pygame
#
# from scripts.ui_elements.colours import Colour
# from scripts.ui_elements.palette import Palette
# from scripts.core.constants import MessageEventTypes, VisualInfo
# from scripts.core.fonts import Font
# from scripts.ui_elements.templates.panel import Panel
#
#
# class OLD_MessageLog:
#     """
#     Store messages, and related functionality, to be shown in the text log.
#
#     Attributes:
#         palette (Palette): Palette of Colours
#         message_list (List(Tuple(MessageEventTypes, string))):  list of messages and their type
#         message_type_to_show  (MessageEventTypes): Type of text to show in log
#         expressions  (Dict): Dictionary of expressions to look for and their colour to show.
#         icons (Dict): Dictionary of icons to look for and the icon to show.
#         hyperlinks (Dict): Dictionary of hyperlinks to look for and the linked info to show.
#         is_dirty:
#         displayed_hyperlinks:
#         index_of_active_hyperlink:
#     """
#
#     def __init__(self):
#         # log setup
#         self.font = Font().message_log
#         self.colour = Colour()
#         self.palette = Palette().message_log
#         self.message_list = [(MessageEventTypes.BASIC, "Welcome to Not Quite Paradise")]
#         self.message_type_to_show = MessageEventTypes.BASIC
#         self.expressions = self.create_expressions_list()
#         self.icons = self.initialise_icons_list()
#         self.hyperlinks = self.initialise_hyperlinks_list()
#
#         # hyperlink info
#         self.is_dirty = True
#         self.displayed_hyperlinks = []
#         self.index_of_active_hyperlink = -1
#
#         # tooltip info # TODO - move to tooltip class when there is one
#         self.seconds_before_tooltip = 0.2
#         self.seconds_before_extended_text = 1
#
#         # panel info
#         panel_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
#         panel_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
#         panel_x = VisualInfo.BASE_WINDOW_WIDTH - panel_width
#         panel_y = VisualInfo.BASE_WINDOW_HEIGHT - panel_height
#         panel_border = 2
#         panel_background_colour = self.palette.background
#         panel_border_colour = self.palette.border
#         self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
#                            panel_border_colour)
#
#         # set panel to be rendered
#
#         # log info
#         self.edge_size = 1
#         self.message_indent = 5
#         self.gap_between_lines = int(self.font.size / 3)
#         self.first_message_to_show = 0
#         self.number_of_messages_to_show = int((panel_height - 2 * self.edge_size) / (self.font.size +
#                                                                                      self.gap_between_lines))
#
#         logging.debug( f"OLD_MessageLog initialised.")
#
#     def draw(self, surface):
#         """
#         Draw the text log and all included text and icons
#         Args:
#             surface(Surface): Main surface to draw to.
#         """
#         # get the surface to draw to
#         panel_surface = self.panel.surface
#
#         # panel background
#         self.panel.draw_background()
#
#         # show only as many message_list as we can or have
#         messages_to_show = min(len(self.message_list), self.number_of_messages_to_show)
#         first_message_index = self.first_message_to_show
#
#         # init info for text render
#         msg_x = self.edge_size + self.message_indent
#         msg_y = self.edge_size
#         font = self.font
#         messages = self.message_list
#         font_size = font.size
#
#         # render the message_list
#         for message_count in range(messages_to_show):
#             # reset offset
#             current_msg_x_offset = 0
#
#             # get y position of line to write to
#             adjusted_y = msg_y + (message_count * (font_size + self.gap_between_lines))
#
#             # parse text for expressions
#             parsed_message = self.parse_message(messages[message_count + first_message_index][1])
#
#             # render all parsed messages
#             for counter in range(len(parsed_message)):
#
#                 # get the text to render and position to render to
#                 msg_to_render = parsed_message[counter][1]
#                 adjusted_x = msg_x + current_msg_x_offset
#
#                 # check if it exists in the icon list
#                 if msg_to_render == "icon":
#                     icon = parsed_message[counter][0]
#                     panel_surface.blit(icon, (adjusted_x, adjusted_y))
#
#                     # update x offset based on width of image
#                     image_size = icon.get_width()
#
#                     current_msg_x_offset += image_size + (font_size / 3)
#
#                 # its not an icon so must be text.
#                 else:
#                     #  Check for a hyperlink
#                     if msg_to_render in self.hyperlinks:
#
#                         link_already_logged = False
#                         msg_colour = self.palette.hyperlink
#
#                         # check we havent already logged it
#                         for link_counter in range(len(self.displayed_hyperlinks)):
#                             if msg_to_render == self.displayed_hyperlinks[link_counter][1]:
#                                 link_already_logged = True
#
#                         if not link_already_logged:
#                             # get the hyperlink rect
#                             hyperlink_rect = font.render_to(panel_surface, (adjusted_x, adjusted_y),
#                                                             msg_to_render, msg_colour)
#
#                             # update the rect to reflect current position
#                             hyperlink_rect.x = adjusted_x
#                             hyperlink_rect.y = adjusted_y
#
#                             # add rect of hyperlink to active list
#                             self.displayed_hyperlinks.append((hyperlink_rect, msg_to_render, 0))
#                             # 0 is mouse over timer
#                     else:
#                         msg_colour = parsed_message[counter][0]
#
#                     font.render_to(panel_surface, (adjusted_x, adjusted_y), msg_to_render, msg_colour)
#
#                     # update x offset based on length of string just rendered
#                     msg_length = len(msg_to_render)
#                     current_msg_x_offset += (msg_length + 2) * (font_size / 2)  # Not sure about the formula, but it
#                                                                                 # seems to works.
#
#         # no longer dirty # TODO - uncomment when able to setup text log is dirty
#         # self.is_dirty = False
#
#         # panel border
#         self.panel.draw_border()
#         surface.blit(self.panel.surface, (self.panel.x, self.panel.y))
#
#     def draw_tooltips(self, surface):
#         """
#         draw the tooltips and  their text
#
#         Args:
#             surface (Surface): Main surface to draw to.
#         """
#         # TODO - extract tooltip method from text log
#         # Message log tooltips
#         font = self.font
#         font_colour = self.palette.tooltip_text
#
#         # update text log tooltip info
#         self.check_mouse_over_link()
#
#         tooltip_info = self.get_active_tooltip()
#
#         if tooltip_info:
#             text_rect, tooltip_text, extended_text_x, extended_text_y, extended_tooltip_text = tooltip_info
#
#             pygame.draw.rect(surface, self.colour.black, text_rect)
#             font.render_to(surface, (text_rect.x, text_rect.y), tooltip_text, font_colour)
#
#             if extended_text_x != -1:
#                 font.render_to(surface, (extended_text_x, extended_text_y), extended_tooltip_text,
#                                font_colour)
#
#     def add_message(self, message_type, text):
#         """
#         Add a text to the OLD_MessageLog
#         Args:
#             message_type(MessageEventTypes):
#             text(str):
#         """
#         logging.info(f"{text} added to text log")
#
#         self.message_list.append((message_type, text))
#
#         # if more messages than we can show at once then increment first text position
#         if len(self.message_list) > self.number_of_messages_to_show:
#             self.update_first_message_position(1)
#
#     def update_first_message_position(self, increment):
#         """
#
#         Args:
#             increment:
#         """
#         #  prevent the first text going too far and showing less than max number of message_list to show
#         self.first_message_to_show = min(self.first_message_to_show + increment, len(self.message_list) -
#                                                                                  self.number_of_messages_to_show)
#
#         # ensure first text position cannot be less than the start of the message_list
#         self.first_message_to_show = max(self.first_message_to_show, 0)
#
#     def set_message_type_to_show(self, message_type):
#         """
#
#         Args:
#             message_type(MessageEventTypes):
#         """
#         self.message_type_to_show = message_type
#
#     def create_expressions_list(self):
#         """
#         Create list of expressions to look for in log and apply formatting
#
#         Returns:
#             Dict
#         """
#         expressions = {}
#
#         expressions["fighter"] = self.palette.expressions_player
#         expressions["moved"] = self.palette.expressions_player
#
#         return expressions
#
#     @staticmethod
#     def initialise_icons_list():
#         """
#         Create list of icons to look for in log and render
#
#         Returns:
#             Dict
#         """
#         icons = {}
#
#         #icons["player"] = pygame.image.load("assets/actor/player.png").convert_alpha()
#         #icons["orc"] = pygame.image.load("assets/actor/enemy.png").convert_alpha()
#
#         return icons
#
#     @staticmethod
#     def initialise_hyperlinks_list():
#         """
#         Create list of hyperlinks to look for in log and render
#
#         Returns:
#             Dict
#         """
#         hyperlinks = {}
#
#         hyperlinks["Welcome"] = ("This is linked text", "This is the extended linked text")
#         hyperlinks["damage"] = ("2nd linked text", "2nd extended")
#
#         return hyperlinks
#
#     def check_mouse_over_link(self):
#         """
#
#         """
#         # TODO - increment displayed_hyperlinks rect positions when new lines added
#
#         for link in range(len(self.displayed_hyperlinks)):
#
#             from scripts.global_singletons.managers import ui_manager
#             pos = ui_manager.get_relative_scaled_mouse_pos("message_log")
#
#             # get the link rect
#             link_rect = self.displayed_hyperlinks[link][0]
#             link_text = self.displayed_hyperlinks[link][1]
#             link_mouse_over_timer = self.displayed_hyperlinks[link][2]
#
#             # check mouse is over the link
#             if link_rect.collidepoint(pos):
#                 # replace tuple with new one that has updated timer value
#                 self.displayed_hyperlinks[link] = (link_rect, link_text, link_mouse_over_timer + 1)
#                 self.index_of_active_hyperlink = link
#                 # TESTING TIMING OVER HOVER OVER  # FIXME - timing isnt working, ~30 frames is 1 sec. Use Delta time?
#                 # print(f"{link_mouse_over_timer + 1}")
#                 # from datetime import datetime
#                 # print(datetime.now().time())
#             else:
#                 self.displayed_hyperlinks[link] = (link_rect, link_text, 0)
#
#     def get_active_tooltip(self):
#         """
#         Get the info from the active tooltip, if there is one
#
#         Returns:
#             List: Either empty or contains text_rect, tooltip_text, extended_text_x, extended_text_y,
#             extended_tooltip_text
#
#         """
#         font_size = self.font.size
#
#         # is there an active link?
#         if self.index_of_active_hyperlink >= 0:
#
#             # init extended info, in case we don't load the real stuff
#             text_rect = -1
#             tooltip_text = ""
#             extended_text_x = -1
#             extended_text_y = -1
#             extended_tooltip_text = ""
#
#             # how long have we been hovering over it?
#             seconds_hovering = self.displayed_hyperlinks[self.index_of_active_hyperlink][2] / VisualInfo.GAME_FPS
#
#             # is it long enough?
#             if seconds_hovering > self.seconds_before_tooltip:
#                 # get linked text
#                 active_link = self.displayed_hyperlinks[self.index_of_active_hyperlink]
#                 hyperlink_strings = self.hyperlinks.get(active_link[1])
#                 tooltip_text = hyperlink_strings[0]
#
#                 # get location to show text
#                 text_x = active_link[0].x + 10
#                 text_y = active_link[0].y
#
#                 # create the text on a surface to get dimensions
#                 text_rect = self.font.render(tooltip_text, self.colour.white)[1]
#
#                 # move tooltip_rect to the place in the message_log
#                 text_rect.x = text_x + self.panel.x
#                 text_rect.y = text_y + self.panel.y - (text_rect.height * 1.5)
#
#                 # is it time for the extended text?
#                 if seconds_hovering > self.seconds_before_extended_text:
#                     extended_tooltip_text = hyperlink_strings[1]
#
#                     # create the text on a surface to get dimensions
#                     extended_text_rect = self.font.render(extended_tooltip_text, self.colour.white)[1]
#
#                     # move tooltip_rect to the place in the message_log, adjusting to be below first tooltip
#                     extended_text_x = text_x + self.panel.x
#                     extended_text_y = text_y + (font_size / 2) + self.panel.y
#
#                     # resize the original rect to encompass both tooltips
#                     width_of_widest_rect = max(text_rect.width, extended_text_rect.width)
#                     text_rect.width = width_of_widest_rect
#                     text_rect.height = text_rect.height + extended_text_rect.height
#
#                     # adjust the rects for new height
#                     text_rect.y -= extended_text_rect.height
#                     extended_text_y -= (extended_text_rect.height + font_size)
#
#                 # resize the rect in place
#                 text_rect.inflate_ip(5, 10)
#
#                 return [text_rect, tooltip_text, extended_text_x, extended_text_y, extended_tooltip_text]
#             else:
#                 return []
#         else:
#             return []
#
#     def parse_message(self, text):
#         """
#         Parse for colours, tags and formatting
#
#         Args:
#              text (str): The text string that needs parsing.
#
#         Returns:
#              List[Tuple[Colour, str]]: List of Tuples containing text and colour
#         """
#
#         updated_message = text
#
#         # add spaces around special chars
#         for char in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'']:
#             if char in text:
#                 updated_message = text.replace(char, " " + char)
#
#         # break text out by spaces
#         message_list = updated_message.split()
#
#         parsed_message_list = []
#         default_colour = self.palette.text_default
#         msg_in_progress = ""
#
#         # check each word for inclusion in lists and rebuild as new list
#         for message_count in range(len(message_list)):
#
#             msg = message_list[message_count]
#
#             # EXPRESSIONS
#             if msg in self.expressions:
#
#                 # expression found so let`s deal with any in progress text
#                 if msg_in_progress != "":
#                     # apply currently built string and then increment line
#                     parsed_message_list.append((default_colour, msg_in_progress))
#                     msg_in_progress = ""
#
#                 # create the expression as a new text
#                 colour = self.expressions.get(msg)
#                 parsed_message_list.append((colour, msg))
#
#             # ICONS
#             elif msg in self.icons:
#
#                 # icon found so let`s deal with any in progress text
#                 if msg_in_progress != "":
#                     # apply currently built string and then increment line
#                     parsed_message_list.append((default_colour, msg_in_progress))
#                     msg_in_progress = ""
#
#                 # create the icon as a new text
#                 icon = self.icons.get(msg)
#                 parsed_message_list.append((icon, "icon"))
#
#             # HYPERLINKS
#             elif msg in self.hyperlinks:
#
#                 # hyperlink found so let`s deal with any in progress text
#                 if msg_in_progress != "":
#                     # apply currently built string and then increment line
#                     parsed_message_list.append((default_colour, msg_in_progress))
#                     msg_in_progress = ""
#
#                 # amend the colour to indicate the text is a  hyperlink
#                 parsed_message_list.append((self.palette.hyperlink, msg))
#
#             # NORMAL TEXT
#             else:
#                 # No match so extend current text line
#                 if msg_in_progress != "":
#                     msg_in_progress += " " + msg
#                 else:
#                     msg_in_progress += msg
#
#         # add any remaining "in progress" messages
#         parsed_message_list.append((default_colour, msg_in_progress))
#
#         return parsed_message_list
