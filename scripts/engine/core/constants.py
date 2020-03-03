from __future__ import annotations

from types import SimpleNamespace
from typing import NewType, Tuple

######################## GENERAL CONSTANTS ######################################

VERSION = "0.95.0"
TILE_SIZE = 64
ICON_IN_TEXT_SIZE = 16
ICON_SIZE = 32
ENTITY_BLOCKS_SIGHT = False
IMAGE_NOT_FOUND_PATH = "assets/image_not_found.png"
TIME_PER_ROUND = 100

######################## NEW TYPES ######################################
# NewType guarantees you don't accidentally pass in a normal str instead of a value explicitly defined as a member of
# that NewType, and that you don't treat that member as a normal str.
#########################################################################
# Instructions:
# To quickly add the new type select the body of a class, replace ([A-Z_]+ = )(".*?")  with $1NewType($2)
# replacing NewType with the relevant type.
#########################################################################
InputIntentType = NewType("InputIntentType", str)
PrimaryStatType = NewType("PrimaryStatType", str)
SecondaryStatType = NewType("SecondaryStatType", str)
GameStateType = NewType("GameStateType", int)
EventTopicType = NewType("EventTopicType", int)
MessageTypeType = NewType("MessageTypeType", int)
TargetTagType = NewType("TargetTagType", int)
DamageTypeType = NewType("DamageTypeType", int)
HitTypeType = NewType("HitTypeType", int)
HitValueType = NewType("HitValueType", int)
HitModifierType = NewType("HitModifierType", float)
EffectTypeType = NewType("EffectTypeType", int)
AfflictionCategoryType = NewType("AfflictionCategoryType", int)
AfflictionTriggerType = NewType("AfflictionTriggerType", int)
SkillShapeType = NewType("SkillShapeType", int)
SkillTerrainCollisionType = NewType("SkillTerrainCollisionType", int)
SkillTravelType = NewType("SkillTravelType", int)
SkillExpiryType = NewType("SkillExpiryType", int)
InputModeType = NewType("InputModeType", int)
UIElementType = NewType("UIElementType", int)
DirectionType = NewType("DirectionType", Tuple[int, int])

#################### CLASSES ###########################################


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


class GameState(SimpleNamespace):
    """
    States the Game can be in.
    """
    PLAYER_TURN = GameStateType(1)
    ENEMY_TURN = GameStateType(2)
    PLAYER_DEAD = GameStateType(3)
    TARGETING_MODE = GameStateType(4)
    EXIT_GAME = GameStateType(5)
    GAME_INITIALISING = GameStateType(6)
    NEW_TURN = GameStateType(7)
    DEV_MODE = GameStateType(8)
    PREVIOUS = GameStateType(9)


class EventTopic(SimpleNamespace):
    """
    Topics that Events can be associated with.
    """
    GAME = EventTopicType(1)
    ENTITY = EventTopicType(2)
    UI = EventTopicType(3)
    MAP = EventTopicType(4)


class MessageType(SimpleNamespace):
    """Types of Message Events"""
    LOG = MessageTypeType(1)
    ENTITY = MessageTypeType(2)
    SCREEN = MessageTypeType(3)


class TargetTag(SimpleNamespace):
    """
    Types of target
    """
    SELF = TargetTagType(1)
    OTHER_ENTITY = TargetTagType(2)
    NO_ENTITY = TargetTagType(3)
    OUT_OF_BOUNDS = TargetTagType(4)
    ANY = TargetTagType(5)
    OPEN_SPACE = TargetTagType(6)
    BLOCKED_MOVEMENT = TargetTagType(7)
    IS_VISIBLE = TargetTagType(8)


class DamageType(SimpleNamespace):
    """
    Damage types
    """
    BURN = DamageTypeType(1)
    CHEMICAL = DamageTypeType(2)
    ASTRAL = DamageTypeType(3)
    COLD = DamageTypeType(4)
    MUNDANE = DamageTypeType(5)


class PrimaryStat(SimpleNamespace):
    """
    Primary stats. Values are strings.
    """
    VIGOUR = PrimaryStatType("vigour")
    CLOUT = PrimaryStatType("clout")
    SKULLDUGGERY = PrimaryStatType("skullduggery")
    BUSTLE = PrimaryStatType("bustle")
    EXACTITUDE = PrimaryStatType("exactitude")


class SecondaryStat(SimpleNamespace):
    """
    Secondary stats
    """
    MAX_HP = SecondaryStatType("max_hp")
    MAX_STAMINA = SecondaryStatType("max_stamina")
    HP = SecondaryStatType("hp")
    STAMINA = SecondaryStatType("stamina")
    ACCURACY = SecondaryStatType("accuracy")
    RESIST_BURN = SecondaryStatType("resist_burn")
    RESIST_CHEMICAL = SecondaryStatType("resist_chemical")
    RESIST_ASTRAL = SecondaryStatType("resist_astral")
    RESIST_COLD = SecondaryStatType("resist_cold")
    RESIST_MUNDANE = SecondaryStatType("resist_mundane")
    SIGHT_RANGE = SecondaryStatType("sight_range")
    RUSH = SecondaryStatType("rush")


