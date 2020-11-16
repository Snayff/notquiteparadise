from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pygame
import pygame_gui
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UIPanel

from scripts.engine.core.constants import GAP_SIZE, InputEvent, InputIntent, RenderLayer, SKILL_BUTTON_SIZE

if TYPE_CHECKING:
    from typing import List


class SkillBar(UIPanel):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        self.button_events = {
            "skill_0": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL0),
            "skill_1": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL1),
            "skill_2": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL2),
            "skill_3": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL3),
            "skill_4": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL4),
            "skill_5": pygame.event.Event(InputEvent.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL5),
        }

        self.buttons: List[UIButton] = []

        self.button_start_x = GAP_SIZE
        self.button_start_y = GAP_SIZE
        self.button_width = SKILL_BUTTON_SIZE
        self.button_height = SKILL_BUTTON_SIZE
        self.space_between_buttons = GAP_SIZE

        # complete base class init
        super().__init__(
            rect,
            RenderLayer.UI_BASE,
            manager,
            object_id="skill_bar",
            anchors={"left": "left", "right": "right", "top": "bottom", "bottom": "bottom"},
        )

        self._init_buttons()

        # confirm init complete
        logging.debug(f"SkillBar initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

            # Find out which button we are clicking
            button = event.ui_element

            # post the new event
            if button in self.buttons:
                # get the id
                ids = event.ui_object_id.split(".")
                button_id = ids[-1]  # get last element
                new_event = self.button_events[button_id]
                pygame.event.post(new_event)

                logging.debug(f"SkillBar button '{ids}' was pressed.")

    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        # extract values for performance
        start_x = self.button_start_x
        y = self.button_start_y
        info = self.button_events
        width = self.button_width
        height = self.button_height
        gap = self.space_between_buttons
        manager = self.ui_manager

        count = 0
        for name in info.keys():
            x = start_x + ((width + gap) * count)

            button = UIButton(
                relative_rect=Rect((x, y), (width, height)),
                text=f"{count + 1}",
                manager=manager,
                container=self,
                object_id=f"{name}",
            )

            self.buttons.append(button)

            count += 1
