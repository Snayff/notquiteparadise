from __future__ import annotations

import logging
import sys
import traceback

import pygame
import snecs
from snecs.world import default_world

import scripts.nqp.processors.input
from scripts.engine.core import chronicle, state, world
from scripts.engine.core.component import NQPComponent
from scripts.engine.core.ui import ui
from scripts.engine.internal import debug
from scripts.engine.internal.constant import GameState
from scripts.engine.internal.debug import enable_profiling, initialise_logging, kill_logging
from scripts.engine.internal.event import event_hub
from scripts.nqp import processors
from scripts.nqp.command import initialise_game
from scripts.nqp.processors import display
from scripts.nqp.ui_elements.camera import camera


def main():
    """
    The entry for the game initialisation and game loop
    """
    # init engine resources
    state.initialise_engine()

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
        if current_state == GameState.GAME_MAP:
            if turn_holder != world.get_player():
                # just in case the turn holder has died but not been replaced as expected
                try:
                    world.take_turn(turn_holder)
                except KeyError:
                    chronicle.rebuild_turn_queue()

        # process pygame events
        for event in pygame.event.get():
            processors.input.process_input_event(event, current_state)
            ui.process_ui_events(event)

        # process NQP events
        event_hub.update()

        # allow everything to update in response to new state
        display.process_updates(time_delta, current_state)
        debug.update()
        ui.update(time_delta)

        try:
            if current_state in [GameState.GAME_MAP, GameState.MENU, GameState.TARGETING]:
                # show the new state
                camera.update(time_delta)
                camera.render(ui._window)
        except AttributeError:
            pass

        ui.draw()


if __name__ == "__main__":  # prevents being run from other modules
    main()
