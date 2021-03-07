from __future__ import annotations

import json
import logging
import os
import time
from typing import TYPE_CHECKING

import pygame

from scripts.engine.internal.constant import DATA_PATH, InputIntent
from scripts.engine.internal.definition import (
    ActorData,
    AfflictionData,
    GameConfigData,
    GodData,
    MapData,
    RoomConceptData,
    SecondaryStatModData,
    SkillData,
    TerrainData,
    TraitData,
    VideoConfigData,
)
from scripts.engine.internal.extend_json import deserialise_dataclasses

if TYPE_CHECKING:
    from typing import Dict, List


__all__ = [
    "TRAITS",
    "AFFLICTIONS",
    "TERRAIN",
    "SECONDARY_STAT_MODS",
    "GODS",
    "SKILLS",
    "MAPS",
    "ACTORS",
    "ROOMS",
    "INPUT_CONFIG",
    "VIDEO_CONFIG",
    "GAME_CONFIG",
    "refresh_library",
]

#################################################################
# This module is for loading external data that is offered to the
# rest of the engine as a reference.
#################################################################


####################### DATA DICTS ##############################

TRAITS: Dict[str, TraitData] = {}
AFFLICTIONS: Dict[str, AfflictionData] = {}
TERRAIN: Dict[str, TerrainData] = {}
SECONDARY_STAT_MODS: Dict[str, SecondaryStatModData] = {}
GODS: Dict[str, GodData] = {}
SKILLS: Dict[str, SkillData] = {}
BLESSINGS: Dict[str, Dict] = {}
MAPS: Dict[str, MapData] = {}
ROOMS: Dict[str, RoomConceptData] = {}
ACTORS: Dict[str, ActorData] = {}
INPUT_CONFIG: Dict[str, List[str]] = {}

# load with defaults, overidden by refresh
VIDEO_CONFIG: VideoConfigData = VideoConfigData()
GAME_CONFIG: GameConfigData = GameConfigData()

# build default list for input - needed in case json doesnt include all required values
for member in InputIntent.__dict__.keys():
    if member[:2] != "__":
        INPUT_CONFIG[member.lower()] = []


####################### REFRESH ##############################


def refresh_library():
    """
    Load all json data into the library.
    """
    if "GENERATING_SPHINX_DOCS" in os.environ:  # when building in CI these fail
        return

    start_time = time.time()

    _load_traits_data()
    _load_affliction_data()
    _load_terrain_data()
    _load_secondary_stat_mod_data()
    _load_gods_data()
    _load_skills_data()
    _load_blessings_data()
    _load_map_data()
    _load_room_data()
    _load_npc_data()
    _load_input_config()
    _load_video_config()
    _load_game_config()

    logging.info(f"Library data refreshed...")

    end_time = time.time()
    logging.debug(f"-> loaded data in {format(end_time - start_time, '.5f')}")


####################### LOAD ##############################


def _load_affliction_data():
    with open(str(DATA_PATH / "game/afflictions.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global AFFLICTIONS
    AFFLICTIONS = data


def _load_terrain_data():
    global TERRAIN
    TERRAIN = {}
    with open("data/game/terrain.json") as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    TERRAIN = data


def _load_traits_data():
    with open(str(DATA_PATH / "game/traits.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global TRAITS
    TRAITS = data


def _load_secondary_stat_mod_data():
    with open(str(DATA_PATH / "game/secondary_stat_mods.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)

    global SECONDARY_STAT_MODS
    SECONDARY_STAT_MODS = data


def _load_gods_data():
    with open(str(DATA_PATH / "game/gods.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global GODS
    GODS = data


def _load_skills_data():
    with open(str(DATA_PATH / "game/skills.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global SKILLS

    SKILLS = data

def _load_blessings_data():
    with open(str(DATA_PATH / "game/blessings.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global BLESSINGS

    BLESSINGS = data

def _load_map_data():
    with open(str(DATA_PATH / "game/maps.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global MAPS

    MAPS = data


def _load_room_data():
    with open(str(DATA_PATH / "game/rooms.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global ROOMS
    ROOMS = data


def _load_npc_data():
    with open(str(DATA_PATH / "game/actors.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global ACTORS
    ACTORS = data


def _load_input_config():
    """
    Load the input config and map to pygame constants
    """
    with open(str(DATA_PATH / "config/input.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)

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
                    logging.warning(f"{value} already mapped to another intent in input.json. Not added to {key}")
            except AttributeError:
                logging.warning(f"{value} specified in input.json not found in pygame constants.")

        # add gathered values
        _input_list[key] = inputs

    # add mapped data
    global INPUT_CONFIG
    INPUT_CONFIG = _input_list


def _load_video_config():
    """
    Load the _video config
    """
    with open(str(DATA_PATH / "config/video.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)

    global VIDEO_CONFIG
    VIDEO_CONFIG = data


def _load_game_config():
    """
    Load the game config
    """
    with open(str(DATA_PATH / "config/game.json")) as file:
        data = json.load(file, object_hook=deserialise_dataclasses)
    global GAME_CONFIG
    GAME_CONFIG = data


####################### REFRESH ON INIT ##############################

if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    # Refresh the library immediately on init. Need this to ensure everything here is init'd and updated.
    refresh_library()
