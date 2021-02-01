from __future__ import annotations

import pytweening

from scripts.engine.core import query, utility, world
from scripts.engine.core.component import Aesthetic, LightSource
from scripts.engine.core.utility import is_close
from scripts.engine.internal.constant import GameState, SpriteCategory, TILE_SIZE

__all__ = ["process_updates"]


def process_updates(time_delta: float, game_state: GameState):
    """
    Fire realtime processors.
    """
    if game_state == GameState.GAME_MAP:
        _process_aesthetic_update(time_delta)
        _process_lighting()


def _process_aesthetic_update(time_delta: float):
    """
    Update aesthetics, such as entity animations and draw positions.
    """
    # move entities screen position towards target
    for entity, (_, aesthetic,) in query.active_and_aesthetic:
        assert isinstance(aesthetic, Aesthetic)

        # ignore idle
        if aesthetic.current_sprite_category == SpriteCategory.IDLE:
            continue

        max_duration = 0.3

        # increment time
        aesthetic.current_sprite_duration += time_delta

        # Have we exceeded animation duration?
        time_exceeded = aesthetic.current_sprite_duration > max_duration

        # if moving, do we need to show moving to a new position?
        if aesthetic.draw_x != aesthetic.target_draw_x or aesthetic.draw_y != aesthetic.target_draw_y:
            lerp_amount = pytweening.easeOutCubic(min(1.0, aesthetic.current_sprite_duration))
            aesthetic.draw_x = utility.lerp(aesthetic.draw_x, aesthetic.target_draw_x, lerp_amount)
            aesthetic.draw_y = utility.lerp(aesthetic.draw_y, aesthetic.target_draw_y, lerp_amount)

        # time for animation exceeded
        if time_exceeded:
            aesthetic.set_draw_to_target()
            aesthetic.set_current_sprite(SpriteCategory.IDLE)


def _process_lighting():
    """
    Update lighting draw position using light sources of all entities
    """
    # get game map details
    game_map = world.get_game_map()
    light_box = game_map.light_box

    # process all light sources
    for entity, (light_source, aesthetic) in query.light_source_and_aesthetic:
        light_source: LightSource
        aesthetic: Aesthetic

        # update lights in the light box
        try:
            light = light_box.get_light(light_source.light_id)
        except KeyError:
            print(light_source.light_id, light_box, light_box.lights)
            raise KeyError()
        x = aesthetic.draw_x * TILE_SIZE + (TILE_SIZE / 2)
        y = aesthetic.draw_y * TILE_SIZE + (TILE_SIZE / 2)
        light.position = [x, y]
