
from scripts.core.constants import LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.global_singletons.event_hub import publisher


class AfflictionEffect:
    """
    Base class for affliction_effects that make up the basis of afflictions. They are effectively a simplified
    version of skill_effects
    """

    def __init__(self, owner, name, description):
        from scripts.skills.affliction import Affliction
        self.owner = owner  # type: Affliction
        self.name = name
        self.description = description
        from scripts.global_singletons.managers import world_manager
        self.effect_type = world_manager.Affliction.get_affliction_effect_type_from_string(name)

    def trigger(self):
        """
        Trigger the effect
        """
        log_string = f"Applying {self.name} affliction effect from {self.owner.name}..."
        publisher.publish(LoggingEvent(LoggingEventTypes.DEBUG, log_string))