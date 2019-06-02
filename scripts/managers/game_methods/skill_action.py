from scripts.core.constants import GameStates
from scripts.events.game_events import ChangeGameStateEvent
from scripts.global_instances.event_hub import publisher


class SkillAction:
    def __init__(self, manager):
        self.manager = manager

    @staticmethod
    def activate_targeting_mode(skill):
        # TODO - should this be in UI manager?
        """
        Change game state to Targeting mode
        Args:
            skill ():
        """

        publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
