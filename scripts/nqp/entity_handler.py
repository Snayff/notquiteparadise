from __future__ import annotations

from typing import TYPE_CHECKING, cast
from scripts.engine import world, chapter
from scripts.engine.core.constants import MessageType, GameState
from scripts.engine.event import MessageEvent, UseSkillEvent, DieEvent, \
    EndRoundEvent
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

        elif isinstance(event, EndRoundEvent):
            self._process_end_round(event)

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

