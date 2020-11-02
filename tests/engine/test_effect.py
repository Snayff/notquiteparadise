from scripts.engine import world
from scripts.engine.action import Affliction
from scripts.engine.component import Afflictions, Identity, Knowledge, Position
from scripts.engine.core.constants import (
    AfflictionTrigger,
)
from scripts.engine.effect import ReduceSkillCooldownEffect, TriggerAfflictionsEffect
from tests.mocks import mock_world
from tests.mocks.mock_effect import MockAfflictionDamage, MockAfflictionMovement, MockSkill


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

        mock_world.mock_methods({"apply_affliction": _trigger_affliction_mock})
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
