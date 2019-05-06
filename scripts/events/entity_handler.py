from scripts.core.constants import EntityEventTypes, LoggingEventTypes, TargetTags, GameStates
from scripts.core.global_data import world_manager, game_manager, turn_manager
from scripts.events.game_events import EndTurnEvent, ChangeGameStateEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber, Event


class EntityHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def run(self, event):
        """

        Args:
            event(Event):
        """

        log_string = f"{self.name} received {event.type}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))

        if event.type == EntityEventTypes.MOVE:
            self.process_move(event)

        if event.type == EntityEventTypes.SKILL:
            self.process_skill(event)

        if event.type == EntityEventTypes.DIE:
            self.process_die(event)

        if event.type == EntityEventTypes.LEARN:
            self.process_learn(event)

    @staticmethod
    def process_move(event):
        """
        Process the move event

        Args:
            event:
        """
        log_string = f"-> Processing {event.entity.name}'s move."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

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
        game_manager.create_event(EndTurnEvent(10))  # TODO - replace magic number with cost to move

    @staticmethod
    def process_skill(event):
        """
        Process the entity's skill
        Args:
            event(EntityEvent): the event to process
        """
        log_string = f"-> Processing {event.entity.name}'s skill: {event.skill_name}."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

        skill = event.entity.actor.get_skill_from_known_skills(event.skill_name)
        target_x, target_y = event.target_pos

        if skill:
            # if no target go to target mode
            if target_x == 0 and target_y == 0:
                game_manager.create_event(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
                return  # prevent further execution

            # confirm target type and resource cost
            tile_target_type = world_manager.game_map.get_target_type_from_tile(target_x, target_y)
            entity_at_tile = world_manager.entity_query.get_blocking_entity_at_location(target_x, target_y)
            if entity_at_tile != event.entity:
                entity_target_type = TargetTags.OTHER_ENTITY
            else:
                entity_target_type = TargetTags.SELF

            if skill.is_valid_target_type(tile_target_type, entity_target_type) and skill.user_can_afford_cost():
                skill.pay_the_resource_cost()
                skill.use(event.target_pos)

    @staticmethod
    def process_die(event):
        """
        Process the entity death
        Args:
            event(EntityEvent): the event to process
        """
        log_string = f"-> Processing {event.dying_entity.name}'s death."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

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
