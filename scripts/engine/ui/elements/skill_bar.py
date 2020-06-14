from __future__ import annotations

import logging
from typing import List, Optional
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIPanel, UIWindow, UIButton

from scripts.engine.core.constants import GAP_SIZE, ICON_SIZE, LAYER_BASE_UI, MAX_SKILLS, SKILL_SIZE


class SkillBar(UIPanel):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        # state info
        self.skills: List[Optional[str]] = []
        # TODO - should be a list of individual skill buttons.
        #  skill"slots" are part of the entity, not this.
        #  use skill name as the identifier
        self.start_x = 0
        self.start_y = 0

        # init skill list
        for skill_slot in range(0, MAX_SKILLS):
            self.skills += [None]

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

    def set_skill(self, slot_number, skill):
        """
        Set skill in the skill bar slot
        """
        self.skills[slot_number] = skill

    ############### ACTIONS #################

    def show(self):
        y = self.start_y
        manager = self.ui_manager

        for skill_slot in range(0, MAX_SKILLS):
            x = self.start_x + ((SKILL_SIZE + GAP_SIZE) * skill_slot)
            skill = UIButton(relative_rect=Rect((x, y), (SKILL_SIZE, SKILL_SIZE)), text=f"{skill_slot + 1}",
                             manager=manager, container=self.get_container(), object_id=f"#skill_button{skill_slot}")


