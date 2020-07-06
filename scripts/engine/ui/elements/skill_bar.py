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

from scripts.engine.core.constants import GAP_SIZE, LAYER_BASE_UI, MAX_SKILLS, SKILL_SIZE


class SkillBar(UIPanel):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        # state info
        self.actions: Dict[int, Callable] = {}
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
        pass

    ############### GET / SET ################

    def set_actions(self, actions: Dict[int, Callable]):
        """
        Set a list of actions to get executed for each button in the skill bar slot
        """
        self.actions = actions

    ############### ACTIONS #################

    def show(self):
        y = self.start_y
        manager = self.ui_manager

        for skill_slot in range(0, MAX_SKILLS):
            x = self.start_x + ((SKILL_SIZE + GAP_SIZE) * skill_slot)
            skill_button = UIButton(relative_rect=Rect((x, y), (SKILL_SIZE, SKILL_SIZE)), text=f"{skill_slot + 1}",
                             manager=manager, container=self.get_container(), object_id=f"#skill_button{skill_slot}")
            self.skill_buttons.append(skill_button)


