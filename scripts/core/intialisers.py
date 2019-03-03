import pygame

from scripts.components.actor import Actor
from scripts.components.combatant import Combatant
from scripts.components.race import Race
from scripts.core.constants import EventTopics, GameStates
from scripts.events.entity_handler import EntityHandler
from scripts.events.logging_handler import LoggingHandler
from scripts.events.message_handler import MessageHandler
from scripts.events.game_handler import GameHandler
from scripts.core.global_data import game_manager, world_manager, entity_manager, turn_manager, ui_manager
from scripts.entities.entity import Entity


def initialise_game():
    """
    Init the game's required info
    """

    pygame.init()

    initialise_event_handlers()

    world_manager.create_new_map(50, 30)  # TODO remove magic numbers
    ui_manager.init_message_log()

    player_sprite = entity_manager.create_actor_sprite_dict("actor_template")
    player = Entity(0, 0, player_sprite, "player", actor=Actor(), combatant=Combatant(), sight_range=5,
                    race=Race("human"))
    # TODO move  to player creation  method

    entity_manager.add_player(player)

    # entity_manager.create_actor_entity(0, 3, "orc_fighter")  # TODO - remove when actor gen is in

    game_manager.update_game_state(GameStates.PLAYER_TURN)  # TODO remove when main menu is starting point
    turn_manager.turn_holder = player


def initialise_event_handlers():
    """
    Create the various event handlers and subscribe to required events.
    """
    game_handler = GameHandler(game_manager.event_hub)
    game_handler.subscribe(EventTopics.GAME)

    message_handler = MessageHandler(game_manager.event_hub)
    message_handler.subscribe(EventTopics.MESSAGE)

    logging_handler = LoggingHandler(game_manager.event_hub)
    logging_handler.subscribe(EventTopics.LOGGING)

    entity_handler = EntityHandler(game_manager.event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)

