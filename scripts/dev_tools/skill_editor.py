from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING
import pygame
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine
from scripts.core.constants import VisualInfo
from scripts.core.library import library
from scripts.skills.skill import SkillData

if TYPE_CHECKING:
    pass


class SkillEditor(UIWindow):
    """
    Dev tool to allow creating and editing skills.
    """
    def __init__(self, rect, manager):
        element_ids = ["skill_editor"]

        super().__init__(rect, manager, element_ids=element_ids)

        self.all_skills = library.get_all_skill_data()
        self.current_skill = "None"
        self.skill_selector = self.create_skill_selector()
        self.skill_details = None

    def create_skill_selector(self):
        options = ["None"]
        for skill in self.all_skills:
            options.append(skill)

        x = 2
        y = 2
        width = self.rect.width
        height = 30
        rect = pygame.Rect((x, y), (width, height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                                       parent_element=self, object_id="skill_selector")

    def reload_skill_details(self, skill_name: str):
        self.skill_details = {}
        num = 0

        # convert to dict to loop values
        skill_data = dataclasses.asdict(self.all_skills[skill_name])

        # set rect sizes
        start_y = 33
        height = 30
        key_x = 2
        key_width = self.rect.width / 4
        value_width = self.rect.width - key_width
        value_x = key_x + key_width
        offset_y = 0

        # create labels and input fields
        for key, value in skill_data.items():
            key_rect = pygame.Rect((key_x, start_y + offset_y), (key_width, height))
            key_label = UILabel(key_rect, key, self.ui_manager, container=self.get_container(), parent_element=self)

            value_rect = pygame.Rect((value_x, start_y + offset_y), (value_width, height))
            value_input = UITextEntryLine(value_rect, self.ui_manager, container=self.get_container(),
                                          parent_element=self, object_id=f"{key}")
            value_input.set_text(f"{value}")

            # increment y
            offset_y += height

            # save refs to the ui widgets
            num += 1
            self.skill_details[f"label{num}"] = key_label
            self.skill_details[f"{key}"] = value_input

    def clear_skill_details(self):
        skill_details = self.skill_details

        for key, value in skill_details.items():
            value.kill()

        self.skill_details = {}

    def update(self, time_delta: float):
        super().update(time_delta)

        # check if new skill selected
        if self.skill_selector.selected_option != self.current_skill:
            self.current_skill = self.skill_selector.selected_option

            if self.current_skill != "None":
                self.reload_skill_details(self.current_skill)
            else:
                self.clear_skill_details()
