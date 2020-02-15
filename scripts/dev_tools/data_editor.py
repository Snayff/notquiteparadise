from __future__ import annotations

import dataclasses
import logging
from enum import Enum
from typing import TYPE_CHECKING, Type, Iterable, List, Dict, Union
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

                    # remove existing instance selector
                    if self.instance_selector:
                        self.instance_selector.kill()
                        self.instance_selector = None

                    # create new instance selector
                    options = ["New"]
                    # FIXME - basestats is StatData and doesnt have keys. How to handle that layer of
                    #  primary/secondary?
                    options.extend(key for key in self.data_options[self.current_data_category].keys())
                    options.sort()
                    self.instance_selector = self.create_data_instance_selector(options)

                    # remove primary details
                    self.clear_primary_details()

        # new selection in instance_selector
        if ui_object_id == "instance_selector":
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.instance_selector.selected_option != self.current_data_instance:
                    self.current_data_instance = self.instance_selector.selected_option
                    self.load_primary_details(self.current_data_instance)

        # saving primary
        if ui_object_id == "primary_save":
            self.save_primary_details()
            library.refresh_library_data()

        # saving secondary
        if ui_object_id == "secondary_save":
            # TODO - save secondary details
            # TODO - reload primary details
            pass

        # handle triggers for secondary details
        prefix = "secondary#"
        if ui_object_id[len(prefix):] == prefix:
            # TODO - clear secondary details
            # TODO - load secondary details
            pass

        # handle multiple choice
        prefix = "multi#"
        if ui_object_id[:len(prefix)] == prefix:
            # get the key
            prefix, key, object_id = ui_object_id.split("#")

            # toggle value
            current_text = self.primary_details[key].text
            if ", " + object_id + ", " in current_text:
                self.primary_details[key].set_text(current_text.replace(f", {object_id}, ", ", "))
            elif object_id + ", " == current_text[:len(object_id + ", ")]:
                self.primary_details[key].set_text(current_text[len(object_id + ", "):])
            else:
                self.primary_details[key].set_text(current_text + object_id + ", ")

    ############## CREATE ################

    def create_data_category_selector(self) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        # get options and sort alphabetically
        options = [keys for keys in self.data_options.keys()]
        options.sort()

        rect = pygame.Rect((self.start_x, self.start_y), (self.width, self.row_height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="category_selector")

    def create_data_instance_selector(self, options: List[str]) -> UIDropDownMenu:
        """
        Create the skill selector drop down menu
        """
        rect = pygame.Rect((self.start_x, self.start_y + self.row_height), (self.width, self.row_height))

        return UIDropDownMenu(options, "None", rect, self.ui_manager, container=self.get_container(),
                              parent_element=self, object_id="instance_selector")

    def create_row_of_buttons(self, button_names: List[str], x: int, y: int, width: int, height: int) -> Dict[
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
            buttons[key] = button

        return buttons

    def create_text_entry(self, rect: pygame.Rect, object_id: str, initial_text: str) -> UITextEntryLine:
        """
        Create an input field  UI widget.
        """
        text_entry = UITextEntryLine(rect, self.ui_manager, container=self.get_container(), parent_element=self,
                                     object_id=object_id)
        text_entry.set_text(f"{initial_text}")

        return text_entry

    def create_multiple_choice(self, button_names: List[str], label_id: str, label_value: List[str], row_x: int,
            label_x: int, y: int, value_width: int, row_width: int, container: UIContainer) -> Tuple[Dict[str,
    UILabel], Dict[str, UIButton]]:
        """
        Create a label row and a subsequent row of buttons.
        """

        # TODO - uncomment when using dropdowns for secondary and replace button_names with this
        # names = []
        # names.extend("multi#" + name for name in button_names)

        # determine how wide to made buttons
        button_width = row_width // len(button_names)

        # ensure there is a value to use as a label
        if not label_value:
            current_value = "None"
        else:
            current_value = ", ".join(label_value)
            current_value += ", "  # add comma to the end to help delimit when adding other values

        # create rect
        row_height = self.row_height
        rect = pygame.Rect((label_x, y), (value_width, row_height))

        # create a label showing each active element
        value_input = {}
        value_input[label_id] = UILabel(rect, current_value, self.ui_manager, container=container,
                              parent_element=self, object_id=label_id)

        # create the buttons
        buttons = self.create_row_of_buttons(button_names, row_x, y + row_height, button_width, row_height)

        return value_input, buttons

    def create_secondary_selector(self, starting_option: str, options_list: List[str], label_id: str, label_value:
    List[str], row_x: int, label_x: int, y: int, row_width: int, button_width: int, container: UIContainer) -> Tuple[
        Dict[str, Union[UILabel, UIDropDownMenu]], Dict[str, UIButton]]:
        """"
        Create a dropdown of options, a label containing the specified values and a button to load selected option 
        into secondary details
        """
        # ensure there is a value to use as a label
        if not label_value:
            current_value = "None"
        else:
            current_value = ", ".join(label_value)

            # create label rect
            row_height = self.row_height
            rect = pygame.Rect((label_x, y), (row_width, row_height))

            # create a label showing each active element
            value_input = {}
            value_input[label_id] = UILabel(rect, current_value, self.ui_manager, container=container,
                                  parent_element=self, object_id=label_id)

            # create dropdown rect
            dropdown_width = row_width - button_width
            rect = pygame.Rect((row_x, y + row_height), (dropdown_width, row_height))

            # create a dropdown for possible options
            value_input["dropdown#" + label_id] = UIDropDownMenu(options_list, starting_option, rect,
                                                                 self.ui_manager, container=container,
                                                                 parent_element=self, object_id=label_id)

            # create button rect
            rect = pygame.Rect((row_x + dropdown_width, y + row_height), (button_width, row_height))

            # create a button to move to secondary details
            tooltip = "Press to open selected item in secondary details."
            button = {}
            button[label_id] = UIButton(rect, "->", self.ui_manager, container=container, tool_tip_text=tooltip,
                              parent_element=self, object_id=f"secondary#{label_id}")

            return value_input, button

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
        key_width = row_width // 4
        value_width = row_width - key_width
        value_x = key_x + key_width
        current_y = start_y
        secondary_select_button_width = 20

        # get any info we can get ahead of time
        container = self.get_container()
        manager = self.ui_manager

        # convert dataclass to dict to loop values
        if data_instance != "New":
            # get the existing data class
            data_dict = dataclasses.asdict(self.data_options[self.current_data_category][data_instance])
        else:
            # create a blank data class based on the data class of the 0th item in the current category
            first_item = next(iter(self.data_options[self.current_data_category].values()))
            data_dict = dataclasses.asdict(type(first_item))

        # create labels and input fields
        for key, value in data_dict.items():
            # reset value input and buttons
            value_input = {}
            buttons = {}

            # create standard elements
            key_rect = pygame.Rect((key_x, current_y), (key_width, row_height))
            key_label = UILabel(key_rect, key, manager, container=container, parent_element=self)
            value_rect = pygame.Rect((value_x, current_y), (value_width, row_height))

            # anything that is a dict or list at the next level down needs to be treated individually
            # effects have another layer
            if key == "effects":
                # get list of effect names for options
                options = []
                options.extend(f"secondary#{key}#{name.name}" for name in EffectTypes)
                options.sort()

                # get current effects
                current = []
                current.extend(current_effect for current_effect in value)
                current.sort()

                # TODO - use this when drop downs can be sized
                # value_input, buttons = self.create_secondary_selector(options[0], options, key, current, start_x,
                #                                                       key_x, current_y, row_width,
                #                                                       secondary_select_button_width, container)

                # TODO - remove when  moving to dropdowns
                value_input, buttons = self.create_multiple_choice(options, key, current, start_x, value_x,
                                                                   current_y, value_width, row_width, container)

                # multiple choice takes 2 lines so increment y
                current_y += row_height

            # interactions have another layer
            elif key == "interactions":
                # get list of current interactions and add new
                options = [f"secondary#{key}#New"]
                # TODO - remove the string prefix when changing to dropdowns
                options.extend(f"secondary#{key}#{current_interaction}" for current_interaction in value.keys())
                options.sort()

                # get current effects
                current = []
                current.extend(current_interaction for current_interaction in value)
                current.sort()

                # TODO - use this when drop downs can be sized
                # value_input, buttons = self.create_secondary_selector(options[0], options, key, current, start_x,
                #                                                       key_x, current_y, row_width,
                #                                                       secondary_select_button_width, container)

                # TODO - remove when  moving to dropdowns
                value_input, buttons = self.create_multiple_choice(options, key, current, start_x, value_x,
                                                                   current_y, value_width,  row_width, container)

                # multiple choice takes 2 lines so increment y
                current_y += row_height

            # icon needs a file picker so doesnt follow normal rules
            elif key == "icon":
                # TODO - change to file picker
                value_input[key] = self.create_text_entry(value_rect, key, value)

            # check if it is a list or dict
            elif isinstance(value, List) or isinstance(value, Dict):
                names = []
                cleaned_values = []

                # get the first value for the enum checking
                if isinstance(value, List):
                    _value = value[0]
                else:
                    # must be a dict
                    _value = next(iter(value.values()))

                # Turn value into a list of strings and handle value being an enum
                if isinstance(_value, Enum):
                    names.extend(f"multi#{key}#{name.name}" for name in _value.__class__.__members__.values())
                    cleaned_values.extend(name.name for name in value)
                else:
                    # as its not an enum it needs to be able to create new items
                    names = [f"multi#{key}#New"]
                    names.extend(f"multi#{key}#{name}" for name in value)
                    cleaned_values.extend(name for name in value)

                    # replace spaces with underscores as object_id doesnt like spaces
                    cleaned_values = [new_value.replace(" ", "_") for new_value in cleaned_values]
                    names = [new_value.replace(" ", "_") for new_value in names]

                # sort lists alphabetically
                names.sort()
                cleaned_values.sort()

                # create
                value_input, buttons = self.create_multiple_choice(names, key, cleaned_values, start_x, value_x,
                                                                   current_y, value_width, row_width, container)

                # multiple choice takes 2 lines so increment y
                current_y += row_height

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
                options.sort()

                # create drop down
                value_input[key] = UIDropDownMenu(options, value_name, value_rect, manager, container=container,
                                             parent_element=self, object_id=key)

            # handle everything else as a single line of text
            else:
                value_input[key] = self.create_text_entry(value_rect, key, value)

            # increment current_y
            current_y += row_height

            # save refs to the ui widgets
            self.primary_labels[key] = key_label
            self.primary_details = {**self.primary_details,  **value_input}
            self.primary_buttons = {**self.primary_buttons, **buttons}

        # create save button and add to
        buttons = self.create_row_of_buttons(["primary_save"], start_x, current_y, row_width,
                                         row_height)
        self.primary_buttons = {**self.primary_buttons, **buttons}

    def load_secondary_details(self, effect_type: EffectTypes):
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

    def clear_primary_details(self):
        """
        Clear currently held primary details from self.primary_details.
        """
        skill_details = self.primary_details
        labels = self.primary_labels
        buttons = self.primary_buttons

        if skill_details:
            for value in skill_details.values():
                if value:
                    value.kill()

        if labels:
            for value in labels.values():
                value.kill()

        if buttons:
            for button in buttons.values():
                button.kill()

        self.primary_details = None
        self.primary_labels = None
        self.primary_buttons = None

    def clear_secondary_details(self):
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
        if self.primary_details:
            self.clear_primary_details()
        if self.secondary_details:
            self.clear_secondary_details()

    ############ SAVING ##################

    def save_primary_details(self):
        """
        Save the edited skill back to the json.
        """
        # TODO - rewrite for primary
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

    def save_secondary_details(self):
        """
        Save the current effect details to the current skill.
        """
        # TODO - rewrite from secondary
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

