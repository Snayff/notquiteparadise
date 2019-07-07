
from scripts.event_handlers.pub_sub_hub import EventHub, Publisher

event_hub = EventHub()
publisher = Publisher(event_hub)