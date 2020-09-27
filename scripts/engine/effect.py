from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, cast
from snecs.typedefs import EntityID
from scripts.engine import utility, world
from scripts.engine.component import Aesthetic, Afflictions, Blocking, Knowledge, Position, Resources
from scripts.engine.core.constants import (
    AfflictionTrigger,
    AfflictionTriggerType,
    DamageTypeType,
    Direction,
    DirectionType,
    PrimaryStatType,
    TargetTag,
)

if TYPE_CHECKING:
    from typing import Optional, List


class Effect(ABC):
    """
    A collection of parameters and instructions to apply a change to an entity's or tile's state.
    """
    def __init__(self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect],
            potency: float = 1.0):
        self.origin = origin
        self.success_effects: List[Effect] = success_effects
        self.failure_effects: List[Effect] = failure_effects
        self.potency: float = potency

    @abstractmethod
    def evaluate(self):
        """
        Evaluate the effect, triggering more if needed. Must be overridden by subclass
        """
        pass

    def _create_affliction_trigger(self, trigger_type, target):
        return TriggerAfflictionsEffect(self.origin, target, trigger_type, [], [])


class DamageEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        stat_to_target: PrimaryStatType,
        accuracy: int,
        damage: int,
        damage_type: DamageTypeType,
        mod_stat: PrimaryStatType,
        mod_amount: float,
        potency: float = 1.0
    ):

        super().__init__(origin, success_effects, failure_effects, potency)

        self.accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.target = target
        self.damage = damage
        self.damage_type = damage_type
        self.mod_amount = mod_amount
        self.mod_stat = mod_stat
        self.success_triggers = [self._create_affliction_trigger(AfflictionTrigger.TAKE_DAMAGE, self.target)]

    def evaluate(self) -> List[Effect]:
        """
        Resolve the damage effect and return the conditional effects based on if the damage is greater than 0.
        """
        logging.debug("Evaluating Damage Effect...")
        defenders_stats = world.create_combat_stats(self.target)
        attackers_stats = world.create_combat_stats(self.origin)

        # get hit type
        stat_to_target_value = getattr(defenders_stats, self.stat_to_target.lower())
        to_hit_score = world.calculate_to_hit_score(attackers_stats.accuracy, self.accuracy, stat_to_target_value)
        hit_type = world.get_hit_type(to_hit_score)

        # calculate damage
        resist_value = getattr(defenders_stats, "resist_" + self.damage_type.lower())
        mod_value = getattr(attackers_stats, self.mod_stat.lower())
        damage = world.calculate_damage(self.damage, mod_value, resist_value, hit_type)

        # apply the damage
        if world.apply_damage(self.target, damage):
            defenders_resources = world.get_entitys_component(self.target, Resources)
            if defenders_resources:
                if damage >= defenders_resources.health:
                    world.kill_entity(self.target)

            return self.success_effects + self.success_triggers
        else:
            return self.failure_effects


class MoveActorEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        target: EntityID,
        direction: DirectionType,
        move_amount: int,
    ):

        super().__init__(origin, success_effects, failure_effects)

        self.target = target
        self.direction = direction
        self.move_amount = move_amount
        self.success_triggers = [self._create_affliction_trigger(AfflictionTrigger.MOVEMENT, self.target)]

    def evaluate(self) -> List[Effect]:
        """
        Resolve the move effect and return the conditional effects based on if the target moved the full amount.
        """
        logging.debug("Evaluating Move Actor Effect...")

        success = False
        pos = world.get_entitys_component(self.target, Position)
        if not pos:
            return self.failure_effects

        dir_x, dir_y = self.direction
        entity = self.target

        # loop each target tile in turn
        for _ in range(0, self.move_amount):
            new_x = pos.x + dir_x
            new_y = pos.y + dir_y
            collides = MoveActorEffect._check_collision(entity, dir_x, dir_y)
            success = not collides

            if not collides:
                # named _position as typing was inferring from position above
                _position = world.get_entitys_component(entity, Position)

                # update position
                if _position:
                    _position.set(new_x, new_y)
                    success = True

                # animate change
                aesthetic = world.get_entitys_component(entity, Aesthetic)
                if aesthetic:
                    aesthetic.target_draw_x, aesthetic.target_draw_y = (new_x, new_y)
                    aesthetic.current_sprite = aesthetic.sprites.move

        if success:
            return self.success_effects + self.success_triggers
        else:
            return self.failure_effects

    @staticmethod
    def _check_collision(entity, dir_x, dir_y):
        """
        Checks if the entity will be able to move in the provided direction
        :param entity: Entity to test
        :param dir_x: X component of the direction
        :param dir_y: Y component of the direction
        :return: A bool that represents if the entity will collide if it moves in the provided direction
        """
        collides = False

        name = world.get_name(entity)
        direction_name = utility.value_to_member((dir_x, dir_y), Direction)
        position = world.get_entitys_component(entity, Position)

        for coordinate in position.coordinates:
            target_x = coordinate[0] + dir_x
            target_y = coordinate[1] + dir_y
            target_tile = world.get_tile((target_x, target_y))

            # check a tile was returned
            if target_tile:
                is_tile_blocking_movement = world.tile_has_tag(target_tile, TargetTag.BLOCKED_MOVEMENT, entity)
                is_entity_on_tile = not world.tile_has_tag(target_tile, TargetTag.NO_ENTITY)
            else:
                is_tile_blocking_movement = True
                is_entity_on_tile = False

            # check for no entity in way but tile is blocked
            if not is_entity_on_tile and is_tile_blocking_movement and target_tile:
                logging.debug(
                    f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was"
                    f" blocked by terrain. "
                )
                collides = True

            # check if entity blocking tile
            elif is_entity_on_tile and target_tile:
                from scripts.engine.core import queries

                for blocking_entity, (position, blocking) in queries.position_and_blocking:
                    # cast for typing
                    position = cast(Position, position)
                    blocking = cast(Blocking, blocking)
                    if blocking_entity != entity and blocking.blocks_movement and (target_x, target_y) in position:
                        # blocked by entity
                        blockers_name = world.get_name(blocking_entity)
                        logging.debug(
                            f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was blocked"
                            f" by '{blockers_name}'. "
                        )
                        collides = True
                        break

        return collides


class TriggerAfflictionsEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        trigger_type: AfflictionTriggerType,
        success_effects: List[Effect],
        failure_effects: List[Effect],
    ):

        super().__init__(origin, success_effects, failure_effects)

        self.trigger_type = trigger_type
        self.target = target

    def evaluate(self) -> List[Effect]:
        """
        Trigger all the afflictions on the self.target entity that match the trigger type. Fail if nothing matches
        """
        logging.debug(f"Evaluating Trigger Affliction Effect of type '{self.trigger_type}'...")
        afflictions = world.get_entitys_component(self.target, Afflictions)
        success = False

        if afflictions:
            # iterate over each affliction and trigger it if necessary
            for affliction in afflictions.active:
                if self.trigger_type in affliction.triggers:
                    success = world.apply_affliction(affliction)

        if success:
            return self.success_effects
        return self.failure_effects


class AffectStatEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        cause_name: str,
        target: EntityID,
        stat_to_target: PrimaryStatType,
        affect_amount: int,
    ):

        super().__init__(origin, success_effects, failure_effects)

        self.stat_to_target = stat_to_target
        self.affect_amount = affect_amount
        self.target = target
        self.cause_name = cause_name

    def evaluate(self) -> List[Effect]:
        """
        Log the affliction and the stat modification in the Affliction component.
        """
        logging.debug("Evaluating Affect Stat Effect...")
        success = False
        afflictions = world.get_entitys_component(self.target, Afflictions)

        if afflictions:
            # if not already applied
            if self.cause_name not in afflictions.stat_modifiers:
                afflictions.stat_modifiers[self.cause_name] = (self.stat_to_target, self.affect_amount)
                success = True

        if success:
            return self.success_effects
        else:
            return self.failure_effects


class ApplyAfflictionEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        affliction_name: str,
        duration: int,
        success_effects: List[Effect],
        failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

        self.affliction_name = affliction_name
        self.target = target
        self.duration = duration

    def evaluate(self) -> List[Effect]:
        """
        Applies an affliction to an entity
        """
        logging.debug("Evaluating Apply Affliction Effect...")

        affliction_instance = world.create_affliction(self.affliction_name, self.origin, self.target, self.duration)
        afflictions = world.get_entitys_component(self.target, Afflictions)
        # add the affliction to the afflictions component
        if afflictions:
            afflictions.add(affliction_instance)
            return self.success_effects
        # didn't have the component, fail
        return self.failure_effects


class ReduceSkillCooldownEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        skill_name: str,
        amount: int,
        success_effects: List[Effect],
        failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

        self.target = target
        self.skill_name = skill_name
        self.amount = amount

    def evaluate(self) -> List[Effect]:
        """
        Reduces the cooldown of a skill of an entity
        """
        logging.debug("Evaluating Reduce Skill Cooldown Effect...")

        knowledge = world.get_entitys_component(self.target, Knowledge)

        if knowledge:
            current_cooldown = knowledge.cooldowns[self.skill_name]
            knowledge.set_skill_cooldown(self.skill_name, current_cooldown - self.amount)
            logging.debug(
                f"Reduced cooldown of skill '{self.skill_name}' from {current_cooldown} to "
                f"{knowledge.cooldowns[self.skill_name]}"
            )
            return self.success_effects

        return self.failure_effects


class AddAspectEffect(Effect):
    def __init__(
        self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Effect]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Add Aspect Effect...")
        logging.warning("-> effect not implemented.")

        return []


class RemoveAspectEffect(Effect):
    def __init__(
        self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Effect]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Remove Aspect Effect...")
        logging.warning("-> effect not implemented.")

        return []


class TriggerSkillEffect(Effect):
    def __init__(
        self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Effect]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Trigger Skill Effect...")
        logging.warning("-> effect not implemented.")

        return []


class KillEffect(Effect):
    def __init__(
        self, origin: EntityID, success_effects: List[Effect], failure_effects: List[Effect],
    ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Effect]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Kill Effect...")
        logging.warning("-> effect not implemented.")

        return []
