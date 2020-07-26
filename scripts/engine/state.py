from __future__ import annotations

import datetime
import json
import logging
import os
from typing import TYPE_CHECKING
from scripts.engine import utility, world
from scripts.engine.core.constants import CURRENT_WORKING_DIRECTORY, GameState, GameStateType, MAX_SAVES, SAVE_PATH, \
    VERSION
from scripts.engine.core.store import store

if TYPE_CHECKING:
    pass


################### GET ##############################


def get_previous() -> GameStateType:
    """
    Get the previous game state
    """
    return store.previous_game_state


def get_internal_clock():
    """
    Get the internal clock
    """
    return store.internal_clock


def get_active_skill() -> str:
    """
    Get the active skill. Used for targeting mode.
    """
    return store.active_skill


def get_current() -> GameStateType:
    """
    Get the current game state
    """
    return store.current_game_state


################### SET ##############################

def set_active_skill(skill_name: str):
    """
    Set the active skill. Used for targeting mode.
    """
    store.active_skill = skill_name


################### MANAGING STATE ###################

def update_clock() -> float:
    """
    Tick the internal clock. Manages the frame rate. Returns delta time.
    """
    return store.internal_clock.tick(store.fps_limit) / 1000.0


def set_new(new_game_state: GameStateType):
    """
    Set the current game state
    """
    store.previous_game_state = store.current_game_state
    store.current_game_state = new_game_state

    prev_name = utility.value_to_member(store.previous_game_state, GameState)
    curr_name = utility.value_to_member(store.current_game_state, GameState)

    log_string = f"game_state updated from {prev_name} to {curr_name}"
    logging.info(log_string)


def save_game(is_auto_save: bool = False):
    """
    Serialise the game data to a file
    """
    # get the info needed
    full_save_path = CURRENT_WORKING_DIRECTORY + SAVE_PATH
    save = {}

    # add data to dict
    save["version"] = VERSION
    save["world"] = world.serialise()

    # prep filename
    player = world.get_player()
    name = world.get_name(player)
    name = name.replace(" ", "_")  # clean name
    date_and_time = datetime.datetime.utcnow().strftime("%Y%m%d@%H%M")
    save_name_prefix = f"{name}"
    new_save_name = f"{save_name_prefix}_{date_and_time}"


    # clear old saves
    existing_saves = []
    # get existing save files and check if they match
    for save_name in os.listdir(full_save_path):
        if save_name_prefix in save_name:
            existing_saves.append(save_name)
    existing_saves = sorted(existing_saves)
    while len(existing_saves) > MAX_SAVES - 1:  # -1 to handle the offset
        save_name = existing_saves.pop(0)
        os.remove(full_save_path + "/" + save_name)


    # write to json
    with open(SAVE_PATH + new_save_name + ".json", "w") as file:
        json.dump(save, file, indent=4)


def load_game(filename: str):
    """
    Deserialise the game data from a file. Filename does not include path to save folder.
    """
    # read from json
    with open(SAVE_PATH + filename + ".json", "r") as file:
        save = json.load(file)

    # deserialise data
    new_world = world.deserialise(save["world"])

    # set the data as the default world
    world.move_world(new_world)
