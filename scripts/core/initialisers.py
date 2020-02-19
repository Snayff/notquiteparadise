import logging
import time
import pygame

from scripts.core.constants import EventTopics, GameStates, TILE_SIZE
from scripts.event_handlers.god_handler import GodHandler
from scripts.event_handlers.map_handler import MapHandler
from scripts.event_handlers.entity_handler import EntityHandler
from scripts.events.game_events import ChangeGameStateEvent
from scripts.event_handlers.game_handler import GameHandler
from scripts.core.event_hub import publisher, event_hub
from scripts.managers.turn_manager import turn
from scripts.managers.world_manager.world_manager import world
from scripts.event_handlers.ui_handler import UiHandler


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
    # TODO - move to engine

    log_file_name = "logs/" + "game.log"
    log_level = logging.INFO
    file_mode = "w"

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename=log_file_name, filemode=file_mode, level=log_level,
                        format="%(asctime)s| %(levelname)-8s| %(message)s")  # 8 adds space for 8 characters (CRITICAL)

    # format in uk time
    logging.Formatter.converter = time.gmtime


def initialise_game():
    """
    Init the game`s required info
    """
    # TODO - move to event handlers

    map_width = 50
    map_height = 30
    world.Map.create_game_map(map_width, map_height)

    # init the player
    world.FOV.create_player_fov_map(map_width, map_height)
    player = world.Entity.create_actor("player", "a desc", 1, 2, "shoom", "soft_tops",
                                       "irascible_dandy", True)

    turn.turn_holder = player

    # create an enemy
    # TODO - remove when enemy gen is in
    enemy = world.Entity.create_actor("steve", "steve's desc", 1, 4, "goblynn", "soft_tops",
                                      "fungechist")

    # create a god
    god = world.Entity.create_god("the_small_gods")

    publisher.publish(ChangeGameStateEvent(GameStates.GAME_INITIALISING))


def initialise_event_handlers():
    """
    Create the various event handlers and subscribe to required events.
    """
    game_handler = GameHandler(event_hub)
    game_handler.subscribe(EventTopics.GAME)

    entity_handler = EntityHandler(event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)

    map_handler = MapHandler(event_hub)
    map_handler.subscribe(EventTopics.MAP)
    map_handler.subscribe(EventTopics.GAME)

    god_handler = GodHandler(event_hub)
    god_handler.subscribe(EventTopics.ENTITY)

    ui_handler = UiHandler(event_hub)
    ui_handler.subscribe(EventTopics.ENTITY)
    ui_handler.subscribe(EventTopics.GAME)
    ui_handler.subscribe(EventTopics.UI)
