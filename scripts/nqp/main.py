from __future__ import annotations

import logging
import sys
import traceback

import pygame
import snecs
from snecs.world import default_world

import scripts.nqp.processors.input
from scripts.engine import chronicle, debug, state, world
from scripts.engine.component import NQPComponent
from scripts.engine.core.constants import GameState
from scripts.engine.debug import enable_profiling, initialise_logging, kill_logging
from scripts.engine.ui.manager import ui
from scripts.nqp import processors
from scripts.nqp.actions import afflictions, behaviours, skills  # must import to register in engine
from scripts.nqp.command import initialise_game
from scripts.nqp.processors import display, game, interactions


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
        # this copies snecs.process_pending_deletions() but adds extra steps.
        for entity in list(default_world._entities_to_delete):
            components = dict(world.get_entitys_components(entity))
            for component in components.values():
                assert isinstance(component, NQPComponent)
                component.on_delete()
            snecs.delete_entity_immediately(entity, default_world)

        # have enemy take turn
        if current_state == GameState.GAMEMAP and turn_holder != world.get_player():
            # just in case the turn holder has died but not been replaced as expected
            try:
                world.take_turn(turn_holder)
            except KeyError:
                chronicle.rebuild_turn_queue()

        # update based on input events
        for event in pygame.event.get():
            processors.input.process_event(event, current_state)
            processors.game.process_event(event, current_state)
            processors.interactions.process_event(event)  # only happens in gamemap so doesnt need state
            ui.process_ui_events(event)

        # allow everything to update in response to new state
        display.process_display_updates(time_delta, current_state)
        debug.update()
        ui.update(time_delta)

        # show the new state
        ui.draw()


if __name__ == "__main__":  # prevents being run from other modules
    main()
