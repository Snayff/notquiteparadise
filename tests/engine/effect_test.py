import pytest
from scripts.engine.effect import TriggerAfflictionsEffect, ReduceSkillCooldownEffect, MoveActorEffect
from scripts.engine import world
from scripts.engine.core.constants import AfflictionTrigger
from scripts.nqp.actions.afflictions import Affliction
from scripts.engine.component import Afflictions


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

    def test_trigger_afflictions_effect(self):
        """
        Test for the trigger afflictions effect
        """
        entity = world.create_entity([])

        mock_affliction_movement = MockAfflictionMovement(entity, entity, 5)
        mock_affliction_damage = MockAfflictionDamage(entity, entity, 5)
        afflictions = Afflictions([mock_affliction_damage, mock_affliction_movement])
        world.add_component(entity, afflictions)

        effect = TriggerAfflictionsEffect(entity, entity, trigger_type=AfflictionTrigger.MOVEMENT, success_effects=[], failure_effects=[])
        effect.evaluate()

    def test_reduce_skill_cooldown_effect(self):
        """
        Test for the reduce skill cooldown effect
        """
        pass

    def test_move_effect(self):
        """
        Test for the reduce skill cooldown effect
        """
        pass

