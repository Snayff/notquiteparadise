import logging
from typing import Dict, Tuple

from scripts.core.constants import GameStates
from scripts.events.game_events import ChangeGameStateEvent, EndRoundEvent
from scripts.global_singletons.event_hub import publisher
from scripts.world.entity import Entity


class TurnManager:
    """
    Manager of turns functions.
    """
    # TODO What do we need from the turn queue?
    #  Add all entities that are within X range of the player;
    #  Add new entities to the queue as they get into range;
    #  Amend an entities position in the queue;
    #  Keep track of rounds;

    def __init__(self):
        self.turn_holder = None  # type: Entity
        self.turn_queue = {}  # type: Dict[Tuple[Entity, int]] # (entity, time)
        self.round = 0  # count of the round
        self.time = 0  # total time of actions taken
        self.time_of_last_turn = 0
        self.time_in_round = 100  # time units in a round
        self.round_time = 0  # tracker of time progressed in current round

        # Note: Can't build turn queue here as dependencies are not loaded (e.g. entities)

        logging.info(f"TurnManager initialised.")

    def build_new_turn_queue(self):
        """
        Build a new turn queue for all entities
        """
        logging.info(f"Building a new turn queue...")

        # create a turn queue from the entities list
        from scripts.global_singletons.managers import world
        entities = world.Entity.get_all_entities()

        for entity in entities:
            if entity.ai or entity == world.player:
                self.turn_queue[entity] = entity.actor.time_of_next_action

        # get the next entity in the queue
        self.turn_holder = min(self.turn_queue, key=self.turn_queue.get)

        # log result
        queue = []
        for entity, time in self.turn_queue.items():
            queue.append((entity.name, time))

        logging.debug(f"-> Queue built. {queue}")

    def end_turn(self, spent_time):
        """
        End the current turn and apply time spent

        Args:
            spent_time:
        """
        logging.debug(f"Ending {self.turn_holder.name}`s turn...")

        entity = self.turn_holder

        #  update actor`s time spent
        entity.actor.spend_time(spent_time)

    def next_turn(self):
        """
        Proceed to the next turn, setting the next entity to act as the turn holder.
        """
        logging.info(f"Moving to the next turn...")

        if not self.turn_queue:
            self.build_new_turn_queue()

        # update turn holders time of next action
        self.turn_queue[self.turn_holder] = self.turn_holder.actor.time_of_next_action

        # get the next entity in the queue
        self.turn_holder = min(self.turn_queue, key=self.turn_queue.get)

        # update time using last action and when new turn holder can act
        time_progressed = self.turn_holder.actor.time_of_next_action - self.time_of_last_turn
        self.time += time_progressed
        self.time_of_last_turn = self.time

        # check if we need to set new round
        if self.round_time + time_progressed > self.time_in_round:
            self.next_round(time_progressed)
        else:
            self.round_time += time_progressed

        logging.debug(f"-> It is now '{self.turn_holder.name}'`s turn.")

    def next_round(self, time_progressed):
        """
        Move to the next round and trigger end of round events

        Args:
            time_progressed (int):
        """
        # trigger end of round actions
        publisher.publish(EndRoundEvent())

        # add progressed time and minus time_in_round to keep the remaining time
        self.round_time = (self.round_time + time_progressed) - self.time_in_round

        # increment rounds
        self.round += 1

        logging.debug(f"It is now round {self.round}.")