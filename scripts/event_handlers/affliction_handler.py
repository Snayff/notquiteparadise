
import logging

from scripts.core.constants import GameEventTypes, AfflictionTriggers, EntityEventTypes
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
        logging.debug(log_string)

        if event.type == GameEventTypes.END_TURN:
            # trigger end of turn afflictions
            self.process_affliction_trigger(event.entity, AfflictionTriggers.END_TURN)

            # reduce duration and cleanse expired
            from scripts.global_singletons.managers import world_manager
            world_manager.Affliction.reduce_affliction_durations_on_entity(event.entity)
            world_manager.Affliction.cleanse_expired_afflictions()

        elif event.type == EntityEventTypes.MOVE:
            self.process_affliction_trigger(event.entity, AfflictionTriggers.MOVE)
            self.process_affliction_trigger(event.entity, AfflictionTriggers.ACTION)

        elif event.type == EntityEventTypes.SKILL:
            self.process_affliction_trigger(event.entity, AfflictionTriggers.ACTION)

    @staticmethod
    def process_affliction_trigger(entity, trigger):
        """
        Process the required affliction trigger

        Args:
            entity (Entity):
            trigger (AfflictionTriggers):
        """
        from scripts.global_singletons.managers import world_manager
        world_manager.Affliction.trigger_afflictions_on_entity(trigger, entity)
