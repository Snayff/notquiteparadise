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
    GAME = auto()
    MESSAGE = auto()
    LOGGING = auto()
    ENTITY = auto()


class GameEventNames(Enum):
    EXIT = auto()
    NEW_GAME = auto()
    END_TURN = auto()


class MessageEventNames(Enum):
    BASIC = auto()


class LoggingEventNames(Enum):
    CRITICAL = auto()
    INTERESTING = auto()
    MUNDANE = auto()


class EntityEventNames(Enum):
    MOVE = auto()
    GET_MOVE_TARGET = auto()
    ATTACK = auto()
    DIE = auto()
