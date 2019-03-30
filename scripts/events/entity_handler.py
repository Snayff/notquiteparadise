from scripts.core.constants import EntityEventTypes, LoggingEventTypes
from scripts.core.global_data import world_manager, entity_manager, game_manager, turn_manager
from scripts.events.game_events import EndTurnEvent
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber


class EntityHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def run(self, event):
        log_string = f"{self.name} received {event.type}"
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))

        if event.type == EntityEventTypes.GET_MOVE_TARGET:
            entity = event.moving_entity
            target = event.target_entity
            log_string = f"{entity.name} ({entity}) looked for a path to {target.name} [{target.x},{target.y}] with a*"
            game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))

            # get destination to move to and then move
            dx, dy = entity_manager.query.get_direction_between_entities(entity, target)
            target_tile = (dx, dy)
            #  game_manager.create_event(MoveEvent(entity, target_tile))

        if event.type == EntityEventTypes.SKILL:
            skill = event.entity.actor.known_skills[event.skill_name]

            if skill:
                if skill.targeting_required:
                    pass
                    # TODO - trigger targeting system and get new target
                else:
                    target_x = event.target[0] + event.entity.x
                    target_y = event.target[1] + event.entity.y

                target_type = world_manager.game_map.get_target_type(target_x, target_y)
                if skill.is_valid_target(event.target, target_type) and skill.user_can_afford_cost():
                    skill.pay_the_resource_cost()
                    skill.use(event.target)

    def process_die(self, event):
        # TODO add player death
        entity = event.dying_entity
        entity.ai = None

        entity_manager.entities.remove(entity)
        del turn_manager.turn_queue[entity]
        if turn_manager.turn_holder == entity:
            turn_manager.build_new_turn_queue()
