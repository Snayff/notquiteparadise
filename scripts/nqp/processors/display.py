from __future__ import annotations

from typing import cast

import pytweening

from scripts.engine import utility, world
from scripts.engine.component import Aesthetic, LightSource
from scripts.engine.core import queries
from scripts.engine.core.constants import GameState, GameStateType, TILE_SIZE, UIElement
from scripts.engine.ui.manager import ui
from scripts.engine.utility import is_close

__all__ = ["process_display_updates"]


def process_display_updates(time_delta: float, game_state: GameStateType):
    """
    Fire realtime processors.
    """
    if game_state == GameState.GAMEMAP:
        _process_aesthetic_update(time_delta)
        _process_lighting()


def _process_aesthetic_update(time_delta: float):
    """
    Update aesthetics, such as entity animations and draw positions.
    """
    # move entities screen position towards target
    for entity, (aesthetic,) in queries.aesthetic:
        # cast for typing
        aesthetic = cast(Aesthetic, aesthetic)

        max_duration = 0.5

        # increment time
        aesthetic.current_sprite_duration += time_delta

        # Have we exceeded animation duration?
        time_exceeded = aesthetic.current_sprite_duration > max_duration

        # do we need to show moving to a new position?
        if aesthetic.draw_x != aesthetic.target_draw_x or aesthetic.draw_y != aesthetic.target_draw_y:

            # time for animation exceeded or animation very close to end
            if time_exceeded or is_close(
                (aesthetic.draw_x, aesthetic.draw_y), (aesthetic.target_draw_x, aesthetic.target_draw_y)
            ):

                # set to target
                aesthetic.draw_x = aesthetic.target_draw_x
                aesthetic.draw_y = aesthetic.target_draw_y

                # reset to idle
                aesthetic.current_sprite = aesthetic.sprites.idle
                aesthetic.current_sprite_duration = 0

            # keep moving:
            else:
                lerp_amount = pytweening.easeOutCubic(min(1.0, aesthetic.current_sprite_duration * 2))
                aesthetic.draw_x = utility.lerp(aesthetic.draw_x, aesthetic.target_draw_x, lerp_amount)
                aesthetic.draw_y = utility.lerp(aesthetic.draw_y, aesthetic.target_draw_y, lerp_amount)

        # arrived at destination
        else:
            aesthetic.current_sprite = aesthetic.sprites.idle
            aesthetic.current_sprite_duration = 0


def _process_lighting():
    """
    Update lighting draw position using light sources of all entities
    """
    # get game map details
    game_map = world.get_game_map()
    light_box = game_map.light_box

    # get camera for world pos
    camera = ui.get_element(UIElement.CAMERA)

    # process all light sources
    for entity, (light_source, aesthetic) in queries.light_source_and_aesthetic:
        light_source: LightSource
        aesthetic: Aesthetic

        # update lights in the light box
        light = light_box.get_light(light_source.light_id)
        draw_pos = camera.world_to_draw_position((aesthetic.draw_x, aesthetic.draw_y))
        light.position = [draw_pos[0], draw_pos[1]]

