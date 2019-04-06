from scripts.core.constants import MessageEventTypes, LoggingEventTypes
from scripts.events.entity_events import DieEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent


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
            entity_blocking_movement = entity_manager.query.get_blocking_entities_at_location(target_tile_x,
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
    """
    def __init__(self, attacking_entity, defending_entities):
        Effect.__init__(self)
        self.description = "This is the damage effect"
        self.attacking_entity = attacking_entity
        self.defending_entities = defending_entities

    def trigger(self):
        """
        Trigger the effect
        """
        from scripts.core.global_data import game_manager
        attacker = self.attacking_entity

        for defender in self.defending_entities:
            damage = self.calculate_damage(defender)

            # apply damage
            if damage > 0:
                defender.combatant.hp -= damage
                msg = f"{attacker.name} deals {damage} damage to {defender.name}."

                # check if defender died
                if defender.combatant.hp <= 0:
                    game_manager.create_event(DieEvent(defender))
                    msg = f"{attacker.name} deals {damage} damage and kills {defender.name}."

            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg))

            log_string = f"{attacker.name} deals {damage} damage to {defender.name} and they have " \
                f"{defender.combatant.hp} health remaining."
            game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

    def calculate_damage(self, defender):
        """
        Work out the damage to be dealt
        Args:
            defender(Entity): the entity getting attacked

        Returns:
            int: damage to be dealt
        """
        damage = max(self.attacking_entity.combatant.power - defender.combatant.defence, 0)
        return damage