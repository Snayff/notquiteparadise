from __future__ import annotations

import pygame
from types import SimpleNamespace
from typing import NewType, Tuple

######################## GENERAL CONSTANTS ######################################

VERSION = "0.111.0"

MAX_SKILLS = 5
TILE_SIZE = 64
ICON_IN_TEXT_SIZE = TILE_SIZE // 4
ICON_SIZE = TILE_SIZE // 2
GAP_SIZE = 2
SKILL_BUTTON_SIZE = 64
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
TargetTagType = NewType("TargetTagType", str)
DamageTypeType = NewType("DamageTypeType", str)
HitTypeType = NewType("HitTypeType", str)
EffectTypeType = NewType("EffectTypeType", str)
AfflictionCategoryType = NewType("AfflictionCategoryType", str)
ShapeType = NewType("ShapeType", str)
TerrainCollisionType = NewType("TerrainCollisionType", str)
TravelMethodType = NewType("TravelMethodType", str)
ProjectileExpiryType = NewType("ProjectileExpiryType", str)
ProjectileSpeedType = NewType("ProjectileSpeedType", int)
UIElementType = NewType("UIElementType", int)
DirectionType = NewType("DirectionType", Tuple[int, int])
TargetingMethodType = NewType("TargetingMethodType", str)
TraitGroupType = NewType("TraitGroupType", str)
AfflictionTriggerType = NewType("AfflictionTriggerType", str)
RenderLayerType = NewType("RenderLayerType", int)


#################### INTERNAL, NON-SERIALISED ###########################################

class EventType(SimpleNamespace):
    """
    Constant info about the different custom event names that we can pass to pygame
    """
    TILE_CLICK = pygame.USEREVENT + 1
    SKILL_BAR_CLICK = pygame.USEREVENT + 2
    EXIT_MENU = pygame.USEREVENT + 3


class RenderLayer(SimpleNamespace):
    """
    The possible render layers. Lower number is further down the stack.
    """
    BOTTOM = RenderLayerType(10)
    TILE = RenderLayerType(20)
    ASPECT = RenderLayerType(30)
    ACTOR = RenderLayerType(40)
    UI_BASE = RenderLayerType(50)
    UI_WINDOW = RenderLayerType(60)


class GameState(SimpleNamespace):
    """
    States the game can be in.
    """
    LOADING = GameStateType(1)  # while loading, to prevent key press.
    GAMEMAP = GameStateType(2)  # while player moving around the gamemap
    PLAYER_DEAD = GameStateType(3)  # while player is dead
    TARGETING = GameStateType(4)  # while player is targeting
    EXIT_GAME = GameStateType(5)  # while exiting
    DEVELOPER = GameStateType(6)  # while using dev mode
    MENU = GameStateType(7)  # while using a menu


class UIElement(SimpleNamespace):
    """
    The different, single instance UI elements
    """
    MESSAGE_LOG = UIElementType(1)
    ACTOR_INFO = UIElementType(2)
    SKILL_BAR = UIElementType(4)
    ENTITY_QUEUE = UIElementType(5)
    CAMERA = UIElementType(6)
    DATA_EDITOR = UIElementType(7)
    TILE_INFO = UIElementType(8)


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
    ACTOR_INFO_TOGGLE = InputIntentType("npc_info_toggle")


#################### EXTERNAL, SERIALISED  ###########################################
# i.e used externally

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


class TargetTag(SimpleNamespace):
    """
    Types of target
    """
    SELF = TargetTagType("self")
    OTHER_ENTITY = TargetTagType("other_entity")
    NO_ENTITY = TargetTagType("no_entity")
    ANY = TargetTagType("any")
    OPEN_SPACE = TargetTagType("open_space")
    BLOCKED_MOVEMENT = TargetTagType("blocked_movement")
    IS_VISIBLE = TargetTagType("is_visible")
    NO_BLOCKING_TILE = TargetTagType("no_blocking_tile")
    ACTOR = TargetTagType("actor")


class TraitGroup(SimpleNamespace):
    """
    The types of player traits
    """
    PEOPLE = TraitGroupType("people")
    SAVVY = TraitGroupType("savvy")
    HOMELAND = TraitGroupType("homeland")
    NPC = TraitGroupType("npc")


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


class EffectType(SimpleNamespace):
    """
    Types of effects
    """
    APPLY_AFFLICTION = EffectTypeType("apply_affliction")
    DAMAGE = EffectTypeType("damage")
    MOVE = EffectTypeType("move")
    AFFECT_STAT = EffectTypeType("affect_stat")
    ADD_ASPECT = EffectTypeType("add_aspect")
    REMOVE_ASPECT = EffectTypeType("remove_aspect")
    TRIGGER_SKILL = EffectTypeType("trigger_skill")
    KILL = EffectTypeType("kill")


class AfflictionTrigger(SimpleNamespace):
    """
    Type of trigger for the affliction
    """
    MOVEMENT = AfflictionTriggerType("movement")
    TAKE_DAMAGE = AfflictionTriggerType("take_damage")


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


class Shape(SimpleNamespace):
    """
    When to trigger the afflictions
    """
    TARGET = ShapeType("target")  # single target
    SQUARE = ShapeType("square")
    CIRCLE = ShapeType("circle")
    CROSS = ShapeType("cross"),
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

    SLOW = ProjectileSpeedType(10)
    AVERAGE = ProjectileSpeedType(int(SLOW / 2))
    FAST = ProjectileSpeedType(int(AVERAGE / 2))
    INSTANT = ProjectileSpeedType(0)

