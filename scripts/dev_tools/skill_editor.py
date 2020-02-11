from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING
import pygame
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine, UIButton
from scripts.core.constants import VisualInfo, Directions, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes, \
    TargetTags, SkillShapes
from scripts.core.library import library
from scripts.skills.effect import EffectData
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

        # data holders
        self.all_skills = library.get_all_skill_data()
        self.current_skill = "None"
        self.skill_details_lowest_y = 0

        # ui widgets
        self.skill_selector = self.create_skill_selector()
        self.skill_details = None
        self.labels = None
        self.save_button = None

    def create_skill_selector(self) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        options = ["None", "New"]
        for skill in self.all_skills:
            options.append(skill)

        x = 2
        y = 2
        width = self.rect.width
        height = 30
        rect = pygame.Rect((x, y), (width, height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="skill_selector")

    def load_skill_details(self, skill_name: str):
        """
        Load skill details into self.skill_details. For population of the fields.

        Args:
            skill_name ():
        """
        self.skill_details = {}
        self.labels = {}
        num = 0
        dropdowns = {
            "terrain_collision": SkillTerrainCollisions,
            "travel_type": SkillTravelTypes,
            "expiry_type": SkillExpiryTypes,
            "shape": SkillShapes
        }

        # get required skill details
        if skill_name != "New":
            # convert to dict to loop values
            skill_data = dataclasses.asdict(self.all_skills[skill_name])
        else:
            skill_data = dataclasses.asdict(SkillData())

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

            # handle different field requirements
            if key in dropdowns:
                options_list = []
                options_list.extend(option.name for option in dropdowns[key])
                value_input = UIDropDownMenu(options_list, f"{value.name}", value_rect, self.ui_manager,
                                             container=self.get_container(), parent_element=self, object_id=key)
            elif key == "effects":
                # TODO - break out effects
                #  Why not just pull that out into a separate UIWindow?
                #  Have effects be a list you can add effects to, and each effect is a button that opens a new
                #  UIWindow to edit that specific effect

                # create button for each effect
                # ? label showing each active effect
                # press button opens the effect's fields (new method) on the side

                pass
            elif key == "icon":
                # TODO - file picker
                pass
            else:
                # everything else uses a single line text entry
                value_input = UITextEntryLine(value_rect, self.ui_manager, container=self.get_container(),
                                              parent_element=self, object_id=key)
                value_input.set_text(f"{value}")

            # increment y
            offset_y += height

            # save refs to the ui widgets
            num += 1
            self.labels[f"label{num}"] = key_label
            self.skill_details[key] = value_input

        # save last used Y pos for other widgets to refer to
        self.skill_details_lowest_y = offset_y

    def clear_skill_details(self):
        """
        Clear currently held skill details from self.skill_details.
        """
        skill_details = self.skill_details
        labels = self.labels

        for value in skill_details.values():
            value.kill()

        for value in labels.values():
            value.kill()

        self.skill_details = None
        self.labels = None

    def create_save_button(self) -> UIButton:
        """
        Create the save button to allow saving of the changes.

        Returns:

        """
        # FIXME - save button can only be clicked on left side
        x = 2
        y = self.skill_details_lowest_y + 1
        width = self.rect.width
        height = 30
        rect = pygame.Rect((x, y), (width, height))

        return UIButton(rect, "Save", self.ui_manager, container=self.get_container(), parent_element=self,
                        object_id="skill_editor_save")

    def clear_save_button(self):
        """
        Remove the save button and all references to it.
        """
        if self.save_button:
            self.save_button.kill()
            self.save_button = None

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.

        Args:
            time_delta ():
        """
        super().update(time_delta)

        # check if new skill selected
        if self.skill_selector.selected_option != self.current_skill:
            self.current_skill = self.skill_selector.selected_option

            if self.current_skill != "None":
                self.load_skill_details(self.current_skill)
                self.save_button = self.create_save_button()
            else:
                self.clear_skill_details()
                self.clear_save_button()

    def cleanse(self):
        """
        Clear all held data.
        """
        if self.skill_selector:
            self.skill_selector.kill()
            self.skill_selector = None
        if self.skill_details:
            self.clear_skill_details()

    def save(self):
        """
        Save the edited skill back to the json.
        """
        edited_name = self.skill_details["name"].text

        # determine dict key for the skill
        if self.current_skill == "New":
            skill_key = edited_name
        else:
            skill_key = self.current_skill

        # extract values to a dict
        edited_skill = {}
        for key, value in self.skill_details.items():
            edited_skill[key] = value.text

        # TODO - need to rebuild effects as EffectData

        # unpack the dict to SkillData
        skill_data = SkillData(**edited_skill)

        # save the edited skill back to all skills
        self.all_skills[skill_key] = skill_data

        # save all skills back to the json
        # TODO - save data back to json
        pass
