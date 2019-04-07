from scripts.core.constants import MessageEventTypes, LoggingEventTypes, TargetTypes, TargetTags
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
    def __init__(self, amount, target_type, tags):
        Effect.__init__(self)
        self.name = "Damage"
        self.description = "This is the damage effect"
        self.damage_amount = amount
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
        log_string = f"Applying effect '{self.name}'..."
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
                    damage = self.calculate_damage(attacker, defender)

        # apply damage
        if damage > 0:
            self.apply_damage(attacker, defender, damage)

            # check if defender died
            if defender.combatant.hp <= 0:
                game_manager.create_event(DieEvent(defender))

            log_string = f"->{attacker.name} deals {damage} damage to {defender.name} and they have " \
                f"{defender.combatant.hp} health remaining."
            game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

    @staticmethod
    def calculate_damage(attacker,  defender):
        """
        Work out the damage to be dealt
        Args:
            attacker(Entity):
            defender(Entity):

        Returns:
            int: damage to be dealt
        """
        damage = max(attacker.combatant.power - defender.combatant.defence, 0)

        from scripts.core.global_data import game_manager
        log_string = f"->Power({attacker.combatant.power}) - Defence({defender.combatant.defence}) = {damage}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        return damage

    @staticmethod
    def apply_damage(attacker, defender, damage):
        """
        Apply damage to an entity

        Args:
            attacker(Entity):
            defender(Entity):
            damage(int):
        """
        defender.combatant.hp -= damage
        from scripts.core.global_data import game_manager
        msg = f"{attacker.name} deals {damage} damage to {defender.name}."
        game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))