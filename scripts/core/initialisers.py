import logging
import time

from scripts.core.constants import EventTopics, GameStates, MessageEventTypes, UIElementTypes
from scripts.event_handlers.affliction_handler import AfflictionHandler
from scripts.event_handlers.god_handler import GodHandler
from scripts.event_handlers.map_handler import MapHandler
from scripts.events.entity_events import LearnEvent
from scripts.event_handlers.entity_handler import EntityHandler
from scripts.events.game_events import ChangeGameStateEvent
from scripts.events.message_events import MessageEvent
from scripts.event_handlers.message_handler import MessageHandler
from scripts.event_handlers.game_handler import GameHandler
from scripts.global_singletons.event_hub import publisher, event_hub
from scripts.global_singletons.managers import game_manager, world_manager, turn_manager, ui_manager
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
    log_file_name = "logs/" + "game.log"
    log_level = logging.DEBUG
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

    map_width = 50
    map_height = 30
    world_manager.Map.create_game_map(map_width, map_height)
    world_manager.FOV.create_player_fov_map(map_width, map_height)

    # TODO - remove when map generation is in
    world_manager.Entity.create_actor_entity(0, 0, "player", "player", True)
    world_manager.Entity.create_actor_entity(0, 3, "goblinn_hand", "steve")
    world_manager.Entity.create_actor_entity(1, 4, "goblinn_hand", "bob")
    world_manager.Entity.create_actor_entity(2, 3, "goblinn_hand", "estaban")
    world_manager.God.create_god("the small gods")

    # TODO - remove when skill learning is in
    # publisher.publish(LearnEvent(world_manager.player, "cleromancer", "basic attack"))
    # publisher.publish(LearnEvent(world_manager.player, "cleromancer", "throw dice"))
    # publisher.publish(LearnEvent(world_manager.player, "cleromancer", "bring down the mountain"))
    # publisher.publish(LearnEvent(world_manager.player, "cleromancer", "burn the deck"))
    publisher.publish(LearnEvent(world_manager.player, "Fungechist", "Flail"))
    publisher.publish(LearnEvent(world_manager.player, "Fungechist", "Eye-watering Mistake"))
    publisher.publish(LearnEvent(world_manager.player, "Fungechist", "Fractious Fungi"))

    publisher.publish(ChangeGameStateEvent(GameStates.GAME_INITIALISING))
    #game_manager.update_game_state(GameStates.GAME_INITIALISING)  # TODO remove when main menu is starting point
    turn_manager.turn_holder = world_manager.player

    publisher.publish(MessageEvent(MessageEventTypes.BASIC, "Welcome to #col.info Not #col.info "
                                                            "Quite  #col.info Paradise. "))


def initialise_event_handlers():
    """
    Create the various event handlers and subscribe to required events.
    """
    game_handler = GameHandler(event_hub)
    game_handler.subscribe(EventTopics.GAME)

    message_handler = MessageHandler(event_hub)
    message_handler.subscribe(EventTopics.MESSAGE)

    entity_handler = EntityHandler(event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)

    map_handler = MapHandler(event_hub)
    map_handler.subscribe(EventTopics.MAP)
    map_handler.subscribe(EventTopics.GAME)

    affliction_handler = AfflictionHandler(event_hub)
    affliction_handler.subscribe(EventTopics.ENTITY)
    affliction_handler.subscribe(EventTopics.GAME)

    god_handler = GodHandler(event_hub)
    god_handler.subscribe(EventTopics.ENTITY)

    ui_handler = UiHandler(event_hub)
    ui_handler.subscribe(EventTopics.ENTITY)
    ui_handler.subscribe(EventTopics.GAME)
    ui_handler.subscribe(EventTopics.UI)


def initialise_ui_elements():
    """
    initialise all ui elements
    """
    ui_manager.Element.init_camera()
    ui_manager.Element.init_entity_info()
    ui_manager.Element.init_entity_queue()
    ui_manager.Element.init_message_log()
    ui_manager.Element.init_skill_bar()
    ui_manager.Element.init_targeting_overlay()
