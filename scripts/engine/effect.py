from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, cast
from snecs.typedefs import EntityID
from scripts.engine import utility, world
from scripts.engine.component import (Aesthetic, Afflictions, Blocking,
                                      Knowledge, Position, Resources)
from scripts.engine.core.constants import (AfflictionTrigger,
                                           AfflictionTriggerType,
                                           DamageTypeType, Direction,
                                           DirectionType, PrimaryStatType,
                                           TargetTag)

if TYPE_CHECKING:
    from typing import Optional, List


class Effect(ABC):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]]):
        self.origin = origin
        self.success_effects: List[Optional[Effect]] = success_effects
        self.failure_effects: List[Optional[Effect]] = failure_effects

    @abstractmethod
    def evaluate(self):
        """
        Evaluate the effect, triggering more if needed. Must be overridden by subclass
        """
        pass

    def _create_affliction_trigger(self, trigger_type, target):
        return TriggerAfflictionsEffect(self.origin, target, trigger_type, [], [])


class DamageEffect(Effect):
    def __init__(self, origin: EntityID, target: EntityID, success_effects: List[Optional[Effect]],
                failure_effects: List[Optional[Effect]], stat_to_target: PrimaryStatType, accuracy: int,
                damage: int, damage_type: DamageTypeType, mod_stat: PrimaryStatType, mod_amount: float):

        super().__init__(origin, success_effects, failure_effects)

        self.accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.target = target
        self.damage = damage
        self.damage_type = damage_type
        self.mod_amount = mod_amount
        self.mod_stat = mod_stat
        self.success_triggers = [
            self._create_affliction_trigger(AfflictionTrigger.TAKE_DAMAGE, self.target)
        ]

    def evaluate(self) -> List[Optional[Effect]]:
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
            if damage >= defenders_resources.health:
                world.kill_entity(self.target)

            return self.success_effects + self.success_triggers
        else:
            return self.failure_effects


class MoveActorEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], target: EntityID, direction: DirectionType, move_amount: int):

        super().__init__(origin, success_effects, failure_effects)

        self.target = target
        self.direction = direction
        self.move_amount = move_amount
        self.success_triggers = [
            self._create_affliction_trigger(AfflictionTrigger.MOVEMENT, self.target)
        ]

    def evaluate(self) -> List[Optional[Effect]]:
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
        name = world.get_name(entity)
        direction_name = utility.value_to_member((dir_x, dir_y), Direction)

        # loop each target tile in turn
        for _ in range(0, self.move_amount):
    
            target_x = pos.x + dir_x
            target_y = pos.y + dir_y
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
                logging.debug(f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was"
                              f" blocked by terrain. ")
                success = False

            # check if entity blocking tile
            elif is_entity_on_tile and target_tile:
                for blocking_entity, (position, blocking) in world.get_components([Position, Blocking]):
                    # cast for typing
                    position = cast(Position, position)
                    blocking = cast(Blocking, blocking)

                    if blocking.blocks_movement and (position.x == target_tile.x and position.y == target_tile.y):
                        # blocked by entity
                        blockers_name = world.get_name(blocking_entity)
                        logging.debug(
                            f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was blocked"
                            f" by '{blockers_name}'. ")
                        success = False
                        break

            # if nothing in the way, time to move!
            # not is_entity_on_tile and not is_tile_blocking_movement
            else:
                # named _position as typing was inferring from position above
                _position = world.get_entitys_component(entity, Position)

                # update position
                if _position:
                    _position.x = target_x
                    _position.y = target_y
                    success = True

                # animate change
                aesthetic = world.get_entitys_component(entity, Aesthetic)
                if aesthetic:
                    aesthetic.target_draw_x, aesthetic.target_draw_y = (target_x, target_y)
                    aesthetic.current_sprite = aesthetic.sprites.move

                # update fov
                world.recompute_fov(entity)

        if success:
            return self.success_effects + self.success_triggers
        else:
            return self.failure_effects


