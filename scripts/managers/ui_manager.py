import logging
import pygame
import pygame_gui
from scripts.core.constants import VisualInfo
from scripts.ui.basic.fonts import Font
from scripts.managers.ui_methods.display_methods import DisplayMethods
from scripts.managers.ui_methods.element_methods import ElementMethods
from scripts.managers.ui_methods.mouse_methods import MouseMethods
from scripts.ui.basic.palette import Palette


class UIManager:
    """
    Manage the UI, such as windows, resource bars etc

    Attributes:
        main_surface (pygame.surface): The main surface to render to
    """

    def __init__(self):
        self.Display = DisplayMethods(self)
        self.Element = ElementMethods(self)
        self.Mouse = MouseMethods(self)
        self.Palette = Palette()  # doesnt need self as only holds data
        self.Font = Font()  # doesnt need self as only holds data
        self.Gui = pygame_gui.UIManager((VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT),
                                        "data/ui/themes.json")

        logging.info(f"UIManager initialised.")

    def update(self, delta_time: float):
        """
        Update all ui elements
        """
        # self.Element.update_elements()
        self.Gui.update(delta_time)

    def process_events(self, event):
        """
        Process input events

        Args:
            event ():
        """
        self.Gui.process_events(event)

    def draw(self):
        """
        Draw the UI.
        """
        main_surface = self.Display.get_main_surface()

        # clear previous frame
        main_surface.fill((0, 0, 0))

        self.Gui.draw_ui(main_surface)

        # resize the surface to the desired resolution
        scaled_surface = pygame.transform.scale(main_surface, self.Display.get_desired_resolution())
        window = self.Display.get_window()
        window.blit(scaled_surface, (0, 0))

        # update the display
        pygame.display.flip()  # make sure to do this as the last drawing element in a frame


ui = UIManager()
