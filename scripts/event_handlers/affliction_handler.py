
import logging

from scripts.core.constants import GameEventTypes, AfflictionTriggers, EntityEventTypes
from scripts.event_handlers.pub_sub_hub import Subscriber, Event
from scripts.events.entity_events import MoveEvent, UseSkillEvent
from scripts.events.game_events import EndTurnEvent
from scripts.managers.world_manager import world
from scripts.world.entity import Entity


class AfflictionHandler(Subscriber):
    """
    Handle afflictions related events
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "affliction_handler", event_hub)

    def process_event(self, event):
        """
        Control events related to afflictions

        Args:
            event(Event): the event in need of processing
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}.")

        if event.event_type == GameEventTypes.END_TURN:
            # trigger end of turn afflictions
            event: EndTurnEvent
            self.process_affliction_trigger(event.entity, AfflictionTriggers.END_TURN)
            self.process_end_of_turn_updates(event)


        elif event.event_type == EntityEventTypes.MOVE:
            event: MoveEvent
            self.process_affliction_trigger(event.entity, AfflictionTriggers.MOVE)
            self.process_affliction_trigger(event.entity, AfflictionTriggers.ACTION)

        elif event.event_type == EntityEventTypes.SKILL:
            event: UseSkillEvent
            self.process_affliction_trigger(event.entity, AfflictionTriggers.ACTION)

    @staticmethod
    def process_affliction_trigger(entity: Entity, trigger: AfflictionTriggers):
        """
        Control the required affliction trigger

        Args:
            entity (Entity):
            trigger (AfflictionTriggers):
        """
        world.Affliction.trigger_afflictions_on_entity(trigger, entity)

    @staticmethod
    def process_end_of_turn_updates(event: EndTurnEvent):
        """
        Reduce durations, cleanse expired.

        Args:
            event ():
        """
        # reduce duration and cleanse expired
        world.Affliction.reduce_affliction_durations_on_entity(event.entity)
        world.Affliction.cleanse_expired_afflictions()