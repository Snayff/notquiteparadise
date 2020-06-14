from __future__ import annotations

from typing import TYPE_CHECKING, cast
from scripts.engine import world
from scripts.engine.event import EndRoundEvent
from scripts.engine.core.event_core import Subscriber
from scripts.engine.component import Knowledge

if TYPE_CHECKING:
    pass


class EntityHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        super().__init__("entity_handler", event_hub)

    def process_event(self, event):
        """
        Control entity events
        """
        if isinstance(event, EndRoundEvent):
            self._process_end_round(event)


    @staticmethod
    def _process_end_round(event: EndRoundEvent):
        """
        Reduce cooldowns and durations
        """
        # skill cooldowns
        for entity, (knowledge, ) in world.get_components([Knowledge]):
            knowledge = cast(Knowledge, knowledge)
            for skill_name, skill_dict in knowledge.skills.items():
                if skill_dict["cooldown"] > 0:
                    knowledge.skills[skill_name]["cooldown"] = skill_dict["cooldown"] - 1

        # # affliction durations
        # for entity, (afflictions, ) in existence.get_components([Afflictions]):
        #     for affliction, duration in afflictions.items():
        #         if duration - 1 <= 0:
        #             # expired
        #             # TODO - create expiry event.
        #             del afflictions[affliction]
        #
        #         elif duration != INFINITE:
        #             # reduce duration if not infinite
        #             afflictions[affliction] = duration - 1

