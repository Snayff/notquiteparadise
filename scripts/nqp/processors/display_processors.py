from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytweening

from scripts.engine import utility, world
from scripts.engine.component import Aesthetic
from scripts.engine.core.constants import UIElement
from scripts.engine.utility import is_close

if TYPE_CHECKING:
    pass


def process_display_updates(delta_time: float):
    """
    Fire realtime processors.
    """
    _process_camera_update(delta_time)
    _process_aesthetic_update(delta_time)


def _process_camera_update(delta_time: float):
    """
    Update realtime camera timers, such as the camera scrolling to reveal new tiles.
    """
    camera = world.ui.get_element(UIElement.CAMERA)

    if not camera:
        return

    max_duration = 1

    # increment time
    camera.current_sprite_duration += delta_time

    if not camera.has_reached_target():

        # time for animation exceeded
        time_exceeded = camera.current_sprite_duration > max_duration

        # time for animation exceeded or animation very close to end
        if time_exceeded or is_close((camera.start_tile_col, camera.start_tile_row),
                                     (camera.target_tile_col, camera.target_tile_row)):

            # set start_tile to target
            camera.set_start_to_target()

        # keep moving:
        else:

            lerp_amount = pytweening.easeOutCubic(min(1.0, camera.current_sprite_duration / max_duration))
            col_ = utility.lerp(camera.start_tile_col, camera.target_tile_col, lerp_amount)
            row_ = utility.lerp(camera.start_tile_row, camera.target_tile_row, lerp_amount)

            camera.set_start_col_row((col_, row_))

    # not moving
    else:
        camera.current_sprite_duration = 0


def _process_aesthetic_update(delta_time: float):
    """
    Update real-time timers on entities, such as entity animations.
    """
    # move entities screen position towards target
    for entity, (aesthetic, ) in world.get_components([Aesthetic]):
        # cast for typing
        aesthetic = cast(Aesthetic, aesthetic)

        max_duration = 0.2

        # increment time
        aesthetic.current_sprite_duration += delta_time

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
