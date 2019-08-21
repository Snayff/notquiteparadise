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

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class EventTopics(Enum):
    """
    Topics that Events can be associated with.
    """
    GAME = auto()
    MESSAGE = auto()
    LOGGING = auto()
    ENTITY = auto()
    UI = auto()
    MAP = auto()


class GameEventTypes(Enum):
    """Types of Game Events"""
    EXIT = auto()
    END_TURN = auto()
    CHANGE_GAME_STATE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MessageEventTypes(Enum):
    """Types of Message Events"""
    BASIC = auto()
    SYSTEM = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class LoggingEventTypes(Enum):
    """Types of Logging Events"""

    CRITICAL = auto()  # A serious error, indicating that may be unable to continue running.
    ERROR = auto()  # A more serious problem, has not been able to perform some function.
    WARNING = auto()  # An indication that something unexpected happened, but otherwise still working as expected.
    INFO = auto()  # Confirmation that things are working as expected.
    DEBUG = auto()  # Detailed information, typically of interest only when diagnosing problems

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class EntityEventTypes(Enum):
    """Types of Entity Events"""
    DIE = auto()
    SKILL = auto()
    MOVE = auto()
    LEARN = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class UIEventTypes(Enum):
    """
    Types of UI events
    """
    CLICK_UI = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MapEventTypes(Enum):
    """
    Types of Map events
    """
    TILE_INTERACTION = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class TargetTags(Enum):
    """
    Types of target
    """
    # TODO - externalise terrain types
    FLOOR = auto()
    WALL = auto()

    SELF = auto()
    OTHER_ENTITY = auto()
    NO_ENTITY = auto()
    OUT_OF_BOUNDS = auto()


    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class DamageTypes(Enum):
    """
    Damage types
    """
    PIERCE = auto()
    BLUNT = auto()
    ELEMENTAL = auto()
    FIRE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class StatTypes(Enum):
    """
    Primary stats
    """
    PRIMARY = auto()
    SECONDARY = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class PrimaryStatTypes(Enum):
    """
    Primary stats
    """
    VIGOUR = auto()
    CLOUT = auto()
    SKULLDUGGERY = auto()
    BUSTLE = auto()
    EXACTITUDE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class SecondaryStatTypes(Enum):
    """
    Secondary stats
    """
    RESIST_BLUNT = auto()
    RESIST_PIERCE = auto()
    RESIST_ELEMENTAL = auto()
    MAX_HP = auto()
    ACCURACY = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class HitTypes(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = auto()
    HIT = auto()
    CRIT = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


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


class EffectTypes(Enum):
    """
    Types of effects
    """
    APPLY_AFFLICTION = auto()
    DAMAGE = auto()
    MOVE = auto()
    CHANGE_TERRAIN = auto()
    AFFECT_STAT = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AfflictionCategory(Enum):
    """
    Boon or Bane
    """
    BANE = auto()
    BOON = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AfflictionTriggers(Enum):
    """
    When to trigger the afflictions
    """
    PASSIVE = auto()  # always applying effects
    END_TURN = auto()  # apply at end of round turn
    MOVE = auto()  # apply if afflicted entity moves
    DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    END_ROUND = auto()  # apply at the end of the round
    ACTION = auto()  # apply when an action is taken

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AspectTypes(Enum):
    # TODO - replace with strings from json (as it is all defined in the json)
    DIRT = auto()
    LONG_GRASS = auto()
    FROZEN = auto()
    SMOKE = auto()
    GAS = auto()
    BOG = auto()
    AFLAME = auto()


class SkillShapes(Enum):
    """
    When to trigger the afflictions
    """
    TARGET = auto()  # single target
    SQUARE = auto()
    CIRCLE = auto()
    CROSS = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None

class InputModes(Enum):
    MOUSE_AND_KB = auto()
    GAMEPAD = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MouseButtons(Enum):
    LEFT_BUTTON = auto()
    RIGHT_BUTTON = auto()
    MIDDLE_BUTTON = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None
