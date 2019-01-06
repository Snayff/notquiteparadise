from scripts.core.constants import EventTopics


class EventHub:
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
                sub.run(event)


class Publisher:
    def __init__(self, event_hub):
        self.event_hub = event_hub

    def publish(self, event):
        self.event_hub.notify(event)


class Subscriber:
    def __init__(self, name, event_hub):
        self.name = name
        self.event_hub = event_hub

    def subscribe(self, event):
        self.event_hub.subscribe(event, self)

    def unsubscribe(self, event):
        self.event_hub.unsubscribe(event, self)

# def run(self, event):
# 	log_msg = f"{self.name} received {event.name}"
# 	game_manager.create_event(Event(LoggingEventNames.MUNDANE, EventTopics.LOGGING,  [log_msg]))


class Event:
    def __init__(self, name, topic, values):
        """
        :type name:
        :type topic: EventTopics
        :type values: list
        """
        self.name = name
        self.topic = topic
        self.values = values
