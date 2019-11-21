
import cProfile
import io
import logging
import pstats
import pygame
from scripts.core.constants import GameStates
from scripts.managers.input_manager import input
from scripts.managers.ui_manager import ui
from scripts.managers.debug_manager import debug
from scripts.managers.turn_manager import turn
from scripts.managers.world_manager import world
from scripts.managers.game_manager import game
from scripts.core.event_hub import event_hub
from scripts.core.initialisers import initialise_game, initialise_event_handlers, initialise_logging, \
    initialise_ui_elements


# Project Wide to do list...
# TODO - create global tooltip method - some relevant code in old message `log -
#  when object created needs a tooltip: pass the rect and create link to a tooltip obj (ui_man?) to store and refer
#  back to. Needs to be able to get updated strings (info not always static) and updated positions
# TODO - swap out nose for pytest
# TODO - change from use fps for timing to delta time
# TODO - draw dirty for map section (use an array to store ref to dirty x,y OR dirty flag on each tile)
# TODO - remember window position and resume at that place
# TODO - move assignation of Owner to the init
# TODO - Review closure
#  https://en.wikipedia.org/wiki/Closure_(computer_programming)
# TODO - Review compression example
#  https://gist.github.com/brianbruggeman/61199d1ddbbf220a4b5cc528da13b5c8
# TODO - move the docstring annotations to the function line, then install mypy
# TODO - use seed for RNG
# TODO - new lighting system
#  entities create light, sight range shows light in range


def main():
    """
    The parent_widget for the game initialisation and game loop
    """
    # initialise logging
    initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = cProfile.Profile()
    profiler.enable()

    # initialise the game
    initialise_ui_elements()
    initialise_event_handlers()
    initialise_game()

    # run the game
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

    while not game.game_state == GameStates.EXIT_GAME:

        # limit frames
        game.internal_clock.tick(60)

        if game.game_state == GameStates.ENEMY_TURN:
            turn.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        input.update()
        game.update()
        debug.update()
        world.update()
        ui.update()
        event_hub.update()

        # DRAW
        debug.draw()
        ui.Element.draw_visible_elements()


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
    out_stream = open("logs/profiling/" + date_and_time.strftime("%y%m%d@%H%M") + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


if __name__ == "__main__":  # prevents being run from other modules
    main()
