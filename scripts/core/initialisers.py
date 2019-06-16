import pygame

from scripts.core.constants import EventTopics, GameStates, MessageEventTypes
from scripts.events.entity_events import LearnEvent
from scripts.events.entity_handler import EntityHandler
from scripts.events.logging_handler import LoggingHandler
from scripts.events.message_events import MessageEvent
from scripts.events.message_handler import MessageHandler
from scripts.events.game_handler import GameHandler
from scripts.global_instances.event_hub import publisher, event_hub
from scripts.global_instances.managers import game_manager, world_manager, turn_manager, ui_manager
from scripts.events.ui_handler import UiHandler


def initialise_game():
    """
    Init the game`s required info
    """

    pygame.init()

    initialise_event_handlers()

    world_manager.create_new_map(50, 30)  # TODO remove magic numbers
    ui_manager.delayed_init()

    world_manager.entity_action.create_actor_entity(0, 0, "player")  # TODO - remove when proper load is in
    world_manager.entity_action.create_actor_entity(0, 3, "goblinn_hand")  # TODO - remove when actor gen is in load

    # TODO - remove when skill learning is in
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "throw_dice"))
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "bring_down_the_mountain"))
    publisher.publish(LearnEvent(world_manager.player, "cleromancer", "burn_the_deck"))

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

