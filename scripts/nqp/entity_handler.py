from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine import world, chapter, existence, state, act, debug, utility
from scripts.engine.core.constants import MessageType, TargetTag, GameState, Direction, DEFAULT_SIGHT_RANGE, \
    BASE_MOVE_COST, DEBUG_LOG_EVENT_RECEIPTS, INFINITE, TargetingMethod
from scripts.engine.event import MessageEvent, WantToUseSkillEvent, UseSkillEvent, DieEvent, MoveEvent, \
    EndTurnEvent, ChangeGameStateEvent, ExpireEvent, TerrainCollisionEvent, EntityCollisionEvent, EndRoundEvent
from scripts.engine.library import library
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.component import Position, Knowledge, IsGod, Aesthetic, FOV, Blocking, HasCombatStats, Afflictions
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
        if isinstance(event, MoveEvent):
            self._process_move(event)

        elif isinstance(event, UseSkillEvent):
            self._process_use_skill(event)

        elif isinstance(event, DieEvent):
            self._process_die(event)

        elif isinstance(event, WantToUseSkillEvent):
            self._process_want_to_use_skill(event)

        elif isinstance(event, EndTurnEvent):
            self._process_end_turn(event)

        elif isinstance(event, EndRoundEvent):
            self._process_end_round(event)

    @staticmethod
    def _process_move(event: MoveEvent):
        """
        Check if entity can move to the target tile, then either cancel the move (if blocked), bump attack (if
        target tile has entity) or move.
        """
        # get info from event
        dir_x, dir_y = event.direction
        ent = event.entity
        name = existence.get_name(ent)
        old_x, old_y = event.start_pos
        target_x = old_x + dir_x
        target_y = old_y + dir_y
        target_tile = world.get_tile((target_x, target_y))
        direction_name = utility.value_to_member((target_x, target_y), Direction)

        # check a tile was returned
        if target_tile:
            is_tile_blocking_movement = world.tile_has_tag(target_tile, TargetTag.BLOCKED_MOVEMENT, ent)
            is_entity_on_tile = world.tile_has_tag(target_tile, TargetTag.NO_ENTITY)
        else:
            is_tile_blocking_movement = True
            is_entity_on_tile = False

        # check for no entity in way but tile is blocked
        if not is_entity_on_tile and is_tile_blocking_movement:
            publisher.publish(TerrainCollisionEvent(ent, target_tile, event.direction, event.start_pos))
            publisher.publish(MessageEvent(MessageType.LOG, f"I can't go that way!"))
            logging.debug(f"'{name}' tried to move in {direction_name} to ({target_x},{target_y}) but was blocked by "
                          f"terrain. ")

        # check if entity blocking tile
        elif is_entity_on_tile:
            entities = existence.get_entities_and_components_in_area([target_tile], [Blocking])
            for blocking_entity, (position, blocking, *rest) in entities.items():
                if blocking.blocks_movement:
                    publisher.publish(EntityCollisionEvent(ent, blocking_entity, event.direction, event.start_pos))
                    break

        # if nothing in the way, time to move!
        elif not is_entity_on_tile and not is_tile_blocking_movement:
            position = existence.get_entitys_component(ent, Position)

            # update position
            if position:
                position.x = target_x
                position.y = target_y

            # TODO - move to UI handler
            aesthetic = existence.get_entitys_component(ent, Aesthetic)
            if aesthetic:
                aesthetic.target_screen_x, aesthetic.target_screen_y = ui.world_to_screen_position((target_x,
                target_y))
                aesthetic.current_sprite = aesthetic.sprites.move

            # update fov if needed
            if existence.has_component(ent, FOV):
                if existence.has_component(ent, HasCombatStats):
                    stats = existence.get_combat_stats(ent)
                    sight_range = max(0, stats.sight_range)
                else:
                    sight_range = DEFAULT_SIGHT_RANGE
                fov_map = existence.get_entitys_component(ent, FOV).map
                world.recompute_fov(position.x, position.y, sight_range, fov_map)

                # update tiles if it is player
                if ent == existence.get_player():
                    # TODO - should probably sit in world handler
                    world.update_tile_visibility(fov_map)

            # if entity that moved is turn holder then end their turn
            if ent == chapter.get_turn_holder():
                publisher.publish(EndTurnEvent(ent, BASE_MOVE_COST))

    @staticmethod
    def _process_want_to_use_skill(event: WantToUseSkillEvent):
        """
        Process the desire to use a skill.
        """
        player = existence.get_player()
        ent = event.entity
        start_x, start_y = event.start_pos
        direction = event.direction
        dir_x, dir_y = direction
        skill_name = event.skill_name
        skill_data = library.get_skill_data(skill_name)

        # flags
        got_target = can_afford = not_on_cooldown = False

        # complete initial checks
        targeting = skill_data.targeting_method
        if (targeting == TargetingMethod.TARGET and direction) or targeting == TargetingMethod.AUTO:
            got_target = True

        can_afford = act.can_afford_cost(player, skill_data.resource_type, skill_data.resource_cost)

        cooldown = existence.get_entitys_component(player, Knowledge).skills[skill_name].cooldown
        if cooldown <= 0:
            not_on_cooldown = True

        # if its the player wanting to use their skill but we dont have a target direction
        if player and player == ent and not got_target:
            game_state = state.get_current()

            # are we already in targeting mode?
            if game_state == GameState.TARGETING_MODE:
                active_skill = state.get_active_skill()

                # if skill pressed doesn't match skill already being targeted
                if skill_name != active_skill:
                    # reactivate targeting mode with the new skill
                    if can_afford and not_on_cooldown:
                        publisher.publish(ChangeGameStateEvent(GameState.TARGETING_MODE, skill_name))

                else:
                    # player pressed the already active skill, so they want to use it
                    if can_afford and not_on_cooldown:
                        # TODO - get selected tile then get direction between that and player
                        logging.warning(f"Tried to use skill from a key press in targeting mode. Not implemented.")
                    pass

            else:
                # we're not in targeting mode but have no direction for skill, so let's get a target
                if can_afford and not_on_cooldown:
                    publisher.publish(ChangeGameStateEvent(GameState.TARGETING_MODE, skill_name))

        elif got_target:
            # we have a direction, let's see if we can use the skill
            if can_afford and not_on_cooldown:
                target_pos = (start_x + dir_x, start_y + dir_y)
                target_tiles = act.get_target_tiles(ent, skill_name, (start_x, start_y), target_pos)

                # we have someone to target, let's go
                if target_tiles:
                    publisher.publish(UseSkillEvent(ent, skill_name, target_tiles))
                else:
                    # no suitable targets
                    publisher.publish(MessageEvent(MessageType.LOG, "I can't do that there!"))
                    # TODO - change to an informational, on screen message.

        else:
            # not player and no target
            # TODO - ai approach
            pass

        # log/inform lack of affordability
        if not can_afford:
            # is it the player that can't afford it?
            if ent == player:
                publisher.publish(MessageEvent(MessageType.LOG, "I cannot afford to do that."))
            else:
                name = existence.get_name(ent)
                logging.warning(f"'{name}' tried to use {skill_name}, which they can`t afford.")

        # log/inform on cooldown
        if not not_on_cooldown:
            # is it the player that's can't afford it?
            if ent == player:
                publisher.publish(MessageEvent(MessageType.LOG, "I'm not ready to do that, yet."))
            else:
                name = existence.get_name(ent)
                logging.warning(f"'{name}' tried to use {skill_name}, but needs to wait {cooldown} more rounds.")

    @staticmethod
    def _process_use_skill(event: UseSkillEvent):
        """
        Process the entity`s use of a skill. Tests affordability and pays resource cost. Creates a projectile to
        carry the skill.
        """
        ent = event.entity
        name = existence.get_name(ent)
        skill_name = event.skill_name
        skill_data = library.get_skill_data(skill_name)

        # pay then use the skill
        act.pay_resource_cost(ent, skill_data.resource_type, skill_data.resource_cost)
        act.use_skill(ent, skill_name, event.target_tiles)

        logging.debug(f"'{name}' used {skill_name} on .")

        # update the cooldown
        knowledge = existence.get_entitys_component(ent, Knowledge)
        knowledge.skills[skill_name].cooldown = skill_data.cooldown  # TODO - modify by entity's stats

        # end the turn if the entity is the turn holder
        if ent == chapter.get_turn_holder():
            publisher.publish(EndTurnEvent(ent, skill_data.time_cost))

    @staticmethod
    def _process_die(event: DieEvent):
        """
        Control the entity death
        """
        ent = event.entity
        turn_queue = chapter.get_turn_queue()

        # if  not player
        # TODO add player death
        if ent != existence.get_player():
            # if turn holder create new queue without them
            if ent == chapter.get_turn_holder():
                chapter.rebuild_turn_queue(ent)
            elif ent in turn_queue:
                # remove from turn queue
                turn_queue.pop(ent)

            # delete from world
            existence.delete(ent)
        else:
            publisher.publish(MessageEvent(MessageType.LOG, "I should have died just then."))

    @staticmethod
    def _process_end_turn(event: EndTurnEvent):
        """
        Have entity spend their time
        """
        #  update turn holder`s time spent
        existence.spend_time(event.entity, event.time_spent)

    @staticmethod
    def _process_end_round(event: EndRoundEvent):
        """
        Reduce cooldowns and durations
        """
        # skill cooldowns
        for ent, (knowledge, ) in existence.get_components([Knowledge]):
            for skill_name, skill in knowledge.skills.items():
                if skill.cooldown > 0:
                    knowledge.skills[skill_name].cooldown = skill.cooldown - 1

        # affliction durations
        for ent, (afflictions, ) in existence.get_components([Afflictions]):
            for affliction, duration in afflictions.items():
                if duration - 1 <= 0:
                    # expired
                    # TODO - create expiry event.
                    del afflictions[affliction]

                elif duration != INFINITE:
                    # reduce duration if not infinite
                    afflictions[affliction] = duration - 1

