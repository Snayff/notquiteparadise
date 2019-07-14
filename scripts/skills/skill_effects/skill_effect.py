from scripts.core.constants import LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.event_hub import publisher


class SkillEffect:
    """
    Base class for skill skill_effects that make up the basis of skills.
    """

    def __init__(self, owner, name, description, skill_effect_type):
        self.owner = owner
        self.name = name
        self.description = description
        self.skill_effect_type = skill_effect_type

    def trigger(self):
        """
        Trigger the effect
        """
        log_string = f"Applying {self.name} skill effect from {self.owner.name}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))


