from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import MapEventTypes, MessageTypes, GameEventTypes
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.managers.world_manager import world

if TYPE_CHECKING:
    from scripts.events.game_events import EndTurnEvent, EndRoundEvent
    from scripts.events.map_events import TileInteractionEvent
    from scripts.events.ui_events import MessageEvent


class MapHandler(Subscriber):
    """
    Handle map related events
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "map_handler", event_hub)

    def process_event(self, event):
        """
        Control world events

        Args:
            event(Event): the event in need of processing
        """

        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}...")

        if event.event_type == MapEventTypes.TILE_INTERACTION:
            event: TileInteractionEvent
            self.process_tile_interaction(event)

        elif event.event_type == GameEventTypes.END_TURN:
            event: EndTurnEvent
            self.process_end_of_turn_updates(event)

        elif event.event_type == GameEventTypes.END_ROUND:
            event: EndRoundEvent
            self.process_end_of_round_updates()

    @staticmethod
    def process_tile_interaction(event: TileInteractionEvent):
        """
        Check the cause on the aspects of a tile and trigger any interactions.

        Args:
            event(TileInteractionEvent):
        """

        # check all tiles
        for tile in event.tiles:

            # only aspects have interactions...
            if tile.aspects:

                for key, aspect in tile.aspects.items():
                    aspect_data = library.get_aspect_data(aspect.name)

                    # check cause is a valid trigger for an interaction
                    for interaction in aspect_data.interactions:
                        if event.cause == interaction.cause:
                            # change aspects
                            world.Map.remove_aspect_from_tile(tile, aspect.name)
                            world.Map.add_aspect_to_tile(tile, interaction.change_to)

                            # log the change
                            log_string = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}"
                            logging.info(log_string)

                            # inform player of change
                            msg = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}."
                            publisher.publish(MessageEvent(MessageTypes.LOG, msg))

    @staticmethod
    def process_end_of_turn_updates(event: EndTurnEvent):
        """
        Trigger aspects on tile turn holder is on

        Args:
            event(EndTurnEvent):
        """
        entity = event.entity
        tile = world.Map.get_tile((entity.x, entity.y))

        # trigger aspects
        world.Map.trigger_aspects_on_tile(tile)

    @staticmethod
    def process_end_of_round_updates():
        """
        Update aspect durations
        """
        game_map = world.Map.get_game_map()

        # TODO - set to only apply within X range of player
        for row in game_map.tiles:
            for tile in row:
                if tile.aspects:

                    # update durations
                    world.Map.reduce_aspect_durations_on_tile(tile)
                    world.Map.cleanse_expired_aspects(tile)
