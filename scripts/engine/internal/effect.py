from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Tuple, TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core import query, utility, world
from scripts.engine.core.event import (
    AffectCooldownEvent,
    AffectStatEvent,
    AfflictionEvent,
    AlterTerrainEvent,
    DamageEvent,
    event_hub,
    MoveEvent,
)
from scripts.engine.internal import library
from scripts.engine.internal.component import (
    Aesthetic,
    Afflictions,
    Identity,
    Knowledge,
    Lifespan,
    Physicality,
    Position,
    Resources,
)
from scripts.engine.internal.constant import DamageTypeType, Direction, DirectionType, PrimaryStatType, TargetTag

if TYPE_CHECKING:
    from typing import List

__all__ = [
    "Effect",
    "DamageEffect",
    "MoveActorEffect",
    "AffectStatEffect",
    "ApplyAfflictionEffect",
    "AffectCooldownEffect",
    "AlterTerrainEffect",
]


class Effect(ABC):
    """
    A collection of parameters and instructions to apply a change to an entity's or tile's state.
    """

    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        potency: float = 1.0,
    ):
        self.origin = origin
        self.target = target
        self.success_effects: List[Effect] = success_effects
        self.failure_effects: List[Effect] = failure_effects
        self.potency: float = potency

    @abstractmethod
    def evaluate(self):
        """
        Evaluate the effect, triggering more if needed. Must be overridden by subclass
        """
        pass


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
        potency: float = 1.0,
    ):

        super().__init__(origin, target, success_effects, failure_effects, potency)

        self.accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.damage = damage
        self.damage_type = damage_type
        self.mod_amount = mod_amount
        self.mod_stat = mod_stat

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Resolve the damage effect and return the conditional effects based on if the damage is greater than 0.
        """
        logging.debug("Evaluating Damage Effect...")
        if self.damage <= 0:
            logging.info(f"Damage given to DamageEffect is {self.damage} and was therefore not executed.")
            return False, self.failure_effects

        if not world.entity_has_component(self.target, Resources):
            logging.info(f"Target doesnt have resources so damage cannot be applied.")
            return False, self.failure_effects

        # get combat stats
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

            # post interaction event
            event = DamageEvent(
                origin=self.origin,
                target=self.target,
                amount=damage,
                damage_type=self.damage_type,
                remaining_hp=defenders_resources.health,
            )
            event_hub.post(event)

            # check if target is dead
            if damage >= defenders_resources.health:
                world.kill_entity(self.target)

            return True, self.success_effects
        else:
            return False, self.failure_effects


class MoveActorEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        direction: DirectionType,
        move_amount: int,
    ):

        super().__init__(origin, target, success_effects, failure_effects)

        self.direction = direction
        self.move_amount = move_amount

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Resolve the move effect and return the conditional effects based on if the target moved the full amount.
        """
        logging.debug("Evaluating Move Actor Effect...")

        success = False
        pos = world.get_entitys_component(self.target, Position)
        if not pos:
            return False, self.failure_effects

        dir_x, dir_y = self.direction
        entity = self.target

        # loop each target tile in turn
        for _ in range(0, self.move_amount):
            new_x = pos.x + dir_x
            new_y = pos.y + dir_y
            collides = self._check_collision(entity, dir_x, dir_y)
            success = not collides

            if not collides:
                # named _position as typing was inferring from position above
                _position = world.get_entitys_component(entity, Position)

                # update position
                if _position:
                    _position.set(new_x, new_y)

                    # post interaction event
                    event = MoveEvent(
                        origin=self.origin, target=self.target, direction=self.direction, new_pos=(new_x, new_y)
                    )
                    event_hub.post(event)

                    success = True

                # animate change
                aesthetic = world.get_entitys_component(entity, Aesthetic)
                if aesthetic:
                    aesthetic.target_draw_x, aesthetic.target_draw_y = (new_x, new_y)
                    aesthetic.current_sprite = aesthetic.sprites.move

        if success:
            return True, self.success_effects
        else:
            return False, self.failure_effects

    @staticmethod
    def _check_collision(entity: EntityID, dir_x: int, dir_y: int) -> bool:
        """
        Checks if the entity will collide with something when trying to move in the provided direction. Returns True
        if blocked.
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
            is_tile_blocking_movement = False
            if target_tile:
                is_tile_blocking_movement = world.tile_has_tag(entity, target_tile, TargetTag.BLOCKED_MOVEMENT)

            # check if tile is blocked
            if is_tile_blocking_movement:
                from scripts.engine.core import query

                for other_entity, (pos, physicality) in query.position_and_physicality:
                    assert isinstance(pos, Position)
                    assert isinstance(physicality, Physicality)
                    if (
                        other_entity != entity
                        and physicality.blocks_movement
                        and (target_x, target_y) in pos.coordinates
                    ):
                        # blocked by entity
                        blockers_name = world.get_name(other_entity)
                        logging.debug(
                            f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was blocked"
                            f" by '{blockers_name}'. "
                        )
                        break
                collides = True

        return collides


class AffectStatEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        cause_name: str,
        stat_to_target: PrimaryStatType,
        affect_amount: int,
    ):

        super().__init__(origin, target, success_effects, failure_effects)

        self.stat_to_target = stat_to_target
        self.affect_amount = affect_amount
        self.cause_name = cause_name

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Log the affliction and the stat modification in the Affliction component.
        """
        logging.debug("Evaluating Affect Stat Effect...")
        success = False
        afflictions = world.get_entitys_component(self.target, Afflictions)

        # if not already applied
        if self.cause_name not in afflictions.stat_modifiers:
            afflictions.stat_modifiers[self.cause_name] = (self.stat_to_target, self.affect_amount)

            # post interaction event
            event = AffectStatEvent(
                origin=self.origin,
                target=self.target,
                stat_to_target=self.stat_to_target,
                amount=self.affect_amount,
            )
            event_hub.post(event)

            success = True

        if success:
            return True, self.success_effects
        else:
            return False, self.failure_effects


class ApplyAfflictionEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        affliction_name: str,
        duration: int,
    ):
        super().__init__(origin, target, success_effects, failure_effects)

        self.affliction_name = affliction_name
        self.duration = duration

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Applies an affliction to an entity
        """
        logging.debug("Evaluating Apply Affliction Effect...")

        affliction_instance = world.create_affliction(self.affliction_name, self.origin, self.target, self.duration)

        # add the affliction to the afflictions component
        if world.entity_has_component(self.target, Afflictions):
            afflictions = world.get_entitys_component(self.target, Afflictions)
            afflictions.add(affliction_instance)
            world.apply_affliction(affliction_instance)

            # post interaction event
            event = AfflictionEvent(
                origin=self.origin,
                target=self.target,
                affliction_name=self.affliction_name,
            )
            event_hub.post(event)

            return True, self.success_effects

        # didn't have the component, fail
        return False, self.failure_effects


class AffectCooldownEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        skill_name: str,
        affect_amount: int,
    ):
        super().__init__(origin, target, success_effects, failure_effects)

        self.skill_name = skill_name
        self.affect_amount = affect_amount

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Reduces the cooldown of a skill of an entity
        """
        logging.debug("Evaluating Reduce Skill Cooldown Effect...")

        knowledge = world.get_entitys_component(self.target, Knowledge)

        if knowledge:
            current_cooldown = knowledge.cooldowns[self.skill_name]
            knowledge.set_skill_cooldown(self.skill_name, current_cooldown - self.affect_amount)

            # post interaction event
            event = AffectCooldownEvent(
                origin=self.origin,
                target=self.target,
                amount=self.affect_amount,
            )
            event_hub.post(event)

            logging.debug(
                f"Reduced cooldown of skill '{self.skill_name}' from {current_cooldown} to "
                f"{knowledge.cooldowns[self.skill_name]}"
            )
            return True, self.success_effects

        return False, self.failure_effects


class AlterTerrainEffect(Effect):
    def __init__(
        self,
        origin: EntityID,
        target: EntityID,
        success_effects: List[Effect],
        failure_effects: List[Effect],
        terrain_name: str,
        affect_amount: int,
    ):
        super().__init__(origin, target, success_effects, failure_effects)

        self.terrain_name = terrain_name
        self.affect_amount = affect_amount

    def evaluate(self) -> Tuple[bool, List[Effect]]:
        """
        Create or reduce the duration of temporary terrain.
        """
        logging.debug("Evaluating Alter Terrain Effect...")

        # check duration
        if self.affect_amount <= 0:
            success = self._reduce_terrain_duration()
        else:
            success = self._create_terrain()

        # return effect sets
        if success:
            return True, self.success_effects
        else:
            return False, self.failure_effects

    def _create_terrain(self) -> bool:
        result = False
        duplicate = False
        terrain_name = self.terrain_name
        target_pos = world.get_entitys_component(self.target, Position)

        # check target location doesnt already have the given terrain
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            assert isinstance(position, Position)
            assert isinstance(identity, Identity)
            assert isinstance(lifespan, Lifespan)
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                duplicate = True
                break

        # can we create the terrain?
        if not duplicate:
            # create target
            terrain_data = library.TERRAIN[terrain_name]
            world.create_terrain(terrain_data, (target_pos.x, target_pos.y), self.affect_amount)
            result = True

            # post interaction event
            event = AlterTerrainEvent(
                origin=self.origin, target=self.target, terrain_name=self.terrain_name, duration=self.affect_amount
            )
            event_hub.post(event)

        return result

    def _reduce_terrain_duration(self) -> bool:
        result = False
        terrain_name = self.terrain_name
        target_pos = world.get_entitys_component(self.target, Position)

        # check there is a terrain at target to reduce duration of
        for entity, (position, identity, lifespan) in query.position_and_identity_and_lifespan:
            assert isinstance(position, Position)
            assert isinstance(identity, Identity)
            assert isinstance(lifespan, Lifespan)
            if identity.name == terrain_name and position.x == target_pos.x and position.y == target_pos.y:
                lifespan.duration -= self.affect_amount
                result = True
                break

        if result:
            # post interaction event
            event = AlterTerrainEvent(
                origin=self.origin, target=self.target, terrain_name=self.terrain_name, duration=self.affect_amount
            )
            event_hub.post(event)

        return result
