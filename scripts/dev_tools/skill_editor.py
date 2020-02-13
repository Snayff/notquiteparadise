from __future__ import annotations

import dataclasses
import logging
from enum import Enum
from typing import TYPE_CHECKING, Type
import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine, UIButton
from scripts.core.constants import VisualInfo, Directions, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes, \
    TargetTags, SkillShapes, EffectTypes, PrimaryStatTypes, DamageTypes
from scripts.core.library import library
from scripts.skills.effect import EffectData
from scripts.skills.skill import SkillData

if TYPE_CHECKING:
    from typing import List, Dict, Iterable, Any


# TODO - expand to be a general data editor
# TODO - add None option to drop downs
# TODO - limit selections based on context. e.g. move effect doesnt have affliction name.


class DataEditor(UIWindow):
    """
    Dev tool to allow creating and editing data.
    """

    def __init__(self, rect, manager):
        element_ids = ["skill_editor"]

        super().__init__(rect, manager, element_ids=element_ids)

        # data options
        self.category_options = {
            "base_stats" : library.get_stat_data(),
            "homelands": library.get_homelands_data(),
            "races": library.get_races_data(),
            "savvys": library.get_savvys_data(),
            "afflictions": library.get_afflictions_data(),
            "skills": library.get_skills_data(),
            "aspects": library.get_aspects_data(),
            "gods": library.get_gods_data()
        }

        # data holders
        self.all_skills = library.get_skills_data()
        self.current_data_instance = None
        self.current_data_category = None
        self.current_held_data = None

        # ui widgets
        self.category_selector = None
        self.instance_selector = None
        self.primary_details = None
        self.secondary_details = None
        self.primary_labels = None
        self.secondary_labels = None
        self.buttons = None

        # size info
        self.start_x = 2
        self.start_y = 2
        self.width = self.rect.width
        self.height = self.rect.height
        self.row_height = 30
        self.max_rows = self.height // self.row_height
        self.selectors_end_y = self.start_y + (self.row_height * 2)  # 2 is number of selectors
        self.primary_width = self.width / 2
        self.secondary_width = self.width - self.primary_width

        # display the initial selector
        self.category_selector = self.create_data_category_selector()

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        ui_object_id = event.ui_object_id

        # new selection in instance_selector
        if ui_object_id == "category_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.category_selector.selected_option != self.current_data_category:
                    self.current_data_category = self.category_selector.selected_option
                    self.instance_selector = self.create_data_instance_selector()

        # new selection in instance_selector
        if ui_object_id == "instance_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.instance_selector.selected_option != self.current_data_instance:
                    self.current_data_instance = self.instance_selector.selected_option
                    self.load_skill_details(self.current_data_instance)

        # TODO - update below to primary/secondary
        # saving a skill
        if ui_object_id == "skill_editor_save":
            self.save_skill_details()
            library.refresh_library_data()

        # editing a skill's effect
        if ui_object_id in EffectTypes._member_names_:
            self.clear_effect_details()
            self.load_effect_details(EffectTypes[ui_object_id])

        # saving an effect
        if ui_object_id == "effect_editor_save":
            self.save_effect_details()
            self.load_skill_details(self.current_data_instance)



    ############## CREATE ################

    def create_data_category_selector(self):
        """
        Create the skill selector drop down menu
        """


        rect = pygame.Rect((self.start_x, self.start_y), (self.width, self.height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="category_selector")

    def create_data_instance_selector(self, options: List[str]) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        options = ["New"]
        for skill in self.all_skills:
            options.append(skill)

        rect = pygame.Rect((self.start_x, self.start_y + self.row_height), (self.width, self.height))

        return UIDropDownMenu(options, "New", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="instance_selector")

    def create_row_of_buttons(self, button_names: Iterable[str], x: int, y: int, width: int, height: int) -> Dict[
        str, UIButton]:
        """
        Create a series of button UI widgets on the same x pos.
        """
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
        """
        Create an input field  UI widget.
        """
        text_entry = UITextEntryLine(rect, self.ui_manager, container=self.get_container(), parent_element=self,
                                     object_id=object_id)
        text_entry.set_text(f"{initial_text}")

        return text_entry

    ############### LOAD ###################

    def load_skill_details(self, skill_name: str):
        """
        Load skill details into self.primary_details. Create required input fields.
        """
        # clear existing info
        self.primary_details = {}
        self.buttons = {}
        self.primary_labels = {}

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
                button_width = skill_details_width // len(EffectTypes)

                # ensure there is a value to use as a label
                if value:
                    active_effects = []
                    active_effects.extend(effect for effect in value)
                else:
                    active_effects = "None"

                # create a label showing each active effect
                value_input = UILabel(value_rect, ", ".join(active_effects), self.ui_manager,
                                      container=self.get_container(), parent_element=self, object_id=key)

                # increment y
                offset_y += height

                # create button for each effect
                effects = []
                effects.extend(effect.name for effect in EffectTypes)
                buttons = self.create_row_of_buttons(effects, key_x, start_y + offset_y, button_width, height)
            elif key == "target_directions":
                # TODO - create dict of listed items to handle all
                # convert the list to a string separated by commas
                directions = ", ".join(direction.name for direction in value)
                value_input = self.create_text_entry(value_rect, key, directions)
            elif key == "required_tags":
                # convert the list to a string separated by commas
                tags = ", ".join(tag.name for tag in value)
                value_input = self.create_text_entry(value_rect, key, tags)

            elif key == "icon":
                # TODO - change to file picker
                value_input = self.create_text_entry(value_rect, key, value)
            else:
                # everything else uses a single line text entry
                if isinstance(value, Enum):
                    value_input = self.create_text_entry(value_rect, key, value.name)
                else:
                    value_input = self.create_text_entry(value_rect, key, value)

            # increment y
            offset_y += height

            # save refs to the ui widgets
            self.primary_labels[key] = key_label
            self.primary_details[key] = value_input
            self.buttons = {**self.buttons, **buttons}

        # create save button
        buttons = self.create_row_of_buttons(["skill_editor_save"], start_x, start_y + offset_y, skill_details_width,
                                             height)
        self.buttons = {**self.buttons, **buttons}

    def load_effect_details(self, effect_type: EffectTypes):
        """
        Load effect details into self.secondary_details. Create required input fields.
        """
        # clear existing info
        self.secondary_details = {}
        self.secondary_labels = {}

        # set the keys that need drop downs
        dropdowns = {
            "mod_stat": PrimaryStatTypes,
            "damage_type": DamageTypes,
            "stat_to_target": PrimaryStatTypes,
            "stat_to_affect": PrimaryStatTypes
        }

        # get required effect details
        if self.current_data_instance != "New":
            try:
                current_effect = self.all_skills[self.current_data_instance].effects[effect_type.name]
            except KeyError:
                current_effect = None
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

            elif key == "effect_type":
                # just a label because it cant be amended
                value_input = UILabel(value_rect, value.name, self.ui_manager, container=self.get_container(),
                                      parent_element=self)
            elif key == "required_tags":
                tags = []
                tags.extend(tag.name for tag in value)
                clean_tags = ", ".join(tags)
                value_input = self.create_text_entry(value_rect, key, clean_tags)
            else:
                # everything else uses a single line text entry
                if isinstance(value, Enum):
                    value_input = self.create_text_entry(value_rect, key, value.name)
                else:
                    value_input = self.create_text_entry(value_rect, key, value)

            # increment y
            offset_y += height

            # save refs to the ui widgets
            self.secondary_labels[key] = key_label
            self.secondary_details[key] = value_input

        # create save button
        buttons = self.create_row_of_buttons(["effect_editor_save"], start_x, start_y + offset_y,
                                             effect_details_width, height)
        self.buttons = {**self.buttons, **buttons}

    ############## CLEAR #####################

    def clear_skill_details(self):
        """
        Clear currently held skill details from self.primary_details.
        """
        skill_details = self.primary_details
        labels = self.primary_labels

        if skill_details:
            for value in skill_details.values():
                if value:
                    value.kill()

        if labels:
            for value in labels.values():
                value.kill()

        self.primary_details = None
        self.primary_labels = None

    def clear_effect_details(self):
        """
        Clear currently held effect details from self.secondary_details.
        """
        effect_details = self.secondary_details
        labels = self.secondary_labels

        if effect_details:
            for value in effect_details.values():
                if value:
                    value.kill()

        if labels:
            for value in labels.values():
                value.kill()

        self.secondary_details = None
        self.secondary_labels = None

    def clear_buttons(self):
        """
        Remove the save button and all references to it.
        """
        if self.buttons:
            for button in self.buttons.values():
                button.kill()
            self.buttons = None

    def cleanse(self):
        """
        Clear all held data.
        """
        if self.instance_selector:
            self.instance_selector.kill()
            self.instance_selector = None
        if self.primary_details:
            self.clear_skill_details()
        if self.secondary_details:
            self.clear_effect_details()
        if self.buttons:
            self.clear_buttons()

    ############ SAVING ##################

    def save_skill_details(self):
        """
        Save the edited skill back to the json.
        """
        edited_name = self.primary_details["name"].text

        # map the classes to their keys
        enums = {
            "terrain_collision": SkillTerrainCollisions,
            "travel_type": SkillTravelTypes,
            "expiry_type": SkillExpiryTypes,
            "shape": SkillShapes
        }
        listed_enums = {
            "target_directions": Directions,
            "required_tags": TargetTags
        }

        # determine dict key for the skill
        if self.current_data_instance == "New":
            skill_key = edited_name
        else:
            skill_key = self.current_data_instance

        # extract values to a dict
        edited_skill = {}
        for key, value in self.primary_details.items():
            # get the required value
            if isinstance(value, UIDropDownMenu):
                value = value.selected_option
            else:
                value = value.text

            # handle the different keys
            edited_skill[key] = self.convert_value_to_required_type(key, value, enums, listed_enums)

        # unpack the dict to SkillData
        skill_data = SkillData(**edited_skill)

        # save the edited skill back to all skills
        self.all_skills[skill_key] = skill_data

        # save all skills back to the json
        # TODO - save data back to json
        pass

    def save_effect_details(self):
        """
        Save the current effect details to the current skill.
        """
        enums = {
            "mod_stat": PrimaryStatTypes,
            "damage_type": DamageTypes,
            "stat_to_target": PrimaryStatTypes,
            "stat_to_affect": PrimaryStatTypes
        }

        listed_enums = {
            "required_tags": TargetTags
        }

        edited_effect = {}

        # loop all input fields and add the data to a single dict
        for key, value in self.secondary_details.items():
            if isinstance(value, UIDropDownMenu):
                value = value.selected_option
            else:
                value = value.text

            # handle the different keys
            edited_effect[key] = self.convert_value_to_required_type(key, value, enums, listed_enums)

        # convert to data class
        effect_data = EffectData(**edited_effect)

        # update data
        self.all_skills[self.current_data_instance].effects[effect_data.effect_type] = effect_data

    def convert_value_to_required_type(self, key: str, initial_value: Any, enums: Dict[str, Type[Enum]],
            listed_enums: Dict[str, Type[Enum]]) -> Any:
        """
        Use key and initial value to determine the required type and convert the type to that value 
        """
        # handle the different keys
        if key == "effects":
            # effects updated directly via effect save so get the info
            value = self.all_skills[self.current_data_instance].effects
        elif key in listed_enums:
            # split the string by comma and add to list, removing whitespace to allow matching to enum's name
            value = [listed_enums[key][string.strip()] for string in initial_value.split(",")]
        elif key in enums:
            value = enums[key][initial_value]
        else:
            # if value doesnt map to an enum try and convert to number if poss
            try:
                value = int(initial_value)
            except ValueError:
                value = initial_value

        return value
