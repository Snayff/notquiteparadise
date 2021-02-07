from __future__ import annotations

import os
from enum import auto, IntEnum
from pathlib import Path
from types import SimpleNamespace
from typing import NewType, Tuple, Union

import pygame
import tcod

######################## TOP LEVEL CONSTANTS ######################################

VERSION = "0.162.0"  # DONT FORGET TO UPDATE SPHINX VERSION
DEBUG_START = False  # Whether to start directly in debug map

MAX_SKILLS = 6
MAX_SAVES = 1
TILE_SIZE = 32
ICON_IN_TEXT_SIZE = TILE_SIZE // 4
ICON_SIZE = TILE_SIZE // 2
GAP_SIZE = 2
SKILL_BUTTON_SIZE = 32
INFINITE = 999
MAX_ACTIVATION_DISTANCE = 5  # this is how far from the player an entity can be and still be considered active
FOV_LIGHT_WALLS = True
FOV_ALGORITHM = tcod.FOV_RESTRICTIVE
MAP_BORDER_SIZE = 4

######################## PATHS ######################################

ROOT_PATH = Path(__file__).parent.parent.parent.parent  # constants.py is three directories deep

# to move up from docs and handle being in Ubuntu in CI
if "GENERATING_SPHINX_DOCS" in os.environ:
    ROOT_PATH = ROOT_PATH / os.pardir

DATA_PATH = ROOT_PATH / "data/"
ASSET_PATH = ROOT_PATH / "assets/"
IMAGE_NOT_FOUND_PATH = ASSET_PATH / "debug/image_not_found.png"
SAVE_PATH = DATA_PATH / "saves/"
UI_PATH = DATA_PATH / "ui/"

######################## NEW TYPES ######################################
# NewType guarantees you don't accidentally pass in a normal str instead of a value explicitly defined as a member of
# that NewType, and that you don't treat that member as a normal str.

InputIntentType = NewType("InputIntentType", str)
PrimaryStatType = NewType("PrimaryStatType", str)
SecondaryStatType = NewType("SecondaryStatType", str)
ResourceType = NewType("ResourceType", str)
TileTagType = NewType("TileTagType", str)
DamageTypeType = NewType("DamageTypeType", str)
HitTypeType = NewType("HitTypeType", str)
EffectTypeType = NewType("EffectTypeType", str)
AfflictionCategoryType = NewType("AfflictionCategoryType", str)
ShapeType = NewType("ShapeType", str)
TerrainCollisionType = NewType("TerrainCollisionType", str)
TravelMethodType = NewType("TravelMethodType", str)
ProjectileExpiryType = NewType("ProjectileExpiryType", str)
ProjectileSpeedType = NewType("ProjectileSpeedType", int)
DirectionType = NewType("DirectionType", Tuple[int, int])
TargetingMethodType = NewType("TargetingMethodType", str)
TraitGroupType = NewType("TraitGroupType", str)
ReactionTriggerType = NewType("ReactionTriggerType", str)
TileCategoryType = NewType("TileCategoryType", str)
HeightType = NewType("HeightType", int)
SpriteCategoryType = NewType("SpriteCategoryType", str)


#################### INTERNAL, NON-SERIALISED ###########################################


class EventType(IntEnum):
    """ The types of possible customer pygame events. """

    INPUT = auto()
    GAME = auto()
    INTERACTION = auto()


class InputEventType(IntEnum):
    """
    Custom pygame event names triggered by input. These need to be interpreted into intents.
    """

    TILE_CLICK = pygame.USEREVENT + 1
    SKILL_BAR_CLICK = pygame.USEREVENT + 2


class GameEventType(IntEnum):
    """
    Custom pygame event names triggered by the game
    """

    EXIT_MENU = auto()
    NEW_GAME = auto()
    LOAD_GAME = auto()
    EXIT_GAME = auto()
    WIN_CONDITION_MET = auto()
    START_GAME = auto()
    NEW_TURN = auto()
    END_TURN = auto()
    NEW_ROUND = auto()
    END_ROUND = auto()
    MESSAGE = auto()


class InteractionEventType(IntEnum):
    """
    Custom pygame events to trigger interactions. Think of these as categories for Reaction Triggers.
    """

    MOVE = auto()
    DAMAGE = auto()
    AFFECT_STAT = auto()
    AFFECT_COOLDOWN = auto()
    AFFLICTION = auto()
    ALTER_TERRAIN = auto()


