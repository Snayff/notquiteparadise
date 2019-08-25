
import logging

from scripts.core.constants import GameEventTypes, AfflictionTriggers
from scripts.event_handlers.pub_sub_hub import Subscriber, Event
from scripts.world.entity import Entity


class AfflictionHandler(Subscriber):
    """
    Handle afflictions related events
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "affliction_handler", event_hub)

    def run(self, event):
        """
        Process events related to afflictions

        Args:
            event(Event): the event in need of processing
        """
        log_string = f"{self.name} received {event.type}..."
        logging.info(log_string)

        if event.type == GameEventTypes.END_TURN:
            # trigger end of turn afflictions
            from scripts.global_singletons.managers import turn_manager
            self.process_affliction_trigger(turn_manager.turn_holder, AfflictionTriggers.END_TURN)

            # reduce duration and cleanse expired
            from scripts.global_singletons.managers import world_manager
            world_manager.Affliction.reduce_affliction_durations_on_entity(turn_manager.turn_holder)
            world_manager.Affliction.cleanse_expired_afflictions()



    def process_affliction_trigger(self, entity, trigger):
        """
        Process the required affliction trigger

        Args:
            entity (Entity):
            trigger (AfflictionTriggers):
        """
        from scripts.global_singletons.managers import world_manager
        world_manager.Affliction.trigger_afflictions_on_entity(trigger, entity)