class TriggerAfflictionsEffect(Effect):
    def __init__(self, origin: EntityID, target: EntityID, trigger_type: AfflictionTriggerType,
            success_effects: List[Optional[Effect]], failure_effects: List[Optional[Effect]]):

        super().__init__(origin, success_effects, failure_effects)

        self.trigger_type = trigger_type
        self.target = target

    def evaluate(self) -> List[Optional[Effect]]:
        """
        Trigger all the afflictions on the self.target entity that match the trigger type. Fail if nothing matches
        """
        logging.debug(f"Evaluating Trigger Affliction Effect of type '{self.trigger_type}'...")
        afflictions = world.get_entitys_component(self.target, Afflictions)
        # iterate over each affliction and trigger it if necessary
        success = True
        for affliction in afflictions.active:
            if self.trigger_type in affliction.triggers:
                success = success and world.apply_affliction(affliction)

        if success:
            return self.success_effects
        return self.failure_effects


class AffectStatEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], cause_name: str,  target: EntityID,
            stat_to_target: PrimaryStatType, affect_amount: int):

        super().__init__(origin, success_effects, failure_effects)

        self.stat_to_target = stat_to_target
        self.affect_amount = affect_amount
        self.target = target
        self.cause_name = cause_name

    def evaluate(self) -> List[Optional[Effect]]:
        """
        Log the affliction and the stat modification in the Affliction component.
        """
        logging.debug("Evaluating Affect Stat Effect...")
        success = False

        afflictions = world.get_entitys_component(self.target, Afflictions)

        # if not already applied
        if self.cause_name not in afflictions.stat_modifiers:
            afflictions.stat_modifiers[self.cause_name] = (self.stat_to_target, self.affect_amount)
            success = True

        if success:
            return self.success_effects
        else:
            return self.failure_effects


class ApplyAfflictionEffect(Effect):
    def __init__(self, origin: EntityID, target: EntityID, affliction_name: str, duration: int,
                 success_effects: List[Optional[Effect]], failure_effects: List[Optional[Effect]]):
        super().__init__(origin, success_effects, failure_effects)

        self.affliction_name = affliction_name
        self.target = target
        self.duration = duration

    def evaluate(self) -> List[Optional[Effect]]:
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
    def __init__(self, origin: EntityID, target: EntityID, skill_name: str, amount: int,
                 success_effects: List[Optional[Effect]], failure_effects: List[Optional[Effect]]):
        super().__init__(origin, success_effects, failure_effects)

        self.target = target
        self.skill_name = skill_name
        self.amount = amount

    def evaluate(self) -> List[Optional[Effect]]:
        """
        Reduces the cooldown of a skill of an entity
        """
        logging.debug("Evaluating Reduce Skill Cooldown Effect...")

        knowledge = world.get_entitys_component(self.target, Knowledge)

        if knowledge:
            current_cooldown = knowledge.get_skill_cooldown(self.skill_name)
            knowledge.set_skill_cooldown(self.skill_name, current_cooldown - self.amount)
            logging.debug(f"Reduced cooldown of skill '{self.skill_name}' from {current_cooldown} to {knowledge.get_skill_cooldown(self.skill_name)}")
            return self.success_effects

        return self.failure_effects


class AddAspectEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Optional[Effect]]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Add Aspect Effect...")
        logging.warning("-> effect not implemented.")

        return []


class RemoveAspectEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Optional[Effect]]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Remove Aspect Effect...")
        logging.warning("-> effect not implemented.")

        return []


class TriggerSkillEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], ):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Optional[Effect]]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Trigger Skill Effect...")
        logging.warning("-> effect not implemented.")

        return []


class KillEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]],):
        super().__init__(origin, success_effects, failure_effects)

    def evaluate(self) -> List[Optional[Effect]]:
        """
        TBC - not implemented
        """
        logging.debug("Evaluating Kill Effect...")
        logging.warning("-> effect not implemented.")

        return []