class RenderLayer(IntEnum):
    """
    The possible render layers. Lower number is further down the stack.
    """

    BOTTOM = 10
    TILE = 20
    TERRAIN = 30
    ACTOR = 40
    UI_BASE = 50
    UI_WINDOW = 60


class GameState(IntEnum):
    """
    States the game can be in.
    """

    LOADING = 1  # while loading, to prevent key press.
    GAME_MAP = 2  # while player moving around the game_map
    PLAYER_DEAD = 3  # while player is dead
    TARGETING = 4  # while player is targeting
    EXITING = 5  # while exiting
    DEVELOPER = 6  # while using dev mode
    MENU = 7  # while using a menu


class UIElement(IntEnum):
    """
    The different, single instance UI elements
    """

    MESSAGE_LOG = auto()
    ACTOR_INFO = auto()
    SKILL_BAR = auto()
    ENTITY_QUEUE = auto()
    TILE_INFO = auto()
    DUNGEN_VIEWER = auto()
    TITLE_SCREEN = auto()
    CHARACTER_SELECTOR = auto()


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
    CENTRE = InputIntentType("centre")
    CONFIRM = InputIntentType("confirm")
    CANCEL = InputIntentType("cancel")
    EXIT = InputIntentType("exit")
    DEBUG_TOGGLE = InputIntentType("debug_toggle")
    SKILL0 = InputIntentType("skill0")
    SKILL1 = InputIntentType("skill1")
    SKILL2 = InputIntentType("skill2")
    SKILL3 = InputIntentType("skill3")
    SKILL4 = InputIntentType("skill4")
    SKILL5 = InputIntentType("skill5")
    REFRESH_DATA = InputIntentType("refresh_data")
    DEV_TOGGLE = InputIntentType("dev_toggle")
    ACTOR_INFO_TOGGLE = InputIntentType("actor_info_toggle")
    BURST_PROFILE = InputIntentType("burst_profile")
    TEST = InputIntentType("test")
    DUNGEON_DEV_VIEW = InputIntentType("dungeon_dev_toggle")
    TOGGLE_UI = InputIntentType("toggle_ui")
    LEFT_CLICKED = InputIntentType("left_clicked")


class Direction(SimpleNamespace):
    """
    Holds a tuple as (x, y) for the relative direction.
    """

    # N.B external values must be actively mapped to these on load as they are not held as strings
    UP_LEFT = DirectionType((-1, -1))
    UP = DirectionType((0, -1))
    UP_RIGHT = DirectionType((1, -1))
    LEFT = DirectionType((-1, 0))
    CENTRE = DirectionType((0, 0))
    RIGHT = DirectionType((1, 0))
    DOWN_LEFT = DirectionType((-1, 1))
    DOWN = DirectionType((0, 1))
    DOWN_RIGHT = DirectionType((1, 1))


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
    ACCURACY = SecondaryStatType("accuracy")
    RESIST_BURN = SecondaryStatType("resist_burn")
    RESIST_CHEMICAL = SecondaryStatType("resist_chemical")
    RESIST_ASTRAL = SecondaryStatType("resist_astral")
    RESIST_COLD = SecondaryStatType("resist_cold")
    RESIST_MUNDANE = SecondaryStatType("resist_mundane")
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


class TraitGroup(SimpleNamespace):
    """
    The types of player traits
    """

    PEOPLE = TraitGroupType("people")
    SAVVY = TraitGroupType("savvy")
    HOMELAND = TraitGroupType("homeland")
    NPC = TraitGroupType("npc")


class EffectType(SimpleNamespace):
    """
    Types of effects
    """

    APPLY_AFFLICTION = EffectTypeType("apply_affliction")
    DAMAGE = EffectTypeType("damage")
    MOVE = EffectTypeType("move")
    AFFECT_STAT = EffectTypeType("affect_stat")
    AFFECT_COOLDOWN = EffectTypeType("affect_cooldown")
    ALTER_TERRAIN = EffectTypeType("alter_terrain")


