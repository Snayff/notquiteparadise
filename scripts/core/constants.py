
from enum import Enum, auto

TILE_SIZE = 64


class VisualInfo:
    """
    Constant info about visual aspects such as resolution and frame rate
    """
    # TODO -  should this be in game manager?
    BASE_WINDOW_WIDTH = 1280
    BASE_WINDOW_HEIGHT = 720

    GAME_FPS = 60
    ENTITY_SPRITE_FRAME_DURATION = 0.05  # seconds


class FOVInfo:
    """
    Constant info about the FOV settings
    """
    LIGHT_WALLS = True
    FOV_ALGORITHM = 0


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
    UI = auto()


class GameEventTypes(Enum):
    """Types of Game Events"""
    EXIT = auto()
    END_TURN = auto()
    CHANGE_GAME_STATE = auto()


class MessageEventTypes(Enum):
    """Types of Message Events"""
    BASIC = auto()
    SYSTEM = auto()


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

class UIEventTypes(Enum):
    CLICK_UI = auto()


class TargetTypes(Enum):
    TERRAIN = auto()
    ENTITY = auto()


class TargetTags(Enum):
    """
    Types of target
    """
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
    SKULLDUGGERY = auto()
    BUSTLE = auto()
    EXACTITUDE = auto()


class SecondaryStatTypes(Enum):
    DODGE_SPEED = auto()
    DODGE_TOUGHNESS = auto()
    DODGE_INTELLIGENCE = auto()
    RESIST_BLUNT = auto()
    RESIST_PIERCE = auto()
    RESIST_ELEMENTAL = auto()
    ACTION_COST_CHANGE = auto()


class HitTypes(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = auto()
    HIT = auto()
    CRIT = auto()


class HitValues(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = 0
    HIT = 100
    CRIT = 130


class HitModifiers(Enum):
    """
    The modifier for each hit type
    """
    GRAZE = 0.6
    HIT = 1
    CRIT = 1.4


class SkillEffectTypes(Enum):
    """
    Types of skill_effects
    """
    APPLY_AFFLICTION = auto()
    DAMAGE = auto()
    MOVE = auto()
    CHANGE_TERRAIN = auto()


class AfflictionCategory(Enum):
    """
    Boon or Bane
    """
    BANE = auto()
    BOON = auto()


class AfflictionTypes(Enum):
    """
    Various types of afflictions
    """

    # TODO - replace with strings from json (as it is all defined in the json)
    # BANES
    MYOPIC = auto()
    BOGGED_DOWN = auto()
    SHAKEN = auto()
    EXPOSED = auto()
    RUPTURED = auto()
    FLAMING = auto()
    EXHAUSTED = auto()
    HOBBLED = auto()
    DISTRACTED = auto()
    TORMENTED = auto()

    # BOONS


class AfflictionTriggers(Enum):
    """
    When to trigger the affliction
    """
    PASSIVE = auto()  # always applying effects
    END_TURN = auto()  # apply at end of round turn
    MOVE = auto()  # apply if afflicted entity moves
    DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    END_ROUND = auto()  # apply at the end of the round
    ACTION = auto()  # apply when an action is taken


class AfflictionEffectTypes(Enum):
    """
    Types of Affliction effects
    """
    DAMAGE = auto()
    AFFECT_STAT = auto()


class AspectTypes(Enum):
    # TODO - replace with strings from json (as it is all defined in the json)
    DIRT = auto()
    LONG_GRASS = auto()
    FROZEN = auto()
    SMOKE = auto()
    GAS = auto()
    BOG = auto()
    AFLAME = auto()


class InputModes(Enum):
    MOUSE_AND_KB = auto()
    GAMEPAD = auto()

class MouseButtons(Enum):
    LEFT_BUTTON = auto()
    RIGHT_BUTTON = auto()
    MIDDLE_BUTTON = auto()