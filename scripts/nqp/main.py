from __future__ import annotations

import cProfile
import datetime
import io
import logging
import pstats
import sys
import time
import traceback
import pygame
import snecs
from snecs.world import default_world
from scripts.engine import chronicle, debug, key, state, world
from scripts.engine.core.constants import GameState, UIElement, VERSION
from scripts.engine.ui.manager import ui
from scripts.nqp.processors import display_processors, input_processors


def main():
    """
    The entry for the game initialisation and game loop
    """
    # initialise logging
    initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = create_profiler()

    # initialise the game
    initialise_game()

    # run the game
    try:
        game_loop()
    except Exception:
        logging.critical(f"Something went wrong and killed the game loop")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in tb_list:
            clean_line = line.replace("\n", "")
            logging.critical(f"{clean_line}")
        traceback.print_exc()

    # we've left the game loop so now close everything down
    disable_profiling(profiler)
    dump_profiling_data(profiler)
    disable_logging()

    # print debug values
    debug.dump()

    pygame.quit()  # clean up pygame resources

    raise SystemExit  # exit window and python


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """

    while not state.get_current() == GameState.EXIT_GAME:

        # get info to support UI updates and handling events
        delta_time = state.get_delta_time()
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

        # progress frame
        state.update_clock()


def initialise_logging():
    """
    Configure logging

    Logging levels:
        CRITICAL - A serious error, indicating that may be unable to continue running.
        ERROR - A more serious problem, has not been able to perform some function.
        WARNING - An indication that something unexpected happened, but otherwise still working as expected.
        INFO - Confirmation that things are working as expected.
        DEBUG - Detailed information, typically of interest only when diagnosing problems

    File mode options:
        'r' - open for reading(default)
        'w' - open for writing, truncating the file first
        'x' - open for exclusive creation, failing if the file already exists
        'a' - open for writing, appending to the end of the file if it exists

    """

    log_file_name = "logs/" + "game.log"
    log_level = logging.DEBUG
    file_mode = "w"

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # 8 adds space for 8 characters (# CRITICAL)
    log_format = "%(asctime)s| %(levelname)-8s| %(message)s"
    logging.basicConfig(filename=log_file_name, filemode=file_mode, level=log_level,
                        format=log_format)

    # format into uk time
    logging.Formatter.converter = time.gmtime


def create_profiler():
    """
    Create and enable the profiler
    """
    profiler = cProfile.Profile()
    profiler.enable()

    return profiler


def disable_logging():
    """
    Turn off current logging and clear logging resources
    """
    logging.shutdown()


def disable_profiling(profiler):
    """
    Turn off current profiling
    """
    profiler.disable()


def dump_profiling_data(profiler):
    """
    Dump data to a readable file
    """
    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    date_and_time = datetime.datetime.utcnow()
    out_stream = open("logs/profiling/" + date_and_time.strftime("%Y%m%d@%H%M") + "_" + VERSION + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


def initialise_game():
    """
    Init the game`s required info
    """
    map_width = 50
    map_height = 30
    world.create_gamemap(map_width, map_height)

    # init the player
    player = world.create_actor("player", "a desc", 1, 2, ["shoom", "soft_tops", "dandy"], True)
    world.recompute_fov(player)

    # tell places about the player
    chronicle.set_turn_holder(player)

    # create an enemy
    # TODO - remove when enemy gen is in
    world.create_actor("dummy steve", "steve's desc", 1, 4, ["training_dummy"])
    world.create_actor("dummy steve", "steve's desc", 1, 5, ["training_dummy"])

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

    # FIXME - entities load before camera so they cant get their screen position. If ui loads before entities then it
    #  fails due to player not existing. Below is a hacky fix.
    from scripts.engine.component import Aesthetic, Position
    for entity, (aesthetic, position) in world.get_components([Aesthetic, Position]):
        aesthetic.draw_x, aesthetic.draw_y = (position.x, position.y)
        aesthetic.target_draw_x = aesthetic.draw_x
        aesthetic.target_draw_y = aesthetic.draw_y

    # init controls
    key.load_input_list_from_config()

    # loading finished, give player control
    state.set_new(GameState.GAMEMAP)

    # prompt turn actions
    world.end_turn(player, 0)


if __name__ == "__main__":  # prevents being run from other modules
    main()