class TileTag(SimpleNamespace):
    """
    Tags identifying a situation on a Tile.
    """

    SELF = TileTagType("self")
    OTHER_ENTITY = TileTagType("other_entity")
    NO_ENTITY = TileTagType("no_entity")
    ANY = TileTagType("any")
    OPEN_SPACE = TileTagType("open_space")
    BLOCKED_MOVEMENT = TileTagType("blocked_movement")
    IS_VISIBLE = TileTagType("is_visible")
    NO_BLOCKING_TILE = TileTagType("no_blocking_tile")
    ACTOR = TileTagType("actor")


class DamageType(SimpleNamespace):
    """
    Damage types
    """

    BURN = DamageTypeType("burn")
    CHEMICAL = DamageTypeType("chemical")
    ASTRAL = DamageTypeType("astral")
    COLD = DamageTypeType("cold")
    MUNDANE = DamageTypeType("mundane")


class ReactionTrigger(SimpleNamespace):
    """
    Type of trigger for the affliction
    """

    MOVE = ReactionTriggerType("move")
    MOVED = ReactionTriggerType("moved")
    PROXIMITY = ReactionTriggerType("proximity")
    TAKE_DAMAGE = ReactionTriggerType("take_damage")
    DEAL_DAMAGE = ReactionTriggerType("deal_damage")
    KILL = ReactionTriggerType("kill")
    DIE = ReactionTriggerType("die")
    COLLISION = ReactionTriggerType("collision")
    STAT_AFFECTED = ReactionTriggerType("stat_affected")
    CAUSED_AFFECT_STAT = ReactionTriggerType("caused_affect_stat")
    COOLDOWN_AFFECTED = ReactionTriggerType("cooldown_affected")
    CAUSED_AFFECT_COOLDOWN = ReactionTriggerType("caused_affect_cooldown")
    AFFLICTED = ReactionTriggerType("afflicted")
    CAUSED_AFFLICTION = ReactionTriggerType("caused_affliction")


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
    TILE = TargetingMethodType("tile")
    LINE_OF_SIGHT = TargetingMethodType("line")


class Shape(SimpleNamespace):
    """
    When to trigger the afflictions
    """

    TARGET = ShapeType("target")  # single target
    SQUARE = ShapeType("square")
    CIRCLE = ShapeType("circle")
    CROSS = ShapeType("cross")
    CONE = ShapeType("cone")


class TerrainCollision(SimpleNamespace):
    """
    What to do when a skill hits terrain
    """

    REFLECT = TerrainCollisionType("reflect")  # bounce back
    ACTIVATE = TerrainCollisionType("activate")  # trigger effects
    FIZZLE = TerrainCollisionType("fizzle")  # kill self


class TravelMethod(SimpleNamespace):
    """
    How the skill travels
    """

    STANDARD = TravelMethodType("standard")  # travels tile by tile
    ARC = TravelMethodType("arc")  # only impacts last tile in range, can reflect if hits terrain early.


class ProjectileExpiry(SimpleNamespace):
    """
    What happens when the skill reaches the range limit
    """

    FIZZLE = ProjectileExpiryType("fizzle")
    ACTIVATE = ProjectileExpiryType("activate")


class ProjectileSpeed(SimpleNamespace):
    """
    The speed at which a projectile travels; how much time to move a tile.
    N.B. does not use base move_cost
    """

    # N.B external values  must be actively mapped to these on load as they are not held as strings
    SLOW = ProjectileSpeedType(10)
    AVERAGE = ProjectileSpeedType(int(SLOW / 2))
    FAST = ProjectileSpeedType(int(AVERAGE / 2))
    INSTANT = ProjectileSpeedType(0)


class TileCategory(SimpleNamespace):
    """
    The type of tile to be placed. Used in Dungen only.
    """

    FLOOR = TileCategoryType("floor")
    WALL = TileCategoryType("wall")
    ACTOR = TileCategoryType("actor")
    DEBUG = TileCategoryType("debug")
    PLAYER = TileCategoryType("player")


class Height(SimpleNamespace):
    """
    How tall an entity is.
    """

    MIN = HeightType(1)
    DIMINUTIVE = HeightType(2)
    MIDDLING = HeightType(3)
    LOFTY = HeightType(4)
    MAX = HeightType(5)


class SpriteCategory(SimpleNamespace):
    ICON = SpriteCategoryType("icon")
    IDLE = SpriteCategoryType("idle")
    ATTACK = SpriteCategoryType("attack")
    HIT = SpriteCategoryType("hit")
    DEAD = SpriteCategoryType("dead")
    MOVE = SpriteCategoryType("move")
