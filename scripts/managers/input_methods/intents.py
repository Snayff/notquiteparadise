from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Intents:
    """
    Hold the input intents
    """
    up: bool = False
    down: bool = False
    left: bool = False
    right: bool = False
    up_right: bool = False
    up_left: bool = False
    down_right: bool = False
    down_left: bool = False
    confirm: bool = False
    cancel: bool = False
    exit_game: bool = False
    skill0: bool = False
    skill1: bool = False
    skill2: bool = False
    skill3: bool = False
    skill4: bool = False
    skill5: bool = False
    refresh_data: bool = False
    button_pressed: bool = False
    debug_toggle: bool = False
    dev_toggle: bool = False