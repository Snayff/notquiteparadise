from dataclasses import dataclass


@dataclass()
class Intents:
    """
    Hold the input intents
    """
    up = False
    down = False
    left = False
    right = False
    up_right = False
    up_left = False
    down_right = False
    down_left = False
    confirm = False
    cancel = False
    debug_toggle = False
    skill0 = False
    skill1 = False
    skill2 = False
    skill3 = False
    skill4 = False
    refresh_data = False