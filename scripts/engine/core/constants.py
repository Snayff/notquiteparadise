from __future__ import annotations

from types import SimpleNamespace
from typing import NewType, Tuple

######################## GENERAL CONSTANTS ######################################
# TODO - segregate to relevant sections and modules
VERSION = "0.100.0"

TILE_SIZE = 64
ICON_IN_TEXT_SIZE = 16
ICON_SIZE = 32
GAP_SIZE = 2
SKILL_SIZE = 64
LAYER_CAMERA = 1
LAYER_BASE_UI = 4

ENTITY_BLOCKS_SIGHT = False  # do entities block sight by default
TIME_PER_ROUND = 20  # amount of time in a round.
DEFAULT_SIGHT_RANGE = 2  # amount in tiles. also used if entity has no combatstats
BASE_MOVE_COST = 20  # amount of time spent to move.
BASE_ACCURACY = 100
BASE_DAMAGE = 5  # base amount of damage a skill should do. used as a starting point.
MAX_SKILLS = 5

DEBUG_LOG_EVENT_RECEIPTS = False  # whether to log event_handlers receiving events or not
IMAGE_NOT_FOUND_PATH = "assets/image_not_found.png"
INFINITE = 999

######################## NEW TYPES ######################################
# NewType guarantees you don't accidentally pass in a normal str instead of a value explicitly defined as a member of
# that NewType, and that you don't treat that member as a normal str.

InputIntentType = NewType("InputIntentType", str)
PrimaryStatType = NewType("PrimaryStatType", str)
SecondaryStatType = NewType("SecondaryStatType", str)
ResourceType = NewType("ResourceType", str)
GameStateType = NewType("GameStateType", int)
EventTopicType = NewType("EventTopicType", int)
MessageTypeType = NewType("MessageTypeType", int)
TargetTagType = NewType("TargetTagType", str)
DamageTypeType = NewType("DamageTypeType", str)
HitTypeType = NewType("HitTypeType", str)
HitValueType = NewType("HitValueType", int)
HitModifierType = NewType("HitModifierType", float)
EffectType = NewType("EffectType", str)
AfflictionCategoryType = NewType("AfflictionCategoryType", str)
InteractionCauseType = NewType("InteractionCauseType", str)
ShapeType = NewType("ShapeType", str)
TerrainCollisionType = NewType("TerrainCollisionType", str)
TravelMethodType = NewType("TravelMethodType", str)
ProjectileExpiryType = NewType("ProjectileExpiryType", str)
ProjectileSpeedType = NewType("ProjectileSpeedType", int)
InputModeType = NewType("InputModeType", int)
UIElementType = NewType("UIElementType", int)
DirectionType = NewType("DirectionType", Tuple[int, int])
TargetingMethodType = NewType("TargetingMethodType", str)


