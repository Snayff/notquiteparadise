import random
from enum import Enum

from scripts.core.constants import MessageEventTypes, LoggingEventTypes, TargetTypes, TargetTags, SecondaryStatTypes, \
    HitTypes, DamageTypes
from scripts.core.entity import Entity
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.world.tiles import Tile


class Effect:
    """
    Base class for effects that make up skills.
    """

    def __init__(self):
        self.owner = None


class MoveEffect(Effect):
    """
    Effect to move an entity towards target tile
    """

    def __init__(self, entity_to_move, target, move_distance):
        Effect.__init__(self)
        self.description = "This is the move effect"
        self.entity_to_move = entity_to_move  # TODO - turn into list and accept multiple entities
        self.target = target
        self.move_distance = move_distance

    def trigger(self):
        """
        Trigger the effect
        """
        from scripts.core.global_data import entity_manager, world_manager

        # get required info
        start_pos_x, start_pos_y = self.entity_to_move.x, self.entity_to_move.y
        target_tile_x, target_tile_y = self.target.x, self.target.y
        direction_x, direction_y = entity_manager.query.get_a_star_direction_between_entities(self.entity_to_move,
                                                                                              self.target)
        # move towards target up to move_distance
        for move in range(1, self.move_distance):
            # check target tile is valid
            in_bounds = world_manager.game_map.is_tile_in_bounds(target_tile_x, target_tile_y)
            tile_blocking_movement = world_manager.game_map.is_tile_blocking_movement(target_tile_x, target_tile_y)
            entity_blocking_movement = entity_manager.query.get_blocking_entity_at_location(target_tile_x,
                                                                                            target_tile_y)
            if in_bounds and not tile_blocking_movement and not entity_blocking_movement:
                # move the entity
                self.entity_to_move.x += direction_x
                self.entity_to_move.y += direction_y

        # update the fov if player moved
        from scripts.core.global_data import entity_manager
        if self.entity_to_move == entity_manager.player:
            from scripts.core.global_data import world_manager
            world_manager.player_fov_is_dirty = True

        # log the movement
        log_string = f"{self.entity_to_move.name} moved from [{start_pos_x},{start_pos_y}] to " \
            f"[{self.entity_to_move.x},{self.entity_to_move.y}]"
        from scripts.core.global_data import game_manager
        from scripts.events.logging_events import LoggingEvent
        from scripts.core.constants import LoggingEventTypes
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))


