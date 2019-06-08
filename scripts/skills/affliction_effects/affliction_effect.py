
from scripts.core.constants import LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher
from scripts.skills.affliction import Affliction


class AfflictionEffect:
    """
    Base class for affliction_effects that make up the basis of afflictions. They are effectively a simplified
    version of skill_effects
    """

    def __init__(self, owner, name, description):
        self.owner = owner  # type: Affliction
        self.name = name
        self.description = description

    def trigger(self):
        """
        Trigger the effect
        """
        log_string = f"Applying '{self.name}' affliction effect from {self.owner.name}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))