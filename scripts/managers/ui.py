import pygame
from pygame.rect import Rect

from scripts.ui_elements.entity_info import SelectedEntityInfo
from scripts.ui_elements.message_log import MessageLog
from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_HEIGHT, BASE_WINDOW_WIDTH, TILE_SIZE
from scripts.core.fonts import Font


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc

    Attributes:
        focused_window (pygame.surface) : The window currently in focus.
        colour (Colour): Game Colours.
        palette (Palette): Palette of Colours
        font (Font): Renderable Font
        main_surface (pygame.surface): The main sufrace to render to
        message_log (MessageLog): Object holding message log functionality
    """

    def __init__(self):
        self.colour = Colour()
        self.palette = Palette()
        self.focused_window = None

        self.font = Font()
        self.desired_width = 1920  # TODO - allow for selection by player but only multiples of base (16:9)
        self.desired_height = 1080
        self.screen_scaling_mod_x = self.desired_width // BASE_WINDOW_WIDTH
        self.screen_scaling_mod_y = self.desired_height // BASE_WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.desired_width, self.desired_height))
        self.main_surface = pygame.Surface((BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT))
        self.visible_panels = {}  # dict of all panels that are currently being rendered

        self.message_log = None
        self.entity_info = None

    def init_message_log(self):
        """
        Initialise the message log
        """
        self.message_log = MessageLog()

    def init_entity_info(self):
        """
        Initialise the selected entity info
        """
        self.entity_info = SelectedEntityInfo()

    def draw_game(self, game_map=None, entities=None, debug_active=False):
        """
        Draw the entire game.

        Args:
            game_map (GameMap): the current game map
            entities (list[Entity]): list of entities
            debug_active (bool): whether to show the debug messages
        """
        # TODO - draw dirty only

        # clear last frames drawing
        self.main_surface.fill(self.colour.black)

        # draw new frame
        if "game_map" in self.visible_panels:
            game_map.draw(entities, self.main_surface)

        # debug doesnt use a panel so we check for the flag
        if debug_active:
            from scripts.core.global_data import debug_manager
            debug_manager.draw(self.main_surface)

        if "message_log" in self.visible_panels:
            self.message_log.draw(self.main_surface)
            self.message_log.draw_tooltips(self.main_surface)

        if "entity_info" in self.visible_panels:
            self.entity_info.draw(self.main_surface)

        # resize the surface to the desired resolution
        scaled_surface = pygame.transform.scale(self.main_surface, (self.desired_width, self.desired_height))
        self.screen.blit(scaled_surface, (0, 0))

        # update the display
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame

    def update_panel_visibility(self, name, panel, visible):
        """
        Update whether a panel is visible.

        Args:
            name(str): Key value
            panel(Panel):   The panel to pull the info from
            visible (bool): Whether to show the panel or not
        """
        if visible:
            self.visible_panels[name] = Rect(panel.x, panel.y, panel.width, panel.height)
        else:
            self.visible_panels.pop(name, None)

    def get_scaled_mouse_pos(self):
        """
        Get the scaled mouse position

        Returns(tuple): Returns mouse position scaled to screen size

        """
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = mouse_pos[0] // self.screen_scaling_mod_x, mouse_pos[1] // self.screen_scaling_mod_y
        return scaled_mouse_pos

    def get_relative_scaled_mouse_pos(self, visible_panel_name):
        """
        Get the scaled mouse position relative to the visible panel

        Returns(tuple): Returns mouse position scaled to screen size

        """
        panel_rect = self.visible_panels.get(visible_panel_name)
        mouse_pos = pygame.mouse.get_pos()
        scaled_mouse_pos = mouse_pos[0] // self.screen_scaling_mod_x, mouse_pos[1] // self.screen_scaling_mod_y
        relative_mouse_pos = scaled_mouse_pos[0] - panel_rect.x, scaled_mouse_pos[1] - panel_rect.y
        return relative_mouse_pos

