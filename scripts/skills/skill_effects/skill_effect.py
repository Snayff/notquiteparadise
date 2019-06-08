from scripts.core.constants import LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_instances.event_hub import publisher


class SkillEffect:
    """
    Base class for skill skill_effects that make up the basis of skills.
    """

    def __init__(self, owner, name, description, required_target_type, required_tags):
        self.owner = owner
        self.name = name
        self.description = description
        self.required_target_type = required_target_type
        self.required_tags = required_tags

    def trigger(self):
        """
        Trigger the effect
        """
        log_string = f"Applying '{self.name}' skill effect from {self.owner.name}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))