class HitType(SimpleNamespace):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = HitTypeType(1)
    HIT = HitTypeType(2)
    CRIT = HitTypeType(3)


class HitValue(SimpleNamespace):
    """
    The value of each hit type. The value is the starting amount.
    """
    # TODO - externalise the values    
    GRAZE = HitValueType(0)
    HIT = HitValueType(5)
    CRIT = HitValueType(20)


class HitModifier(SimpleNamespace):
    """
    The modifier for each hit type
    """
    # TODO - externalise the values    
    GRAZE = HitModifierType(0.6)
    HIT = HitModifierType(1)
    CRIT = HitModifierType(1.4)


class EffectType(SimpleNamespace):
    """
    Types of effects
    """
    APPLY_AFFLICTION = EffectTypeType(1)
    DAMAGE = EffectTypeType(2)
    MOVE = EffectTypeType(3)
    AFFECT_STAT = EffectTypeType(4)
    ADD_ASPECT = EffectTypeType(5)


class AfflictionCategory(SimpleNamespace):
    """
    Boon or Bane
    """
    BANE = AfflictionCategoryType(1)
    BOON = AfflictionCategoryType(2)


class AfflictionTrigger(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    PASSIVE = AfflictionTriggerType(1)  # always applying effects, overrides duration
    END_TURN = AfflictionTriggerType(2)  # apply at end of round turn
    MOVE = AfflictionTriggerType(3)  # apply if afflicted entity moves
    ACTION = AfflictionTriggerType(4)  # apply when an action is taken

    # Other triggers to consider
    # DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    # TAKE_DAMAGE = auto()  # apply if afflicted entity receives damage
    # USE_BURN = auto()  # apply if afflicted entity uses a burn type - etc.
    # DEATH = auto()  # apply if afflicted entity dies


class SkillShape(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    TARGET = SkillShapeType(1)  # single target
    SQUARE = SkillShapeType(2)
    CIRCLE = SkillShapeType(3)
    CROSS = SkillShapeType(4)


class SkillTerrainCollision(SimpleNamespace):
    """
    What to do when a skill hits terrain
    """
    REFLECT = SkillTerrainCollisionType(1)
    ACTIVATE = SkillTerrainCollisionType(2)
    FIZZLE = SkillTerrainCollisionType(3)


class SkillTravel(SimpleNamespace):
    """
    How the skill travels
    """
    PROJECTILE = SkillTravelType(1)  # travels tile by tile
    THROW = SkillTravelType(2)  # only impacts last tile in range


class SkillExpiry(SimpleNamespace):
    """
    What happens when the skill reaches the range limit
    """
    FIZZLE = SkillExpiryType(1)
    ACTIVATE = SkillExpiryType(2)


class InputMode(SimpleNamespace):
    """
    Input hardware being used
    """
    MOUSE_AND_KB = InputModeType(1)
    GAMEPAD = InputModeType(2)


class InputIntent(SimpleNamespace):
    """
    Values of the conversion from input to intent. Strings.
    """
    UP = InputIntentType("up")
    DOWN = InputIntentType("down")
    LEFT = InputIntentType("left")
    RIGHT = InputIntentType("right")
    UP_RIGHT = InputIntentType("up_right")
    UP_LEFT = InputIntentType("up_left")
    DOWN_RIGHT = InputIntentType("down_right")
    DOWN_LEFT = InputIntentType("down_left")
    CONFIRM = InputIntentType("confirm")
    CANCEL = InputIntentType("cancel")
    EXIT_GAME = InputIntentType("exit_game")
    DEBUG_TOGGLE = InputIntentType("debug_toggle")
    SKILL0 = InputIntentType("skill0")
    SKILL1 = InputIntentType("skill1")
    SKILL2 = InputIntentType("skill2")
    SKILL3 = InputIntentType("skill3")
    SKILL4 = InputIntentType("skill4")
    SKILL5 = InputIntentType("skill5")
    REFRESH_DATA = InputIntentType("refresh_data")
    DEV_TOGGLE = InputIntentType("dev_toggle")


class UIElement(SimpleNamespace):
    """
    The different UI elements
    """
    MESSAGE_LOG = UIElementType(1)
    ENTITY_INFO = UIElementType(2)
    TARGETING_OVERLAY = UIElementType(3)
    SKILL_BAR = UIElementType(4)
    ENTITY_QUEUE = UIElementType(5)
    CAMERA = UIElementType(6)
    DATA_EDITOR = UIElementType(7)


class Direction(SimpleNamespace):
    """
    Holds a tuple for each direction of the (x, y) relative direction.
    """
    UP_LEFT = DirectionType((-1, -1))
    UP = DirectionType((0, -1))
    UP_RIGHT = DirectionType((1, -1))
    LEFT = DirectionType((-1, 0))
    CENTRE = DirectionType((0, 0))
    RIGHT = DirectionType((1, 0))
    DOWN_LEFT = DirectionType((-1, 1))
    DOWN = DirectionType((0, 1))
    DOWN_RIGHT = DirectionType((1, 1))
