
import logging

from scripts.core.constants import MapEventTypes, MessageEventTypes
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.events.map_events import TileInteractionEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher


class MapHandler(Subscriber):
    def __init__(self, event_hub):
        Subscriber.__init__(self, "map_handler", event_hub)

    def run(self, event):
        """
        Process world events

        Args:
            event(Event): the event in need of processing
        """

        log_string = f"{self.name} received {event.type}..."
        logging.debug(log_string)

        if event.type == MapEventTypes.TILE_INTERACTION:
            log_string = f"-> Processing {event.cause} interaction on tiles"
            logging.debug(log_string)
            self.process_tile_interaction(event)

    @staticmethod
    def process_tile_interaction(event):
        """
        Check the cause on the aspect of a tile and trigger any interactions.

        Args:
            event(TileInteractionEvent):
        """

        # check all tiles
        for tile in event.tiles:

            # only aspects have interactions...
            if tile.aspect:
                aspect_data = library.get_aspect_data(tile.aspect.name)

                # check cause is a valid trigger for an interaction
                for interaction in aspect_data.interactions:
                    if event.cause == interaction.cause:
                        # change aspect
                        from scripts.global_singletons.managers import world_manager
                        world_manager.Map.set_aspect_on_tile(tile, interaction.change_to)

                        # log the change
                        log_string = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}"
                        logging.info( log_string)

                        # inform player of change
                        from scripts.events.message_events import MessageEvent
                        msg = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