#################### INTERNAL, NON-SERIALISED ###########################################

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
    States the game can be in.
    """
    PLAYER_TURN = GameStateType(1)
    NPC_TURN = GameStateType(2)
    PLAYER_DEAD = GameStateType(3)
    TARGETING_MODE = GameStateType(4)
    EXIT_GAME = GameStateType(5)
    GAME_INITIALISING = GameStateType(6)
    NEW_TURN = GameStateType(7)  # interim stage to handle  changes between stages
    DEV_MODE = GameStateType(8)
    PREVIOUS = GameStateType(9)


class EventTopic(SimpleNamespace):
    """
    Topics that Events can be associated with.
    """
    GAME = EventTopicType(1)
    ENTITY = EventTopicType(2)
    UI = EventTopicType(3)
    INTERACTION = EventTopicType(4)


class MessageType(SimpleNamespace):
    """Types of Message Events"""
    LOG = MessageTypeType(1)
    ENTITY = MessageTypeType(2)
    SCREEN = MessageTypeType(3)


class InputMode(SimpleNamespace):
    """
    Input hardware being used
    """
    MOUSE_AND_KB = InputModeType(1)
    GAMEPAD = InputModeType(2)


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


#################### EXTERNAL, SERIALISED ###########################################

class TargetTag(SimpleNamespace):
    """
    Types of target
    """
    SELF = TargetTagType("self")
    OTHER_ENTITY = TargetTagType("other_entity")
    NO_ENTITY = TargetTagType("no_entity")
    OUT_OF_BOUNDS = TargetTagType("out_of_bounds")
    ANY = TargetTagType("any")
    OPEN_SPACE = TargetTagType("open_space")
    BLOCKED_MOVEMENT = TargetTagType("blocked_movement")
    IS_VISIBLE = TargetTagType("is_visible")
    NO_BLOCKING_TILE = TargetTagType("no_blocking_tile")
    ACTOR = TargetTagType("actor")


class DamageType(SimpleNamespace):
    """
    Damage types
    """
    BURN = DamageTypeType("burn")
    CHEMICAL = DamageTypeType("chemical")
    ASTRAL = DamageTypeType("astral")
    COLD = DamageTypeType("cold")
    MUNDANE = DamageTypeType("mundane")


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
    MAX_HEALTH = SecondaryStatType("max_health")
    MAX_STAMINA = SecondaryStatType("max_stamina")
    HEALTH = SecondaryStatType("health")
    STAMINA = SecondaryStatType("stamina")
    ACCURACY = SecondaryStatType("accuracy")
    RESIST_BURN = SecondaryStatType("resist_burn")
    RESIST_CHEMICAL = SecondaryStatType("resist_chemical")
    RESIST_ASTRAL = SecondaryStatType("resist_astral")
    RESIST_COLD = SecondaryStatType("resist_cold")
    RESIST_MUNDANE = SecondaryStatType("resist_mundane")
    SIGHT_RANGE = SecondaryStatType("sight_range")
    RUSH = SecondaryStatType("rush")


class Resource(SimpleNamespace):
    """
    Resources that can be used. Must map to secondary stats.
    """
    HEALTH = ResourceType("health")
    STAMINA = ResourceType("stamina")


class HitType(SimpleNamespace):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = HitTypeType("graze")
    HIT = HitTypeType("hit")
    CRIT = HitTypeType("crit")


class Effect(SimpleNamespace):
    """
    Types of effects
    """
    APPLY_AFFLICTION = EffectType("apply_affliction")
    DAMAGE = EffectType("damage")
    MOVE = EffectType("move")
    AFFECT_STAT = EffectType("affect_stat")
    ADD_ASPECT = EffectType("add_aspect")
    REMOVE_ASPECT = EffectType("remove_aspect")
    TRIGGER_SKILL = EffectType("trigger_skill")
    ACTIVATE_SKILL = EffectType("activate_skill")
    KILL_ENTITY = EffectType("kill_entity")


class AfflictionCategory(SimpleNamespace):
    """
    Boon or Bane
    """
    BANE = AfflictionCategoryType("boon")
    BOON = AfflictionCategoryType("bane")


class TargetingMethod(SimpleNamespace):
    """
    Specify the way in which as skill is targeted
    """
    AUTO = TargetingMethodType("auto")
    TARGET = TargetingMethodType("target")


class InteractionCause(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    EXPIRE = InteractionCauseType("expire")  # when the entity expires
    ENTITY_COLLISION = InteractionCauseType("entity_collision")
    TERRAIN_COLLISION = InteractionCauseType("terrain_collision")
    END_TURN = InteractionCauseType("end_turn")  # when entity ends their turn
    MOVE = InteractionCauseType("move")  # when entity moves
    PASSIVE = InteractionCauseType("passive")  # passively affects entity at all times. usually modifiers.
    BURNED = InteractionCauseType("burned")  # when an entity is affected by burn damage

    # Other triggers to consider
    # DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    # TAKE_DAMAGE = auto()  # apply if afflicted entity receives damage
    # USE_BURN = auto()  # apply if afflicted entity uses a burn type - etc.
    # DEATH = auto()  # apply if afflicted entity dies


class Shape(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    TARGET = ShapeType("target")  # single target
    SQUARE = ShapeType("square")
    CIRCLE = ShapeType("circle")
    CROSS = ShapeType("cross")


class TerrainCollision(SimpleNamespace):
    """
    What to do when a skill hits terrain
    """
    REFLECT = TerrainCollisionType("reflect")
    ACTIVATE = TerrainCollisionType("activate")
    FIZZLE = TerrainCollisionType("fizzle")


class TravelMethod(SimpleNamespace):
    """
    How the skill travels
    """
    STANDARD = TravelMethodType("standard")  # travels tile by tile
    # TODO - extend to allow throw shorter than total length and implement bounces
    ARC = TravelMethodType("arc")  # only impacts last tile in range, can reflect if hits terrain early.
    INSTANT = TravelMethodType("instant")  # doesn't travel, doesn't interact with terrain except for blocking


class ProjectileExpiry(SimpleNamespace):
    """
    What happens when the skill reaches the range limit
    """
    FIZZLE = ProjectileExpiryType("fizzle")
    ACTIVATE = ProjectileExpiryType("activate")


class ProjectileSpeed(SimpleNamespace):
    """
    The speed at which a projectile travels. How much time to move a tile.
    """
    # TODO - externalise the values
    SLOW = ProjectileSpeedType(10)
    FAST = ProjectileSpeedType(30)
