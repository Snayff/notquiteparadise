from __future__ import annotations

import json
import logging  # type: ignore
import os
from typing import TYPE_CHECKING
from scripts.engine.core.extend_json import deserialise_dataclasses
from scripts.engine.core.constants import EffectType, PrimaryStat, SecondaryStat, SecondaryStatType, EffectTypeType, \
    PrimaryStatType
from scripts.engine.core.definitions import BasePrimaryStatData, BaseSecondaryStatData, SkillData,\
    InterventionData, GodData, EffectData, CharacteristicData, AspectData, AttitudeData, AfflictionData

if TYPE_CHECKING:
    from typing import Dict


class LibraryOfAlexandria:
    """
    The centre of all knowledge in the world_objects.
    """

    def __init__(self):
        self._homelands = {}
        self._peoples = {}
        self._savvys = {}
        self._afflictions = {}
        self._aspects = {}
        self._terrain = {}
        self._base_stats_primary = {}
        self._base_stats_secondary = {}
        self._gods = {}
        self._skills = {}

        self.refresh_library_data()

        logging.info(f"Data Library initialised.")

    ####################### LIBRARY MANAGEMENT ####################

    def refresh_library_data(self):
        """
        Load all json data into the library.
        """
        # N.B. this is set in Sphinx config when Sphinx is running
        if "GENERATING_SPHINX_DOCS" not in os.environ:
            self._load_homeland_json()
            self._load_people_json()
            self._load_savvy_json()
            self._load_affliction_json()
            self._load_aspects_json()
            self._load_terrain_json()
            self._load_base_stat_primary_json()
            self._load_base_stat_secondary_json()
            self._load_gods_json()
            self._load_skills_json()

        logging.info(f"Library data refreshed.")

    ####################### GET ##############################

    def get_aspects_data(self) -> Dict[str, AspectData]:
        """
        Get all aspects from the library
        """

        data = self._aspects
        return data

    def get_aspect_data(self, aspect_name: str) -> AspectData:
        """
        Get data for an aspects from the library
        """

        data = self._aspects[aspect_name]
        return data

    def get_aspect_effect_data(self, aspect_name: str, effect_type: EffectTypeType) -> EffectData:
        """
        Get effect data for an aspects from the library
        """
        try:
            data = self._aspects[aspect_name].effects[effect_type]
        except KeyError:
            data = None

        return data

    def get_afflictions_data(self) -> Dict[str, AfflictionData]:
        """
        Get all afflictions from the library
        """

        data = self._afflictions
        return data

    def get_affliction_data(self, affliction_name: str) -> AfflictionData:
        """
        Get data for an affliction from the library
        """

        data = self._afflictions[affliction_name]
        return data

    def get_affliction_effect_data(self, affliction_name: str, effect_type: EffectData) -> EffectData:
        """
        Get data for an affliction from the library

        """
        try:
            data = self._afflictions[affliction_name].effects[effect_type]
        except KeyError:
            data = None

        return data

    def get_savvys_data(self) -> Dict[str, CharacteristicData]:
        """
        Get all savvys from the library
        """

        data = self._savvys
        return data

    def get_savvy_data(self, savvy_name: str) -> CharacteristicData:
        """
        Get data for a savvys from the library
        """

        data = self._savvys[savvy_name]
        return data

    def get_peoples_data(self) -> Dict[str, CharacteristicData]:
        """
        Get all peoples from the library
        """

        data = self._peoples
        return data

    def get_people_data(self, people_name: str) -> CharacteristicData:
        """
        Get data for a peoples from the library
        """

        data = self._peoples[people_name]
        return data

    def get_homelands_data(self) -> Dict[str, CharacteristicData]:
        """
        Get all homelands from the library
        """

        data = self._homelands
        return data

    def get_homeland_data(self, homeland_name: str) -> CharacteristicData:
        """
        Get data for a homelands from the library
        """

        data = self._homelands[homeland_name]
        return data

    def get_skills_data(self) -> Dict[str, SkillData]:
        """
        Get all skill data from the library
        """
        return self._skills

    def get_skill_data(self, skill_name: str) -> SkillData:
        """
        Get data for a skill from the library
        """
        # FIXME - it is possible for keys to have spaces and be compared to those that dont
        skill_data = self._skills[skill_name]

        return skill_data

    def get_skill_effect_data(self, skill_name: str, effect_type: EffectTypeType) -> EffectData:
        """
        Get effect data for a skill from the library
        """
        try:
            effect_data = self._skills[skill_name].effects[effect_type]

        except KeyError:
            effect_data = None

        return effect_data

    def get_primary_stat_data(self, primary_stat_type: PrimaryStatType) -> BasePrimaryStatData:
        """
        Get data for a primary stat from the library

        """
        stat_data = self._base_stats_primary[primary_stat_type]
        return stat_data

    def get_primary_stats_data(self) -> Dict[str, BasePrimaryStatData]:
        """
        Get all data for primary stats from the library
        """
        stat_data = self._base_stats_primary
        return stat_data

    def get_secondary_stat_data(self, secondary_stat_type: SecondaryStatType) -> BaseSecondaryStatData:
        """
        Get data for a secondary stat from the library
        """

        stat_data = self._base_stats_secondary[secondary_stat_type]

        return stat_data

    def get_secondary_stats_data(self) -> Dict[str, BaseSecondaryStatData]:
        """
        Get all data for secondary stats from the library
        """
        stat_data = self._base_stats_secondary
        return stat_data

    def get_gods_data(self) -> Dict[str, GodData]:
        """
        Get all gods data from the library

        """
        god_data = self._gods

        return god_data

    def get_god_data(self, god_name: str) -> GodData:
        """
        Get data for a god from the library
        """

        god_data = self._gods[god_name]

        return god_data

    def get_god_interventions_data(self, god_name: str) -> Dict[str, InterventionData]:
        """
        Get data for a god's interventions from the library
        """
        interventions_data = self._gods[god_name].interventions

        return interventions_data

    def get_god_intervention_data(self, god_name: str, intervention_name: str) -> InterventionData:
        """
        Get data for a god's specified intervention from the library
        """
        interventions_data = self._gods[god_name].interventions[intervention_name]

        return interventions_data

    def get_god_intervention_effects_data(self, god_name: str, intervention_name: str) -> Dict[str, EffectData]:
        """
        Get data for the effects in a god's intervention from the library
        """
        effects_data = self._gods[god_name].interventions[intervention_name].effects

        return effects_data

    def get_god_intervention_effect_data(self, god_name: str, intervention_name: str, effect_type: EffectTypeType) \
            -> EffectData:
        """
        Get data for a specified effect in a god's intervention from the library
        """
        effects_data = self._gods[god_name].interventions[intervention_name].effects[effect_type]

        return effects_data

    def get_god_attitudes_data(self, god_name: str) -> AttitudeData:
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
        with open('data/game/aspects.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._aspects = data

    def _load_terrain_json(self):
        with open('data/game/terrain.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._terrain = data

    def _load_homeland_json(self):
        with open('data/game/homelands.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._homelands = data

    def _load_savvy_json(self):
        with open('data/game/savvys.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._savvys = data

    def _load_people_json(self):
        with open('data/game/peoples.json') as file:
            data = json.load(file, object_hook=deserialise_dataclasses)

        self._peoples = data

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


library = LibraryOfAlexandria()