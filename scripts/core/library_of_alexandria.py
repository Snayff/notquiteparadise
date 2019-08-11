
import json

from scripts.components.race_dataclass import RaceData
from scripts.core.constants import LoggingEventTypes, TargetTags, EffectTypes, PrimaryStatTypes, \
    AfflictionCategory, AfflictionTriggers, DamageTypes, StatTypes, SecondaryStatTypes, SkillShapes
from scripts.entity.stat_dataclasses import PrimaryStatData, SecondaryStatData, StatData
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.event_hub import publisher
from scripts.skills.affliction_dataclasses import AfflictionData
from scripts.skills.skill_dataclasses import EffectData, SkillData, SkillTreeData
from scripts.world.aspect_dataclass import AspectData


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world.
    """

    def __init__(self):
        # TODO - add conversion to data class for remaining dicts
        self.skills = {}  # conversion done
        self.homelands = {}
        self.races = {}  # conversion done
        self.savvys = {}
        self.afflictions = {}  # conversion done
        self.aspects = {}  # conversion done
        self.terrains = {}
        self.actor_template = {}
        self.stats = {}  # conversion done

        self.refresh_library_data()

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"Data Library initialised."))

    def convert_skills_to_data_classes(self):
        """
        Take skill data from library and convert to data classes 
        """
        all_skill_data = self.skills
        converted_data = {}

        # loop all skill trees
        for skill_tree_name, skill_tree_data in all_skill_data.items():
            converted_skills = {}

            # loop all skills in each skill tree
            for skill_name, skill_data in skill_tree_data.items():
                converted_skill_effects = {}

                # loop skill effects in each skill
                for index, skill_effect_data in enumerate(skill_data["effects"]):
                    # convert the skill effect data to the data class
                    skill_effect = EffectData(**skill_effect_data)
                    converted_skill_effects[skill_effect.effect_type.name] = skill_effect

                # set the temp dict to contain the converted skill effects
                new_skill_dict = skill_data.copy()
                new_skill_dict["effects"] = converted_skill_effects

                # unpack the temp dict and convert the skill data to the data class
                skill = SkillData(**new_skill_dict)
                converted_skills[skill.name] = skill

            # convert to the data class
            converted_skill_tree = SkillTreeData(name=skill_tree_name, skill=converted_skills)

            # set the dict to contain the converted skills
            converted_data[converted_skill_tree.name] = converted_skill_tree

        # delete all info from skill and replace with the converted data
        self.skills = {}
        self.skills = converted_data

    def convert_afflictions_to_data_classes(self):
        """
        Take affliction data from library and convert to data classes
        """
        all_afflictions_data = self.afflictions
        converted_afflictions = {}

        # loop all skill trees
        for affliction_name, affliction_data in all_afflictions_data.items():
            converted_effects = {}

            # loop skill effects in each skill
            for index, effect_data in enumerate(affliction_data["effects"]):
                # convert the skill effect data to the data class
                effect = EffectData(**effect_data)
                converted_effects[effect.effect_type.name] = effect

            # set the temp dict to contain the converted skill effects
            new_affliction_dict = affliction_data.copy()
            new_affliction_dict["effects"] = converted_effects

            # unpack the temp dict and convert the afflictions data to the data class
            affliction = AfflictionData(**new_affliction_dict)
            converted_afflictions[affliction.name] = affliction

        # delete all info from afflictions and replace with the converted data
        self.afflictions = {}
        self.afflictions = converted_afflictions

    def convert_aspects_to_data_classes(self):
        """
        Take aspect data from library and convert to data classes
        """
        all_aspect_data = self.aspects
        converted_aspects = {}

        # loop all skill trees
        for aspect_name, aspect_data in all_aspect_data.items():
            converted_effects = {}

            # loop skill effects in each skill
            for index, effect_data in enumerate(aspect_data["effects"]):
                # convert the skill effect data to the data class
                effect = EffectData(**effect_data)
                converted_effects[effect.effect_type.name] = effect

            # set the temp dict to contain the converted skill effects
            new_aspect_dict = aspect_data.copy()
            new_aspect_dict["effects"] = converted_effects

            # unpack the temp dict and convert the aspect data to the data class
            aspect = AspectData(**new_aspect_dict)
            converted_aspects[aspect.name] = aspect

        # delete all info from aspect and replace with the converted data
        self.aspects = {}
        self.aspects = converted_aspects

    def convert_races_to_data_classes(self):
        """
        Take race data from library and convert to data classes
        """
        all_race_data = self.races
        converted_races = {}

        # loop all skill trees
        for race_name, race_data in all_race_data.items():

            # unpack the dict and convert the data to the data class
            race = RaceData(**race_data)
            converted_races[race.name] = race

        # delete all info from races and replace with the converted data
        self.races = {}
        self.races = converted_races

    def convert_stats_to_data_classes(self):
        """
        Take skill data from library and convert to data classes
        """
        all_stat_data = self.stats
        converted_primary_stats = {}
        converted_secondary_stats = {}

        # loop all skill trees
        for stat_type_name, stat_type_data in all_stat_data.items():

            # loop all skills in each skill tree
            for stat_name, stat_data in stat_type_data.items():

                # unpack the dict and convert the stat data to the data class
                if stat_type_name == "primary":
                    stat = PrimaryStatData(**stat_data)
                    converted_primary_stats[stat.primary_stat_type.name] = stat

                elif stat_type_name == "secondary":
                    stat = SecondaryStatData(**stat_data)
                    converted_secondary_stats[stat.secondary_stat_type.name] = stat

        # delete all info from skill and replace with the converted data
        converted_data = StatData(primary=converted_primary_stats, secondary=converted_secondary_stats)
        self.stats = {}
        self.stats = converted_data

    def convert_external_strings_to_internal_enums(self):
        """
        Where there are external values that are utilised internally convert them to the internal constant.
        """
        # Update shared values
        lists_to_convert = [self.aspects, self.skills, self.afflictions]
        
        for current_list in lists_to_convert:
            # Effects:required_tags
            self.recursive_replace(current_list, "required_tags", "other_entity", TargetTags.OTHER_ENTITY)
            self.recursive_replace(current_list, "required_tags", "no_entity", TargetTags.NO_ENTITY)
            self.recursive_replace(current_list, "required_tags", "floor", TargetTags.FLOOR)
            self.recursive_replace(current_list, "required_tags", "wall", TargetTags.WALL)
            self.recursive_replace(current_list, "required_tags", "self", TargetTags.SELF)

            # Effects:name
            self.recursive_replace(current_list, "effect_type", "damage", EffectTypes.DAMAGE)
            self.recursive_replace(current_list, "effect_type", "apply_affliction", EffectTypes.APPLY_AFFLICTION)
            self.recursive_replace(current_list, "effect_type", "move", EffectTypes.MOVE)
            self.recursive_replace(current_list, "effect_type", "change_terrain", EffectTypes.CHANGE_TERRAIN)
            self.recursive_replace(current_list, "effect_type", "affect_stat", EffectTypes.AFFECT_STAT)

            # Effects:damage_type
            self.recursive_replace(current_list, "damage_type", "pierce", DamageTypes.PIERCE)
            self.recursive_replace(current_list, "damage_type", "blunt", DamageTypes.BLUNT)
            self.recursive_replace(current_list, "damage_type", "elemental", DamageTypes.ELEMENTAL)

            # Effects:stat_to_target
            self.recursive_replace(current_list, "stat_to_target", "bustle", PrimaryStatTypes.BUSTLE)
            self.recursive_replace(current_list, "stat_to_target", "vigour", PrimaryStatTypes.VIGOUR)
            self.recursive_replace(current_list, "stat_to_target", "clout", PrimaryStatTypes.CLOUT)
            self.recursive_replace(current_list, "stat_to_target", "skullduggery", PrimaryStatTypes.SKULLDUGGERY)
            self.recursive_replace(current_list, "stat_to_target", "exactitude", PrimaryStatTypes.EXACTITUDE)

            # Effects:new_terrain
            self.recursive_replace(current_list, "new_terrain", "floor", TargetTags.FLOOR)
            self.recursive_replace(current_list, "new_terrain", "wall", TargetTags.WALL)
       
        # Update Afflictions
        # Affliction:category
        self.recursive_replace(self.afflictions, "category", "bane", AfflictionCategory.BANE)
        self.recursive_replace(self.afflictions, "category", "boon", AfflictionCategory.BOON)

        # Affliction:trigger_event
        self.recursive_replace(self.afflictions, "trigger_event", "end_turn", AfflictionTriggers.END_TURN)
        self.recursive_replace(self.afflictions, "trigger_event", "passive", AfflictionTriggers.PASSIVE)
        self.recursive_replace(self.afflictions, "trigger_event", "move", AfflictionTriggers.MOVE)
        self.recursive_replace(self.afflictions, "trigger_event", "deal_damage", AfflictionTriggers.DEAL_DAMAGE)
        self.recursive_replace(self.afflictions, "trigger_event", "end_round", AfflictionTriggers.END_ROUND)
        self.recursive_replace(self.afflictions, "trigger_event", "action", AfflictionTriggers.ACTION)

        # Update Stats
        # Stat:Primary:primary_stat_type
        self.recursive_replace(self.stats, "primary_stat_type", "bustle", PrimaryStatTypes.BUSTLE)
        self.recursive_replace(self.stats, "primary_stat_type", "vigour", PrimaryStatTypes.VIGOUR)
        self.recursive_replace(self.stats, "primary_stat_type", "clout", PrimaryStatTypes.CLOUT)
        self.recursive_replace(self.stats, "primary_stat_type", "skullduggery", PrimaryStatTypes.SKULLDUGGERY)
        self.recursive_replace(self.stats, "primary_stat_type", "exactitude", PrimaryStatTypes.EXACTITUDE)

        # Stat:Secondary:secondary_stat_type
        self.recursive_replace(self.stats, "secondary_stat_type", "max_hp", SecondaryStatTypes.MAX_HP)
        self.recursive_replace(self.stats, "secondary_stat_type", "accuracy", SecondaryStatTypes.ACCURACY)

        # Update skills
        # SkillTree:Skill:shape
        self.recursive_replace(self.skills, "shape", "target", SkillShapes.TARGET)
        self.recursive_replace(self.skills, "shape", "square", SkillShapes.SQUARE)

    def recursive_replace(self, obj, key, value_to_replace, new_value):
        """
        Check through any number of nested dicts or lists for the specified key->value pair and replace the value.

        Args:
            obj (object): dict, list, string, or anything else to be checked.
            key (str): The key to look for in the object
            value_to_replace (): The value to look for, stored against the key.
            new_value (): The value to set.
        """
        if isinstance(obj, dict):
            # Break the dict out and run recursively against the elements
            for k, v in obj.items():
                if k == key:
                    # The value may be a list so handle it if so
                    if isinstance(v, list):
                        # Loop the list and replace the required value
                        for index, item in enumerate(v):
                            if item == value_to_replace:
                                v[index] = new_value
                    elif v == value_to_replace:
                        obj[key] = new_value
                else:
                    self.recursive_replace(v, key, value_to_replace, new_value)

        elif isinstance(obj, list):
            # Break the list out and run recursively against the elements
            for element in obj:
                self.recursive_replace(element, key, value_to_replace, new_value)

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
        named_tuple = namedtuple(terrain_name, self.terrains[terrain_name])
        data = named_tuple(**self.terrains[terrain_name])

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
        Get data for an aspect from the central library

        Args:
            aspect_name (str):

        Returns:
            AspectData: data for a specified aspect.
        """

        data = self.aspects[aspect_name]
        return data

    def get_aspect_effect_data(self, aspect_name, effect_type):
        """
        Get data for an aspect from the central library

        Args:
            aspect_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified effect.
        """

        data = self.aspects[aspect_name].effects[effect_type.name]
        return data

    def get_affliction_data(self, affliction_name):
        """
        Get data for an affliction from the central library

        Args:
            affliction_name (str):

        Returns:
            AfflictionData: data for a specified Affliction.
        """

        data = self.afflictions[affliction_name]
        return data

    def get_affliction_effect_data(self, affliction_name, effect_type):
        """
        Get data for an affliction from the central library

        Args:
            affliction_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified effect.
        """

        data = self.afflictions[affliction_name].effects[effect_type.name]
        return data

    def get_savvy_data(self, savvy_name):
        """
        Get data for a savvys from the central library

        Args:
            savvy_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(savvy_name, self.savvys[savvy_name])
        data = named_tuple(**self.savvys[savvy_name])

        return data

    def get_race_data(self, race_name):
        """
        Get data for a races from the central library

        Args:
            race_name (str):

        Returns:
            RaceData: data for a specified Race.
        """

        data = self.races[race_name]
        return data

    def get_homeland_data(self, homeland_name):
        """
        Get data for a homelands from the central library

        Args:
            homeland_name (str):

        Returns:
            tuple: named tuple of values.
        """
        # NOTE: I do not know how any of this works.  Let's live in hope that fact never causes a problem.
        from collections import namedtuple
        named_tuple = namedtuple(homeland_name, self.homelands[homeland_name])
        data = named_tuple(**self.homelands[homeland_name])

        return data

    def get_skill_data(self, skill_tree, skill_name):
        """
        Get data for a skill from the central library

        Args:
            skill_tree (str):
            skill_name (str):

        Returns:
            SkillData: data for a specified skill.
        """

        skill_data = self.skills[skill_tree].skill[skill_name]
        return skill_data

    def get_primary_stat_data(self, primary_stat_type):
        """
        Get data for a primary stat from the central library

        Args:
            primary_stat_type (PrimaryStatTypes):

        Returns:
            PrimaryStatData:  stat data for specified stat.
        """

        stat_data = self.stats.primary[primary_stat_type.name]

        return stat_data

    def get_secondary_stat_data(self, secondary_stat_type):
        """
        Get data for a secondary stat from the central library

        Args:
            secondary_stat_type (SecondaryStatTypes):

        Returns:
            SecondaryStatData:  stat data for specified stat.
        """

        stat_data = self.stats.secondary[secondary_stat_type.name]

        return stat_data

    def get_skill_effect_data(self, skill_tree, skill_name, effect_type):
        """
        Get data for a skill from the central library

        Args:
            skill_tree(str):
            skill_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified skill effect.
        """

        effect_data = self.skills[skill_tree].skill[skill_name].effects[effect_type.name]
        return effect_data

    def refresh_library_data(self):
        """
        Load json data into the library, convert strings to enums and dicts to data classes.
        """
        self.load_data_into_library()
        self.convert_external_strings_to_internal_enums()
        self.convert_skills_to_data_classes()
        self.convert_afflictions_to_data_classes()
        self.convert_aspects_to_data_classes()
        self.convert_races_to_data_classes()
        self.convert_stats_to_data_classes()

    def load_data_into_library(self):
        """
        Load data from all external jsons to this central data library
        """
        import os
        # N.B. this is set in Sphinx config when Sphinx is running
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self.skills = self.load_values_from_skill_json()
            self.homelands = self.load_values_from_homeland_json()
            self.races = self.load_values_from_race_json()
            self.savvys = self.load_values_from_savvy_json()
            self.afflictions = self.load_values_from_affliction_json()
            self.aspects = self.load_values_from_aspect_json()
            self.terrains = self.load_values_from_terrain_json()
            self.actor_template = self.load_values_from_actor_json()
            self.stats = self.load_values_from_stat_json()

        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, f"Data Library refreshed."))

    @staticmethod
    def load_values_from_skill_json():
        """

        Returns:

        """
        # TODO - create rules to confirm every tree has a basic attack
        with open('data/game/skills/skill_trees.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_affliction_json():
        """

        Returns:

        """
        with open('data/game/skills/afflictions.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_aspect_json():
        """

        Returns:

        """
        with open('data/game/world/aspect.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_terrain_json():
        """

        Returns:

        """
        with open('data/game/world/terrain.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_homeland_json():
        """

        Returns:

        """
        with open('data/game/entity/homelands.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_savvy_json():
        """

        Returns:

        """
        with open('data/game/entity/savvys.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_race_json():
        """

        Returns:

        """
        with open('data/game/entity/races.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_actor_json():
        """

        Returns:

        """

        with open('data/game/entity/actor_templates.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_values_from_stat_json():
        """

        Returns:

        """
        with open('data/game/entity/stats.json') as file:
            data = json.load(file)

        return data
