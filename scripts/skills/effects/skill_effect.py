from scripts.core.constants import TargetTypes, LoggingEventTypes
from scripts.events.logging_events import LoggingEvent
from scripts.world.entity import Entity
from scripts.world.terrain.terrain import Terrain


class SkillEffect:
    """
    Base class for skill effects that make up the basis of skills.
    """

    def __init__(self, name, description, required_target_type, required_tags):
        self.owner = None
        self.name = name
        self.description = description
        self.required_target_type = required_target_type
        self.required_tags = required_tags

    def trigger(self):
        """
        Trigger the effect
        """
        from scripts.core.global_data import game_manager
        log_string = f"Applying '{self.name}' effect from {self.owner.name}..."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

    @staticmethod
    def get_target_type(target):
        """
        Get the type of the required target

        Args:
            target: the target; terrain or entity

        Returns:
            TargetTypes:
        """

        # TODO - remove and point to owner's version

        if isinstance(target, Terrain):
            target_type = TargetTypes.TERRAIN
        elif isinstance(target, Entity):
            target_type = TargetTypes.ENTITY

        return target_type
