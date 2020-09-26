
from typing import List
from snecs.typedefs import EntityID

from scripts.engine import world
from scripts.engine.action import Affliction, Skill
from scripts.engine.component import Aesthetic, Afflictions, Identity, Knowledge, Position
from scripts.engine.core.constants import (
    AfflictionTrigger,
    Direction,
    EffectType,
    Resource,
    Shape,
    TargetingMethod,
    TargetTag,
)
from scripts.engine.effect import Effect, ReduceSkillCooldownEffect, TriggerAfflictionsEffect
from tests.mocks import world_mock


class MockAffliction(Affliction):
    name = 'mock_affliction'
    identity_tags = [
        EffectType.AFFECT_STAT
    ]
    triggers = [
        AfflictionTrigger.MOVEMENT
    ]
    required_tags = [
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
    required_tags = [TargetTag.SELF]
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

    def build_effects(self, entity: EntityID, effect_strength: float = 1.0) -> List[Effect]:
        return []

    def get_animation(self, aesthetic: Aesthetic):
        pass


class TestEffects:

    @staticmethod
    def _create_default_entity():
        components = [Identity("mock_entity"), Position((0, 0))]
        entity = world.create_entity(components)
        return entity

    def test_trigger_afflictions_effect(self):
        """
        Test for the trigger afflictions effect
        """
        affliction_called = None

        def _trigger_affliction_mock(affliction: Affliction):
            nonlocal affliction_called
            affliction_called = affliction

        world_mock.mock_methods({"apply_affliction": _trigger_affliction_mock})
        entity = TestEffects._create_default_entity()

        mock_affliction_movement = MockAfflictionMovement(entity, entity, 5)
        mock_affliction_damage = MockAfflictionDamage(entity, entity, 5)
        afflictions = Afflictions([mock_affliction_damage, mock_affliction_movement])
        world.add_component(entity, afflictions)

        effect = TriggerAfflictionsEffect(entity, entity, AfflictionTrigger.MOVEMENT, [], [])
        effect.evaluate()

        assert affliction_called == mock_affliction_movement

    def test_reduce_skill_cooldown_effect(self):
        """
        Test for the reduce skill cooldown effect
        """
        knowledge = Knowledge([MockSkill])
        knowledge.set_skill_cooldown("mock_skill", 15)

        entity = TestEffects._create_default_entity()
        world.add_component(entity, knowledge)

        effect = ReduceSkillCooldownEffect(entity, entity, "mock_skill", 5, [], [])
        effect.evaluate()

        assert knowledge.cooldowns["mock_skill"] == 10
