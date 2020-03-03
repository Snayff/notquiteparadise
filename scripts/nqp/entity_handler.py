from __future__ import annotations

import logging  # type: ignore
from typing import TYPE_CHECKING

from scripts.engine import world, chrono, entity, state, skill
from scripts.engine.core.constants import MessageType, TargetTag, GameState
from scripts.engine.event import MessageEvent, WantToUseSkillEvent, UseSkillEvent, DieEvent, MoveEvent, EndTurnEvent, \
    ChangeGameStateEvent
from scripts.engine.library import library
from scripts.engine.core.event_core import publisher, Subscriber



from scripts.engine.component import Position, Knowledge, IsGod, Aesthetic
from scripts.engine.ui.manager import ui

if TYPE_CHECKING:
    pass


class EntityHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "entity_handler", event_hub)

    def process_event(self, event):
        """
        Control entity events
        """
        # log that event has been received
        logging.debug(f"{self.name} received {event.topic}:{event.__class__.__name__}.")

        if isinstance(event, MoveEvent):
            self.process_move(event)

        elif isinstance(event, UseSkillEvent):
            self.process_skill(event)

        elif isinstance(event, DieEvent):
            self.process_die(event)

        elif isinstance(event, WantToUseSkillEvent):
            self.process_want_to_use_skill(event)

        elif isinstance(event, EndTurnEvent):
            self.process_end_turn(event)

    @staticmethod
    def process_move(event: MoveEvent):
        """
        Check if entity can move to the target tile, then either cancel the move (if blocked), bump attack (if
        target tile has entity) or move.
        """
        # get info from event
        dir_x, dir_y = event.direction
        distance = event.distance
        ent = event.entity
        old_x, old_y = event.start_pos

        for step in range(0, distance):
            target_x = old_x + dir_x
            target_y = old_y + dir_y

            # is there something in the way?
            target_tile = world.get_tile((target_x, target_y))

            # check a tile was returned
            if target_tile:
                is_tile_blocking_movement = world.tile_has_tag(target_tile, TargetTag.BLOCKED_MOVEMENT, ent)
                is_entity_on_tile = world.tile_has_tag(target_tile, TargetTag.OTHER_ENTITY, ent)
            else:
                is_tile_blocking_movement = True
                is_entity_on_tile = False

            # check for no entity in way but tile is blocked
            if not is_entity_on_tile and is_tile_blocking_movement:
                publisher.publish(MessageEvent(MessageType.LOG, f"There`s something in the way!"))

            # check if entity blocking tile to attack
            elif is_entity_on_tile:
                knowledge = entity.get_entitys_component(ent, Knowledge)
                skill_name = knowledge.skills[0]
                skill_data = library.get_skill_data(skill_name)
                #direction = Direction((dir_x, dir_y))
                if (dir_x, dir_y) in skill_data.target_directions:
                    publisher.publish((UseSkillEvent(ent, skill_name, event.start_pos, (dir_x, dir_y))))
                else:
                    publisher.publish(MessageEvent(MessageType.LOG, f"{skill_name} doesn't go that way!"))

            # if nothing in the way, time to move!
            elif not is_entity_on_tile and not is_tile_blocking_movement:
                position = entity.get_entitys_component(ent, Position)
                position.x = target_x
                position.y = target_y

                aesthetic: Aesthetic = entity.get_entitys_component(ent, Aesthetic)
                aesthetic.target_screen_x, aesthetic.target_screen_y = ui.world_to_screen_position((target_x,
                target_y))
                aesthetic.current_sprite = aesthetic.sprites.move

                # update fov if needed
                if entity == entity.get_player():
                    stats = entity.get_combat_stats(ent)
                    sight_range = max(0, stats.sight_range)
                    world.recompute_fov(position.x, position.y, sight_range)

                # if entity that moved is turn holder then end their turn
                if entity == chrono.get_turn_holder():
                    publisher.publish(EndTurnEvent(entity, 10))  # TODO - replace magic number with cost to move

    @staticmethod
    def process_skill(event: UseSkillEvent):
        """
        Process the entity`s skill
        Args:
            event(EntityEvent): the event to process
        """
        ent = event.entity
        skill_name = event.skill_name
        skill_data = library.get_skill_data(skill_name)

        # check it can be afforded
        if skill.can_afford_cost(ent, skill_data.resource_type, skill_data.resource_cost):
            skill.pay_resource_cost(ent, skill_data.resource_type, skill_data.resource_cost)

            # use skill
            skill.use(ent, skill_name, event.start_pos, event.direction)

            # end the turn if the entity isnt a god
            if not ent.has_component(ent, IsGod):
                publisher.publish(EndTurnEvent(ent, skill_data.time_cost))

        else:
            # is it the player that's can't afford it?
            if ent == entity.get_player():
                publisher.publish(MessageEvent(MessageType.LOG, "You cannot afford to do that."))
            else:
                identity = entity.get_identity(ent)
                logging.warning(f"{identity.name} tried to use {skill_name}, which they can`t afford")

    @staticmethod
    def process_die(event: DieEvent):
        """
        Control the entity death
        """

        # TODO add player death
        entity = event.dying_entity
        turn_queue = chrono.get_turn_queue()

        # remove from turn queue
        if entity in turn_queue:
            turn_queue.pop(entity)

        # if turn holder and not player create new queue
        if entity == chrono.get_turn_holder() and entity != entity.get_player():
            chrono.build_new_turn_queue()

        # delete from world
        entity.delete(entity)

    @staticmethod
    def process_want_to_use_skill(event: WantToUseSkillEvent):
        """
        Process the desire to use a skill. """
        skill_number = event.skill_number
        player = entity.get_player()
        player_pos = entity.get_entitys_component(player, Position)
        skill_name = state.get_active_skill()
        skill_pressed = player.actor.known_skills[skill_number]

        # confirm skill pressed doesn't match skill already pressed
        if skill_pressed != skill_name:
            knowledge = entity.get_entitys_component(player, Knowledge)
            skill_name = knowledge.skills[skill_number]
            skill_data = library.get_skill_data(skill_name)

            if skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                publisher.publish(ChangeGameStateEvent(GameState.TARGETING_MODE, skill_name))

        # skill matches already selected so use skill!
        else:
            pass
            # TODO - activate skill. Need to get selected tile.
            # publisher.publish(UseSkillEvent(player, skill_name, (player_pos.x, player_pos.y), ))

    @staticmethod
    def process_end_turn(event: EndTurnEvent):
        """
        Have entity spend their time
        """
        #  update turn holder`s time spent
        entity.spend_time(event.entity, event.time_spent)