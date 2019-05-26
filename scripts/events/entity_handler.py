from scripts.core.constants import EntityEventTypes, LoggingEventTypes, GameStates
from scripts.global_instances.event_hub import publisher
from scripts.global_instances.managers import world_manager, turn_manager
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
            log_string = f"-> Processing {event.entity.name}'s move."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_move(event)

        if event.type == EntityEventTypes.SKILL:
            log_string = f"-> Processing {event.entity.name}'s skill: {event.skill_name}."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_skill(event)

        if event.type == EntityEventTypes.DIE:
            log_string = f"-> Processing {event.dying_entity.name}'s death."
            publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))
            self.process_die(event)

        if event.type == EntityEventTypes.LEARN:
            log_string = f"-> Processing {event.entity.name}'s learning of {event.skill_name} from " \
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

        # update fov if needed
        if entity.player:
            world_manager.player_fov_is_dirty = True

        # end turn
        publisher.publish(EndTurnEvent(10))  # TODO - replace magic number with cost to move

    @staticmethod
    def process_skill(event):
        """
        Process the entity's skill
        Args:
            event(EntityEvent): the event to process
        """

        skill = event.entity.actor.get_skill_from_known_skills(event.skill_name)
        target_x, target_y = event.target_pos

        if skill:
            # if no target go to target mode
            if target_x == 0 and target_y == 0:
                log_string = f"Skill event has no target. Go to targeting mode."
                publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

                publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
                return  # prevent further execution

            # get info about the tile and the skill requirements
            tile = world_manager.game_map.get_tile(target_x, target_y)
            is_required_type = skill.is_required_target_type(tile)
            has_tags = skill.has_required_tags(tile)

            # check we have everything we need and if so use the skill
            if is_required_type and has_tags:
                if skill.user_can_afford_cost():
                    skill.pay_the_resource_cost()
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
