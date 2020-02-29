from __future__ import annotations

import pygame
from scripts.core.constants import GameStates
from scripts.managers.input_manager.input_manager import input
from scripts.managers.ui_manager.ui_manager import ui

from scripts.managers.world_manager.world_manager import world
from scripts.managers.game_manager.game_manager import game
from scripts.core.event_hub import event_hub
from scripts.core.initialisers import initialise_game, initialise_event_handlers

# Project Wide to do list...
# FIXME - collision isnt working - can walk through walls
# FIXME - Directions not working - cant basic attack in any direction.
# TODO - swap out nose for pytest
# TODO - remember window position and resume at that place
# TODO - Review closure
#  https://en.wikipedia.org/wiki/Closure_(computer_programming)
# TODO - Review compression example
#  https://gist.github.com/brianbruggeman/61199d1ddbbf220a4b5cc528da13b5c8
# TODO - install mypy
# TODO - use seed for RNG
# TODO - new lighting system
#  entities create light, sight range shows light in range
# TODO - standardise use of xy and tile xy. xy as standard, meaning tiles. otherwise use screen_xy
# TODO - add skill modifiers (blessings?)
# TODO - write tests / checking for json values - use schema
# TODO - could turn manager sit under game?
# TODO - add piercing so projectile can damage and keep going
# TODO - add projectiles, i.e. entity creation, movement and collision
# TODO - multi-tile entities
# TODO - write tests to check data values against expected, e.g. total stat per characteristic should be +5
# TODO - edit the UI json
# TODO - ingame descriptions written first hand by observes. Like excerpts from a book.
# TODO - use a global for font size so it can be amended in options


def main():
    """
    The entry for the game initialisation and game loop
    """
    # initialise logging
    game.Debug.initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    game.Debug.initialise_profiling()

    # initialise the game
    initialise_event_handlers()
    initialise_game()

    # run the game
    game_loop()

    # we've left the game loop so now close everything down
    game.Debug.disable_profiling()
    game.Debug.dump_profiling_data()
    game.Debug.disable_logging()

    pygame.quit()  # clean up pygame resources

    raise SystemExit  # exit window and python


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """

    while not game.State.get_current() == GameStates.EXIT_GAME:

        # get delta time to support UI updates
        delta_time = game.State.get_delta_time()

        if game.State.get_current() == GameStates.ENEMY_TURN:
            pass
            #turn.turn_holder.ai.take_turn()

        # update based on input events
        for event in pygame.event.get():
            input.update(event, game.State.get_current())
            ui.process_ui_events(event)
            ui.handle_ui_events(event)

        # allow everything to update in response to new state
        game.update()
        world.update(delta_time)
        ui.update(delta_time)
        event_hub.update()

        # show the new state
        ui.draw()


if __name__ == "__main__":  # prevents being run from other modules
    main()
