from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Type

from scripts.engine import world, entity, skill, utility
from scripts.engine.core.constants import InteractionCause, InteractionCauseType
from scripts.engine.core.event_core import Subscriber
from scripts.engine.component import Position, Interaction
from scripts.engine.event import EndTurnEvent, EndRoundEvent, TileInteractionEvent, ExpireEvent
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import List


class InteractionHandler(Subscriber):
    """
    Handle interaction events
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "interaction_handler", event_hub)

    def process_event(self, event):
        """
        Control interaction events
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.__class__.__name__}...")

        if isinstance(event, TileInteractionEvent):
            self._process_tile_interaction(event)

        elif isinstance(event, EndTurnEvent):
            self._process_end_turn(event)

        elif isinstance(event, EndRoundEvent):
            self._process_end_round()

        elif isinstance(event, ExpireEvent):
            self._process_expiry(event)

    @staticmethod
    def _process_expiry(event: ExpireEvent):
        ent = event.entity
        interactions = entity.get_entitys_component(ent, Interaction)
        interaction = interactions.interactions.get(InteractionCause.EXPIRE)

    @staticmethod
    def _process_tile_interaction(event: TileInteractionEvent):
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
    def _process_end_turn(event: EndTurnEvent):
        """
        Trigger aspects on tile turn holder is on
        """
        ent = event.entity
        # position = entity.get_entitys_component(ent, Position)
        # tile = world.get_tile((position.x, position.y))

        # trigger aspects
        #  FIXME - update to EC approach
        #world.trigger_aspects_on_tile(tile)

    @staticmethod
    def _process_end_round():
        """
        Update aspect durations
        """
        game_map = world.get_game_map()

        # TODO - set to only apply to activated entities
        #  TODO - update to EC approach
        # for row in game_map.tiles:
        #     for tile in row:
        #         if tile.aspects:
        #             # update durations
        #             world.reduce_aspect_durations_on_tile(tile)
        #             world.cleanse_expired_aspects(tile)

    @staticmethod
    def _apply_effects_to_tiles(ent: int, interaction_cause: InteractionCauseType):
        """
        Apply all effects relating to a cause of interaction.
        """
        # get current position
        position = entity.get_entitys_component(ent, Position)
        current_x = position.x
        current_y = position.y

        # get interactions effects for specified cause
        interactions = entity.get_entitys_component(ent, Interaction)
        caused_interactions = interactions.interactions.get(interaction_cause)
        effect_names = utility.get_class_members(Type[caused_interactions])

        # loop each effect name and get the data from the field
        for effect_name in effect_names:
            if effect_name != "cause":
                effect = getattr(caused_interactions, effect_name)

                # if we have details for the effect
                if effect:
                    # each effect applies to a different area so get effected tiles
                    coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
                    effected_tiles = world.get_tiles(current_x, current_y, coords)

                    # apply effects
                    skill.apply_effect(effect, effected_tiles, ent)