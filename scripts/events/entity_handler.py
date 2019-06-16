from scripts.core.constants import EntityEventTypes, LoggingEventTypes, GameStates
from scripts.global_instances.event_hub import publisher
from scripts.global_instances.managers import world_manager, turn_manager, game_manager
from scripts.events.game_events import EndTurnEvent, ChangeGameStateEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber, Event


class EntityHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def run(self, event):
        """
        Process entity events

        Args:
            event(Event): the event in need of processing
        """

        log_string = f"{self.name} received {event.type}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

        if event.type == EntityEventTypes.MOVE:
            log_string = f"-> Processing '{event.entity.name}'`s move."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_move(event)

        if event.type == EntityEventTypes.SKILL:
            log_string = f"-> Processing '{event.entity.name}'`s skill: {event.skill.name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_skill(event)

        if event.type == EntityEventTypes.DIE:
            log_string = f"-> Processing '{event.dying_entity.name}'`s death."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_die(event)

        if event.type == EntityEventTypes.LEARN:
            log_string = f"-> Processing '{event.entity.name}'`s learning of {event.skill_name} from " \
                f"{event.skill_tree_name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_learn(event)

    @staticmethod
    def process_move(event):
        """
        Process the move event

        Args:
            event:
        """
        # get info from event
        target_x, target_y = event.target_pos
        entity = event.entity
        old_x, old_y = entity.x, entity.y

        # clean up old tile
        old_tile = world_manager.game_map.get_tile(old_x, old_y)
        old_tile.remove_entity()

        # move entity to new tile
        new_tile = world_manager.game_map.get_tile(target_x, target_y)
        new_tile.set_entity(entity)

        # activate the tile's aspect affect
        new_tile.trigger_aspect_effect()

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

        skill = event.skill
        world_manager.entity_action.pay_resource_cost(event.entity, event.skill.resource_type,
                                                      event.skill.resource_cost)
        skill.use(event.target_pos)

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
        tile = world_manager.game_map.get_tile(tile_x, tile_y)
        tile.remove_entity()

        # remove from turn queue
        del turn_manager.turn_queue[entity]
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
