from __future__ import annotations

import logging  # type: ignore
from typing import TYPE_CHECKING

from scripts.engine import world, entity
from scripts.engine.core.event_core import Subscriber

from scripts.engine.component import Position
from scripts.engine.event import EndTurnEvent, EndRoundEvent, TileInteractionEvent

if TYPE_CHECKING:
    pass


class MapHandler(Subscriber):
    """
    Handle map related events
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "map_handler", event_hub)

    def process_event(self, event):
        """
        Control world_objects events

        Args:
            event(Event): the event in need of processing
        """

        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.__class__.__name__}...")

        if isinstance(event, TileInteractionEvent):
            event: TileInteractionEvent
            self.process_tile_interaction(event)

        elif isinstance(event, EndTurnEvent):
            event: EndTurnEvent
            self.process_end_of_turn_updates(event)

        elif isinstance(event, EndRoundEvent):
            event: EndRoundEvent
            self.process_end_of_round_updates()

    @staticmethod
    def process_tile_interaction(event: TileInteractionEvent):
        """
        Check the cause on the aspects of a tile and trigger any interactions.

        Args:
            event(TileInteractionEvent):
        """
        pass

        # # check all tiles
        # for tile in event.tiles:
        #     # TODO - rebuild to work for EC
        #     # only aspects have interactions...
        #     if tile.aspects:
        #
        #         for key, aspect in tile.aspects.items():
        #             aspect_data = library.get_aspect_data(aspect.name)
        #
        #             # check cause is a valid trigger for an interaction
        #             for interaction in aspect_data.interactions:
        #                 if event.cause == interaction.cause:
        #                     # change aspects
        #                     world.remove_aspect_from_tile(tile, aspect.name)
        #                     world.add_aspect_to_tile(tile, interaction.change_to)
        #
        #                     # log the change
        #                     log_string = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}"
        #                     logging.info(log_string)
        #
        #                     # inform player of change
        #                     msg = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}."
        #                     publisher.publish(MessageEvent(MessageType.LOG, msg))

    @staticmethod
    def process_end_of_turn_updates(event: EndTurnEvent):
        """
        Trigger aspects on tile turn holder is on

        Args:
            event(EndTurnEvent):
        """
        ent = event.entity
        position = entity.get_entitys_component(ent, Position)
        tile = world.get_tile((position.x, position.y))

        # trigger aspects
        #  TODO - update to EC approach
        #world.trigger_aspects_on_tile(tile)

    @staticmethod
    def process_end_of_round_updates():
        """
        Update aspect durations
        """
        game_map = world.get_game_map()

        # TODO - set to only apply within X range of player
        #  TODO - update to EC approach
        # for row in game_map.tiles:
        #     for tile in row:
        #         if tile.aspects:
        #             # update durations
        #             world.reduce_aspect_durations_on_tile(tile)
        #             world.cleanse_expired_aspects(tile)
