from __future__ import annotations

import logging
import sys
import traceback

import pygame
import snecs
from snecs.world import default_world

from scripts.engine import chronicle, debug, state, world
from scripts.engine.core.constants import GameState, UIElement
from scripts.engine.debug import enable_profiling, initialise_logging, kill_logging
from scripts.engine.ui.manager import ui
from scripts.nqp.actions import skills  # must import to register skills
from scripts.nqp.processors import display_processors, input_processors


def main():
    """
    The entry for the game initialisation and game loop
    """
    # initialise logging
    if debug.is_logging():
        initialise_logging()

    # initialise profiling
    if debug.is_profiling():
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
    if debug.is_logging():
        kill_logging()
        # print debug values
        debug.print_values_to_console()
    if debug.is_profiling():
        debug.kill_profiler()

    # clean up pygame resources
    pygame.quit()

    # exit window and python
    raise SystemExit


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """
    while not state.get_current() == GameState.EXITING:
        # progress frame
        time_delta = state.update_clock()

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
        display_processors.process_display_updates(time_delta)
        debug.update()
        ui.update(time_delta)

        # show the new state
        ui.draw()


def initialise_game():
    """
    Init the game`s required info
    """
    state.set_new(GameState.MENU)
    ui.set_element_visibility(UIElement.TITLE_SCREEN, True)


if __name__ == "__main__":  # prevents being run from other modules
    main()
