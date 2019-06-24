
from scripts.events.pub_sub_hub import EventHub, Publisher

event_hub = EventHub()
publisher = Publisher(event_hub)