from enum import Enum, auto

# game info
BASE_WINDOW_WIDTH = 640
BASE_WINDOW_HEIGHT = 360
TILE_SIZE = 16
GAME_FPS = 60
ENTITY_SPRITE_FRAME_DURATION = 0.05  # seconds

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
    """
    Topics that Events can be associated with.
    """
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

    CRITICAL = auto()  # A serious error, indicating that may be unable to continue running.
    ERROR = auto()  # A more serious problem, has not been able to perform some function.
    WARNING = auto()  # An indication that something unexpected happened, but otherwise still working as expected.
    INFO = auto()  # Confirmation that things are working as expected.
    DEBUG = auto()  # Detailed information, typically of interest only when diagnosing problems


class EntityEventTypes(Enum):
    """Types of Entity Events"""
    DIE = auto()
    SKILL = auto()


class TargetTypes(Enum):
    """Types of target"""
    FLOOR = auto()
    WALL = auto()
    ENTITY = auto()
    OUT_OF_BOUNDS = auto()
