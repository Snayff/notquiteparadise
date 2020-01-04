from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import MessageEventTypes

from scripts.managers.ui_manager import ui
from scripts.event_handlers.pub_sub_hub import Subscriber

if TYPE_CHECKING:
    from scripts.events.message_events import MessageEvent


class MessageHandler(Subscriber):
    """
    Handle messaging to player
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "message_handler", event_hub)

    def process_event(self, event):
        """
        Process message events

        Args:
            event ():
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.event_type == MessageEventTypes.BASIC:
            event: MessageEvent
            self.process_basic(event)

    @staticmethod
    def process_basic(event: MessageEvent):
        """
        Process basic message

        Args:
            event ():
        """
        ui.Element.add_to_message_log(event.message)
