from __future__ import annotations

import logging
from abc import ABC
from typing import TYPE_CHECKING, cast
from snecs.typedefs import EntityID
from scripts.engine import world, utility
from scripts.engine.component import Blocking, Aesthetic, Position, Resources
from scripts.engine.core.constants import PrimaryStatType, DamageTypeType, Direction, TargetTag, DirectionType
from scripts.engine.core.event_core import publisher
from scripts.engine.event import EntityCollisionEvent, TerrainCollisionEvent

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class Effect(ABC):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]]):
        self.origin = origin
        self.success_effects: List[Optional[Effect]] = success_effects
        self.failure_effects: List[Optional[Effect]] = failure_effects


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

            return self.success_effects
        else:
            return self.failure_effects


class MoveActorEffect(Effect):
    def __init__(self, origin: EntityID, success_effects: List[Optional[Effect]],
            failure_effects: List[Optional[Effect]], target: EntityID, direction: DirectionType, move_amount: int):

        super().__init__(origin, success_effects, failure_effects)

        self.target = target
        self.direction = direction
        self.move_amount = move_amount

    def evaluate(self) -> List[Optional[Effect]]:
        """
        Resolve the move effect and return the conditional effects based on if the target moved the full amount.
        """
        logging.debug("Evaluating Move Actor Effect...")

        success = False
        pos = world.get_entitys_component(self.target, Position)
        if not pos:
            return self.failure_effects

        start_pos = (pos.x, pos.y)
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
                is_entity_on_tile = world.tile_has_tag(target_tile, TargetTag.NO_ENTITY)
            else:
                is_tile_blocking_movement = True
                is_entity_on_tile = False
                
            # check for no entity in way but tile is blocked
            if not is_entity_on_tile and is_tile_blocking_movement and target_tile:
                publisher.publish(TerrainCollisionEvent(entity, target_tile, self.direction, start_pos))
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
                        publisher.publish(EntityCollisionEvent(entity, blocking_entity, self.direction, start_pos))
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

                # TODO - move to UI handler
                # animate change
                aesthetic = world.get_entitys_component(entity, Aesthetic)
                if aesthetic:
                    aesthetic.target_screen_x, aesthetic.target_screen_y = (target_x, target_y)
                    aesthetic.current_sprite = aesthetic.sprites.move

                # update fov if needed
                world.recompute_fov(entity)

        if success:
            return self.success_effects
        else:
            return self.failure_effects
