from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from scripts.engine.internal.constant import InputIntent, InputIntentType
from scripts.engine.internal.library import INPUT_CONFIG

if TYPE_CHECKING:
    from typing import Optional, Tuple


def convert_vector_to_intent(direction: Tuple[int, int]) -> Optional[InputIntentType]:
    direction_map = {
        (0, 1): InputIntent.UP,
        (0, -1): InputIntent.DOWN,
        (1, 0): InputIntent.RIGHT,
        (-1, 0): InputIntent.LEFT,
        (1, 1): InputIntent.UP_RIGHT,
        (-1, 1): InputIntent.UP_LEFT,
        (1, -1): InputIntent.DOWN_RIGHT,
        (-1, -1): InputIntent.DOWN_LEFT,
    }
    if direction in direction_map:
        return direction_map[direction]
    return None


def convert_to_intent(event: pygame.event) -> Optional[InputIntentType]:
    """
    Convert input to an intent.
    """
    intent = None

    checks = {1: _check_directions, 2: _check_actions, 3: _check_dev_actions}

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
        if event.key in INPUT_CONFIG["up"]:
            return InputIntent.UP
        elif event.key in INPUT_CONFIG["down"]:
            return InputIntent.DOWN
        elif event.key in INPUT_CONFIG["left"]:
            return InputIntent.LEFT
        elif event.key in INPUT_CONFIG["right"]:
            return InputIntent.RIGHT
        elif event.key in INPUT_CONFIG["up_left"]:
            return InputIntent.UP_LEFT
        elif event.key in INPUT_CONFIG["up_right"]:
            return InputIntent.UP_RIGHT
        elif event.key in INPUT_CONFIG["down_left"]:
            return InputIntent.DOWN_LEFT
        elif event.key in INPUT_CONFIG["down_right"]:
            return InputIntent.DOWN_RIGHT


def _check_actions(event: pygame.event):
    """
    Get actions such as confirm or cancel, or skill usage.
    """

    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key in INPUT_CONFIG["skill0"]:
            return InputIntent.SKILL0
        elif event.key in INPUT_CONFIG["skill1"]:
            return InputIntent.SKILL1
        elif event.key in INPUT_CONFIG["skill2"]:
            return InputIntent.SKILL2
        elif event.key in INPUT_CONFIG["skill3"]:
            return InputIntent.SKILL3
        elif event.key in INPUT_CONFIG["skill4"]:
            return InputIntent.SKILL4
        elif event.key in INPUT_CONFIG["skill5"]:
            return InputIntent.SKILL5
        elif event.key in INPUT_CONFIG["confirm"]:
            return InputIntent.CONFIRM
        elif event.key in INPUT_CONFIG["exit"]:
            return InputIntent.EXIT
        elif event.key in INPUT_CONFIG["cancel"]:
            return InputIntent.CANCEL


def _check_dev_actions(event: pygame.event):
    """
    Get any dev intents
    """
    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            return InputIntent.DEBUG_TOGGLE
        elif event.key == pygame.K_F2:
            return InputIntent.DEV_TOGGLE
        elif event.key == pygame.K_F3:
            return InputIntent.BURST_PROFILE
        elif event.key == pygame.K_F4:
            return InputIntent.REFRESH_DATA
        elif event.key == pygame.K_F5:
            return InputIntent.DUNGEON_DEV_VIEW
        elif event.key == pygame.K_F6:
            return InputIntent.TOGGLE_UI

        elif event.key == pygame.K_F12:
            return InputIntent.TEST
