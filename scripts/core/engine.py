
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
from scripts.core.initialisers import initialise_game, initialise_event_handlers, initialise_logging


# Project Wide to do list...
# TODO - swap out nose for pytest
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
# TODO - standardise use of xy and tile xy. xy for pixels, tile xy for grid
# TODO - convert interventions to skills, gods to entities
# TODO - move skills to their own json and only hold skill names in the savvy, homeland etc.
# TODO - add skill modifiers (blessings?)
# TODO - ensure all skills in json have required fields
# TODO - write tests / checking for json values


def main():
    """
    The entry for the game initialisation and game loop
    """

    # initialise logging
    initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = cProfile.Profile()
    profiler.enable()

    # initialise the game
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

        # get delta time and set frame rate with .tick()
        delta_time = game.internal_clock.tick(60) / 1000.0

        if game.game_state == GameStates.ENEMY_TURN:
            turn.turn_holder.ai.take_turn()

        # update based on input events
        for event in pygame.event.get():
            input.update(event)
            ui.process_events(event)

        # allow everything to update in response to new state
        game.update()
        debug.update()
        world.update()
        ui.update(delta_time)
        event_hub.update()

        # show the new state
        debug.draw()
        ui.draw()


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
