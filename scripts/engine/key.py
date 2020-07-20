from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

import pygame

from scripts.engine.core.constants import InputIntent, InputIntentType, EventType

if TYPE_CHECKING:
    from typing import Optional, Tuple

_input_list = {}  # holds values from input config


def load_input_list_from_config():
    """
    Load input.json and map values to pygame constants before storing in _input_list dict
    -"""
    with open('data/config/input.json') as file:
        data = json.load(file)

    # unpack input config
    for key, values in data.items():
        inputs = []
        for value in values:
            try:
                inputs.append(getattr(pygame, value))
            except AttributeError:
                logging.warning(f"{value} specified in input.json not found in pygame constants.")
        _input_list[key] = inputs

    logging.debug("Input config loaded.")


def convert_vector_to_intent(direction: Tuple[int, int]) -> Optional[InputIntentType]:
    direction_map = {
        (0, 1): InputIntent.UP,
        (0, -1): InputIntent.DOWN,
        (1, 0): InputIntent.RIGHT,
        (-1, 0): InputIntent.LEFT,
        (1, 1): InputIntent.UP_RIGHT,
        (-1, 1): InputIntent.UP_LEFT,
        (1, -1): InputIntent.DOWN_RIGHT,
        (-1, -1): InputIntent.DOWN_LEFT
    }
    if direction in direction_map:
        return direction_map[direction]
    return None


def convert_to_intent(event: pygame.event) -> Optional[InputIntentType]:
    """
    Convert input to an intent.
    """
    intent = None

    checks = {
        1: _check_directions,
        2: _check_actions,
        3: _check_dev_actions
    }

    # loop each check in turn and return first value found
    for check in checks.values():
        intent = check(event)

        if intent is not None:
            return intent

    return intent


def _check_directions(event: pygame.event):
    """
    Get directional input from the keyboard
    """

    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key in _input_list["up"]:
            return InputIntent.UP
        elif event.key in _input_list["down"]:
            return InputIntent.DOWN
        elif event.key in _input_list["left"]:
            return InputIntent.LEFT
        elif event.key in _input_list["right"]:
            return InputIntent.RIGHT
        elif event.key in _input_list["up_left"]:
            return InputIntent.UP_LEFT
        elif event.key in _input_list["up_right"]:
            return InputIntent.UP_RIGHT
        elif event.key in _input_list["down_left"]:
            return InputIntent.DOWN_LEFT
        elif event.key in _input_list["down_right"]:
            return InputIntent.DOWN_RIGHT


def _check_actions(event: pygame.event):
    """
    Get actions such as confirm or cancel, or skill usage.
    """

    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key in _input_list["skill0"]:
            return InputIntent.SKILL0
        elif event.key in _input_list["skill1"]:
            return InputIntent.SKILL1
        elif event.key in _input_list["skill2"]:
            return InputIntent.SKILL2
        elif event.key in _input_list["skill3"]:
            return InputIntent.SKILL3
        elif event.key in _input_list["skill4"]:
            return InputIntent.SKILL4
        elif event.key in _input_list["skill5"]:
            return InputIntent.SKILL5
        elif event.key in _input_list["confirm"]:
            return InputIntent.CONFIRM
        elif event.key in _input_list["exit"]:
            return InputIntent.EXIT


def _check_dev_actions(event: pygame.event):
    """
    Get any dev intents
    """
    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            return InputIntent.DEBUG_TOGGLE
        elif event.key == pygame.K_F5:
            return InputIntent.REFRESH_DATA
        elif event.key == pygame.K_F2:
            return InputIntent.DEV_TOGGLE

