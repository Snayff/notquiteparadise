from __future__ import annotations

import json
import logging
import os
from typing import TYPE_CHECKING

from scripts.engine.core.constants import (EffectTypeType, PrimaryStatType,
                                           SecondaryStatType)
from scripts.engine.core.definitions import (
    AfflictionData, AspectData, BasePrimaryStatData, BaseSecondaryStatData,
    EffectData, SkillData, TraitData)
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

        self.refresh_library_data()

        logging.info(f"Data Library initialised.")  # FIXME - this isnt being logged

    ####################### LIBRARY MANAGEMENT ####################

    def refresh_library_data(self):
        """
        Load all json data into the library.
        """
        # N.B. this is set in Sphinx config when Sphinx is running
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self._load_traits_json()
            self._load_affliction_json()
            self._load_aspects_json()
            self._load_base_stat_primary_json()
            self._load_base_stat_secondary_json()
            self._load_gods_json()
            self._load_skills_json()

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

    def get_god_data(self, god_name: str) -> Dict:
        """
        Get data for a god from the library
        """

        god_data = self._gods[god_name]

        return god_data

    def get_god_intervention_data(self, god_name: str, intervention_name: str) -> Dict:
        """
        Get data for a god's specified intervention from the library
        """
        interventions_data = self._gods[god_name].interventions[intervention_name]

        return interventions_data

    def get_god_attitude_data(self, god_name: str) -> Dict[int, Dict]:
        """
        Get data for a god's attitudes from the library
        """
        attitude_data = self._gods[god_name].attitudes

        return attitude_data

    ####################### LOAD ##############################

    def _load_affliction_json(self):
        with open('data/game/afflictions.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)
        self._afflictions = data

    def _load_aspects_json(self):
        self._aspects = {}  # FIXME - unstub when json updated inline with skills
        return
        with open('data/game/aspects.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)
        self._aspects = data

    def _load_traits_json(self):
        with open('data/game/traits.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)
        self._traits = data

    def _load_base_stat_primary_json(self):
        with open('data/game/base_stats_primary.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._base_stats_primary = data

    def _load_base_stat_secondary_json(self):
        with open('data/game/base_stats_secondary.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._base_stats_secondary = data

    def _load_gods_json(self):
        with open('data/game/gods.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._gods = data

    def _load_skills_json(self):
        with open('data/game/skills.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._skills = data


library = _LibraryOfAlexandria()
