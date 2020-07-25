from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.engine import utility
from scripts.engine.core.constants import GameState, GameStateType
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


def get_delta_time() -> float:
    """
    get delta time and set frame rate with .tick()
    """
    return store.internal_clock.tick(store.fps_limit) / 1000.0


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

def update_clock():
    """
    Tick the internal clock. Manages the frame rate.
    """
    # set frame rate
    store.internal_clock.tick(store.fps_limit)


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
