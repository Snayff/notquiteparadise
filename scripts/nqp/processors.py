from __future__ import annotations

import pytweening
from scripts.engine import utilities, entity
from scripts.engine.components import Aesthetic
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def process_all(delta_time: float):
    """
    Process all processors
    """
    _process_aesthetic_update(delta_time)


def _process_aesthetic_update(delta_time: float):
    """
    Update real-time timers on entities
    """
    # move entities screen position towards target
    for ent, aesthetic in entity.get_component(Aesthetic):
        max_duration = 0.3

        # increment time
        aesthetic.current_sprite_duration += delta_time

        # do we need to show moving to a new position? Have we exceeded animation duration?
        if (aesthetic.screen_x != aesthetic.target_screen_x or aesthetic.screen_y != aesthetic.target_screen_y) \
                and aesthetic.current_sprite_duration <= max_duration:
            # are we close?
            if (aesthetic.screen_x - 1 < aesthetic.target_screen_x < aesthetic.screen_x + 1) and \
                    (aesthetic.screen_y - 1 < aesthetic.target_screen_y < aesthetic.screen_y + 1):
                # jump to target
                aesthetic.screen_x = aesthetic.target_screen_x
                aesthetic.screen_y = aesthetic.target_screen_y

            # keep moving:
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, aesthetic.current_sprite_duration * 2))
                aesthetic.screen_x = utilities.lerp(aesthetic.screen_x, aesthetic.target_screen_x, lerp_amount)
                aesthetic.screen_y = utilities.lerp(aesthetic.screen_y, aesthetic.target_screen_y, lerp_amount)
        # not moving so reset to idle
        else:
            aesthetic.current_sprite = aesthetic.sprites.idle
            aesthetic.current_sprite_duration = 0