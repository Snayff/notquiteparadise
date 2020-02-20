from __future__ import annotations

import dataclasses
import json
import logging
import pygame
import pygame_gui
from pprint import pprint
from enum import Enum
from typing import TYPE_CHECKING, List, Dict
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIDropDownMenu, UILabel, UITextEntryLine, UIButton

from scripts.core.constants import EffectTypes, AfflictionTriggers
from scripts.core.extend_json import ExtendedJsonEncoder
from scripts.core.library import library
from scripts.managers.game_manager.game_manager import game
from scripts.skills.effect import EffectData

if TYPE_CHECKING:
    from typing import Any, Tuple

# TODO - there are no more Enums. Remove all refs and rebuild functionality.
# TODO - add None option to drop downs
# TODO - dropdown change isnt saving
# TODO - primary details not clearing on new category
# TODO - don't remove "_" from skill field - these are the skill keys
# TODO - don't clean "_" from keys
# TODO - add special case for "skills" field - get all keys from skills.json
# TODO - ability to add new


class DataEditor(UIWindow):
    """
    Dev tool to allow creating and editing data.
    """

    def __init__(self, rect, manager):
        element_ids = ["skill_editor"]

        super().__init__(rect, manager, element_ids=element_ids)

        # data holders
        self.all_data = None
        self.current_data_instance = None
        self.current_data_category = None
        self.field_options = None

        # data selectors
        self.category_selector: UIDropDownMenu = None
        self.instance_selector: UIDropDownMenu = None

        # dicts of data fields
        self.primary_data_fields: Dict[str, DataField] = {}
        self.secondary_data_fields: Dict[str, DataField] = {}

        # size info
        self.start_x = 2
        self.start_y = 2
        self.width = self.rect.width
        self.height = self.rect.height
        self.row_height = 25
        self.max_rows = self.height // self.row_height
        self.selectors_end_y = self.start_y + (self.row_height * 2)  # 2 is number of selectors

        self.primary_x = self.start_x
        self.primary_y = self.selectors_end_y
        self.primary_width = self.width // 2

        self.secondary_x = self.primary_x + self.primary_width
        self.secondary_y = self.selectors_end_y
        self.secondary_width = self.width - self.primary_width

        self.label_width_mod = 0.3  # decimal % of row width that label takes up

        self.max_y = self.height

        # get the data & field options
        self._load_library_data()
        self._load_field_options()

        # display the initial selector
        self.category_selector = self._create_data_category_selector()

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
        has_updated = False
        new_value = None
        data_field = None

        # new selection in instance_selector
        if ui_object_id == "category_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.category_selector.selected_option != self.current_data_category:
                    self.current_data_category = self.category_selector.selected_option

                    # clear existing details fields
                    self._kill_details_fields("primary")
                    self._kill_details_fields("secondary")

                    # clear existing instance selector
                    if self.instance_selector:
                        self.instance_selector.kill()
                        self.instance_selector = None

                    # create new instance selector
                    options = []
                    options.extend(key for key in self.all_data[self.current_data_category].keys())
                    options.sort()
                    self.instance_selector = self._create_data_instance_selector(options)

        # new selection in instance_selector
        if ui_object_id == "instance_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.instance_selector.selected_option != self.current_data_instance:
                    # clear existing details fields
                    self._kill_details_fields("primary")
                    self._kill_details_fields("secondary")

                    # create new
                    self.current_data_instance = self.instance_selector.selected_option
                    self._load_details("primary", self.current_data_instance)

        # new selection in a different, non-selector dropdown
        if ui_object_id != "instance_selector" and ui_object_id != "category_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                key = ui_object_id
                data_field = self.primary_data_fields[key]
                new_value = data_field.input_element.selected_option

                # check the value has changed
                if new_value != data_field.value:
                    has_updated = True

        # handle text field finished typing (triggers on enter press)
        if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            key = ui_object_id
            data_field = self.primary_data_fields[key]
            new_value = self.instance_selector.selected_option

            has_updated = True

        # handle triggers for secondary details
        prefix = "edit#"
        if ui_object_id[len(prefix):] == prefix:
            # TODO - clear secondary details
            # TODO - load secondary details
            pass

        # handle multiple choice to toggle the value
        prefix = "multi#"
        if ui_object_id[:len(prefix)] == prefix:
            # get the key
            prefix, key, object_id = ui_object_id.split("#")

            data_field = self.primary_data_fields[key]

            # get current value
            current_value: List = data_field.value
            id_as_value = data_field.options[object_id]

            if id_as_value in current_value:
                current_value.remove(id_as_value)
            else:
                current_value.append(id_as_value)

            new_value = current_value
            has_updated = True

        # process the update and reload
        # TODO - implement approach to determine if primary or secondary has changed
        if has_updated and new_value and data_field:
            self._save_updated_field("primary", data_field, new_value)

            # clear existing
            self._kill_details_fields("primary")

            # reload to reflect new changes
            self._load_details("primary", self.current_data_instance)

    ############## CREATE ################

    def _create_data_category_selector(self) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        # get options and sort alphabetically
        options = [keys for keys in self.all_data.keys()]
        options.sort()

        rect = pygame.Rect((self.start_x, self.start_y), (self.width, self.row_height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="category_selector")

    def _create_data_instance_selector(self, options: List[str]) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        rect = pygame.Rect((self.start_x, self.start_y + self.row_height), (self.width, self.row_height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="instance_selector")

    def _create_one_from_options_field(self, key, value, x, y, width, height, container,
            ui_manager) -> DataField:
        """
        Create a data field containing label, current value and a dropdown of possible options.
        """
        labels = []

        # get value name
        if value:
            value_name = value.name
        else:
            value_name = "None"

        # get list of enums names from the enum that contains the current value
        options = []
        options.extend(name.name for name in value.__class__.__members__.values())
        options.sort()

        # create the key label
        key_width = int(width * self.label_width_mod)
        key_rect = pygame.Rect((x, y), (key_width, height))
        key_label = UILabel(key_rect, key, ui_manager, container=container, parent_element=self)
        labels.append(key_label)

        # create the current values label
        value_width = width - key_width
        value_x = x + key_width
        value_rect = pygame.Rect((value_x, y), (value_width, height))
        value_label = UILabel(value_rect, value_name, ui_manager, container=container, parent_element=self)
        labels.append(value_label)

        # create the option's dropwdown, incremented by height
        input_rect = pygame.Rect((x, y + height), (width, height))
        input = UIDropDownMenu(options, value_name, input_rect, ui_manager, container=container,
                               parent_element=self, object_id=key)

        # create the data field
        data_field = DataField(key, value, value_name, Enum, labels, height*2, input_element=input, options=options)

        return data_field

    def _create_edit_detail_field(self, key, value, x, y, width, height, container, ui_manager) -> DataField:
        """
        Create a data field containing label, current values and a row of buttons for possible options. Buttons are
        prefixed with edit#
        """
        labels = []
        options = []
        values_list = []

        # Turn value into a list of strings
        options.extend(f"edit#{key}#{name}" for name in value)
        values_list.extend(name for name in value)

        # replace spaces with underscores as object_id doesnt like spaces
        values_list = [new_value.replace(" ", "_") for new_value in values_list]
        options = [new_value.replace(" ", "_") for new_value in options]

        # sort lists alphabetically
        options.sort()
        values_list.sort()

        # as its not an enum it needs to be able to create new items so add a new option at the start of the list
        options.insert(0, f"edit#{key}#New")

        # create the key label
        key_width = int(width * self.label_width_mod)
        key_rect = pygame.Rect((x, y), (key_width, height))
        key_label = UILabel(key_rect, key, ui_manager, container=container, parent_element=self)
        labels.append(key_label)

        # convert the list to a string
        values_str = ", ".join(values_list)
        values_str += ", "  # add comma to the end to help delimit when adding other values

        # create the current values label
        value_width = width - key_width
        value_x = x + key_width
        value_rect = pygame.Rect((value_x, y), (value_width, height))
        value_label = UILabel(value_rect, values_str, ui_manager, container=container, parent_element=self)
        labels.append(value_label)

        # determine how wide to make buttons
        button_width = width // len(options)

        # create the option's buttons, incremented by height
        buttons = self._create_row_of_buttons(options, x, y + height, button_width, height)

        # create the data field
        data_field = DataField(key, value, values_str, Dict, labels, height*2, buttons=buttons, options=options)

        return data_field

    def _create_multiple_from_options_field(self, key, value, x, y, width, height, container,
            ui_manager) -> DataField:
        """
        Create a data field containing label, current values and a row of buttons for possible options. Button's
        object_ids are prefixed with multi#
        """
        labels = []
        options = []
        values_list = []

        # get the first value to check if it is an enum
        _value = value[0]

        # Turn value into a list of strings; whether value is enum or strings
        if isinstance(_value, Enum):
            # add prefix and get other enum members
            options.extend(f"multi#{key}#{name.name}" for name in _value.__class__.__members__.values())
            values_list.extend(name.name for name in value)
        else:
            # as its not an enum it needs to be able to create new items so add a new option
            options = [f"multi#{key}#New"]
            options.extend(f"multi#{key}#{name}" for name in value)
            values_list.extend(name for name in value)

            # replace spaces with underscores as object_id doesnt like spaces
            values_list = [new_value.replace(" ", "_") for new_value in values_list]
            options = [new_value.replace(" ", "_") for new_value in options]

        # sort lists alphabetically
        options.sort()
        values_list.sort()
                
        # create the key label
        key_width = int(width * self.label_width_mod)
        key_rect = pygame.Rect((x, y), (key_width, height))
        key_label = UILabel(key_rect, key, ui_manager, container=container, parent_element=self)
        labels.append(key_label)
        
        # convert the list to a string
        values_str = ", ".join(values_list)
        values_str += ", "  # add comma to the end to help delimit when adding other values

        # create the current values label
        value_width = width - key_width
        value_x = x + key_width
        value_rect = pygame.Rect((value_x, y), (value_width, height))
        value_label = UILabel(value_rect, values_str, ui_manager, container=container, parent_element=self)
        labels.append(value_label)

        # determine how wide to make buttons
        button_width = width // len(options)
        
        # create the option's buttons, incremented by height
        buttons = self._create_row_of_buttons(options, x, y + height, button_width, height)
        
        # create the data field
        data_field = DataField(key, value, values_str, List, labels, height*2, buttons=buttons,
                               options=_value.__class__.__members__)

        return data_field

    def _create_text_entry_field(self, key, value, x, y, width, height, container, ui_manager) -> DataField:
        """
        Create a data field containing a text input widget.
        """
        # create the label
        label_width = int(width * self.label_width_mod)
        label_rect = pygame.Rect((x, y), (label_width, height))
        label = UILabel(label_rect, key, ui_manager, container=container, parent_element=self)

        # create the input
        input_width = width - label_width
        input_x = x + label_width
        input_rect = pygame.Rect((input_x, y), (input_width, height))
        input = UITextEntryLine(input_rect, ui_manager, container=container, parent_element=self, object_id=key)
        input.set_text(f"{value}")

        # create the data field
        data_field = DataField(key, value, str(value), str, [label], height, input_element=input)

        return data_field

    def _create_row_of_buttons(self, button_names: List[str], x: int, y: int, width: int, height: int) -> Dict[
        str, UIButton]:
        """
        Create a series of button UI widgets on the same x pos.
        """
        offset_x = 0
        container = self.get_container()
        buttons = {}

        for button_name in button_names:
            # split the prefix from the name
            try:
                prefix, key, name = button_name.split("#")
            except ValueError:
                # if no prefix
                name = button_name
                key = button_name

            # create the button
            button_rect = pygame.Rect((x + offset_x, y), (width, height))
            button = UIButton(button_rect, name, self.ui_manager, container=container,
                              parent_element=self, object_id=button_name)
            offset_x += width
            buttons[key + name] = button
            print(f"Created btn {key}:{button_name}")

        return buttons

    def _load_field_options(self) -> Dict[str, Tuple]:
        """
        Maps the various data keys to their related (options, dataclass). The dataclass is only provided if the key
        relates to sub-details that need adding. E.g. effects: (EffectTypes.__dict__.keys(), EffectData)
        """
        effect_options = game.Utility.get_class_members(EffectTypes)
        trigger_event_options = game.Utility.get_class_members(AfflictionTriggers)
        affliction_options = self.all_data["afflictions"].keys()

        key_options = {
            "effects": (effect_options, EffectData),
            "trigger_event": (trigger_event_options, None),
            "affliction_name": (affliction_options , None)
        }

        return key_options
    ############### LOAD ###################

    def _load_details(self, primary_or_secondary: str, data_instance: str):
        """
        Load details of the specified instance into the primary or secondary section
        """

        # get initial pos info
        if primary_or_secondary == "primary":
            start_x = self.primary_x
            start_y = self.primary_y
            row_width = self.primary_width
            self.primary_data_fields = []
        elif primary_or_secondary == "secondary":
            start_x = self.primary_x
            start_y = self.primary_y
            row_width = self.primary_width
            self.secondary_data_fields = []
        else:
            logging.warning("Wrong key passed to data_editor:_load_details. Using primary info.")
            start_x = self.primary_x
            start_y = self.primary_y
            row_width = self.primary_width
            self.primary_data_fields = []

        # get any info we can get ahead of time
        container = self.get_container()
        manager = self.ui_manager
        row_height = self.row_height
        current_y = start_y
        data_fields = {}

        # convert dataclass to dict to loop values
        if data_instance != "New":
            # get the existing data class
            data_dict = dataclasses.asdict(self.all_data[self.current_data_category][data_instance])
        else:
            # create a blank data class based on the data class of the 0th item in the current category
            first_item = next(iter(self.all_data[self.current_data_category].values()))
            data_dict = dataclasses.asdict(type(first_item))

        # create data fields
        for key, value in data_dict.items():
            try:
                # TODO - there are no more enums, find way to identify those that fit here.
                if isinstance(value, Enum):
                    data_field = self._create_one_from_options_field(key, value, start_x, current_y, row_width,
                                                                     row_height, container, manager)
                elif isinstance(value, List):
                    data_field = self._create_multiple_from_options_field(key, value, start_x, current_y,
                                                                          row_width, row_height, container, manager)
                elif isinstance(value, Dict):
                    data_field = self._create_edit_detail_field(key, value, start_x, current_y, row_width,
                                                                row_height, container, manager)
                else:
                    data_field = self._create_text_entry_field(key, value, start_x, current_y, row_width,
                                                               row_height, container, manager)

                # increment Y
                current_y += data_field.height + 1

                # save the data field
                data_fields[key] = data_field
            except ValueError:
                logging.warning(f"Error trying to create data field for {key}:{value}")

        # update the main record
        if primary_or_secondary == "primary":
            self.primary_data_fields = {}
            self.primary_data_fields = data_fields
        elif primary_or_secondary == "secondary":
            self.secondary_data_fields = {}
            self.secondary_data_fields = data_fields
        else:
            self.primary_data_fields = {}
            self.primary_data_fields = data_fields

        # take note of the highest used y, for the scroll bar
        self.max_y = max(current_y, self.max_y)

    def _load_library_data(self):
        """
        Load all of the data options into self.all_data
        """
        self.all_data = {
            "base_stats_primary": library.get_primary_stats_data(),
            "base_stats_secondary": library.get_secondary_stats_data(),
            "homelands": library.get_homelands_data(),
            "peoples": library.get_peoples_data(),
            "savvys": library.get_savvys_data(),
            "afflictions": library.get_afflictions_data(),
            "skills": library.get_skills_data(),
            "aspects": library.get_aspects_data(),
            "gods": library.get_gods_data()
        }

    ############## CLEAR #####################

    def cleanse(self):
        """
        Clear all held data.
        """
        if self.category_selector:
            self.category_selector.kill()
            self.category_selector = None
        if self.instance_selector:
            self.instance_selector.kill()
            self.instance_selector = None
        if self.primary_data_fields:
            self._kill_details_fields("primary")
            self.primary_data_fields = {}
        if self.secondary_data_fields:
            self._kill_details_fields("secondary")
            self.secondary_data_fields = {}

    def _kill_details_fields(self, primary_or_secondary: str):
        """
        Clear currently held details in the given dict of data fields.
        """
        if primary_or_secondary == "primary":
            data_fields = self.primary_data_fields
        elif primary_or_secondary == "secondary":
            data_fields = self.secondary_data_fields
        else:
            data_fields = self.primary_data_fields

        # clear the data fields
        for data_field in data_fields.values():
            data_field.kill()

        # clear the dict
        if primary_or_secondary == "primary":
            self.primary_data_fields = {}
        elif primary_or_secondary == "secondary":
            self.secondary_data_fields = {}
        else:
            self.primary_data_fields = {}

    ############ SAVING ##################

    def _save_updated_field(self, primary_or_secondary, data_field: DataField, updated_value: Any):
        """
        Save the updated value to the main dict held in self.all_data
        """
        # if primary then grab from 4th layer; all_data:category:instance:data_field
        if primary_or_secondary == "primary":
            # TODO - remove prints after confirming
            before = getattr(self.all_data[self.current_data_category][self.current_data_instance],
                             data_field.key)
            pprint(before)
            setattr(self.all_data[self.current_data_category][self.current_data_instance], data_field.key,
                    updated_value)
            after = getattr(self.all_data[self.current_data_category][self.current_data_instance], data_field.key)
            pprint(after)

            # save back to json
            with open(f"data/game/{self.current_data_category}.json", "w") as file:
                json.dump(self.all_data[self.current_data_category], file, sort_keys=True, indent=4,
                          cls=ExtendedJsonEncoder)


class DataField:
    """
    Holds a set of related data and ui elements
    """
    def __init__(self, key: str, value: Any, value_as_str: str, value_type, labels: List, height: int,
    input_element=None, buttons: Dict[str, UIButton] = None, options: List = None):
        self.key = key
        self.value = value
        self.value_as_str = value_as_str
        self.value_type = value_type
        self.options = options
        self.height = height

        # ui elements
        self.input_element = input_element
        self.labels = labels
        self.buttons = buttons

    def kill(self):
        """
        Kill all held ui elements
        """
        if self.input_element:
            self.input_element.kill()
            self.input_element = None

        if self.labels:
            for label in self.labels:
                label.kill()
            self.labels = None

        if self.buttons:
            for key, button in self.buttons.items():
                print(f"Killed btn {key}:{button.object_ids}")
                button.kill()
            self.buttons = None