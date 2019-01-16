import pygame

from scripts.components.actor import Actor
from scripts.components.combatant import Combatant
from scripts.core.constants import EventTopics, WINDOW_WIDTH, WINDOW_HEIGHT, SPRITE_PLAYER, GameStates
from scripts.core.event_handlers import GameHandler, MessageHandler, LoggingHandler, EntityHandler
from scripts.core.global_data import game_manager, world_manager, entity_manager, turn_manager
from scripts.entities.entity import Entity


def initialise_game():
    """Init the game's required info"""

    pygame.init()

    main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    initialise_event_handlers()

    world_manager.create_new_map()

    player = Entity(0, 0, SPRITE_PLAYER, "player", actor=Actor(), combatant=Combatant())

    entity_manager.add_player(player)

    entity_manager.create_actor(0, 3, "orc_fighter")

    game_manager.update_game_state(GameStates.PLAYER_TURN)
    turn_manager.turn_holder = player

    return main_surface


def initialise_event_handlers():
    game_handler = GameHandler(game_manager.event_hub)
    game_handler.subscribe(EventTopics.GAME)

    message_handler = MessageHandler(game_manager.event_hub)
    message_handler.subscribe(EventTopics.MESSAGE)

    logging_handler = LoggingHandler(game_manager.event_hub)
    logging_handler.subscribe(EventTopics.LOGGING)

    entity_handler = EntityHandler(game_manager.event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)
