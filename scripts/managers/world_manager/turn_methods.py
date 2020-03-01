from __future__ import annotations

import logging

from typing import TYPE_CHECKING
from scripts.engine.events import EndRoundEvent
from scripts.engine.core.event_core import publisher
from scripts.engine.components import Resources, Identity

if TYPE_CHECKING:
    from typing import Dict, Tuple
    from scripts.managers.world_manager.world_manager import WorldManager


class TurnMethods:
    """
    Manager of turns functions.
    """
    # TODO What do we need from the turn queue?
    #  Add all entities that are within X range of the player;
    #  Add new entities to the queue as they get into range;
    #  Amend an entities position in the queue;
    #  Keep track of rounds;

    def __init__(self, manager):
        self._manager: WorldManager = manager
        self._turn_queue: Dict[Tuple[int, int]] = {}  # (entity, time)
        self._round: int = 1  # count of the round
        self._time: int = 1  # total time of actions taken
        self._time_of_last_turn: int = 1
        self._time_in_round: int = 100  # time units in a round
        self._round_time: int = 0  # tracker of time progressed in current round
        self._turn_holder: int = None  # current acting entity

    ############ ACTIONS ##################

    def build_new_turn_queue(self):
        """
        Build a new turn queue for all entities
        """
        logging.debug(f"Building a new turn queue...")

        get_component = self._manager.Entity.get_component
        get_identity = self._manager.Entity.get_identity

        # create a turn queue from the entities list
        for entity, resource in get_component(Resources):
            self._turn_queue[entity] = resource.time_spent

        # get the next entity in the queue
        new_turn_holder = min(self._turn_queue, key=self._turn_queue.get)
        self._turn_holder = new_turn_holder

        # log result
        queue = []
        for entity, time in self._turn_queue.items():
            identity = get_identity(entity)
            if identity:
                queue.append((identity.name, time))

        logging.debug(f"-> Queue built. {queue}")

    def next_turn(self):
        """
        Proceed to the next turn, setting the next entity to act as the turn holder.
        """
        logging.debug(f"Moving to the next turn...")

        if not self._turn_queue:
            self.build_new_turn_queue()

        # get the next entity in the queue
        new_turn_holder = min(self._turn_queue, key=self._turn_queue.get)
        self._turn_holder = new_turn_holder

        # update time using last action and when new turn holder can act
        resources = self._manager.Entity.get_entitys_component(new_turn_holder, Resources)
        time_progressed = resources.time_spent - self._time_of_last_turn
        self._time += time_progressed
        self._time_of_last_turn = self._time

        # check if we need to set new round
        if self._round_time + time_progressed > self._time_in_round:
            self.next_round(time_progressed)
        else:
            self._round_time += time_progressed

        # log result
        identity = self._manager.Entity.get_entitys_component(new_turn_holder, Identity)
        if identity:
            name = identity.name
        else:
            name = "(not found!)"
        logging.debug(f"-> It is now '{name}'`s turn.")

    def next_round(self, time_progressed):
        """
        Move to the next round and trigger end of round events

        Args:
            time_progressed (int):
        """
        # trigger end of round actions
        publisher.publish(EndRoundEvent())

        # add progressed time and minus time_in_round to keep the remaining time
        self._round_time = (self._round_time + time_progressed) - self._time_in_round

        # increment rounds
        self._round += 1

        logging.info(f"It is now _round {self._round}.")

    ############# GET ###################

    def get_turn_holder(self) -> int:
        """
        Get the entity who has the current turn
        """
        return self._turn_holder

    def get_turn_queue(self) -> Dict[Tuple[int, int]]:
        """
        Get the turn queue
        """
        return self._turn_queue

    ############# SET ###################

    def set_turn_holder(self, entity: int):
        """
        Get the entity who has the current turn
        """
        self._turn_holder = entity
