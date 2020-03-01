from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine.core.constants import MessageTypes, TargetTags, GameStates
from scripts.engine.events import MessageEvent, WantToUseSkillEvent, UseSkillEvent, DieEvent, MoveEvent, EndTurnEvent, \
    ChangeGameStateEvent
from scripts.engine.library import library
from scripts.engine.core.event_core import publisher, Subscriber


from scripts.managers.world_manager.world_manager import world
from scripts.engine.components import Position, Knowledge, IsGod, Aesthetic

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
        entity = event.entity
        old_x, old_y = event.start_pos

        for step in range(0, distance):
            target_x = old_x + dir_x
            target_y = old_y + dir_y

            # is there something in the way?
            target_tile = world.Map.get_tile((target_x, target_y))

            # check a tile was returned
            if target_tile:
                is_tile_blocking_movement = world.Map.tile_has_tag(target_tile, TargetTags.BLOCKED_MOVEMENT, entity)
                is_entity_on_tile = world.Map.tile_has_tag(target_tile, TargetTags.OTHER_ENTITY, entity)
            else:
                is_tile_blocking_movement = True
                is_entity_on_tile = False

            # check for no entity in way but tile is blocked
            if not is_entity_on_tile and is_tile_blocking_movement:
                publisher.publish(MessageEvent(MessageTypes.LOG, f"There`s something in the way!"))

            # check if entity blocking tile to attack
            elif is_entity_on_tile:
                knowledge = world.Entity.get_entitys_component(entity, Knowledge)
                skill_name = knowledge.skills[0]
                skill_data = library.get_skill_data(skill_name)
                #direction = Directions((dir_x, dir_y))
                if (dir_x, dir_y) in skill_data.target_directions:
                    publisher.publish((UseSkillEvent(entity, skill_name, event.start_pos, (dir_x, dir_y))))
                else:
                    publisher.publish(MessageEvent(MessageTypes.LOG, f"{skill_name} doesn't go that way!"))

            # if nothing in the way, time to move!
            elif not is_entity_on_tile and not is_tile_blocking_movement:
                position = world.Entity.get_entitys_component(entity, Position)
                position.x = target_x
                position.y = target_y

                aesthetic: Aesthetic = world.Entity.get_entitys_component(entity, Aesthetic)
                aesthetic.target_screen_x, aesthetic.target_screen_y = ui_manager.Element.world_to_screen_position((target_x,
                target_y))
                aesthetic.current_sprite = aesthetic.sprites.move

                # update fov if needed
                if entity == world.Entity.get_player():
                    stats = world.Entity.get_combat_stats(entity)
                    sight_range = max(0, stats.sight_range)
                    world.FOV.recompute_fov(position.x, position.y, sight_range)

                # if entity that moved is turn holder then end their turn
                if entity == world.Turn.get_turn_holder():
                    publisher.publish(EndTurnEvent(entity, 10))  # TODO - replace magic number with cost to move

    @staticmethod
    def process_skill(event: UseSkillEvent):
        """
        Process the entity`s skill
        Args:
            event(EntityEvent): the event to process
        """
        entity = event.entity
        skill_name = event.skill_name
        skill_data = library.get_skill_data(skill_name)

        # check it can be afforded
        if world.Skill.can_afford_cost(entity, skill_data.resource_type, skill_data.resource_cost):
            world.Skill.pay_resource_cost(entity, skill_data.resource_type, skill_data.resource_cost)

            # use skill
            world.Skill.use(entity, skill_name, event.start_pos, event.direction)

            # end the turn if the entity isnt a god
            if not world.Entity.has_component(entity, IsGod):
                publisher.publish(EndTurnEvent(entity, skill_data.time_cost))

        else:
            # is it the player that's can't afford it?
            if entity == world.Entity.get_player():
                publisher.publish(MessageEvent(MessageTypes.LOG, "You cannot afford to do that."))
            else:
                identity = world.Entity.get_identity(entity)
                logging.warning(f"{identity.name} tried to use {skill_name}, which they can`t afford")

    @staticmethod
    def process_die(event: DieEvent):
        """
        Control the entity death
        """

        # TODO add player death
        entity = event.dying_entity
        turn_queue = world.Turn.get_turn_queue()

        # remove from turn queue
        if entity in turn_queue:
            turn_queue.pop(entity)

        # if turn holder and not player create new queue
        if entity == world.Turn.get_turn_holder() and entity != world.Entity.get_player():
            world.Turn.build_new_turn_queue()

        # delete from world
        world.Entity.delete(entity)

    @staticmethod
    def process_want_to_use_skill(event: WantToUseSkillEvent):
        """
        Process the desire to use a skill. """
        skill_number = event.skill_number
        player = world.Entity.get_player()
        player_pos = world.Entity.get_entitys_component(player, Position)
        skill_name = game.State.get_active_skill()
        skill_pressed = player.actor.known_skills[skill_number]

        # confirm skill pressed doesn't match skill already pressed
        if skill_pressed != skill_name:
            knowledge = world.Entity.get_entitys_component(player, Knowledge)
            skill_name = knowledge.skills[skill_number]
            skill_data = library.get_skill_data(skill_name)

            if world.Skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill_name))

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
        world.Entity.spend_time(event.entity, event.time_spent)