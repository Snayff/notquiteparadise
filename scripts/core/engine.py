
import cProfile
import io
import logging
import pstats
import pygame

from scripts.core.constants import GameStates
from scripts.global_singletons.managers import world_manager, game_manager, turn_manager, ui_manager, debug_manager, \
    input_manager, start
from scripts.global_singletons.event_hub import event_hub
from scripts.core.initialisers import initialise_game, initialise_event_handlers, initialise_logging


# Project Wide to do list...
# TODO - UI information should be pulled once then held
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





def main():
    """
    The container for the game initialisation and game loop
    """
    # initialise logging
    initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = cProfile.Profile()
    profiler.enable()

    #################################################
    # alternate approach to init the managers
    # TODO - determine if alternate approach is worthwhile
    start()
    from scripts.global_singletons import managers
    managers.game_manager2.update_game_state(GameStates.PLAYER_TURN)
    #################################################

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
    while not game_manager.game_state == GameStates.EXIT_GAME:

        # limit frames
        game_manager.internal_clock.tick(60)

        if game_manager.game_state == GameStates.ENEMY_TURN:
            turn_manager.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        input_manager.update()
        game_manager.update()
        debug_manager.update()
        world_manager.update()
        ui_manager.update()
        event_hub.update()

        # DRAW
        ui_manager.draw_game(world_manager.game_map, debug_manager.visible)


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
