import numpy

from scripts.core.constants import LoggingEventTypes, MessageEventTypes
from scripts.core.global_data import entity_manager, game_manager, world_manager
from scripts.events.entity_events import UseSkillEvent
from scripts.events.game_events import EndTurnEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent


class BasicMonster:
    # TODO create initial AI class, and then derive diff types from that
    def take_turn(self):
        """
        Take turn for BasicMonster AI
        """
        entity = self.owner
        target = self.get_target()
        direction_x, direction_y = self.get_target_direction(target)
        distance_to_target = entity_manager.query.get_distance_between_entities(entity, target)
        target_tile_x, target_tile_y = entity.x + direction_x, entity.y + direction_y

        # try to attack first
        for skill_key, skill_value in entity.actor.known_skills.items():
            # TODO - loop skills in priority order
            # ignore the move skill
            if skill_value.name == "move":
                break

            # are we in range to attack?
            attack_range = skill_value.range

            if distance_to_target <= attack_range:
                # can we attack?
                game_manager.create_event(UseSkillEvent(entity, target, skill_value.name))
                return None  # stop further processing in function

        # we can't attack so try to move closer
        # check target tile is valid
        if world_manager.game_map.is_tile_in_bounds(target_tile_x, target_tile_y):
            if direction_x != 0 or direction_y != [0]:
                # limit to only moving one tile then move
                target_tile = int(numpy.sign(direction_x)), int(numpy.sign(direction_y))
                game_manager.create_event(UseSkillEvent(entity, target_tile, "move"))
            else:
                # TODO - if they can't move where they want move in a random direction before passing.
                msg_string = f"{entity.name} passed their turn."
                game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg_string))
                game_manager.create_event(EndTurnEvent(10))  # TODO -replace with pass turn skill
        else:
            msg_string = f"{entity.name} passed their turn."
            game_manager.create_event(MessageEvent(MessageEventTypes.BASIC, msg_string))
            game_manager.create_event(EndTurnEvent(10))  # TODO -replace with pass turn skill

    def get_target(self):
        """
        Get the target to pursue and attack
        Returns:
            Entity: the entity to pursue

        """
        target = entity_manager.player

        log_string = f"{self.owner.name} choose {target.name} as a target."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))
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
        direction = entity_manager.query.get_a_star_direction_between_entities(entity, target)

        # if direction == 0 then we aren't intending to move, did something fail?
        if direction[0] == 0 and direction[1] == 0:
            direction = entity_manager.query.get_direct_direction_between_entities(entity, target)

        return direction
