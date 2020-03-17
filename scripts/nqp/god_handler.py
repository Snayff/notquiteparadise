from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.engine import entity
from scripts.engine.core.constants import Effect, Direction
from scripts.engine.core.event_core import Subscriber, publisher
from scripts.engine.library import library

from scripts.engine.component import Position, IsGod
from scripts.engine.event import UseSkillEvent

if TYPE_CHECKING:
    pass


class GodHandler(Subscriber):
    """
    Handle events affecting entities
    """

    def __init__(self, event_hub):
        Subscriber.__init__(self, "god_handler", event_hub)

    def process_event(self, event):
        """
        Control god actions from events

        Args:
            event(Event): the event in need of processing
        """
        # TODO -
        #  create events for receiving afflictions
        #  create events for receiving damage types
        #  create events for causing and receiving hit type
        #  create events for being the cause of death

        # log that event has been received
        logging.debug(f"{self.name} received {event.__class__.__name__}...")

        if isinstance(event, UseSkillEvent):
            event: UseSkillEvent
            # if the entity isnt another god then judge it
            if not entity.has_component(event.entity, IsGod):
                self.process_judgements(event)
                self.process_interventions(event)

    @staticmethod
    def process_judgements(event):
        """
        Pass any actions taken to be judged by the gods.

        Args:
            event ():
        """
        skill_name = event.skill_name
        ent = event.entity
        skill_data = library.get_skill_data(skill_name)

        # check effect types used
        for effect_name, effect_data in skill_data.effects.items():
            entity.judge_action(ent, effect_data.effect_type)

        # check damage type used
        if Effect.DAMAGE in skill_data.effects:
            damage_type = skill_data.effects[Effect.DAMAGE].damage_type
            entity.judge_action(ent, damage_type)

        # check afflictions applied
        if Effect.APPLY_AFFLICTION in skill_data.effects:
            affliction_name = skill_data.effects[Effect.APPLY_AFFLICTION].affliction_name
            entity.judge_action(ent, affliction_name)

    @staticmethod
    def process_interventions(event):
        """
        Consider taking possible interventions and then take them.

        Args:
            event ():
        """
        skill_name = event.skill_name
        ent = event.entity
        position = entity.get_entitys_component(ent, Position)

        interventions = entity.consider_intervening(ent, skill_name)

        for god_entity_id, intervention_name in interventions:
            # create use skill event with direction of centre
            # N.B. 0 time cost because god's dont spend time
            publisher.publish(UseSkillEvent(god_entity_id, intervention_name, (position.x, position.y),
                                            Direction.CENTRE, 0))


