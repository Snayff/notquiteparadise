import logging

from scripts.core.constants import EntityEventTypes, MessageEventTypes
from scripts.events.entity_events import UseSkillEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.global_singletons.managers import world_manager, turn_manager
from scripts.events.game_events import EndTurnEvent
from scripts.event_handlers.pub_sub_hub import Subscriber, Event


class EntityHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def run(self, event):
        """
        Process entity events

        Args:
            event(Event): the event in need of processing
        """

        log_string = f"{self.name} received {event.type}..."
        logging.debug(log_string)

        if event.type == EntityEventTypes.MOVE:
            log_string = f"-> Processing '{event.entity.name}'`s move."
            logging.debug(log_string)
            self.process_move(event)

        if event.type == EntityEventTypes.SKILL:
            log_string = f"-> Processing '{event.entity.name}'`s skill: {event.skill.name}."
            logging.debug(log_string)
            self.process_skill(event)

        if event.type == EntityEventTypes.DIE:
            log_string = f"-> Processing '{event.dying_entity.name}'`s death."
            logging.debug(log_string)
            self.process_die(event)

        if event.type == EntityEventTypes.LEARN:
            log_string = f"-> Processing '{event.entity.name}'`s learning of {event.skill_name} from " \
                f"{event.skill_tree_name}."
            logging.debug(log_string)
            self.process_learn(event)

    @staticmethod
    def process_move(event):
        """
        Check if entity can move to the target tile, then either cancel the move (if blocked), bump attack (if
        target tile has entity) or move.

        Args:
            event(MoveEvent):
        """
        # get info from event
        target_x, target_y = event.target_pos
        entity = event.entity
        old_x, old_y = entity.x, entity.y

        # is there something in the way?
        in_bounds = world_manager.Map.is_tile_in_bounds(target_x, target_y)
        tile_blocking_movement = world_manager.Map.is_tile_blocking_movement(target_x, target_y)
        entity_blocking_movement = world_manager.Entity.get_blocking_entity_at_location(target_x, target_y)

        if in_bounds:

            # check for no entity in way but tile is blocked
            if not entity_blocking_movement and tile_blocking_movement:
                msg = f"There`s something in the way!"
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            # check if entity blocking tile to attack
            elif entity_blocking_movement:
                skill = entity.actor.known_skills[0]
                publisher.publish((UseSkillEvent(entity, (target_x, target_y), skill)))

            # if nothing in the way, time to move!
            elif not entity_blocking_movement and not tile_blocking_movement:

                # clean up old tile
                old_tile = world_manager.Map.get_tile(old_x, old_y)
                world_manager.Map.set_entity_on_tile(old_tile, None)

                # move entity to new tile
                new_tile = world_manager.Map.get_tile(target_x, target_y)
                world_manager.Map.set_entity_on_tile(new_tile, entity)

                # activate the tile's aspects affect
                world_manager.Map.trigger_aspects_on_tile(new_tile)

                # update fov if needed
                if entity.player:
                    world_manager.player_fov_is_dirty = True

                # end turn
                publisher.publish(EndTurnEvent(10))  # TODO - replace magic number with cost to move

    @staticmethod
    def process_skill(event):
        """
        Process the entity`s skill
        Args:
            event(EntityEvent): the event to process
        """

        skill_data = library.get_skill_data(event.skill.skill_tree_name, event.skill.name)
        world_manager.Skill.pay_resource_cost(event.entity, skill_data.resource_type, skill_data.resource_cost)
        event.skill.use(event.target_pos)

    @staticmethod
    def process_die(event):
        """
        Process the entity death
        Args:
            event(EntityEvent): the event to process
        """

        # TODO add player death
        entity = event.dying_entity

        # just in case... remove the ai
        if entity.ai:
            entity.ai = None

        # get the tile and remove the entity from it
        tile_x, tile_y = entity.x, entity.y
        tile = world_manager.Map.get_tile(tile_x, tile_y)
        world_manager.Map.set_entity_on_tile(tile, None)

        # remove from turn queue
        if entity in turn_manager.turn_queue:
            turn_manager.turn_queue.pop(entity)
        if turn_manager.turn_holder == entity:
            turn_manager.build_new_turn_queue()

    @staticmethod
    def process_learn(event):
        """
        Have an entity learn a skill.

        Args:
            event:
        """
        event.entity.actor.learn_skill(event.skill_tree_name, event.skill_name)
