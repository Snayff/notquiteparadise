from __future__ import annotations

import pygame  # type: ignore
from typing import TYPE_CHECKING, Type, Union, Optional

from scripts.engine.core.constants import InputIntent, InputIntentType

if TYPE_CHECKING:
    pass


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
    # TODO - refer to key mapping to enable key rebinding

    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_KP8 or event.key == pygame.K_k:
            return InputIntent.UP
        elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2 or event.key == pygame.K_j:
            return InputIntent.DOWN
        elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4 or event.key == pygame.K_h:
            return InputIntent.LEFT
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6 or event.key == pygame.K_l:
            return InputIntent.RIGHT
        elif event.key == pygame.K_KP7 or event.key == pygame.K_y:
            return InputIntent.UP_LEFT
        elif event.key == pygame.K_KP9 or event.key == pygame.K_u:
            return InputIntent.UP_RIGHT
        elif event.key == pygame.K_KP1 or event.key == pygame.K_b:
            return InputIntent.DOWN_LEFT
        elif event.key == pygame.K_KP3 or event.key == pygame.K_n:
            return InputIntent.DOWN_RIGHT


def _check_actions(event: pygame.event):
    """
    Get actions such as confirm or cancel, or skill usage.
    """
    # TODO - refer to key mapping to enable key rebinding
    # handle key press events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            return InputIntent.SKILL0
        elif event.key == pygame.K_2:
            return InputIntent.SKILL1
        elif event.key == pygame.K_3:
            return InputIntent.SKILL2
        elif event.key == pygame.K_4:
            return InputIntent.SKILL3
        elif event.key == pygame.K_5:
            return InputIntent.SKILL4
        elif event.key == pygame.K_RETURN:
            return InputIntent.CONFIRM
        elif event.key == pygame.K_ESCAPE:
            return InputIntent.EXIT_GAME


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
