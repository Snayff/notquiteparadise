from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import EntityEventTypes, MessageEventTypes
from scripts.events.message_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.managers.turn_manager import turn
from scripts.managers.world_manager import world
from scripts.event_handlers.pub_sub_hub import Subscriber, Event
from scripts.events.entity_events import UseSkillEvent

if TYPE_CHECKING:
    from scripts.events.entity_events import DieEvent, LearnEvent, MoveEvent


class EntityHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def process_event(self, event):
        """
        Control entity events

        Args:
            event(Event): the event in need of processing
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.event_type}.")

        if event.event_type == EntityEventTypes.MOVE:
            event: MoveEvent
            self.process_move(event)

        if event.event_type == EntityEventTypes.SKILL:
            event: UseSkillEvent
            self.process_skill(event)

        if event.event_type == EntityEventTypes.DIE:
            event: DieEvent
            self.process_die(event)

        if event.event_type == EntityEventTypes.LEARN:
            event: LearnEvent
            self.process_learn(event)

    @staticmethod
    def process_move(event: MoveEvent):
        """
        Check if entity can move to the target tile, then either cancel the move (if blocked), bump attack (if
        target tile has entity) or move.

        Args:
            event(MoveEvent):
        """
        # get info from event
        dir_x, dir_y = event.direction
        distance = event.distance
        entity = event.entity
        old_x, old_y = entity.x, entity.y

        for step in range(0, distance):
            target_x = old_x + dir_x
            target_y = old_y + dir_y

            # is there something in the way?
            if world.Map.is_tile_in_bounds(target_x, target_y):
                is_tile_blocking_movement = world.Map.is_tile_blocking_movement(target_x, target_y)
                entity_blocking_movement = world.Entity.get_blocking_entity(target_x, target_y)

                # check for no entity in way but tile is blocked
                if not entity_blocking_movement and is_tile_blocking_movement:
                    msg = f"There`s something in the way!"
                    publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

                # check if entity blocking tile to attack
                elif entity_blocking_movement:
                    skill = entity.actor.known_skills[0]
                    publisher.publish((UseSkillEvent(entity, skill, (dir_x, dir_y))))

                # if nothing in the way, time to move!
                elif not entity_blocking_movement and not is_tile_blocking_movement:
                    # clean up old tile
                    old_tile = world.Map.get_tile((old_x, old_y))
                    world.Map.set_entity_on_tile(old_tile, None)

                    # move entity to new tile
                    new_tile = world.Map.get_tile((target_x, target_y))
                    world.Map.set_entity_on_tile(new_tile, entity)

                    # activate the tile's aspects affect
                    world.Map.trigger_aspects_on_tile(new_tile)

                # update fov if needed
                if entity.player:
                    world.FOV.recompute_player_fov(entity.x, entity.y, entity.sight_range)

    @staticmethod
    def process_skill(event: UseSkillEvent):
        """
        Process the entity`s skill
        Args:
            event(EntityEvent): the event to process
        """
        entity = event.entity
        skill = event.skill
        skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)

        # check it can be afforded
        if world.Skill.can_afford_cost(entity, skill_data.resource_type, skill_data.resource_cost):
            world.Skill.pay_resource_cost(entity, skill_data.resource_type, skill_data.resource_cost)

            # use skill
            event.skill.use(event.direction)
        else:
            # is it the player that's can't afford it?
            if entity == world.Entity.get_player():
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, "You cannot afford to do that."))
            else:
                logging.warning(f"{entity.name} tried to use {skill.name}, which they can`t afford")

    @staticmethod
    def process_die(event: DieEvent):
        """
        Control the entity death
        Args:
            event(EntityEvent): the event to process
        """

        # TODO add player death
        entity = event.dying_entity

        # just in case... remove the ai
        if entity.ai:
            entity.ai = None

        # get the tile and remove the entity from it
        tile_x, tile_y = entity.x, entity.y
        tile = world.Map.get_tile((tile_x, tile_y))
        world.Map.set_entity_on_tile(tile, None)

        # remove from turn queue
        if entity in turn.turn_queue:
            turn.turn_queue.pop(entity)
        if turn.turn_holder == entity:
            turn.build_new_turn_queue()

    @staticmethod
    def process_learn(event: LearnEvent):
        """
        Have an entity learn a skill.

        Args:
            event:
        """
        event.entity.actor.learn_skill(event.skill_tree_name, event.skill_name)
