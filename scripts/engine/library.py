from __future__ import annotations

import json
import logging
import os
from typing import List, TYPE_CHECKING, Union
from scripts.engine import utility
from scripts.engine.core.constants import (EffectTypeType, InputIntent, PrimaryStatType,
    SecondaryStatType)
from scripts.engine.core.definitions import (
    AfflictionData, AspectData, AttitudeData, BasePrimaryStatData, BaseSecondaryStatData,
    EffectData, GodData, InterventionData, SkillData, TraitData)
from scripts.engine.core.extend_json import deserialise_dataclasses

if TYPE_CHECKING:
    from typing import Dict


class _LibraryOfAlexandria:
    """
    The centre of all knowledge in the world_objects.
    """

    def __init__(self):
        self._traits = {}
        self._afflictions = {}
        self._aspects = {}
        self._base_stats_primary = {}
        self._base_stats_secondary = {}
        self._gods = {}
        self._skills = {}
        self._input = self._get_default_input_dict()
        self.video = {}

        self.refresh_library_data()

        logging.info(f"Data Library initialised.")  # FIXME - this isnt being logged

    ####################### LIBRARY MANAGEMENT ####################

    def refresh_library_data(self):
        """
        Load all json data into the library.
        """
        # N.B. this is set in Sphinx config when Sphinx is running
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self._load_traits_data()
            self._load_affliction_data()
            self._load_aspects_data()
            self._load_base_stat_primary_data()
            self._load_base_stat_secondary_data()
            self._load_gods_data()
            self._load_skills_data()
            self._load_input_config()
            self._load_video_config()

        logging.info(f"Library data refreshed.")

    ####################### GET ##############################

    def get_aspect_data(self, aspect_name: str) -> AspectData:
        """
        Get data for an aspects from the library
        """

        data = self._aspects[aspect_name]
        return data

    def get_affliction_data(self, affliction_name: str) -> AfflictionData:
        """
        Get data for an affliction from the library
        """

        data = self._afflictions[affliction_name]
        return data

    def get_trait_data(self, trait_name: str) -> TraitData:
        """
        Get data for a trait from the library
        """

        data = self._traits[trait_name]
        return data

    def get_skill_data(self, skill_name: str) -> SkillData:
        """
        Get data for a skill from the library
        """
        # FIXME - it is possible for keys to have spaces and be compared to those that dont
        skill_data = self._skills[skill_name]

        return skill_data

    def get_primary_stat_data(self, primary_stat_type: PrimaryStatType) -> BasePrimaryStatData:
        """
        Get data for a primary stat from the library

        """
        stat_data = self._base_stats_primary[primary_stat_type]
        return stat_data

    def get_secondary_stat_data(self, secondary_stat_type: SecondaryStatType) -> BaseSecondaryStatData:
        """
        Get data for a secondary stat from the library
        """

        stat_data = self._base_stats_secondary[secondary_stat_type]

        return stat_data

    def get_god_data(self, god_name: str) -> GodData:
        """
        Get data for a god from the library
        """

        god_data = self._gods[god_name]

        return god_data

    def get_god_intervention_data(self, god_name: str, intervention_name: str) -> InterventionData:
        """
        Get data for a god's specified intervention from the library
        """
        interventions_data = self._gods[god_name].interventions[intervention_name]

        return interventions_data

    def get_god_attitude_on_action_data(self, god_name: str, action_name: str) -> AttitudeData:
        """
        Get data for a god's attitude on an action
        """
        attitude_data = self._gods[god_name].attitudes[action_name]

        return attitude_data

    def get_god_attitudes_data(self, god_name: str) -> Dict[str, AttitudeData]:
        """
        Get data for a god's attitudes from the library
        """
        attitude_data = self._gods[god_name].attitudes

        return attitude_data

    def get_all_input_data(self) -> Dict[str, List[int]]:
        """
        Get the input data
        """
        return self._input

    def _get_default_input_dict(self) -> Dict[str, List]:
        """
        Get the values needed for all input options and return an unmapped input dict.
        """
        _input: Dict[str, List] = {}

        for name in utility.get_class_members(InputIntent):
            _input[name.lower()] = []

        return _input

    def get_video_data(self, key: str) -> int:
        """
        Get video config data
        """
        return utility.recursive_find_in_dict(self._video, key)

    ####################### LOAD ##############################

    def _load_affliction_data(self):
        with open('data/game/afflictions.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)
        self._afflictions = data

    def _load_aspects_data(self):
        self._aspects = {}  # FIXME - unstub when json updated inline with skills
        return
        # with open('data/game/aspects.json') as file:
        #     data = json.load(file, object_hook=deserialise_dataclasses)
        # self._aspects = data

    def _load_traits_data(self):
        with open('data/game/traits.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)
        self._traits = data

    def _load_base_stat_primary_data(self):
        with open('data/game/base_stats_primary.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._base_stats_primary = data

    def _load_base_stat_secondary_data(self):
        with open('data/game/base_stats_secondary.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._base_stats_secondary = data

    def _load_gods_data(self):
        with open('data/game/gods.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._gods = data

    def _load_skills_data(self):
        with open('data/game/skills.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._skills = data

    def _load_input_config(self):
        """
        Load the input config and map to pygame constants
        """
        with open('data/config/input.json') as file:
            data = json.load(file)

        import pygame
        _input_list = {}

        # unpack input config
        for key, values in data.items():
            inputs = []
            for value in values:
                try:
                    # try to map the string to a pygame constant
                    pygame_constant = getattr(pygame, value)

                    # is the input already mapped to another intent?
                    if not any(pygame_constant in sublist for sublist in _input_list.values()):
                        inputs.append(pygame_constant)
                    else:
                        logging.warning(
                            f"{value} already mapped to another intent in input.json. Not added to {key}")
                except AttributeError:
                    logging.warning(f"{value} specified in input.json not found in pygame constants.")

            # add gathered values
            _input_list[key] = inputs

        # add mapped data
        self._input = _input_list

    def _load_video_config(self):
        """
        Load the video config
        """
        with open('data/config/video.json') as file:
            data = json.load(file)

        self._video = data

library = _LibraryOfAlexandria()
