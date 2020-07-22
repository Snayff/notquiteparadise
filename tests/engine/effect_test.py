import pytest

from scripts.engine import world
from scripts.engine.component import Afflictions, Identity, Knowledge, Position
from scripts.engine.core.constants import AfflictionTrigger
from scripts.engine.effect import (ReduceSkillCooldownEffect,
                                   TriggerAfflictionsEffect)
from scripts.nqp.actions.afflictions import Affliction
from scripts.nqp.actions.skills import Move
from tests.mocks import world_mock


class MockAffliction(Affliction):
    name = 'mock_affliction'
    identity_tags = [
        "affect_stat"
    ]
    triggers = [
        "movement"
    ]
    required_tags = [
        "other_entity"
    ]

    def __init__(self, creator, affected_entity, duration):
        super().__init__(creator, affected_entity, duration)
        self.triggered = False

    def build_effects(self, entity):
        self.triggered = True
        return []


class MockAfflictionDamage(MockAffliction):
    triggers = [
        "take_damage"
    ]


class MockAfflictionMovement(MockAffliction):
    triggers = [
        "movement"
    ]


class TestEffects:

    @staticmethod
    def _create_default_entity():
        components = [Identity('mock_entity'), Position(0, 0)]
        entity = world.create_entity(components)
        return entity

    def test_trigger_afflictions_effect(self):
        """
        Test for the trigger afflictions effect
        """
        affliction_called = None

        def _trigger_affliction_mock(affliction):
            nonlocal affliction_called
            affliction_called = affliction

        world_mock.mock_methods({'apply_affliction': _trigger_affliction_mock})
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
        knowledge = Knowledge([Move])
        knowledge.set_skill_cooldown('move', 15)

        entity = TestEffects._create_default_entity()
        world.add_component(entity, knowledge)

        effect = ReduceSkillCooldownEffect(entity, entity, 'move', 5, [], [])
        effect.evaluate()

        assert knowledge.get_skill_cooldown('move') == 10
