from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional, Dict, Callable

import pygame_gui
import pygame
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UIPanel

from scripts.engine.core.constants import GAP_SIZE, LAYER_BASE_UI, MAX_SKILLS, SKILL_SIZE, EventType, InputIntent, InputIntentType


class SkillBar(UIPanel):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        # state info
        self.intents: List[InputIntentType] = [
            InputIntent.SKILL0,
            InputIntent.SKILL1,
            InputIntent.SKILL2,
            InputIntent.SKILL3,
            InputIntent.SKILL4
        ]
        self.skill_buttons: List[UIButton] = []

        self.start_x = 0
        self.start_y = 0

        # complete base class init
        super().__init__(rect, LAYER_BASE_UI, manager, element_id="skill_bar",
                         anchors={"left": "left",
                             "right": "right",
                             "top": "bottom",
                             "bottom": "bottom"})

        # show self
        self.show()

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
            if button in self.skill_buttons:
                slot_number = self.skill_buttons.index(button)
                # execute a skill clicked event
                event = pygame.event.Event(EventType.SKILL_BAR_CLICK, skill_intent=self.intents[slot_number])
                pygame.event.post(event)

                logging.debug(f"SkillBar button '{slot_number}' was pressed.")

    ############### ACTIONS #################

    def show(self):
        y = self.start_y
        manager = self.ui_manager

        for skill_slot in range(0, len(self.intents)):
            x = self.start_x + ((SKILL_SIZE + GAP_SIZE) * skill_slot)
            skill_button = UIButton(relative_rect=Rect((x, y), (SKILL_SIZE, SKILL_SIZE)), text=f"{skill_slot + 1}",
                             manager=manager, container=self.get_container(), object_id=f"#skill_button{skill_slot}")
            self.skill_buttons.append(skill_button)

