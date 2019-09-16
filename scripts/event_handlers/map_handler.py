
import logging

from scripts.core.constants import MapEventTypes, MessageEventTypes, GameEventTypes
from scripts.event_handlers.pub_sub_hub import Subscriber
from scripts.events.game_events import EndTurnEvent
from scripts.events.map_events import TileInteractionEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher


class MapHandler(Subscriber):
    """
    Handle map related events
    """
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
            log_string = f"-> Processing {event.cause} interaction on tiles."
            logging.debug(log_string)
            self.process_tile_interaction(event)
        elif event.type == GameEventTypes.END_TURN:
            log_string = f"-> Processing end of turn map updates."
            logging.debug(log_string)
            self.process_end_of_turn_updates(event)
        elif event.type == GameEventTypes.END_ROUND:
            log_string = f"-> Processing end of round map updates."
            logging.debug(log_string)
            self.process_end_of_round_updates()

    @staticmethod
    def process_tile_interaction(event):
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
                            from scripts.global_singletons.managers import world_manager
                            world_manager.Map.remove_aspect_from_tile(tile, aspect.name)
                            world_manager.Map.add_aspect_to_tile(tile, interaction.change_to)

                            # log the change
                            log_string = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}"
                            logging.info(log_string)

                            # inform player of change
                            from scripts.events.message_events import MessageEvent
                            msg = f"{interaction.cause} changed {aspect_data.name} to {interaction.change_to}."
                            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

    @staticmethod
    def process_end_of_turn_updates(event):
        """
        Trigger aspects on tile turn holder is on

        Args:
            event(EndTurnEvent):
        """
        entity = event.entity
        from scripts.global_singletons.managers import world_manager
        tile = world_manager.Map.get_tile(entity.x, entity.y)

        # trigger aspects
        world_manager.Map.trigger_aspects_on_tile(tile)

    @staticmethod
    def process_end_of_round_updates():
        """
        Update aspect durations
        """

        from scripts.global_singletons.managers import world_manager
        game_map = world_manager.Map.get_game_map()

        # TODO - set to only apply within X range of player
        for row in game_map.tiles:
            for tile in row:
                if tile.aspects:

                    # update durations
                    world_manager.Map.reduce_aspect_durations_on_tile(tile)
                    world_manager.Map.cleanse_expired_aspects(tile)
