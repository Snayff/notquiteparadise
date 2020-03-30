# TODO - clean up module
import logging
from abc import ABC
from scripts.engine.core.constants import DEBUG_LOG_EVENT_RECEIPTS


class EventHub:
    """
    Event hub to handle the interactions between events and subscribers
    """
    def __init__(self):
        self.events = []
        self.subscribers = {}

    def notify(self, event):
        self.events.append(event)

    def subscribe(self, event, subscriber):
        self.subscribers.setdefault(event, []).append(subscriber)

    def unsubscribe(self, event, subscriber):
        self.subscribers[event].remove(subscriber)

    def update(self):

        # loop every event and notify every subscriber
        while self.events:
            event = self.events.pop(0)

            for sub in self.subscribers.get(event.topic, []):
                sub.process_event(event)


class Publisher:
    """
    Class to create_entity events and log them with the event hub
    """
    def __init__(self, event_hub):
        self.event_hub = event_hub

    def publish(self, event):
        self.event_hub.notify(event)


class Subscriber:
    """
    Class to set default behaviour for handlers listening for events
    """
    def __init__(self, name, event_hub):
        self.name = name
        self.event_hub = event_hub

    def subscribe(self, event):
        self.event_hub.subscribe(event, self)

    def unsubscribe(self, event):
        self.event_hub.unsubscribe(event, self)

    def process_event(self, event):
        """
        Process game events.
        """
        if DEBUG_LOG_EVENT_RECEIPTS:
            # log that event has been received
            logging.debug(f"{self.name} received {event.__class__.__name__}.")


class Event(ABC):
    """
    Events to cause top level actions to take place
    """
    def __init__(self, name, topic):
        """
        Base class for events
        """
        self.name = name
        self.topic = topic


event_hub = EventHub()
publisher = Publisher(event_hub)