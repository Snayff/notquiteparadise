from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine import world, chrono, entity, state, skill, debug
from scripts.engine.core.constants import MessageType, TargetTag, GameState, Direction, DEFAULT_SIGHT_RANGE, \
    BASE_MOVE_COST
from scripts.engine.event import MessageEvent, WantToUseSkillEvent, UseSkillEvent, DieEvent, MoveEvent, \
    EndTurnEvent, ChangeGameStateEvent, ExpireEvent, TerrainCollisionEvent, EntityCollisionEvent
from scripts.engine.library import library
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.component import Position, Knowledge, IsGod, Aesthetic, FOV
from scripts.engine.ui.manager import ui
from scripts.engine.utility import value_to_member
from scripts.engine.world_objects.combat_stats import CombatStats

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
        ent = event.entity
        old_x, old_y = event.start_pos
        target_x = old_x + dir_x
        target_y = old_y + dir_y
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
            publisher.publish(TerrainCollisionEvent(ent, target_tile, (target_x, target_y), event.start_pos))
            publisher.publish(MessageEvent(MessageType.LOG, f"I can't go that way!"))

        # check if entity blocking tile
        elif is_entity_on_tile:
            entities_at_location = entity.get_entities_and_components_in_area([target_tile], None)
            blocking_entity = next(iter(entities_at_location))  # we only have one entity per tile so get that
            publisher.publish(EntityCollisionEvent(ent, blocking_entity, (target_x, target_y), event.start_pos))

        # if nothing in the way, time to move!
        elif not is_entity_on_tile and not is_tile_blocking_movement:
            position = entity.get_entitys_component(ent, Position)

            # update position
            if position:
                position.x = target_x
                position.y = target_y
            else:
                debug.log_component_not_found(ent, "update sprite to move", Position)

            # TODO - move to UI handler
            aesthetic = entity.get_entitys_component(ent, Aesthetic)
            if aesthetic:
                aesthetic.target_screen_x, aesthetic.target_screen_y = ui.world_to_screen_position((target_x,
                target_y))
                aesthetic.current_sprite = aesthetic.sprites.move
            else:
                debug.log_component_not_found(ent, "tried to update sprite to move", Aesthetic)

            # update fov if needed
            if entity.has_component(ent, FOV):
                if entity.has_component(ent, CombatStats):
                    stats = entity.get_combat_stats(ent)
                    sight_range = max(0, stats.sight_range)
                else:
                    sight_range = DEFAULT_SIGHT_RANGE
                fov_map = entity.get_entitys_component(ent, FOV).map
                world.recompute_fov(position.x, position.y, sight_range, fov_map)

                # update tiles if it is player
                if ent == entity.get_player():
                    world.update_tile_visibility(fov_map)

            # if entity that moved is turn holder then end their turn
            if entity == chrono.get_turn_holder():
                publisher.publish(EndTurnEvent(entity, BASE_MOVE_COST))

    @staticmethod
    def process_skill(event: UseSkillEvent):
        """
        Process the entity`s skill
        """
        ent = event.entity
        skill_name = event.skill_name
        skill_data = library.get_skill_data(skill_name)

        # check it can be afforded
        if skill_data.resource_type:
            if skill.can_afford_cost(ent, skill_data.resource_type, skill_data.resource_cost):
                skill.pay_resource_cost(ent, skill_data.resource_type, skill_data.resource_cost)

                # use skill i.e create projectile
                skill.use(ent, skill_name, event.start_pos, event.direction)

                # end the turn if the entity isnt a god
                if not entity.has_component(ent, IsGod):
                    publisher.publish(EndTurnEvent(ent, skill_data.time_cost))

            else:
                # is it the player that's can't afford it?
                if ent == entity.get_player():
                    publisher.publish(MessageEvent(MessageType.LOG, "I cannot afford to do that."))
                else:
                    name = entity.get_name(ent)
                    logging.warning(f"{name} tried to use {skill_name}, which they can`t afford")

    @staticmethod
    def process_die(event: DieEvent):
        """
        Control the entity death
        """

        # TODO add player death
        ent = event.entity
        turn_queue = chrono.get_turn_queue()

        # remove from turn queue
        if ent in turn_queue:
            turn_queue.pop(ent)

        # if turn holder and not player create new queue
        if entity == chrono.get_turn_holder() and entity != entity.get_player():
            chrono.build_new_turn_queue()

        # delete from world
        entity.delete(ent)

    @staticmethod
    def process_want_to_use_skill(event: WantToUseSkillEvent):
        """
        Process the desire to use a skill. """
        skill_number = event.skill_number
        player = entity.get_player()

        if player:
            active_skill = state.get_active_skill()
            knowledge = entity.get_entitys_component(player, Knowledge)

            if knowledge:
                skill_pressed = knowledge.skills[skill_number]
            else:
                skill_pressed = ""
                debug.log_component_not_found(player, "tried to process wanting to use a skill", Knowledge)

            # confirm skill pressed doesn't match skill already pressed
            if skill_pressed != active_skill and knowledge:
                skill_data = library.get_skill_data(skill_pressed)

                if skill_data.resource_type and skill_data.resource_cost:
                    if skill.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost):
                        publisher.publish(ChangeGameStateEvent(GameState.TARGETING_MODE, skill_pressed))

            # skill matches already selected so use skill!
            else:
                pass
                # TODO - activate skill. Need to get selected tile.
                # TODO - add time cost
                # player_pos = entity.get_entitys_component(player, Position)
                # publisher.publish(UseSkillEvent(player, skill_name, (player_pos.x, player_pos.y), ))

    @staticmethod
    def process_end_turn(event: EndTurnEvent):
        """
        Have entity spend their time
        """
        #  update turn holder`s time spent
        entity.spend_time(event.entity, event.time_spent)
