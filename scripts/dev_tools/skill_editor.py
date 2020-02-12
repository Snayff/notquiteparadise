from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING, List, Dict
import pygame
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine, UIButton
from scripts.core.constants import VisualInfo, Directions, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes, \
    TargetTags, SkillShapes, EffectTypes, PrimaryStatTypes, DamageTypes
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

        # ui widgets
        self.skill_selector = None
        self.skill_details = None
        self.effect_details = None
        self.labels = None
        self.buttons = None

        # display the widgets
        self.skill_selector = self.create_skill_selector()
        self.current_skill = self.skill_selector.selected_option
        self.load_skill_details(self.current_skill)

    def create_skill_selector(self) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        options = ["New"]
        for skill in self.all_skills:
            options.append(skill)

        x = 2
        y = 2
        width = self.rect.width
        height = 30
        rect = pygame.Rect((x, y), (width, height))

        return UIDropDownMenu(options, "New", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="skill_selector")

    def load_skill_details(self, skill_name: str):
        """
        Load skill details into self.skill_details. Create required input fields.

        Args:
            skill_name ():
        """
        # clear existing info
        self.skill_details = {}
        self.buttons = {}
        self.labels = {}

        # set the keys that need drop downs
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
        skill_details_width = self.rect.width / 2
        start_x = 0
        start_y = 33
        height = 30
        key_x = start_x
        key_width = skill_details_width / 4
        value_width = skill_details_width - key_width
        value_x = key_x + key_width
        offset_y = 0

        # create labels and input fields
        for key, value in skill_data.items():
            # reset value input
            value_input = None
            buttons = {}

            # create standard elements
            key_rect = pygame.Rect((key_x, start_y + offset_y), (key_width, height))
            key_label = UILabel(key_rect, key, self.ui_manager, container=self.get_container(), parent_element=self)
            value_rect = pygame.Rect((value_x, start_y + offset_y), (value_width, height))

            # handle different field requirements
            if key in dropdowns:
                options_list = []
                options_list.extend(option.name for option in dropdowns[key])

                # ensure there is a value
                if value:
                    value_name = value.name
                else:
                    value_name = "None"

                # create drop down
                value_input = UIDropDownMenu(options_list, value_name, value_rect, self.ui_manager,
                                             container=self.get_container(), parent_element=self, object_id=key)
            elif key == "effects":
                button_width = int(skill_details_width / len(EffectTypes))

                # ensure there is a value to use as a label
                if value:
                    active_effects = []
                    active_effects.extend(effect for effect in value)
                else:
                    active_effects = "None"

                # create a label showing each active effect
                value_input = UILabel(value_rect, str(active_effects).strip("[]"), self.ui_manager,
                                      container=self.get_container(), parent_element=self, object_id=key)

                # increment y
                offset_y += height

                # create button for each effect
                effects = []
                effects.extend(effect.name for effect in EffectTypes)
                buttons = self.create_row_of_buttons(effects, key_x, start_y + offset_y, button_width, height)

            elif key == "icon":
                # TODO - file picker
                pass
            else:
                # everything else uses a single line text entry
                value_input = self.create_text_entry(value_rect, key, value)

            # increment y
            offset_y += height

            # save refs to the ui widgets
            self.labels[key] = key_label
            self.skill_details[key] = value_input
            self.buttons = {**self.buttons, **buttons}

        # create save button
        buttons = self.create_row_of_buttons(["skill_editor_save"], start_x, start_y + offset_y, skill_details_width,
                                             height)
        self.buttons = {**self.buttons, **buttons}

    def load_effect_details(self, effect_type: EffectTypes):
        """
        Load effect details into self.effect_details. Create required input fields.

        Args:
            effect_type ():
        """
        # clear existing info
        self.effect_details = {}

        # set the keys that need drop downs
        dropdowns = {
            "mod_stat": PrimaryStatTypes,
            "damage_type": DamageTypes,
            "stat_to_target": PrimaryStatTypes,
            "stat_to_affect": PrimaryStatTypes
        }

        # get required effect details
        if self.current_skill != "New":
            current_effect = self.all_skills[self.current_skill].effects[effect_type.name]
        else:
            current_effect = None

        if current_effect:
            # convert to dict to loop values
            effect_data = dataclasses.asdict(current_effect)
        else:
            effect_data = dataclasses.asdict(EffectData(effect_type))

        # set rect sizes
        effect_details_width = self.rect.width / 2
        start_x = effect_details_width
        start_y = 33
        height = 30
        key_x = start_x
        key_width = effect_details_width / 4
        value_width = effect_details_width - key_width
        value_x = key_x + key_width
        offset_y = 0

        # create labels and input fields
        for key, value in effect_data.items():

            # create standard elements
            key_rect = pygame.Rect((key_x, start_y + offset_y), (key_width, height))
            key_label = UILabel(key_rect, key, self.ui_manager, container=self.get_container(), parent_element=self)
            value_rect = pygame.Rect((value_x, start_y + offset_y), (value_width, height))

            # handle different field requirements
            if key in dropdowns:
                options_list = []
                options_list.extend(option.name for option in dropdowns[key])

                # ensure there is a value
                if value:
                    value_name = value.name
                else:
                    value_name = "None"

                # create drop down
                value_input = UIDropDownMenu(options_list, value_name, value_rect, self.ui_manager,
                                             container=self.get_container(), parent_element=self, object_id=key)
            else:
                # everything else uses a single line text entry
                value_input = self.create_text_entry(value_rect, key, value)

            # increment y
            offset_y += height

            # save refs to the ui widgets
            self.labels[key] = key_label
            self.effect_details[key] = value_input

        # create save button
        buttons = self.create_row_of_buttons(["effect_editor_save"], start_x, start_y + offset_y,
                                             effect_details_width, height)
        self.buttons = {**self.buttons, **buttons}

    def create_row_of_buttons(self, button_names: List[str], x: int, y: int, width: int, height: int) -> Dict:
        offset_x = 0
        buttons = {}

        for name in button_names:
            button_rect = pygame.Rect((x + offset_x, y), (width, height))
            button = UIButton(button_rect, name, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id=name)
            offset_x += width
            buttons[name] = button

        return buttons

    def create_text_entry(self, rect: pygame.Rect, object_id: str, initial_text: str) -> UITextEntryLine:
        text_entry = UITextEntryLine(rect, self.ui_manager, container=self.get_container(), parent_element=self,
                                     object_id=object_id)
        text_entry.set_text(f"{initial_text}")

        return text_entry

    def clear_skill_details(self):
        """
        Clear currently held skill details from self.skill_details.
        """
        skill_details = self.skill_details
        labels = self.labels

        for value in skill_details.values():
            if value:
                value.kill()

        for value in labels.values():
            value.kill()

        self.skill_details = None
        self.labels = None

    def clear_save_button(self):
        """
        Remove the save button and all references to it.
        """
        if self.buttons:
            for button in self.buttons:
                button.kill()
            self.buttons = None

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.

        Args:
            time_delta ():
        """
        super().update(time_delta)

        # check if new skill selected and then reload details
        if self.skill_selector.selected_option != self.current_skill:
            self.current_skill = self.skill_selector.selected_option
            self.load_skill_details(self.current_skill)


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
