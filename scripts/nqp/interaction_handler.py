from __future__ import annotations

import logging
import scripts.engine.world
from typing import TYPE_CHECKING
from scripts.engine import world, entity, skill, utility
from scripts.engine.core.constants import InteractionCause, InteractionCauseType, TerrainCollision
from scripts.engine.core.event_core import Subscriber
from scripts.engine.component import Position, Interaction, Behaviour, IsProjectile
from scripts.engine.event import EndTurnEvent, EndRoundEvent, TileInteractionEvent, ExpireEvent, \
    EntityCollisionEvent, TerrainCollisionEvent, MoveEvent
from scripts.engine.library import library

if TYPE_CHECKING:
    from typing import List, Type, Tuple


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

        elif isinstance(event, EntityCollisionEvent):
            self._process_entity_collision(event)

        elif isinstance(event, MoveEvent):
            self._process_move(event)

    def _process_move(self, event: MoveEvent):
        # N.B. impacts moving entities current position
        position = entity.get_entitys_component(event.entity, Position)
        self._apply_effects_to_tiles(event.entity, InteractionCause.MOVE, (position.x, position.y))

    def _process_expiry(self, event: ExpireEvent):
        position = entity.get_entitys_component(event.entity, Position)
        self._apply_effects_to_tiles(event.entity, InteractionCause.EXPIRE, (position.x, position.y))

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
        #     # FIXME - rebuild to work for EC
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

    def _process_entity_collision(self, event: EntityCollisionEvent):
        current_x, current_y = event.start_pos[0], event.start_pos[1]
        target_x, target_y = current_x + event.direction[0], current_y + event.direction[1]

        self._apply_effects_to_tiles(event.entity, InteractionCause.ENTITY_COLLISION, (target_x, target_y))

    def _process_terrain_collision(self, event: TerrainCollisionEvent):
        ent = event.entity
        name = entity.get_name(ent)
        current_x, current_y = event.start_pos[0], event.start_pos[1]
        target_x, target_y = current_x + event.direction[0], current_y + event.direction[1]

        # what hit the terrain?
        # Is it a projectile?
        if entity.has_component(ent, IsProjectile):
            logging.debug(f"{name} hit a blocking tile and will...")
            behaviour = entity.get_entitys_component(ent, Behaviour)
            projectile_data = library.get_skill_data(behaviour.behaviour.skill_name).projectile
            terrain_collision = projectile_data.terrain_collision

            if terrain_collision == TerrainCollision.ACTIVATE:
                logging.debug(f"-> activate at ({target_x}, {target_y}).")
                self._apply_effects_to_tiles(ent, InteractionCause.TERRAIN_COLLISION, (target_x, target_y))

            elif terrain_collision == TerrainCollision.REFLECT:
                dir_x, dir_y = scripts.engine.world.get_reflected_direction((current_x, current_y), event.direction)
                logging.info(f"-> change direction to ({dir_x}, {dir_y}).")
                behaviour.behaviour.direction = (dir_x, dir_y)

            elif terrain_collision == TerrainCollision.FIZZLE:
                logging.info(f"fizzle at ({current_x}, {current_y}).")

            else:
                logging.debug(f"{name} hit blocking tile and did nothing.")

    @staticmethod
    def _apply_effects_to_tiles(causing_entity: int, interaction_cause: InteractionCauseType,
            target_pos: Tuple[int, int]):
        """
        Apply all effects relating to a cause of interaction.
        """
        # get current position

        target_x, target_y = target_pos[0],  target_pos[1]

        # get interactions effects for specified cause
        interactions = entity.get_entitys_component(causing_entity, Interaction)
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
                    effected_tiles = world.get_tiles(target_x, target_y, coords)

                    # apply effects
                    skill.process_effect(effect, effected_tiles, causing_entity)