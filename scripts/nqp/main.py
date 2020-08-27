from __future__ import annotations

import logging
import sys
import traceback

import pygame
import snecs
from snecs.world import default_world

from scripts.engine import chronicle, debug, state, world
from scripts.engine.core.constants import GameState, UIElement
from scripts.engine.core.definitions import ActorData
from scripts.engine.core.store import store
from scripts.engine.debug import (
    enable_profiling,
    initialise_logging,
    kill_logging,
)
from scripts.engine.ui.manager import ui
from scripts.engine.world_objects.gamemap import GameMap
from scripts.nqp.processors import display_processors, input_processors


def main():
    """
    The entry for the game initialisation and game loop
    """
    # initialise logging
    if debug.IS_LOGGING:
        initialise_logging()

    # initialise profiling
    if debug.IS_PROFILING:
        enable_profiling()

    # initialise the game
    initialise_game()

    # run the game
    try:
        game_loop()

    except Exception:
        logging.critical(f"Something went wrong and killed the game loop!")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in tb_list:
            clean_line = line.replace("\n", "")
            logging.critical(f"{clean_line}")
        traceback.print_exc()

    # dump any held save data
    state.dump_save_game()

    # we've left the game loop so now close everything down
    if debug.IS_LOGGING:
        kill_logging()
        # print debug values
        debug.print_values_to_console()
    if debug.IS_PROFILING:
        debug.kill_profiler()

    # clean up pygame resources
    pygame.quit()

    # exit window and python
    raise SystemExit


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """
    while not state.get_current() == GameState.EXIT_GAME:
        # progress frame
        delta_time = state.update_clock()

        # get info to support UI updates and handling events
        current_state = state.get_current()
        turn_holder = chronicle.get_turn_holder()

        # process any deletions from last frame
        snecs.process_pending_deletions(default_world)

        # have enemy take turn
        if current_state == GameState.GAMEMAP and turn_holder != world.get_player():
            # just in case the turn holder has died but not been replaced as expected
            try:
                world.take_turn(turn_holder)
            except AttributeError:
                chronicle.rebuild_turn_queue()

        # update based on input events
        for event in pygame.event.get():
            input_processors.process_event(event, current_state)
            ui.process_ui_events(event)

        # allow everything to update in response to new state
        display_processors.process_display_updates(delta_time)
        debug.update()
        ui.update(delta_time)

        # show the new state
        ui.draw()


def _create_entity_pool() -> EntityPool:
    """
    Return a pool of entities for the gamemap
    """
    pool = EntityPool()
    pool.add("player", "a desc", [(0, 0)], ["shoom", "soft_tops", "dandy"], True, 1, 1),
    pool.add("dummy steve", "steve's desc", [(0, 0)], ["training_dummy"], False, 3, 0.25)
    return pool


def initialise_game():
    """
    Init the game`s required info
    """
    # init and save map
    game_map = GameMap("cave", 10)
    store.current_gamemap = game_map

    # populate the map
    player_data = ActorData(["player"], "a desc", [(0, 0)], ["shoom", "soft_tops", "dandy"])
    game_map.generate_new_map(player_data)

    # init the player
    player = world.get_player()
    world.recompute_fov(player)

    # tell places about the player
    chronicle.set_turn_holder(player)

    # create a god
    world.create_god("the_small_gods")

    # turn on the ui
    ui.init_all_ui_elements()

    # show the ui
    ui.set_element_visibility(UIElement.CAMERA, True)
    ui.set_element_visibility(UIElement.MESSAGE_LOG, True)
    ui.set_element_visibility(UIElement.SKILL_BAR, True)

    # welcome message
    ui.create_screen_message("Welcome to Not Quite Paradise", "", 6)

    # FIXME - entities load before camera so they cant get their screen position.
    #  If ui loads before entities then it fails due to player not existing. Below is a hacky fix.
    from scripts.engine.component import Aesthetic, Position, FOV
    for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
        aesthetic.draw_x, aesthetic.draw_y = (position.x, position.y)
        aesthetic.target_draw_x = aesthetic.draw_x
        aesthetic.target_draw_y = aesthetic.draw_y

    # entities load with a blank fov, update them now
    for entity, (fov, position) in world.get_components([FOV, Position]):
        world.update_tile_visibility(fov.map)

    # loading finished, give player control
    state.set_new(GameState.GAMEMAP)

    # prompt turn actions
    chronicle.end_turn(player, 0)


if __name__ == "__main__":  # prevents being run from other modules
    main()
