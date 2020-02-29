from __future__ import annotations

from types import SimpleNamespace
from typing import NewType

VERSION = "0.94.0"
TILE_SIZE = 64
ICON_IN_TEXT_SIZE = 16
ICON_SIZE = 32
ENTITY_BLOCKS_SIGHT = False
IMAGE_NOT_FOUND_PATH = "assets/image_not_found.png"


class VisualInfo(SimpleNamespace):
    """
    Constant info about visual aspects such as resolution and frame rate
    """
    # TODO -  should this be in UI?
    BASE_WINDOW_WIDTH = 1280
    BASE_WINDOW_HEIGHT = 720
    GAME_FPS = 60


class FOVInfo(SimpleNamespace):
    """
    Constant info about the FOV settings
    """
    LIGHT_WALLS = True
    FOV_ALGORITHM = 0


class GameStates(SimpleNamespace):
    """
    States the Game can be in.
    """
    PLAYER_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    TARGETING_MODE = 4
    EXIT_GAME = 5
    GAME_INITIALISING = 6
    NEW_TURN = 7
    DEV_MODE = 8
    PREVIOUS = 9


class EventTopics(SimpleNamespace):
    """
    Topics that Events can be associated with.
    """
    GAME = 1
    ENTITY = 2
    UI = 3
    MAP = 4


class MessageTypes(SimpleNamespace):
    """Types of Message Events"""
    LOG = 1
    ENTITY = 2
    SCREEN = 3


class TargetTags(SimpleNamespace):
    """
    Types of target
    """
    SELF = 1
    OTHER_ENTITY = 2
    NO_ENTITY = 3
    OUT_OF_BOUNDS = 4
    ANY = 5
    OPEN_SPACE = 6
    BLOCKED_MOVEMENT = 7
    IS_VISIBLE = 8


class DamageTypes(SimpleNamespace):
    """
    Damage types
    """
    BURN = 1
    CHEMICAL = 2
    ASTRAL = 3
    COLD = 4
    MUNDANE = 5


class PrimaryStatTypes(SimpleNamespace):
    """
    Primary stats. Values are strings.
    """
    VIGOUR = "vigour"
    CLOUT = "clout"
    SKULLDUGGERY = "skullduggery"
    BUSTLE = "bustle"
    EXACTITUDE = "exactitude"


class SecondaryStatTypes(SimpleNamespace):
    """
    Secondary stats
    """
    MAX_HP = "max_hp"
    MAX_STAMINA = "max_stamina"
    HP = "hp"
    STAMINA = "stamina"
    ACCURACY = "accuracy"
    RESIST_BURN = "resist_burn"
    RESIST_CHEMICAL = "resist_chemical"
    RESIST_ASTRAL = "resist_astral"
    RESIST_COLD = "resist_cold"
    RESIST_MUNDANE = "resist_mundane"
    SIGHT_RANGE = "sight_range"
    RUSH = "rush"


class HitTypes(SimpleNamespace):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = 1
    HIT = 2
    CRIT = 3


# TODO - externalise the values
class HitValues(SimpleNamespace):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = 0
    HIT = 5
    CRIT = 20


# TODO - externalise the values
class HitModifiers(SimpleNamespace):
    """
    The modifier for each hit type
    """
    GRAZE = 0.6
    HIT = 1
    CRIT = 1.4


class EffectTypes(SimpleNamespace):
    """
    Types of effects
    """
    APPLY_AFFLICTION = 1
    DAMAGE = 2
    MOVE = 3
    AFFECT_STAT = 4
    ADD_ASPECT = 5


class AfflictionCategory(SimpleNamespace):
    """
    Boon or Bane
    """
    BANE = 1
    BOON = 2


class AfflictionTriggers(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    PASSIVE = 1  # always applying effects, overrides duration
    END_TURN = 2  # apply at end of round turn
    MOVE = 3  # apply if afflicted entity moves
    ACTION = 4  # apply when an action is taken

    # Other triggers to consider
    # DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    # TAKE_DAMAGE = auto()  # apply if afflicted entity receives damage
    # USE_BURN = auto()  # apply if afflicted entity uses a burn type - etc.
    # DEATH = auto()  # apply if afflicted entity dies


class SkillShapes(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    TARGET = 1  # single target
    SQUARE = 2
    CIRCLE = 3
    CROSS = 4


class SkillTerrainCollisions(SimpleNamespace):
    """
    What to do when a skill hits terrain
    """
    REFLECT = 1
    ACTIVATE = 2
    FIZZLE = 3


class SkillTravelTypes(SimpleNamespace):
    """
    How the skill travels
    """
    PROJECTILE = 1  # travels tile by tile
    THROW = 2  # only impacts last tile in range


class SkillExpiryTypes(SimpleNamespace):
    """
    What happens when the skill reaches the range limit
    """
    FIZZLE = 1
    ACTIVATE = 2


class InputModes(SimpleNamespace):
    """
    Input hardware being used
    """
    MOUSE_AND_KB = 1
    GAMEPAD = 2

# TODO - add types to the different classes here
#  e.g. UP = InputIntentType("up")
InputIntentType = NewType('InputIntentType', str)
class InputIntents(SimpleNamespace):
    """
    Values of the conversion from input to intent. Strings.
    """
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    UP_RIGHT = "up_right"
    UP_LEFT = "up_left"
    DOWN_RIGHT = "down_right"
    DOWN_LEFT = "down_left"
    CONFIRM = "confirm"
    CANCEL = "cancel"
    EXIT_GAME = "exit_game"
    DEBUG_TOGGLE = "debug_toggle"
    SKILL0 = "skill0"
    SKILL1 = "skill1"
    SKILL2 = "skill2"
    SKILL3 = "skill3"
    SKILL4 = "skill4"
    SKILL5 = "skill5"
    REFRESH_DATA = "refresh_data"
    DEV_TOGGLE = "dev_toggle"


class UIElementTypes(SimpleNamespace):
    """
    The different UI elements
    """
    MESSAGE_LOG = 1
    ENTITY_INFO = 2
    TARGETING_OVERLAY = 3
    SKILL_BAR = 4
    ENTITY_QUEUE = 5
    CAMERA = 6
    DATA_EDITOR = 7


class Directions(SimpleNamespace):
    """
    Holds a tuple for each direction of the (x, y) relative direction.
    """
    UP_LEFT = (-1, -1)
    UP = (0, -1)
    UP_RIGHT = (1, -1)
    LEFT = (-1, 0)
    CENTRE = (0, 0)
    RIGHT = (1, 0)
    DOWN_LEFT = (-1, 1)
    DOWN = (0, 1)
    DOWN_RIGHT = (1, 1)
