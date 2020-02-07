from __future__ import annotations

import json
import logging
import os
from typing import TYPE_CHECKING
from scripts.world.data_classes.characteristic_dataclass import CharacteristicData
from scripts.core.constants import TargetTags, EffectTypes, PrimaryStatTypes, \
    AfflictionCategory, AfflictionTriggers, DamageTypes, SecondaryStatTypes, SkillShapes, HitTypes, \
    Directions, SkillTerrainCollisions, SkillTravelTypes, SkillExpiryTypes
from scripts.world.data_classes.stat_dataclass import StatData, PrimaryStatData, SecondaryStatData
from scripts.skills.affliction import AfflictionData
from scripts.skills.skill import SkillData
from scripts.skills.effect import EffectData
from scripts.world.data_classes.aspect_dataclass import AspectData
from scripts.world.data_classes.attitude_dataclass import AttitudeData
from scripts.world.data_classes.god_dataclass import GodData
from scripts.world.data_classes.interaction_dataclass import InteractionData
from scripts.world.data_classes.intervention_dataclass import InterventionData

if TYPE_CHECKING:
    pass


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world.
    """

    def __init__(self):
        self.homelands = {}
        self.races = {}  
        self.savvys = {}  
        self.afflictions = {}  
        self.aspects = {}  
        self.terrains = {}
        self.stats = {}  
        self.gods = {}
        self.skills = {}

        self.refresh_library_data()

        logging.info(f"Data Library initialised.")

    ####################### LIBRARY MANAGEMENT ####################
    def refresh_library_data(self):
        """
        Load json data into the library, convert strings to enums and dicts to data classes.
        """
        self.load_data_into_library()
        self.convert_external_strings_to_internal_values()
        self.convert_afflictions_to_data_classes()
        self.convert_aspects_to_data_classes()
        self.convert_stats_to_data_classes()
        self.convert_gods_to_data_classes()
        self.convert_homelands_to_data_classes()
        self.convert_savvys_to_data_classes()
        self.convert_races_to_data_classes()
        self.convert_skills_to_data_classes()


        logging.info(f"Library refreshed.")

    def load_data_into_library(self):
        """
        Load data from all external jsons to this central data library
        """
        # N.B. this is set in Sphinx config when Sphinx is running
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self.homelands = self.load_homeland_json()
            self.races = self.load_race_json()
            self.savvys = self.load_savvy_json()
            self.afflictions = self.load_affliction_json()
            self.aspects = self.load_aspect_json()
            self.terrains = self.load_terrain_json()
            self.stats = self.load_base_stat_json()
            self.gods = self.load_gods_json()
            self.skills = self.load_skills_json()

        logging.info(f"Data loaded into the Library.")

    ####################### UTILITY ##############################

    @staticmethod
    def cleanse_name(name: str):
        """
        Force name to lowercase, replace underscores with spaces, turn double space to single
        Args:
            name ():

        Returns:

        """
        cleansed_name = name.lower()
        cleansed_name = cleansed_name.replace("_", " ")
        cleansed_name = cleansed_name.replace("  ", " ")
        return cleansed_name

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

    ####################### CONVERT ##############################

    def convert_afflictions_to_data_classes(self):
        """
        Take affliction data from library and convert to data classes
        """
        all_afflictions_data = self.afflictions
        converted_afflictions = {}

        # loop all afflictions
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
            affliction.name = self.cleanse_name(affliction.name)
            converted_afflictions[affliction.name] = affliction

        # delete all info from afflictions and replace with the converted data
        self.afflictions = {}
        self.afflictions = converted_afflictions

    def convert_aspects_to_data_classes(self):
        """
        Take aspects data from library and convert to data classes
        """
        all_aspect_data = self.aspects
        converted_aspects = {}

        # loop all aspects
        for aspect_name, aspect_data in all_aspect_data.items():
            converted_effects = {}
            converted_interactions = []

            # loop effects
            for index, effect_data in enumerate(aspect_data["effects"]):
                # convert the skill effect data to the data class
                effect = EffectData(**effect_data)
                converted_effects[effect.effect_type.name] = effect

            # loop interactions
            for index, interaction_data in enumerate(aspect_data["interactions"]):
                # convert the skill effect data to the data class
                interaction = InteractionData(**interaction_data)
                converted_interactions.append(interaction)

            # set the temp dict to contain the converted skill effects
            new_aspect_dict = aspect_data.copy()
            new_aspect_dict["effects"] = converted_effects
            new_aspect_dict["interactions"] = converted_interactions

            # unpack the temp dict and convert the aspects data to the data class
            aspect = AspectData(**new_aspect_dict)
            aspect.name = self.cleanse_name(aspect.name)
            converted_aspects[aspect.name] = aspect

        # delete all info from aspects and replace with the converted data
        self.aspects = {}
        self.aspects = converted_aspects

    def convert_races_to_data_classes(self):
        """
        Take race data from library and convert to data classes
        """
        all_race_data = self.races
        converted_races = {}

        # loop all races
        for race_name, race_data in all_race_data.items():
            converted_skills = []

            # loop skills and convert to data class
            for index, skill_name in enumerate(race_data["skills"]):
                converted_skills.append(self.cleanse_name(skill_name))

            # set the temp dict to contain the converted skill effects
            new_race_dict = race_data.copy()
            new_race_dict["skills"] = converted_skills

            # unpack the temp dict and convert the aspects data to the data class
            race = CharacteristicData(**new_race_dict)
            race.name = self.cleanse_name(race.name)
            converted_races[race.name] = race

        # delete all info from aspects and replace with the converted data
        self.races = {}
        self.races = converted_races
        
    def convert_savvys_to_data_classes(self):
        """
        Take savvy data from library and convert to data classes
        """
        all_savvy_data = self.savvys
        converted_savvys = {}

        # loop all savvys
        for savvy_name, savvy_data in all_savvy_data.items():
            converted_skills = []

            # loop skills and convert to data class
            for index, skill_name in enumerate(savvy_data["skills"]):
                converted_skills.append(self.cleanse_name(skill_name))

            # set the temp dict to contain the converted skill effects
            new_savvy_dict = savvy_data.copy()
            new_savvy_dict["skills"] = converted_skills

            # unpack the temp dict and convert the aspects data to the data class
            savvy = CharacteristicData(**new_savvy_dict)
            savvy.name = self.cleanse_name(savvy.name)
            converted_savvys[savvy.name] = savvy

        # delete all info from aspects and replace with the converted data
        self.savvys = {}
        self.savvys = converted_savvys
        
    def convert_homelands_to_data_classes(self):
        """
        Take homeland data from library and convert to data classes
        """
        all_homeland_data = self.homelands
        converted_homelands = {}

        # loop all homelands
        for homeland_name, homeland_data in all_homeland_data.items():
            converted_skills = []

            # loop skills and convert to data class
            for index, skill_name in enumerate(homeland_data["skills"]):
                converted_skills.append(self.cleanse_name(skill_name))

            # set the temp dict to contain the converted skill effects
            new_homeland_dict = homeland_data.copy()
            new_homeland_dict["skills"] = converted_skills

            # unpack the temp dict and convert the aspects data to the data class
            homeland = CharacteristicData(**new_homeland_dict)
            homeland.name = self.cleanse_name(homeland.name)
            converted_homelands[homeland.name] = homeland

        # delete all info from aspects and replace with the converted data
        self.homelands = {}
        self.homelands = converted_homelands

    def convert_stats_to_data_classes(self):
        """
        Take skill data from library and convert to data classes
        """
        all_stat_data = self.stats
        converted_primary_stats = {}
        converted_secondary_stats = {}

        # loop all stats types
        for stat_type_name, stat_type_data in all_stat_data.items():

            # loop all individual stats
            for stat_name, stat_data in stat_type_data.items():

                # unpack the dict and convert the stat data to the data class
                if stat_type_name == "primary":
                    stat = PrimaryStatData(**stat_data)
                    converted_primary_stats[stat.primary_stat_type.name] = stat

                elif stat_type_name == "secondary":
                    stat = SecondaryStatData(**stat_data)
                    converted_secondary_stats[stat.secondary_stat_type.name] = stat

        # delete all info from stat and replace with the converted data
        converted_data = StatData(primary=converted_primary_stats, secondary=converted_secondary_stats)
        self.stats = {}
        self.stats = converted_data

    def convert_gods_to_data_classes(self):
        """
        Take aspects data from library and convert to data classes
        """
        all_god_data = self.gods
        converted_gods = {}

        # loop all gods
        for god_name, god_data in all_god_data.items():
            converted_interventions = {}
            converted_attitudes = {}

            # loop attitudes and convert to data class
            for index, attitude_data in enumerate(god_data["attitudes"]):
                attitude = AttitudeData(**attitude_data)
                try:
                    converted_attitudes[attitude.action.name] = attitude
                except:  # Need to handle unhashable for the enums... but I don't know the exception type.
                    converted_attitudes[attitude.action] = attitude

            # loop interventions and convert to data class
            for index, intervention_data in enumerate(god_data["interventions"]):

                # unpack the dict and convert the intervention data to the data class
                intervention = InterventionData(**intervention_data)
                converted_interventions[intervention.name] = intervention

            # set the temp dict to contain the converted skill effects
            new_god_dict = god_data.copy()
            new_god_dict["attitudes"] = converted_attitudes
            new_god_dict["interventions"] = converted_interventions

            # unpack the temp dict and convert the aspects data to the data class
            god = GodData(**new_god_dict)
            god.name = self.cleanse_name(god.name)
            converted_gods[god.name] = god

        # delete all info from aspects and replace with the converted data
        self.gods = {}
        self.gods = converted_gods

    def convert_skills_to_data_classes(self):
        """
         Take homeland data from library and convert to data classes
         """
        all_skill_data = self.skills
        converted_skills = {}

        # loop all skills
        for skill_name, skill_data in all_skill_data.items():
            converted_effects = {}

            # loop effects
            for index, effect_data in enumerate(skill_data["effects"]):
                # convert the effect data to the data class
                effect = EffectData(**effect_data)
                converted_effects[effect.effect_type.name] = effect

            # set the temp dict to contain the converted effects
            new_skill_dict = skill_data.copy()
            new_skill_dict["effects"] = converted_effects

            # unpack the temp dict and convert the data to the data class
            skill = SkillData(**new_skill_dict)
            skill.name = self.cleanse_name(skill.name)
            converted_skills[skill.name] = skill

        # delete all info from self and replace with the converted data
        self.skills = {}
        self.skills = converted_skills
        
    def convert_external_strings_to_internal_values(self):
        """
        Where there are external values that are utilised internally convert them to the internal constant.
        """
        # Update shared values
        lists_to_convert = [self.aspects, self.afflictions, self.gods, self.savvys, self.races,
            self.homelands, self.skills]
        
        for current_list in lists_to_convert:
            # Effects:required_tags
            for value in TargetTags:
                self.recursive_replace(current_list, "required_tags", value.name.lower(), value)

            # Effects:name
            for value in EffectTypes:
                self.recursive_replace(current_list, "effect_type", value.name.lower(), value)

            # Effects:damage_type
            for value in DamageTypes:
                self.recursive_replace(current_list, "damage_type", value.name.lower(), value)

            # Effects:mod_stat
            for value in PrimaryStatTypes:
                self.recursive_replace(current_list, "mod_stat", value.name.lower(), value)
            self.recursive_replace(current_list, "mod_stat", "none", None)  # need to add this as mod_stat can be none

            # Effects:stat_to_target
            for value in PrimaryStatTypes:
                self.recursive_replace(current_list, "stat_to_target", value.name.lower(), value)
            for value in SecondaryStatTypes:
                self.recursive_replace(current_list, "stat_to_target", value.name.lower(), value)

            # Effects:stat_to_affect
            for value in PrimaryStatTypes:
                self.recursive_replace(current_list, "stat_to_affect", value.name.lower(), value)
            for value in SecondaryStatTypes:
                self.recursive_replace(current_list, "stat_to_affect", value.name.lower(), value)

            # Skill:shape
            for value in SkillShapes:
                self.recursive_replace(current_list, "shape", value.name.lower(), value)

            # Skill:resource_type
            for value in SecondaryStatTypes:
                self.recursive_replace(current_list, "resource_type", value.name.lower(), value)

            # Skill:target_directions
            for value in Directions:
                self.recursive_replace(current_list, "target_directions", value.name.lower(), value)

            # Skill:travel_type
            for value in SkillTravelTypes:
                self.recursive_replace(current_list, "travel_type", value.name.lower(), value)

            # Skill:terrain_collision
            for value in SkillTerrainCollisions:
                self.recursive_replace(current_list, "terrain_collision", value.name.lower(), value)

            # Skill:expiry_type
            for value in SkillExpiryTypes:
                self.recursive_replace(current_list, "expiry_type", value.name.lower(), value)
       
        # Affliction:category
        for value in AfflictionCategory:
            self.recursive_replace(self.afflictions, "category", value.name.lower(), value)

        # Affliction:trigger_event
        for value in AfflictionTriggers:
            self.recursive_replace(self.afflictions, "trigger_event", value.name.lower(), value)

        # Stat:Primary:primary_stat_type
        for value in PrimaryStatTypes:
            self.recursive_replace(self.stats, "primary_stat_type", value.name.lower(), value)

        # Stat:Secondary:secondary_stat_type
        for value in SecondaryStatTypes:
            self.recursive_replace(self.stats, "secondary_stat_type", value.name.lower(), value)

        # Gods:attitudes:action
        for value in EffectTypes:
            self.recursive_replace(self.gods, "action", value.name.lower(), value)
        for value in DamageTypes:
            self.recursive_replace(self.gods, "action", value.name.lower(), value)
        for value in HitTypes:
            self.recursive_replace(self.gods, "action", value.name.lower(), value)

        # Aspect:duration
        self.recursive_replace(self.aspects, "duration", "none", None)  # need to add this as duration can be none

    ####################### GET ##############################

    def get_aspect_data(self, aspect_name):
        """
        Get data for an aspects from the central library

        Args:
            aspect_name (str):

        Returns:
            AspectData: data for a specified aspects.
        """

        data = self.aspects[aspect_name]
        return data

    def get_aspect_effect_data(self, aspect_name, effect_type):
        """
        Get effect data for an aspects from the central library

        Args:
            aspect_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified effect.
        """
        try:
            data = self.aspects[aspect_name].effects[effect_type.name]
        except KeyError:
            data = None

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
        try:
            data = self.afflictions[affliction_name].effects[effect_type.name]
        except KeyError:
            data = None

        return data

    def get_savvy_data(self, savvy_name):
        """
        Get data for a savvys from the central library

        Args:
            savvy_name (str):

        Returns:
            CharacteristicData: data for a specified Race.
        """

        data = self.savvys[savvy_name]
        return data

    def get_race_data(self, race_name):
        """
        Get data for a races from the central library

        Args:
            race_name (str):

        Returns:
            CharacteristicData: data for a specified Race.
        """

        data = self.races[race_name]
        return data

    def get_homeland_data(self, homeland_name):
        """
        Get data for a homelands from the central library

        Args:
            homeland_name (str):

        Returns:
            CharacteristicData: data for a specified Race.
        """

        data = self.homelands[homeland_name]
        return data

    def get_skill_data(self, skill_name):
        """
        Get data for a skill from the central library

        Args:
            skill_name (str):

        Returns:
            SkillData: data for a specified skill.
        """
        skill_data = self.skills[skill_name]

        return skill_data

    def get_skill_effect_data(self, skill_name, effect_type):
        """
        Get data for a skill from the central library

        Args:

            skill_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified skill effect.
        """
        try:
            effect_data = self.skills[skill_name].effects[effect_type.name]

        except KeyError:
            effect_data = None

        return effect_data

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

    def get_god_data(self, god_name):
        """
        Get data for a god from the central library

        Args:
            god_name (str):

        Returns:
            GodData:  data for specified god.
        """

        god_data = self.gods[god_name]

        return god_data

    def get_god_interventions_data(self, god_name):
        """
        Get data for a god's interventions from the central library

        Args:
            god_name(str):

        Returns:
            dict: data for a specified god's interventions. (key, InterventionData)
        """
        interventions_data = self.gods[god_name].interventions

        return interventions_data

    def get_god_intervention_data(self, god_name, intervention_name):
        """
        Get data for a god's specified intervention from the central library

        Args:
            god_name(str):
            intervention_name(str):

        Returns:
            InterventionData: data for a specified god's  specified intervention.
        """
        interventions_data = self.gods[god_name].interventions[intervention_name]

        return interventions_data

    def get_god_intervention_effects_data(self, god_name, intervention_name):
        """
        Get data for the effects in a god's intervention from the central library

        Args:
            god_name(str):
            intervention_name(str):

        Returns:
            List[EffectData]: list of effects data
        """
        effects_data = self.gods[god_name].interventions[intervention_name].effects

        return effects_data

    def get_god_intervention_effect_data(self, god_name, intervention_name, effect_type):
        """
        Get data for a specified effect in a god's intervention from the central library

        Args:
            god_name(str):
            intervention_name(str):
            effect_type(EffectTypes):

        Returns:
            EffectData: data for a specified skill effect.
        """
        effects_data = self.gods[god_name].interventions[intervention_name].effects[effect_type.name]

        return effects_data

    def get_god_attitudes_data(self, god_name):
        """
        Get data for a god's attitudes from the central library

        Args:
            god_name(str):

        Returns:
            AttitudeData: data for a specified god.
        """
        attitude_data = self.gods[god_name].attitudes

        return attitude_data

    ####################### LOAD ##############################

    @staticmethod
    def load_affliction_json():
        """

        Returns:

        """
        with open('data/game/skills/afflictions.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_aspect_json():
        """

        Returns:

        """
        with open('data/game/world/aspect.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_terrain_json():
        """

        Returns:

        """
        with open('data/game/world/terrain.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_homeland_json():
        """

        Returns:

        """
        with open('data/game/entity/homelands.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_savvy_json():
        """

        Returns:

        """
        with open('data/game/entity/savvys.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_race_json():
        """

        Returns:

        """
        with open('data/game/entity/races.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_base_stat_json():
        """

        Returns:

        """
        with open('data/game/entity/base_stats.json') as file:
            data = json.load(file)

        return data

    @staticmethod
    def load_gods_json():
        """

        Returns:

        """
        with open('data/game/world/gods.json') as file:
            data = json.load(file)

        return data
    
    @staticmethod
    def load_skills_json():
        """

        Returns:

        """
        with open('data/game/skills/skills.json') as file:
            data = json.load(file)

        return data


library = LibraryOfAlexandria()