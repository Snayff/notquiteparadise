from __future__ import annotations

import logging
from typing import TYPE_CHECKING, cast
from scripts.engine import world, chapter,  state
from scripts.engine.core.constants import MessageType, GameState, TargetingMethod
from scripts.engine.event import MessageEvent, WantToUseSkillEvent, UseSkillEvent, DieEvent, \
    ChangeGameStateEvent, EndRoundEvent
from scripts.engine.core.event_core import publisher, Subscriber
from scripts.engine.component import Knowledge

if TYPE_CHECKING:
    pass


class EntityHandler(Subscriber):
    """
    Handle events affecting entities
    """
    def __init__(self, event_hub):
        super().__init__("entity_handler", event_hub)

    def process_event(self, event):
        """
        Control entity events
        """
        if isinstance(event, UseSkillEvent):
            self._process_use_skill(event)

        elif isinstance(event, DieEvent):
            self._process_die(event)

        elif isinstance(event, WantToUseSkillEvent):
            self._process_want_to_use_skill(event)

        elif isinstance(event, EndRoundEvent):
            self._process_end_round(event)

    @staticmethod
    def _process_want_to_use_skill(event: WantToUseSkillEvent):
        """
        Process the desire to use a skill.
        """
        player = world.get_player()
        entity = event.entity
        start_x, start_y = event.start_pos
        direction = event.direction
        skill_name = event.skill_name
        skill = world.get_known_skill(entity, skill_name)

        # flags
        got_target = can_afford = not_on_cooldown = False

        # if we dont have skill we cant do anything
        if not skill:
            logging.warning(f"'{world.get_name(entity)}' tried to use {skill_name} but doesnt know it.")
            return None

        # complete initial checks
        targeting = skill.targeting_method
        if targeting == TargetingMethod.AUTO or (targeting == TargetingMethod.TARGET and direction):
            got_target = True

        can_afford = world.can_afford_cost(entity, skill.resource_type, skill.resource_cost)

        knowledge = world.get_entitys_component(entity, Knowledge)
        cooldown = knowledge.skills[skill_name]["cooldown"]
        if cooldown <= 0:
            not_on_cooldown = True

        # if its the player wanting to use their skill but we dont have a target direction
        if player and player == entity and not got_target:
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

        elif got_target and direction:
            # we have a direction, let's see if we can use the skill
            if can_afford and not_on_cooldown:
                target_tile = world.get_tile((start_x + direction[0], start_y + direction[1]))

                # we have someone to target, let's go
                if target_tile:
                    # is it the right target?
                    if world.tile_has_tags(target_tile, skill.required_tags, entity):
                        publisher.publish(UseSkillEvent(entity, skill_name, target_tile, direction))

                    else:
                        # no suitable targets
                        publisher.publish(MessageEvent(MessageType.LOG, "I can't do that there!"))
                        # TODO - change to an informational, on screen message.
                else:
                    logging.warning(f"Targeted ({start_x},{start_y}) which is not a valid tile.")

        else:
            # not player and no target
            # TODO - ai approach
            pass

        # log/inform lack of affordability
        if not can_afford:
            # is it the player that can't afford it?
            if entity == player:
                publisher.publish(MessageEvent(MessageType.LOG, "I cannot afford to do that."))
            else:
                name = world.get_name(entity)
                logging.warning(f"'{name}' tried to use {skill_name}, which they can`t afford.")

        # log/inform on cooldown
        if not not_on_cooldown:
            # is it the player that's can't afford it?
            if entity == player:
                publisher.publish(MessageEvent(MessageType.LOG, "I'm not ready to do that, yet."))
            else:
                name = world.get_name(entity)
                logging.warning(f"'{name}' tried to use {skill_name}, but needs to wait {cooldown} more rounds.")

    @staticmethod
    def _process_use_skill(event: UseSkillEvent):
        """
        Process the entity`s use of a skill. Tests affordability and pays resource cost. Creates a projectile to
        carry the skill.
        """
        entity = event.entity
        skill = world.get_known_skill(entity, event.skill_name)
        if skill:
            # pay then use the skill
            world.pay_resource_cost(entity, skill.resource_type, skill.resource_cost)
            world.use_skill(entity, skill, event.target_tile)

            # update the cooldown
            knowledge = world.get_entitys_component(entity, Knowledge)
            if knowledge:
                knowledge.skills[event.skill_name]["cooldown"] = skill.base_cooldown
            # TODO - modify by entity's stats - perhaps move to a func to ensure always uses entities mod

            # end the turn if the entity is the turn holder
            if entity == chapter.get_turn_holder():
                world.end_turn(entity, skill.time_cost)

    @staticmethod
    def _process_die(event: DieEvent):
        """
        Control the entity death
        """
        entity = event.entity
        turn_queue = chapter.get_turn_queue()

        # if  not player
        # TODO add player death
        if entity != world.get_player():
            # if turn holder create new queue without them
            if entity == chapter.get_turn_holder():
                chapter.rebuild_turn_queue(entity)
                # ensure the game state reflects the new queue
                publisher.publish(ChangeGameStateEvent(GameState.NEW_TURN))
            elif entity in turn_queue:
                # remove from turn queue
                turn_queue.pop(entity)

            # delete from world
            world.delete(entity)
        else:
            publisher.publish(MessageEvent(MessageType.LOG, "I should have died just then."))


    @staticmethod
    def _process_end_round(event: EndRoundEvent):
        """
        Reduce cooldowns and durations
        """
        # skill cooldowns
        for entity, (knowledge, ) in world.get_components([Knowledge]):
            knowledge = cast(Knowledge, knowledge)
            for skill_name, skill_dict in knowledge.skills.items():
                if skill_dict["cooldown"] > 0:
                    knowledge.skills[skill_name]["cooldown"] = skill_dict["cooldown"] - 1

        # # affliction durations
        # for entity, (afflictions, ) in existence.get_components([Afflictions]):
        #     for affliction, duration in afflictions.items():
        #         if duration - 1 <= 0:
        #             # expired
        #             # TODO - create expiry event.
        #             del afflictions[affliction]
        #
        #         elif duration != INFINITE:
        #             # reduce duration if not infinite
        #             afflictions[affliction] = duration - 1

