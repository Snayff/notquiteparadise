from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytweening

from scripts.engine import utility, world
from scripts.engine.component import Aesthetic
from scripts.engine.core.constants import UIElement
from scripts.engine.utility import is_close

if TYPE_CHECKING:
    pass


def process_display_updates(time_delta: float):
    """
    Fire realtime processors.
    """
    _process_aesthetic_update(time_delta)


def _process_aesthetic_update(time_delta: float):
    """
    Update real-time timers on entities, such as entity animations.
    """
    # move entities screen position towards target
    for entity, (aesthetic, ) in world.get_components([Aesthetic]):
        # cast for typing
        aesthetic = cast(Aesthetic, aesthetic)

        max_duration = 0.3

        # increment time
        aesthetic.current_sprite_duration += time_delta

        # Have we exceeded animation duration?
        time_exceeded = aesthetic.current_sprite_duration > max_duration

        # do we need to show moving to a new position?
        if aesthetic.draw_x != aesthetic.target_draw_x or aesthetic.draw_y != aesthetic.target_draw_y:

            # time for animation exceeded or animation very close to end
            if time_exceeded or is_close((aesthetic.draw_x, aesthetic.draw_y),
                                         (aesthetic.target_draw_x, aesthetic.target_draw_y)):

                # set to target
                aesthetic.draw_x = aesthetic.target_draw_x
                aesthetic.draw_y = aesthetic.target_draw_y

            # keep moving:
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, aesthetic.current_sprite_duration * 2))
                aesthetic.draw_x = utility.lerp(aesthetic.draw_x, aesthetic.target_draw_x, lerp_amount)
                aesthetic.draw_y = utility.lerp(aesthetic.draw_y, aesthetic.target_draw_y, lerp_amount)

        # if not moving and the animation ended then reset to idle
        elif (aesthetic.current_sprite == aesthetic.sprites.move) or time_exceeded:
            aesthetic.current_sprite = aesthetic.sprites.idle
            aesthetic.current_sprite_duration = 0
