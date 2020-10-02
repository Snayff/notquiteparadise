from __future__ import annotations
from typing import TYPE_CHECKING, Type


from pygame_gui.elements import UIButton, UIPanel

from scripts.engine import library
from scripts.engine.core.constants import RenderLayer

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List
    from pygame import Rect
    from pygame_gui import UIManager


class TitleScreen(UIPanel):
    """
    Initial screen menu
    """
    
    def __init__(self, rect: Rect, manager: UIManager):

        self.buttons_info = ["new game", "load game", "exit game"]

        width = rect.width
        height = rect.height
        self.button_start_x = int((width / 2) - (width / 5))
        self.button_start_y = int(height / 4)
        self.button_height = int(height / 8)
        self.button_width = int(width / 4)
        self.space_between_buttons = int(((height - self.button_start_y) / len(self.buttons_info)) - \
                                     self.button_height)


        self.buttons: List[UIButton] = []

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="title_screen")


    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        x = self.button_start_x
        start_y = self.button_start_y
        info = self.buttons_info
        width = self.button_width
        height = self.button_height
        gap = self.space_between_buttons
        manager = self.ui_manager

        for count in range(0, len(info)):
            y = start_y + ((height + gap) * count)
            name = info[count]

            button = UIButton(
                relative_rect=Rect((x, y), (width, height)),
                text=name,
                manager=manager,
                container=self.get_container(),
                object_id=f"title_screen#{name}",
            )

            self.buttons.append(button)


