
import json

from scripts.core.constants import LoggingEventTypes, TargetTypes, TargetTags, SkillEffectTypes, PrimaryStatTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.event_hub import publisher


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world.
    """

    def __init__(self):
        self.skills = {}
        self.homeland = {}
        self.race = {}
        self.savvy = {}
        self.general = {}
        self.affliction = {}
        self.aspect = {}
        self.terrain = {}
        self.actor_template = {}

        self.load_data_into_library()
        self.convert_strings_to_enums()

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"Data Library initialised."))

    def load_data_into_library(self):
        """
        Load data from all external jsons to this central data library
        """
        import os
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self.skills = self.get_values_from_skill_json()
            self.homeland = self.get_values_from_homeland_json()
            self.race = self.get_values_from_race_json()
            self.savvy = self.get_values_from_savvy_json()
            self.affliction = self.get_values_from_affliction_json()
            self.aspect = self.get_values_from_aspect_json()
            self.terrain = self.get_values_from_terrain_json()
            self.actor_template = self.get_values_from_actor_json()

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"Data Library refreshed."))

    def convert_strings_to_enums(self):
        # Update skills
        # Skills:TargetTags
        self.change_value_of_key_if_value_matches(self.skills, "required_tags", "other_entity",
                                                  TargetTags.OTHER_ENTITY)
        self.change_value_of_key_if_value_matches(self.skills, "required_tags", "no_entity",
                                                  TargetTags.NO_ENTITY)
        self.change_value_of_key_if_value_matches(self.skills, "required_tags", "floor",
                                                  TargetTags.FLOOR)
        self.change_value_of_key_if_value_matches(self.skills, "required_tags", "wall",
                                                  TargetTags.WALL)
        self.change_value_of_key_if_value_matches(self.skills, "required_tags", "self",
                                                  TargetTags.SELF)

        # Skills:SkillEffects:Name
        self.change_value_of_key_if_value_matches(self.skills, "name", "damage", SkillEffectTypes.DAMAGE)
        self.change_value_of_key_if_value_matches(self.skills, "name", "apply_affliction",
                                                  SkillEffectTypes.APPLY_AFFLICTION)
        self.change_value_of_key_if_value_matches(self.skills, "name", "move",
                                                  SkillEffectTypes.MOVE)
        self.change_value_of_key_if_value_matches(self.skills, "name", "change_terrain",
                                                  SkillEffectTypes.CHANGE_TERRAIN)

        # Skills:SkillEffects:Name
        self.change_value_of_key_if_value_matches(self.skills, "stat_to_target", "bustle",
                                                  PrimaryStatTypes.BUSTLE)





    def change_value_of_key_if_value_matches(self, dict_to_look_in, key_to_look_for, value_to_check, new_value):
        for k, v in dict_to_look_in.items():
            if isinstance(v, dict):
                self.change_value_of_key_if_value_matches(v, key_to_look_for, value_to_check, new_value)
            if k == key_to_look_for:
                value_for_key = dict_to_look_in[k]
                print(f"compared {value_for_key} to {value_to_check}")
                if value_for_key == value_to_check:
                    dict_to_look_in[k] = new_value


    
    def get_terrain_data(self, terrain_name):
        """
        Get data for a terrains from the central library

        Args:
            terrain_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(terrain_name, self.terrain[terrain_name])
        data = named_tuple(**self.terrain[terrain_name])

        return data
    
    def get_actor_template_data(self, actor_template_name):
        """
        Get data for a actor_templates from the central library

        Args:
            actor_template_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(actor_template_name, self.actor_template[actor_template_name])
        data = named_tuple(**self.actor_template[actor_template_name])

        return data
    
    def get_aspect_data(self, aspect_name):
        """
        Get data for a aspects from the central library

        Args:
            aspect_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(aspect_name, self.aspect[aspect_name])
        data = named_tuple(**self.aspect[aspect_name])

        return data
    
    def get_affliction_data(self, affliction_name):
        """
        Get data for a afflictions from the central library

        Args:
            affliction_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(affliction_name, self.affliction[affliction_name])
        data = named_tuple(**self.affliction[affliction_name])

        return data

    def get_savvy_data(self, savvy_name):
        """
        Get data for a savvy from the central library

        Args:
            savvy_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(savvy_name, self.savvy[savvy_name])
        data = named_tuple(**self.savvy[savvy_name])

        return data

    def get_race_data(self, race_name):
        """
        Get data for a race from the central library

        Args:
            race_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(race_name, self.race[race_name])
        data = named_tuple(**self.race[race_name])

        return data
    
    def get_homeland_data(self, homeland_name):
        """
        Get data for a homeland from the central library

        Args:
            homeland_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(homeland_name, self.homeland[homeland_name])
        data = named_tuple(**self.homeland[homeland_name])

        return data

    def get_skill_data(self, skill_tree, skill_name):
        """
        Get data for a skill from the central library

        Args:
            skill_tree (str):
            skill_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(skill_name, list(self.skills[skill_tree][skill_name]))
        data = named_tuple(**self.skills[skill_tree][skill_name])

        return data

    @staticmethod
    def get_values_from_skill_json():
        """

        Returns:

        """
        # TODO - create rules to confirm every tree has a basic attack
        with open('data/game/skills/skill_trees.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_affliction_json():
        """

        Returns:

        """
        with open('data/game/skills/afflictions.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_aspect_json():
        """

        Returns:

        """
        with open('data/game/world/aspect.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_terrain_json():
        """

        Returns:

        """
        with open('data/game/world/terrain.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_homeland_json():
        """

        Returns:

        """
        with open('data/game/entity/homeland.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_savvy_json():
        """

        Returns:

        """
        with open('data/game/entity/savvy.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_race_json():
        """

        Returns:

        """
        with open('data/game/entity/race.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_values_from_actor_json():
        """

        Returns:

        """

        with open('data/game/entity/actor_template.json') as file:
            data = json.load(file)

        return data
