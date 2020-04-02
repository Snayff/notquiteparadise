from __future__ import annotations

import logging

from snecs.typedefs import EntityID
from typing import TYPE_CHECKING, Type, Optional
from scripts.engine import world, utility
from scripts.engine.core.constants import InteractionCause, InteractionCauseType, TerrainCollision, Effect, \
    DEBUG_LOG_EVENT_RECEIPTS
from scripts.engine.core.definitions import InteractionData
from scripts.engine.core.event_core import Subscriber
from scripts.engine.component import Position, Interactions, Behaviour, IsProjectile, Afflictions
from scripts.engine.event import EndTurnEvent, EndRoundEvent, ExpireEvent, \
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
        Control interaction events. Looks for InteractionCause associated events.
        """
        if isinstance(event, EndTurnEvent):
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
        target_pos = (event.start_pos[0] + event.direction[0], event.start_pos[1] + event.direction[1])
        self._process_caused_interactions(event.entity, InteractionCause.MOVE, (event.start_pos[0], event.start_pos[1]),
                                     target_pos)

    def _process_expiry(self, event: ExpireEvent):
        position = world.get_entitys_component(event.entity, Position)
        if position:
            self._process_caused_interactions(event.entity, InteractionCause.EXPIRE, (position.x, position.y),
                                     (position.x, position.y))
            world.delete(event.entity)
        else:
            logging.warning(f"Unable to process expiry as position not found.")

    @staticmethod
    def _process_end_turn(event: EndTurnEvent):
        """
        Trigger aspects on tile turn holder is on
        """
        entity = event.entity
        # position = entity.get_entitys_component(entity, Position)
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
        entity = event.entity
        a_name = world.get_name(entity)
        b_name = world.get_name(event.blocking_entity)
        logging.debug(f"'{a_name}' collided with '{b_name}'.")

        # check if projectile as we would need the instigating entity
        is_projectile = world.get_entitys_component(entity, IsProjectile)
        # FIXME - throws regular warning as regularly not a projectile

        # ensure creators_name is passed if projectile hit someone
        if is_projectile:
            instigating_entity: Optional[EntityID]
            instigating_entity = is_projectile.creator
        else:
            instigating_entity = None

        target_x, target_y = event.start_pos[0] + event.direction[0], event.start_pos[1] + event.direction[1]
        self._process_caused_interactions(entity, InteractionCause.ENTITY_COLLISION,
                                     (event.start_pos[0], event.start_pos[1]), (target_x, target_y),
                                     instigating_entity)

    def _process_terrain_collision(self, event: TerrainCollisionEvent):
        entity = event.entity
        name = world.get_name(entity)
        current_x, current_y = event.start_pos[0], event.start_pos[1]
        target_x, target_y = current_x + event.direction[0], current_y + event.direction[1]

        # what hit the terrain?
        # Is it a projectile?
        if world.has_component(entity, IsProjectile):
            logging.debug(f"{name} hit a blocking tile and will...")

            # TODO - readd projectile support
            # behaviour = world.get_entitys_component(entity, Behaviour)
            # projectile_data = library.get_skill_data(behaviour.behaviour.skill_name).projectile
            # terrain_collision = projectile_data.terrain_collision

            terrain_collision = None
            if terrain_collision == TerrainCollision.ACTIVATE:
                logging.debug(f"-> activate at ({target_x}, {target_y}).")
                self._process_caused_interactions(entity, InteractionCause.TERRAIN_COLLISION, (current_x, current_y),
                                             (target_x, target_y))

            elif terrain_collision == TerrainCollision.REFLECT:
                dir_x, dir_y = world.get_reflected_direction((current_x, current_y), event.direction)
                logging.info(f"-> change direction to ({dir_x}, {dir_y}).")
                #behaviour.behaviour.direction = (dir_x, dir_y)

            elif terrain_collision == TerrainCollision.FIZZLE:
                logging.info(f"fizzle at ({current_x}, {current_y}).")

            else:
                logging.debug(f"{name} hit blocking tile and did nothing.")

    def _process_caused_interactions(self, causing_entity: EntityID, interaction_cause: InteractionCauseType,
            start_pos: Tuple[int, int], target_pos: Tuple[int, int], instigating_entity: Optional[EntityID] = None):
        caused_interactions = None
        # TODO - rebuild
        pass
        # # get interactions effects for specified cause
        # if world.has_component(causing_entity, Interactions):
        #     interactions = world.get_entitys_component(causing_entity, Interactions)
        #     if interactions:
        #         caused_interactions = interactions.get(interaction_cause)
        #     if caused_interactions:
        #         self._apply_effects_to_tiles(causing_entity, caused_interactions, start_pos, target_pos,
        #                                      instigating_entity)
        #
        # if world.has_component(causing_entity, Afflictions):
        #     afflictions = world.get_entitys_component(causing_entity, Afflictions)
        #     for affliction in afflictions.keys():
        #         interactions = library.get_affliction_data(affliction).interactions
        #         caused_interactions = interactions.get(interaction_cause)
        #         if caused_interactions:
        #             # these effects have not been unpacked into Interactions so need to do so now
        #             caused_interactions = caused_interactions.effects
        #             self._apply_effects_to_tiles(causing_entity, caused_interactions, start_pos, target_pos,
        #                                          effect_creator=affliction)

    @staticmethod
    def _apply_effects_to_tiles(causing_entity: int, caused_interaction: InteractionData,
            start_pos: Tuple[int, int], target_pos: Tuple[int, int], instigating_entity: Optional[EntityID] = None,
            effect_creator: Optional[str] = ""):
        """
        Apply all effects relating to a cause of interaction.
        """
        pass
        # TODO - rebuild

        # # get positions
        # start_x, start_y = start_pos[0], start_pos[1]
        # target_x, target_y = target_pos[0],  target_pos[1]
        #
        # # copy effects so we can extend list with new effects
        # effects = caused_interaction.copy()
        #
        # # loop each effect name and get the data from the field
        # for effect in effects:
        #     # each effect applies to a different area so get effected tiles
        #     coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
        #     effected_tiles = world.get_tiles(target_x, target_y, coords)
        #
        #     # pass the entity to refer back to for stats and such
        #     if instigating_entity:
        #         originating_entity = instigating_entity
        #     else:
        #         originating_entity = causing_entity
        #
        #     # apply effects
        #     if effect_creator:
        #         effect.creator = effect_creator
        #     #act.process_effect(effect, effected_tiles, originating_entity)