class DamageEffect(Effect):
    """
    Effect to damage an entity

    Args:
        amount(int):
        tags(list): list of TargetType enums
    """

    def __init__(self, damage, damage_type, target_type, tags, accuracy, stat_to_target):
        Effect.__init__(self)
        self.name = "Damage"
        self.description = "This is the damage effect"
        self.base_damage = damage
        self.damage_type = damage_type
        self.base_accuracy = accuracy
        self.stat_to_target = stat_to_target
        self.target_type = target_type
        self.target_tags = tags

    def trigger(self, attacking_entity, defending_entity):
        """
        Trigger the effect

        Args:
            attacking_entity:
            defending_entity:
        """
        attacker = attacking_entity
        defender = defending_entity
        damage = 0

        from scripts.core.global_data import game_manager
        log_string = f"Applying '{self.name}' effect from {self.owner}..."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        # store the base class type for comparison
        target_type_for_comparison = None
        if self.target_type == TargetTypes.TILE:
            target_type_for_comparison = type(Tile(0, 0))
        elif self.target_type == TargetTypes.ENTITY:
            target_type_for_comparison = type(attacker)

        # check the type is correct, then that the tags match
        if type(defender) == target_type_for_comparison:
            # if it needs to be another entity then it can't be looking at itself
            if TargetTags.OTHER_ENTITY in self.target_tags:
                if attacker != defender:
                    to_hit_score = self.calculate_to_hit_score(attacker, defender)
                    hit_type = self.get_hit_type(to_hit_score)
                    damage = self.calculate_damage(attacker, defender, hit_type)

            # apply damage
            if damage > 0:
                self.apply_damage(attacker, defender, damage)

                # check if defender died
                if defender.combatant.hp <= 0:
                    game_manager.create_event(DieEvent(defender))

                log_string = f"-> {attacker.name} deals {damage} damage to {defender.name} and they have " \
                    f"{defender.combatant.hp} health remaining."
                game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
                # TODO - add the damage type to the message and replace the type with an icon
                # TODO - add the explanation of the damage roll to a tooltip

            else:
                msg = f"{attacker.name} uses {self.owner.name} and deals no damage to {defender.name}."
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

        else:
            msg = f"You can't do that there!"
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

    def calculate_to_hit_score(self, attacker, defender):
        """
        Get the to hit score from the stats of both entities
        Args:
            attacker:
            defender:
        """
        roll = random.randint(1, 100)
        modified_to_hit_score = attacker.combatant.secondary_stats.chance_to_hit + self.base_accuracy + roll

        # get dodge score
        dodge_value = 0
        if self.stat_to_target == SecondaryStatTypes.DODGE_SPEED:
            dodge_value = defender.combatant.secondary_stats.dodge_speed
        elif self.stat_to_target == SecondaryStatTypes.DODGE_TOUGHNESS:
            dodge_value = defender.combatant.secondary_stats.dodge_toughness
        elif self.stat_to_target == SecondaryStatTypes.DODGE_INTELLIGENCE:
            dodge_value = defender.combatant.secondary_stats.dodge_intelligence

        # mitigate the to hit
        mitigated_to_hit_score = modified_to_hit_score - dodge_value

        # log the info
        from scripts.core.global_data import game_manager
        log_string = f"-> Roll:{roll}, Modified:{modified_to_hit_score}, Mitigated:{mitigated_to_hit_score}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return mitigated_to_hit_score

    @staticmethod
    def get_hit_type(to_hit_score):
        """
        Get the hit type from the to hit score
        Args:
            to_hit_score:

        Returns:
            HitTypes:
        """
        if to_hit_score >= HitTypes.CRIT_VALUE.value:
            return HitTypes.CRIT
        elif to_hit_score >= HitTypes.HIT_VALUE.value:
            return HitTypes.HIT
        else:
            return HitTypes.GRAZE

    def calculate_damage(self, attacker, defender, hit_type):
        """
        Work out the damage to be dealt
        Args:
            attacker(Entity):
            defender(Entity):
            hit_type(HitTypes):
        Returns:
            int: damage to be dealt
        """

        initial_damage = self.base_damage  # TODO - add skill dmg modifier to allow dmg growth

        # get resistance value
        resist_value = 0
        if self.damage_type == DamageTypes.PIERCE:
            resist_value = defender.combatant.secondary_stats.resist_pierce
        elif self.damage_type == DamageTypes.BLUNT:
            resist_value = defender.combatant.secondary_stats.resist_blunt
        elif self.damage_type == DamageTypes.ELEMENTAL:
            resist_value = defender.combatant.secondary_stats.resist_elemental

        # mitigate damage with defence
        mitigated_damage = initial_damage - resist_value

        # apply to hit modifier to damage
        if hit_type == HitTypes.CRIT:
            modified_damage = mitigated_damage * HitTypes.CRIT_MODIFIER.value
        elif hit_type == HitTypes.HIT:
            modified_damage = mitigated_damage * HitTypes.HIT_MODIFIER.value
        else:
            modified_damage = mitigated_damage * HitTypes.GRAZE_MODIFIER.value

        # round down the dmg
        modified_damage = int(modified_damage)

        # log the info
        from scripts.core.global_data import game_manager
        log_string = f"Initial:{initial_damage}, Mitigated:{mitigated_damage},  Modified:{modified_damage}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return modified_damage

    def apply_damage(self, attacker, defender, damage):
        """
        Apply damage to an entity

        Args:
            attacker(Entity):
            defender(Entity):
            damage(int):
        """
        defender.combatant.hp -= damage
        from scripts.core.global_data import game_manager
        msg = f"{attacker.name} uses {self.owner.name}  and deals {damage} damage to {defender.name}."
        game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))
