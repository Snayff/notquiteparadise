from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.core.constants import EntityEventTypes, MessageTypes, Directions
from scripts.events.ui_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher, Subscriber, Event
from scripts.managers.turn_manager import turn
from scripts.managers.world_manager import world
from scripts.world.components import Position

if TYPE_CHECKING:
    from scripts.events.entity_events import DieEvent, LearnEvent, MoveEvent
    from scripts.events.entity_events import UseSkillEvent


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
        old_x, old_y = event.start_pos[0], event.start_pos[1]

        for step in range(0, distance):
            target_x = old_x + dir_x
            target_y = old_y + dir_y

            # is there something in the way?
            if world.Map.is_tile_in_bounds(target_x, target_y):
                target_tile = world.Map.get_tile((target_x, target_y))
                is_tile_blocking_movement = target_tile.blocks_movement
                entity_on_tile = target_tile.has_entity

                # check for no entity in way but tile is blocked
                if not entity_on_tile and is_tile_blocking_movement:
                    publisher.publish(MessageEvent(MessageTypes.LOG, f"There`s something in the way!"))

                # check if entity blocking tile to attack
                elif entity_on_tile:
                    # TODO - change to EC approach
                    skill = entity.actor.known_skills[0]
                    skill_data = library.get_skill_data(skill.skill_tree_name, skill.name)
                    direction = Directions((dir_x, dir_y))
                    if direction in skill_data.target_directions:
                        publisher.publish((UseSkillEvent(entity, skill, (dir_x, dir_y))))
                    else:
                        publisher.publish(MessageEvent(MessageTypes.LOG, f"{skill.name} doesn't go that way!"))

                # if nothing in the way, time to move!
                elif not entity_on_tile and not is_tile_blocking_movement:
                    position = world.Entity.get_component(entity, Position)
                    position.x = target_x
                    position.y = target_y

                    # update fov if needed
                    if entity == world.Entity.get_player():
                        sight_range = 3  # TODO - update to get sight_range from entity components
                        world.FOV.recompute_player_fov(position.x, position.y, sight_range)

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
                publisher.publish(MessageEvent(MessageTypes.LOG, "You cannot afford to do that."))
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

        # remove from turn queue
        if entity in turn.turn_queue:
            turn.turn_queue.pop(entity)
        if turn.turn_holder == entity:
            turn.build_new_turn_queue()

        # delete from world
        world.Entity.delete(entity)

    @staticmethod
    def process_learn(event: LearnEvent):
        """
        Have an entity learn a skill.

        Args:
            event:
        """
        event.entity.actor.learn_skill(event.skill_tree_name, event.skill_name)
