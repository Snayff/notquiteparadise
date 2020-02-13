from __future__ import annotations

import dataclasses
import logging
from enum import Enum
from typing import TYPE_CHECKING, Type, Iterable, List, Dict
import pygame
import pygame_gui
from pygame_gui.core import UIWindow, UIContainer
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine, UIButton
from scripts.core.constants import VisualInfo, Directions, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes, \
    TargetTags, SkillShapes, EffectTypes, PrimaryStatTypes, DamageTypes
from scripts.core.library import library
from scripts.skills.effect import EffectData
from scripts.skills.skill import SkillData

if TYPE_CHECKING:
    from typing import Any, Tuple


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

        # data holders
        self.data_options = None
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
        self.primary_buttons = None
        self.secondary_buttons = None

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

        # get the data options
        self.load_data_options()

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
                    options = [key for key in self.data_options[self.current_data_category].keys()]
                    self.instance_selector = self.create_data_instance_selector(options)

        # new selection in instance_selector
        if ui_object_id == "instance_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.instance_selector.selected_option != self.current_data_instance:
                    self.current_data_instance = self.instance_selector.selected_option
                    self.load_primary_details(self.current_data_instance)

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
        options = [keys for keys in self.data_options.keys()]
        rect = pygame.Rect((self.start_x, self.start_y), (self.width, self.row_height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="category_selector")

    def create_data_instance_selector(self, options: List[str]) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        rect = pygame.Rect((self.start_x, self.start_y + self.row_height), (self.width, self.row_height))

        return UIDropDownMenu(options, "New", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="instance_selector")

    def create_row_of_buttons(self, button_names: List[str], x: int, y: int, width: int, height: int) -> Dict[
        str, UIButton]:
        """
        Create a series of button UI widgets on the same x pos.
        """
        offset_x = 0
        container = self.get_container()
        buttons = {}

        for name in button_names:
            button_rect = pygame.Rect((x + offset_x, y), (width, height))
            button = UIButton(button_rect, name, self.ui_manager, container=container,
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

    def load_primary_details(self, data_instance: str):
        """
        Load the primary details fields based on the data instance
        """
        # clear existing info
        self.primary_details = {}
        self.primary_buttons = {}
        self.primary_labels = {}

        # set rect sizes
        row_width = self.primary_width
        row_height = self.row_height
        start_x = self.start_x
        start_y = self.selectors_end_y
        key_x = start_x
        key_width = row_width / 4
        value_width = row_width - key_width
        value_x = key_x + key_width
        current_y = start_y

        # get any info we can get ahead of time
        container = self.get_container()
        manager = self.ui_manager

        # convert dataclass to dict to loop values
        if data_instance != "New":
            # get the existing data class
            data_dict = dataclasses.asdict(self.data_options[self.current_data_category][data_instance])
        else:
            # create a blank data class based on the data class of the 0th item in the current category
            data_dict = dataclasses.asdict(type(self.data_options[self.current_data_category][0]))

        # create labels and input fields
        for key, value in data_dict.items():
            # reset value input and buttons
            value_input = None
            buttons = {}

            # create standard elements
            key_rect = pygame.Rect((key_x, current_y), (key_width, row_height))
            key_label = UILabel(key_rect, key, manager, container=container, parent_element=self)
            value_rect = pygame.Rect((value_x, current_y), (value_width, row_height))

            # pull effects out as they follow their own rules
            if key == "effects":
                # get list of effect names for options
                options = []
                options.extend("secondary#" + name.name for name in EffectTypes)

                # get current effects
                effects = []
                effects.extend(effect for effect in value)

                value_input, buttons = self.create_multiple_choice(options, key, effects, start_x, current_y,
                                                                   row_width, container)

            elif key == "icon":
                # TODO - change to file picker
                value_input = self.create_text_entry(value_rect, key, value)

            # check if it is a list or dict
            elif isinstance(value, List) or isinstance(value, Dict):
                names = []
                cleaned_values = []

                # Turn value into a list of strings and handle value being an enum
                if isinstance(value[0], Enum):
                    names.extend("multi#" + name.name for name in value)
                    cleaned_values.extend(name.name for name in value)
                else:
                    names.extend("multi#" + name for name in value)
                    cleaned_values.extend(name for name in value)

                value_input, buttons = self.create_multiple_choice(names, key, cleaned_values, start_x, current_y,
                                                                   row_width, container)

            # check if it is an enum
            elif isinstance(value, Enum):
                # get value name
                if value:
                    value_name = value.name
                else:
                    value_name = "None"

                # get list of enums names from the enum that contains the current value
                options = []
                options.extend(name.name for name in value.__class__.__members__.values())

                # create drop down
                value_input = UIDropDownMenu(options, value_name, value_rect, manager, container=container,
                                             parent_element=self, object_id=key)

            # handle everything else as a single line of text
            else:
                value_input = self.create_text_entry(value_rect, key, value)

            # increment current_y
            current_y += row_height

            # save refs to the ui widgets
            self.primary_labels[key] = key_label
            self.primary_details[key] = value_input
            self.primary_buttons = {**self.primary_buttons, **buttons}

        # create save button and add to
        buttons = self.create_row_of_buttons(["skill_editor_save"], start_x, current_y, row_width,
                                         row_height)
        self.primary_buttons = {**self.primary_buttons, **buttons}

    def create_multiple_choice(self, button_names: List[str], label_id: str, label_value: List[str],  x: int, y: int,
            row_width: int, container: UIContainer) -> Tuple[UILabel, Dict[str, UIButton]]:
        """
        Create a label row and a subsequent row of buttons.
        """

        # determine how wide to made buttons
        button_width = row_width // len(button_names)

        # ensure there is a value to use as a label
        if not label_value:
            current_value = "None"
        else:
            current_value = ", ".join(label_value)

        # create rect
        row_height = self.row_height
        rect = pygame.Rect((x, y), (row_width, row_height))

        # create a label showing each active effect
        value_input = UILabel(rect, current_value, self.ui_manager, container=container,
                              parent_element=self, object_id=label_id)

        # create the buttons
        buttons = self.create_row_of_buttons(button_names, x, y + row_height, button_width, row_height)

        return value_input, buttons

    def load_skill_details(self, skill_name: str):
        """
        Load skill details into self.primary_details. Create required input fields.
        """
        # clear existing info
        self.primary_details = {}
        self.primary_buttons = {}
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
            self.primary_buttons = {**self.primary_buttons, **buttons}

        # create save button
        buttons = self.create_row_of_buttons(["skill_editor_save"], start_x, start_y + offset_y, skill_details_width,
                                             height)
        self.primary_buttons = {**self.primary_buttons, **buttons}

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
        self.primary_buttons = {**self.primary_buttons, **buttons}

    def load_data_options(self):
        """
        Load all of the data options into self.data_options
        """
        self.data_options = {
            "base_stats": library.get_stat_data(),
            "homelands": library.get_homelands_data(),
            "races": library.get_races_data(),
            "savvys": library.get_savvys_data(),
            "afflictions": library.get_afflictions_data(),
            "skills": library.get_skills_data(),
            "aspects": library.get_aspects_data(),
            "gods": library.get_gods_data()
        }

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
        if self.primary_buttons:
            for button in self.primary_buttons.values():
                button.kill()
            self.primary_buttons = None

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
        if self.primary_buttons:
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

    ############ UTILITY ################

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

