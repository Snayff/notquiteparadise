
import logging
import pygame

from scripts.core.fonts import Font
from scripts.managers.ui_methods.element_methods import ElementMethods
from scripts.managers.ui_methods.message_methods import MessageMethods
from scripts.managers.ui_methods.mouse_methods import MouseMethods
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.entity_info import SelectedEntityInfo
from scripts.core.constants import VisualInfo
from scripts.ui_elements.entity_queue import EntityQueue
from scripts.ui_elements.palette import Palette
from scripts.ui_elements.skill_bar import SkillBar
from scripts.ui_elements.targeting_overlay import TargetingOverlay


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc

    Attributes:
        main_surface (pygame.surface): The main surface to render to
    """

    def __init__(self):
        # methods
        self.Element = ElementMethods(self)
        self.Mouse = MouseMethods(self)
        self.Message = MessageMethods(self)
        self.Palette = Palette()  # doesnt need self as only holds data
        self.Font = Font()  # doesnt need self as only holds data

        self.elements = {}  # list of all init'd ui elements

        # display info - move to display?
        self.desired_width = VisualInfo.BASE_WINDOW_WIDTH  # TODO - allow for selection by player but only multiples of
                                                           #  base (16:9)
        self.desired_height = VisualInfo.BASE_WINDOW_HEIGHT
        self.screen_scaling_mod_x = self.desired_width // VisualInfo.BASE_WINDOW_WIDTH
        self.screen_scaling_mod_y = self.desired_height // VisualInfo.BASE_WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.desired_width, self.desired_height))
        self.main_surface = pygame.Surface((VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT))

        logging.info(f"UIManager initialised.")

    def update(self):
        """
        No updates currently needed but must have the method
        """


def example_code():
    pass
# Camera class from pygame tutorial
# class obj_Camera:
#
#     def __init__(self):
#
#         self.width = constants.CAMERA_WIDTH
#         self.height = constants.CAMERA_HEIGHT
#         self.x, self.y = (0, 0)
#
#     @property
#     def rectangle(self):
#
#         pos_rect = pygame.Rect((0, 0), (constants.CAMERA_WIDTH,
#                                         constants.CAMERA_HEIGHT))
#
#         pos_rect.center = (self.x, self.y)
#
#         return pos_rect
#
#     @property
#     def map_address(self):
#
#         map_x = self.x / constants.CELL_WIDTH
#         map_y = self.y / constants.CELL_HEIGHT
#
#         return (map_x, map_y)
#
#     def update(self):
#
#         target_x = PLAYER.x * constants.CELL_WIDTH + (constants.CELL_WIDTH/2)
#         target_y = PLAYER.y * constants.CELL_HEIGHT + (constants.CELL_HEIGHT/2)
#
#         distance_x, distance_y = self.map_dist((target_x, target_y))
#
#         self.x += int(distance_x)
#         self.y += int(distance_y)
#
#     def win_to_map(self, coords):
#
#         tar_x, tar_y = coords
#
#         #convert window coords to distace from camera
#         cam_d_x, cam_d_y = self.cam_dist((tar_x, tar_y))
#
#         #distance from cam -> map coord
#         map_p_x = self.x + cam_d_x
#         map_p_y = self.y + cam_d_y
#
#         return((map_p_x, map_p_y))
#
#
#     def map_dist(self, coords):
#
#         new_x, new_y = coords
#
#         dist_x = new_x - self.x
#         dist_y = new_y - self.y
#
#         return (dist_x, dist_y)
#
#     def cam_dist(self, coords):
#
#         win_x, win_y = coords
#
#         dist_x = win_x - (self.width / 2)
#         dist_y = win_y - (self.height / 2)
#
#         return (dist_x, dist_y)


# button  from pygame tutorial
# class ui_Button:
#
#     def __init__(self, surface, button_text, size, center_coords,
#                  color_box_mouseover = constants.COLOR_RED,
#                  color_box_default = constants.COLOR_GREEN,
#                  color_text_mouseover = constants.COLOR_GREY,
#                  color_text_default = constants.COLOR_GREY):
#
#         self.surface = surface
#         self.button_text = button_text
#         self.size = size
#         self.center_coords = center_coords
#
#         self.c_box_mo = color_box_mouseover
#         self.c_box_default = color_box_default
#         self.c_text_mo = color_text_mouseover
#         self.c_text_default = color_text_default
#         self.c_c_box = color_box_default
#         self.c_c_text = color_text_default
#
#         self.rect = pygame.Rect((0, 0), size)
#         self.rect.center = center_coords
#
#     def update(self, player_input):
#
#         mouse_clicked = False
#
#         local_events, local_mousepos = player_input
#         mouse_x, mouse_y = local_mousepos
#
#         mouse_over = (   mouse_x >= self.rect.left
#                      and mouse_x <= self.rect.right
#                      and mouse_y >= self.rect.top
#                      and mouse_y <= self.rect.bottom )
#
#         for event in local_events:
#             if event.event_type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1: mouse_clicked = True
#
#         if mouse_over and mouse_clicked:
#             return True
#
#         if mouse_over:
#             self.c_c_box = self.c_box_mo
#             self.c_c_text = self.c_text_mo
#         else:
#             self.c_c_box = self.c_box_default
#             self.c_c_text = self.c_text_default
#
#     def draw(self):
#
#         pygame.draw.rect(self.surface, self.c_c_box, self.rect)
#         draw_text(self.surface,
#                   self.button_text,
#                   constants.FONT_DEBUG_MESSAGE,
#                   self.center_coords,
#                   self.c_c_text,
#                   center = True)


# slider from pygame tutorial
# class ui_Slider:
#
#     def __init__(self,
#                  surface,
#                  size,
#                  center_coords,
#                  bg_color,
#                  fg_color,
#                  parameter_value):
#
#         self.surface = surface
#         self.size = size
#         self.bg_color = bg_color
#         self.fg_color = fg_color
#         self.current_val = parameter_value
#
#         self.bg_rect = pygame.Rect((0, 0), size)
#         self.bg_rect.center = center_coords
#         self.fg_rect = pygame.Rect((0, 0),
#                             (self.bg_rect.w * self.current_val, self.bg_rect.h))
#         self.fg_rect.topleft = self.bg_rect.topleft
#
#         self.grip_tab = pygame.Rect((0, 0), (20, self.bg_rect.h + 4))
#         self.grip_tab.center = (self.fg_rect.right, self.bg_rect.centery)
#
#     def update(self, player_input):
#
#         mouse_down = pygame.mouse.get_pressed()[0]
#
#         local_events, local_mousepos = player_input
#         mouse_x, mouse_y = local_mousepos
#
#         mouse_over = (   mouse_x >= self.bg_rect.left
#                      and mouse_x <= self.bg_rect.right
#                      and mouse_y >= self.bg_rect.top
#                      and mouse_y <= self.bg_rect.bottom )
#
#         if mouse_down and mouse_over:
#
#             self.current_val = (float(mouse_x) - float(self.bg_rect.left)) / self.bg_rect.w
#
#             self.fg_rect.width = self.bg_rect.width * self.current_val
#
#             self.grip_tab.center = (self.fg_rect.right, self.bg_rect.centery)
#
#
#
#     def draw(self):
#
#         # draw background rectangle
#         pygame.draw.rect(self.surface, self.bg_color, self.bg_rect)
#
#         # draw foreground rectangle
#         pygame.draw.rect(self.surface, self.fg_color, self.fg_rect)
#
#         # draw slider tab
#         pygame.draw.rect(self.surface, constants.COLOR_BLACK, self.grip_tab)
#



# menus from pygame tutorial
# def menu_main():
#
#     button_y_offset = 40
#
#     game_initialize()
#
#     menu_running = True
#
#     title_x = constants.CAMERA_WIDTH/2
#     title_y = constants.CAMERA_HEIGHT/2 - button_y_offset
#     title_text = "Python - RL"
#
#     # BUTTON ADDRESSES
#     continue_button_y = title_y + button_y_offset
#     new_game_button_y = continue_button_y + button_y_offset
#     options_button_y = new_game_button_y + button_y_offset
#     quit_button_y = options_button_y + button_y_offset
#
#     continue_game_button = ui_Button(SURFACE_MAIN,
#                             "Continue",
#                             (150, 30),
#                             (title_x, continue_button_y))
#
#     new_game_button = ui_Button(SURFACE_MAIN,
#                                 "New Game",
#                                 (150, 30),
#                                 (title_x, new_game_button_y))
#
#     options_button = ui_Button(SURFACE_MAIN,
#                                "Options",
#                                (150, 30),
#                                (title_x, options_button_y))
#
#     quit_button = ui_Button(SURFACE_MAIN,
#                             "Quit Game",
#                             (150, 30),
#                             (title_x, quit_button_y))
#
#     pygame.mixer.music.load(ASSETS.music_background)
#     pygame.mixer.music.play(-1)
#
#     while menu_running:
#
#         list_of_events = pygame.event.get()
#         mouse_position = pygame.mouse.get_pos()
#
#         game_input = (list_of_events, mouse_position)
#
#         # handle menu events
#         for event in list_of_events:
#             if event.event_type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#         #button updates
#         if continue_game_button.update(game_input):
#             pygame.mixer.music.stop()
#             # try to load game, start new if problems
#             try:
#                 game_load()
#             except:
#                 game_new()
#
#             game_main_loop()
#             game_initialize()
#
#
#         if new_game_button.update(game_input):
#             pygame.mixer.music.stop()
#             game_new()
#             game_main_loop()
#             game_initialize()
#
#         if options_button.update(game_input):
#             menu_options()
#
#         if quit_button.update(game_input):
#             # quit the game
#             pygame.quit()
#             sys.exit()
#
#         # draw menu
#         SURFACE_MAIN.blit(ASSETS.MAIN_MENU_BG, (0, 0))
#
#         draw_text(SURFACE_MAIN,
#                   title_text,
#                   constants.FONT_TITLE_SCREEN,
#                   (title_x, title_y),
#                   constants.COLOR_RED,
#                   back_color = constants.COLOR_BLACK,
#                   center = True)
#
#         continue_game_button.draw()
#         new_game_button.draw()
#         options_button.draw()
#         quit_button.draw()
#
#         #update surface
#         pygame.display.update()
#
# def menu_options():
#
#     # MENU VARS #
#     settings_menu_width = 200
#     settings_menu_height = 200
#     settings_menu_bgcolor = constants.COLOR_GREY
#
#     # SLIDER VARS #
#     slider_x = constants.CAMERA_WIDTH/2
#     sound_effect_slider_y = constants.CAMERA_HEIGHT/2 - 60
#     sound_effect_vol = .5
#     music_effect_slider_y = sound_effect_slider_y + 50
#
#     # TEXT VARS #
#     text_y_offset = 20
#     sound_text_y = sound_effect_slider_y - text_y_offset
#     music_text_y = music_effect_slider_y - text_y_offset
#
#     # BUTTON VARS#
#     button_save_y = music_effect_slider_y + 50
#
#     window_center = (constants.CAMERA_WIDTH/2, constants.CAMERA_HEIGHT/2)
#
#     settings_menu_surface = pygame.Surface((settings_menu_width,
#                                             settings_menu_height))
#
#     settings_menu_rect = pygame.Rect(0, 0,
#                                      settings_menu_width,
#                                      settings_menu_height)
#
#     settings_menu_rect.center = window_center
#
#     menu_close = False
#
#     sound_effect_slider = ui_Slider(SURFACE_MAIN,
#                                     (125, 15),
#                                     (slider_x, sound_effect_slider_y),
#                                     constants.COLOR_RED,
#                                     constants.COLOR_GREEN,
#                                     PREFERENCES.vol_sound)
#
#     music_effect_slider = ui_Slider(SURFACE_MAIN,
#                                     (125, 15),
#                                     (slider_x, music_effect_slider_y),
#                                     constants.COLOR_RED,
#                                     constants.COLOR_GREEN,
#                                     PREFERENCES.vol_music)
#
#     save_button = ui_Button(SURFACE_MAIN,
#                             "Save",
#                             (60, 30),
#                             (slider_x, button_save_y),
#                             constants.COLOR_DARKERGREY,
#                             constants.COLOR_DGREY,
#                             constants.COLOR_BLACK,
#                             constants.COLOR_BLACK)
#
#     while not menu_close:
#
#         list_of_events = pygame.event.get()
#         mouse_position = pygame.mouse.get_pos()
#
#         game_input = (list_of_events, mouse_position)
#
#         # handle menu events
#         for event in list_of_events:
#             if event.event_type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#             if event.event_type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     menu_close = True
#
#         current_sound_vol = PREFERENCES.vol_sound
#         current_music_vol = PREFERENCES.vol_music
#
#         sound_effect_slider.update(game_input)
#         music_effect_slider.update(game_input)
#
#         if current_sound_vol is not sound_effect_slider.current_val:
#             PREFERENCES.vol_sound = sound_effect_slider.current_val
#             ASSETS.volume_adjust()
#
#         if current_music_vol is not music_effect_slider.current_val:
#             PREFERENCES.vol_music = music_effect_slider.current_val
#             ASSETS.volume_adjust()
#
#         if save_button.update(game_input):
#             preferences_save()
#             menu_close = True
#
#         # Draw the Menu
#         settings_menu_surface.fill(settings_menu_bgcolor)
#
#         SURFACE_MAIN.blit(settings_menu_surface, settings_menu_rect.topleft)
#
#         draw_text(SURFACE_MAIN,
#               "SOUND",
#               constants.FONT_DEBUG_MESSAGE,
#               (slider_x, sound_text_y),
#               constants.COLOR_BLACK,
#               center = True)
#
#         draw_text(SURFACE_MAIN,
#               "MUSIC",
#               constants.FONT_DEBUG_MESSAGE,
#               (slider_x, music_text_y),
#               constants.COLOR_BLACK,
#               center = True)
#
#         sound_effect_slider.draw()
#         music_effect_slider.draw()
#         save_button.draw()
#
#         pygame.display.update()
#
# def menu_pause():

#     '''This menu pauses the game and displays a simple message.'''
#
#     # intialize to False, pause ends when set to True
#     menu_close = False
#
#     # window dimentions
#     window_width = constants.CAMERA_WIDTH
#     window_height = constants.CAMERA_HEIGHT
#
#     # Window Text characteristics
#     menu_text = "PAUSED"
#     menu_font = constants.FONT_DEBUG_MESSAGE
#
#     # helper vars
#     text_height = helper_text_height(menu_font)
#     text_width = len(menu_text) * helper_text_width(menu_font)
#
#     while not menu_close: # while False, pause continues
#
#         # get list of inputs
#         events_list = pygame.event.get()
#
#         # evaluate for each event
#         for event in events_list:
#
#             # if a key has been pressed
#             if event.event_type == pygame.KEYDOWN:
#
#                 # was it the 'p' key?
#                 if event.key == pygame.K_p:
#                     menu_close = True  # if yes, close the menu.
#
#         # Draw the pause message on the screen.
#         draw_text(SURFACE_MAIN, menu_text, constants.FONT_DEBUG_MESSAGE,
#             ((window_width / 2) - (text_width / 2), (window_height / 2) - (text_height / 2)),
#             constants.COLOR_WHITE, constants.COLOR_BLACK)
#
#         CLOCK.tick(constants.GAME_FPS)
#
#         # update the display surface
#         pygame.display.flip()
#
# def menu_inventory():
#
#     '''Opens up the inventory menu.
#
#     The inventory menu allows the player to examine whatever items they are
#     currently holding.  Selecting an item will drop it.
#
#     '''
#
#     # initialize to False, when True, the menu closes
#     menu_close = False
#
#     # Calculate window dimensions
#     window_width = constants.CAMERA_WIDTH
#     window_height = constants.CAMERA_HEIGHT
#
#     # Menu Characteristics
#     menu_width = 200
#     menu_height = 200
#     menu_x = (window_width / 2) - (menu_width / 2)
#     menu_y = (window_height / 2) - (menu_height / 2)
#
#     # Menu Text Characteristics
#     menu_text_font = constants.FONT_MESSAGE_TEXT
#     menu_text_color = constants.COLOR_WHITE
#
#     # Helper var
#     menu_text_height = helper_text_height(menu_text_font)
#
#     # create a new surface to draw on.
#     local_inventory_surface = pygame.Surface((menu_width, menu_height))
#
#     while not menu_close:
#
#         ## Clear the menu
#         local_inventory_surface.fill(constants.COLOR_BLACK)
#
#         # collect list of item names
#         print_list = [obj.display_name for obj in PLAYER.container.inventory]
#
#         ## Get list of input events
#         events_list = pygame.event.get()
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#
#         mouse_x_rel = mouse_x - menu_x
#         mouse_y_rel = mouse_y - menu_y
#
#         mouse_in_window = (mouse_x_rel > 0 and
#                            mouse_y_rel > 0 and
#                            mouse_x_rel < menu_width and
#                            mouse_y_rel < menu_height)
#
#         mouse_line_selection = mouse_y_rel / menu_text_height
#
#
#
#         # cycle through events
#         for event in events_list:
#             if event.event_type == pygame.KEYDOWN:
#                 # if player presses 'i' again, close menu
#                 if event.key == pygame.K_i:
#                     menu_close = True
#
#             if event.event_type == pygame.MOUSEBUTTONDOWN:
#
#                 if event.button == 1:
#
#                     if (mouse_in_window and
#                         mouse_line_selection <= len(print_list) - 1) :
#
#                         PLAYER.container.inventory[mouse_line_selection].item.use()
#                         menu_close = True
#
#
#         ## Draw the list
#         for line, (name) in enumerate(print_list):
#
#             if line == mouse_line_selection and mouse_in_window:
#                 draw_text(local_inventory_surface,
#                           name,
#                           menu_text_font,
#                           (0, 0 + (line * menu_text_height)),
#                           menu_text_color, constants.COLOR_GREY)
#             else:
#                 draw_text(local_inventory_surface,
#                           name,
#                           menu_text_font,
#                           (0, 0 + (line * menu_text_height)),
#                           menu_text_color)
#
#         # RENDER GAME #
#         draw_game()
#
#         ## Display Menu
#         SURFACE_MAIN.blit(local_inventory_surface, (menu_x, menu_y))
#
#
#         CLOCK.tick(constants.GAME_FPS)
#
#         # update the display surface
#         pygame.display.update()
