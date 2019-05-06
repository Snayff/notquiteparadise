from enum import Enum, auto

# game info
BASE_WINDOW_WIDTH = 1280
BASE_WINDOW_HEIGHT = 720
TILE_SIZE = 64
GAME_FPS = 60
ENTITY_SPRITE_FRAME_DURATION = 0.05  # seconds


class GameStates(Enum):
    """
    States the Game can be in.
    """
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    TARGETING_MODE = auto()
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
    END_TURN = auto()
    CHANGE_GAME_STATE = auto()


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
    MOVE = auto()
    LEARN = auto()


class TargetTypes(Enum):
    TERRAIN = auto()
    ENTITY = auto()


class TargetTags(Enum):
    """Types of target"""

    FLOOR = auto()
    WALL = auto()
    SELF = auto()
    OTHER_ENTITY = auto()
    NO_ENTITY = auto()
    OUT_OF_BOUNDS = auto()


class DamageTypes(Enum):
    PIERCE = auto()
    BLUNT = auto()
    ELEMENTAL = auto()


class PrimaryStatTypes(Enum):
    VIGOUR = auto()
    CLOUT = auto()
    SUBTLETY = auto()
    BUSTLE = auto()
    EXACTITUDE = auto()


class SecondaryStatTypes(Enum):
    DODGE_SPEED = auto()
    DODGE_TOUGHNESS = auto()
    DODGE_INTELLIGENCE = auto()
    RESIST_BLUNT = auto()
    RESIST_PIERCE = auto()
    RESIST_ELEMENTAL = auto()


class HitTypes(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = auto()
    HIT = auto()
    CRIT = auto()
    GRAZE_VALUE = 0
    HIT_VALUE = 100
    CRIT_VALUE = 120
    GRAZE_MODIFIER = 0.5
    HIT_MODIFIER = 1
    CRIT_MODIFIER = 1.3
