import cProfile
import io
import logging
import pstats

import pygame

from scripts.core.constants import GameStates
from scripts.core.global_data import world_manager, game_manager, entity_manager, turn_manager, ui_manager, \
    debug_manager
from scripts.core.input import get_input, handle_input
from scripts.core.intialisers import initialise_game

# Project Wide to do list...
# TODO - swap out nose for pytest
# TODO - setup README, setup.py and requirements.txt
# TODO - move json data to a dictionary on load; create reload/refresh function (to allow mid game changes of data)
# TODO - create global tooltip method
# TODO - skill activation events (so that animation can listen and play)
# TODO - effect activation events (so that world can update)
# TODO - text wrapping, especially in message log
# TODO - check if in battle; once damage taken keep an eye on enemy states
# TODO - change from use fps for timing to delta time


def main():
    """
    The container for the game initialisation and game loop
    """
    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = cProfile.Profile()
    profiler.enable()

    # load the game
    initialise_game()

    game_loop()

    # we've left the game loop so now close everything down

    profiler.disable()
    dump_profiling_data(profiler)
    logging.shutdown()  # clear logging resources
    pygame.quit()  # clean up pygame resources
    raise SystemExit  # exit window and python


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """
    while not game_manager.game_state == GameStates.EXIT_GAME:

        # limit frames
        game_manager.internal_clock.tick(60)

        # HANDLE INPUT
        # determine the action to take from the input with the context of the game state
        input_values = get_input()
        handle_input(input_values)

        if game_manager.game_state == GameStates.ENEMY_TURN:
            turn_manager.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        game_manager.update()
        debug_manager.update()
        world_manager.update()
        entity_manager.update(world_manager.game_map)

        # DRAW
        ui_manager.draw_game(world_manager.game_map, entity_manager.entities, debug_manager.visible)


def dump_profiling_data(profiler):
    """
    End profiling
    Args:
        profiler: The profiler
    """

    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    import datetime
    date_and_time = datetime.datetime.utcnow()

    # TODO - add version number to profile logs
    out_stream = open("logs/profiling/" + date_and_time.strftime("%d%m%y@%H%M") + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


if __name__ == "__main__":  # prevents being run from other modules
    main()
