import logging

from scripts.core.event_hub import publisher
from scripts.world.entity import Entity
from scripts.managers.world_manager import world
from scripts.events.game_events import EndTurnEvent


class BasicMonster:
    # TODO create initial AI class, and then derive diff types from that
    def take_turn(self):
        """
        Take turn for BasicMonster AI
        """
        entity = self.owner
        # target = self.get_target()
        # direction_x, direction_y = self.get_target_direction(target)
        # distance_to_target = world.Entity.get_chebyshev_distance_between_tiles(entity, target)
        # target_tile_x, target_tile_y = entity.x + direction_x, entity.y + direction_y

        log_string = f"'{entity.name}' is starting to take their turn..."
        logging.info(log_string)

        # !!!! TESTING ONLY!!!!!!!
        publisher.publish(EndTurnEvent(entity, 10))  # TODO -remove when  ai needs to act
        logging.info(f"-> Passed their turn.")
        return

        # FIXME - change to using the new list format
        # for skill_key, skill_value in entity.actor.known_skills.items():
        #     # TODO - loop skills in priority order
        #
        #     # are we in range to attack?
        #     attack_range = skill_value.range
        #
        #     if distance_to_target <= attack_range:
        #         log_string = f"-> '{entity.name}' decided to use {skill_value.name}."
        #         logging.debug(log_string)
        #
        #         publisher.publish(UseSkillEvent(entity, (target_tile_x, target_tile_y), skill_value))
        #         return None  # stop further processing in function
        #
        # log_string = f"-> '{entity.name}' found no possible attack."
        # logging.debug(log_string)
        #
        # # we can't attack so try to move closer
        # # check target tile is valid
        # in_bounds = world.Map.is_tile_in_bounds(target_tile_x, target_tile_y)
        # tile_blocking_movement = is_tile_blocking_movement(target_tile_x, target_tile_y)
        # entity_blocking_movement = world.Entity.get_blocking_entity(target_tile_x, target_tile_y)
        # if in_bounds and not tile_blocking_movement and not entity_blocking_movement:
        #     if direction_x != 0 or direction_y != 0:
        #         # limit to only moving one tile then move
        #         target_x, target_y = int(numpy.sign(direction_x)) + entity.x, int(numpy.sign(direction_y)) + entity.y
        #         publisher.publish(MoveEvent(entity, (target_x, target_y)))
        #     else:
        #         # TODO - if they can't move where they want move in a random direction before deciding to pass.
        #         msg_string = f"{entity.name} passed their turn."
        #         publisher.publish(MessageEvent(MessageTypes.LOG, msg_string))
        #         publisher.publish(EndTurnEvent(10))  # TODO -replace with pass turn skill
        # else:
        #     msg_string = f"{entity.name} passed their turn."
        #     publisher.publish(MessageEvent(MessageTypes.LOG, msg_string))
        #     publisher.publish(EndTurnEvent(10))  # TODO -replace with pass turn skill

    def get_target(self):
        """
        Get the target to pursue and attack
        Returns:
            Entity: the entity to pursue

        """
        # TODO - actually get a target
        target = world.player

        log_string = f"{self.owner.name} chose '{target.name}' as a target."
        logging.info(log_string)
        return target

    def get_target_direction(self, target):
        """
        Get the target direction
        Args:
            target(Entity): the entity to target

        Returns:
            tuple: x,y to aim towards
        """
        entity = self.owner
        direction = world.Entity.get_a_star_direction_between_entities(entity, target)

        # if direction == 0 then we aren't intending to move, did something fail?
        if direction[0] == 0 and direction[1] == 0:
            direction = world.Entity.get_direction_between_entities(entity, target)

        return direction
