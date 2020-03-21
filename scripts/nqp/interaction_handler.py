from __future__ import annotations

import logging
import scripts.engine.world
from snecs.types import EntityID
from typing import TYPE_CHECKING, Type, Optional
from scripts.engine import world, entity, skill, utility
from scripts.engine.core.constants import InteractionCause, InteractionCauseType, TerrainCollision, Effect, \
    DEBUG_LOG_EVENT_RECEIPTS
from scripts.engine.core.event_core import Subscriber
from scripts.engine.component import Position, Interactions, Behaviour, IsProjectile
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
        self._apply_effects_to_tiles(event.entity, InteractionCause.MOVE, (event.start_pos[0], event.start_pos[1]),
                                     (event.direction[0], event.direction[1]))

    def _process_expiry(self, event: ExpireEvent):
        position = entity.get_entitys_component(event.entity, Position)
        self._apply_effects_to_tiles(event.entity, InteractionCause.EXPIRE, (position.x, position.y),
                                     (position.x, position.y))
        entity.delete(event.entity)

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
        ent = event.entity
        a_name = entity.get_name(ent)
        b_name = entity.get_name(event.blocking_entity)
        logging.debug(f"'{a_name}' collided with '{b_name}'.")

        # check if projectile as we would need the instigating entity
        is_projectile = entity.get_entitys_component(ent, IsProjectile)

        # ensure creator is passed if projectile hit someone
        if is_projectile:
            instigating_entity = is_projectile.creator
        else:
            instigating_entity = None

        target_x, target_y = event.start_pos[0] + event.direction[0], event.start_pos[1] + event.direction[1]
        self._apply_effects_to_tiles(ent, InteractionCause.ENTITY_COLLISION,
                                     (event.start_pos[0], event.start_pos[1]), (target_x, target_y),
                                     instigating_entity)

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
                self._apply_effects_to_tiles(ent, InteractionCause.TERRAIN_COLLISION, (current_x, current_y),
                                             (target_x, target_y))

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
            start_pos: Tuple[int, int], target_pos: Tuple[int, int], instigating_entity: Optional[EntityID] = None):
        """
        Apply all effects relating to a cause of interaction.
        """
        # get positions
        start_x, start_y = start_pos[0], start_pos[1]
        target_x, target_y = target_pos[0],  target_pos[1]

        # get interactions effects for specified cause
        if entity.has_component(causing_entity, Interactions):
            interactions = entity.get_entitys_component(causing_entity, Interactions)
            caused_interactions = interactions.get(interaction_cause)

            # do we have anything we need to trigger?
            if caused_interactions:
                effect_names = utility.get_class_members(Effect)

                # loop each effect name and get the data from the field
                for effect_name in effect_names:
                    effect_name = effect_name.lower()

                    if effect_name != "cause":
                        try:
                            effect = getattr(caused_interactions, effect_name)

                            # each effect applies to a different area so get effected tiles
                            coords = utility.get_coords_from_shape(effect.shape, effect.shape_size)
                            effected_tiles = world.get_tiles(target_x, target_y, coords)

                            # pass the entity to refer back to for stats and such
                            if instigating_entity:
                                originating_entity = instigating_entity
                            else:
                                originating_entity = causing_entity

                            # apply effects
                            skill.process_effect(effect, effected_tiles, originating_entity)
                        except AttributeError:
                            pass