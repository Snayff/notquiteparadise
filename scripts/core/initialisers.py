
import pygame

from scripts.core.constants import EventTopics, GameStates, MessageEventTypes
from scripts.events.entity_events import LearnEvent
from scripts.event_handlers.entity_handler import EntityHandler
from scripts.event_handlers.logging_handler import LoggingHandler
from scripts.events.message_events import MessageEvent
from scripts.event_handlers.message_handler import MessageHandler
from scripts.event_handlers.game_handler import GameHandler
from scripts.global_singletons.event_hub import publisher, event_hub
from scripts.global_singletons.managers import game_manager, world_manager, turn_manager, ui_manager
from scripts.event_handlers.ui_handler import UiHandler


def initialise_game():
    """
    Init the game`s required info
    """
    pygame.init()

    initialise_event_handlers()

    map_width = 50
    map_height = 30
    world_manager.Map.create_new_map(map_width, map_height)
    world_manager.FOV.create_player_fov_map(map_width, map_height)
    ui_manager.delayed_init()

    world_manager.Entity.create_actor_entity(0, 0, "player", True)  # TODO - remove when proper load is in
    world_manager.Entity.create_actor_entity(0, 3, "goblinn_hand")  # TODO - remove when actor gen is in load

    # TODO - remove when skill learning is in
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "basic attack"))
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "throw dice"))
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "bring down the mountain"))
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "burn the deck"))

    game_manager.update_game_state(GameStates.PLAYER_TURN)  # TODO remove when main menu is starting point
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

    logging_handler = LoggingHandler(event_hub)
    logging_handler.subscribe(EventTopics.LOGGING)

    entity_handler = EntityHandler(event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)

    ui_handler = UiHandler(event_hub)
    ui_handler.subscribe(EventTopics.ENTITY)
    ui_handler.subscribe(EventTopics.GAME)
    ui_handler.subscribe(EventTopics.UI)

