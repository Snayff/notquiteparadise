import logging  # type: ignore
from typing import List

import pygame  # type: ignore
import pygame_gui  # type: ignore
from pygame_gui.core import UIWindow  # type: ignore


class SkillBar(UIWindow):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager):
        # state info
        self.skills: List[str] = []
        self.max_skills = 5

        # init skill list
        for skill_slot in range(0, self.max_skills):
            self.skills += [None]

        # complete base class init
        super().__init__(rect, manager, ["skill_bar"])

        # create skill primary_buttons
        start_x = 5
        start_y = 5
        width = 64
        height = 64
        gap = 2

        for skill_slot in range(0, self.max_skills):
            x = start_x
            y = start_y + (height * skill_slot) + (gap * skill_slot)
            skill = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (width, height)),
                                                 text=f"{skill_slot}",  manager=manager,
                                                 container=self.get_container(),
                                                 object_id=f"#skill_button{skill_slot}")

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

    def set_skill(self, slot_number, skill):
        """
        Set skill in the skill bar slot

        Args:
            slot_number ():
            skill ():
        """
        self.skills[slot_number] = skill



