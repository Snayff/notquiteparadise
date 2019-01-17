from enum import Enum, auto

import pygame.freetype

# game info
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16

# colours
# COLOUR_BLACK = (255, 255, 255)
# COLOUR_WHITE = (0, 0, 0)
# COLOUR = {  "primary": {"darkest": (66, 48, 28),
#                         "darker": (73, 60, 46),
#                         "neutral": (121, 105, 88),
#                         "lighter": (164, 146, 126),
#                         "lightest": (211, 193, 175)
#                         },
#             "secondary": {"darkest": (0, 0, 0),
#                             "darker": (0, 0, 0),
#                             "neutral": (0, 0, 0),
#                             "lighter": (0, 0, 0),
#                             "lightest": (0, 0, 0)
#                          },
#             "tertiary": {"darkest": (0, 0, 0),
#                         "darker": (0, 0, 0),
#                         "neutral": (0, 0, 0),
#                         "lighter": (0, 0, 0),
#                         "lightest": (0, 0, 0)
#                         },
#             "complement": {"darkest": (0, 0, 0),
#                             "darker": (0, 0, 0),
#                             "neutral": (0, 0, 0),
#                             "lighter": (0, 0, 0),
#                             "lightest": (0, 0, 0)
#                         },
#         }

# colour palette
# PALETTE_BACKGROUND = COLOUR_WHITE

# sprites
SPRITE_PLAYER = pygame.image.load("assets/actor/player.png")
SPRITE_ENEMY = pygame.image.load("assets/actor/enemy.png")
SPRITE_FLOOR = pygame.image.load("assets/world/floor.png")
SPRITE_WALL = pygame.image.load("assets/world/wall.png")

# fonts
pygame.freetype.init()
DEBUG_FONT = pygame.freetype.Font(None, 12)


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


class EquipmentSlots(Enum):
    MAIN_HAND = auto()
    OFF_HAND = auto()


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
