from enum import Enum, auto

import pygame.freetype

# game info
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
GAME_FPS = 60

# sprites
SPRITE_PLAYER = pygame.image.load("assets/actor/player.png")
SPRITE_ENEMY = pygame.image.load("assets/actor/enemy.png")
SPRITE_FLOOR = pygame.image.load("assets/world/floor.png")
SPRITE_WALL = pygame.image.load("assets/world/wall.png")


class GameStates(Enum):
    """
    States the Game can be in.
    """
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    SHOW_INVENTORY = auto()
    DROP_INVENTORY = auto()
    TARGETING = auto()
    LEVEL_UP = auto()
    CHARACTER_SCREEN = auto()
    MAIN_MENU = auto()
    EXIT_GAME = auto()
    GAME_INITIALISING = auto()


class EventTopics(Enum):
    """Topics that Events can be associated with."""
    GAME = auto()
    MESSAGE = auto()
    LOGGING = auto()
    ENTITY = auto()


class GameEventTypes(Enum):
    """Types of Game Events"""
    EXIT = auto()
    NEW_GAME = auto()
    END_TURN = auto()


class MessageEventTypes(Enum):
    """Types of Message Events"""
    BASIC = auto()


class LoggingEventTypes(Enum):
    """Types of Logging Events"""
    CRITICAL = auto()
    INTERESTING = auto()
    MUNDANE = auto()


class EntityEventTypes(Enum):
    """Types of Entity Events"""
    MOVE = auto()
    GET_MOVE_TARGET = auto()
    ATTACK = auto()
    DIE = auto()
