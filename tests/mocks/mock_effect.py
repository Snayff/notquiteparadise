from __future__ import annotations

from typing import List

from snecs.typedefs import EntityID

from scripts.engine.action import Affliction, Skill
from scripts.engine.component import Aesthetic
from scripts.engine.core.constants import AfflictionTrigger, Direction, EffectType, Resource, Shape, TargetTag, \
    TargetingMethod
from scripts.engine.effect import Effect


class MockAffliction(Affliction):
    name = 'mock_affliction'
    identity_tags = [
        EffectType.AFFECT_STAT
    ]
    triggers = [
        AfflictionTrigger.MOVEMENT
    ]
    target_tags = [
        TargetTag.OTHER_ENTITY
    ]

    def __init__(self, creator, affected_entity, duration):
        super().__init__(creator, affected_entity, duration)
        self.triggered = False

    def build_effects(self, entity):
        self.triggered = True
        return []


class MockAfflictionDamage(MockAffliction):
    triggers = [
        AfflictionTrigger.TAKE_DAMAGE
    ]


class MockAfflictionMovement(MockAffliction):
    triggers = [
        AfflictionTrigger.MOVEMENT
    ]


class MockSkill(Skill):
    key = "mock_skill"
    target_tags = [TargetTag.SELF]
    description = "this is the normal movement."
    icon_path = ""
    resource_type = Resource.STAMINA
    resource_cost = 0
    time_cost = 10
    base_cooldown = 0
    targeting_method = TargetingMethod.TARGET
    target_directions = [
        Direction.UP_LEFT,
        Direction.UP,
        Direction.UP_RIGHT,
        Direction.LEFT,
        Direction.CENTRE,
        Direction.RIGHT,
        Direction.DOWN_LEFT,
        Direction.DOWN,
        Direction.DOWN_RIGHT
    ]
    shape = Shape.TARGET
    shape_size = 1
    uses_projectile = False

    def build_effects(self, entity: EntityID, potency: float = 1.0) -> List[Effect]:
        return []

    def get_animation(self, aesthetic: Aesthetic):
        pass