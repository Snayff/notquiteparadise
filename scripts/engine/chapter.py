from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from snecs.typedefs import EntityID
from scripts.engine import existence
from scripts.engine.component import Resources, Identity, Tracked
from scripts.engine.core.constants import TIME_PER_ROUND
from scripts.engine.core.event_core import publisher
from scripts.engine.core.store import store
from scripts.engine.event import EndRoundEvent

if TYPE_CHECKING:
    from typing import Dict, Tuple, List, Optional

# TODO What do we need from the turn queue?
#  Add all entities that are within X range of the player;
#  Add new entities to the queue as they get into range;
#  Function to amend an entities position in the queue;


############ ACTIONS ##################

def rebuild_turn_queue(entity_to_exclude: Optional[EntityID] = None):
    """
    Build a new turn queue that includes all timed entities. entity_to_exclude is one that should not be added
    to the queue. Usually used in relation to deletion.
    """
    logging.debug(f"Building a new turn queue...")

    get_component = existence.get_components

    # create a turn queue from the entities list
    new_queue = {}
    for entity, (tracked, ) in get_component([Tracked]):
        if entity != entity_to_exclude:
            new_queue[entity] = tracked.time_spent
    set_turn_queue(new_queue)

    # get the next entity in the queue and set as new turn holder
    set_turn_holder(_get_next_entity_in_queue())

    # log result
    logging.debug(f"-> New queue built: {_get_pretty_queue()}")


def next_turn():
    """
    Proceed to the next turn, setting the next entity to act as the turn holder and updating the passage of time.
    """
    logging.info(f"Moving to the next turn...")

    # update the queue
    rebuild_turn_queue()

    # get next entity in queue
    turn_holder = get_turn_holder()

    # whats the difference between current time and when they last acted?
    next_entity_time = existence.get_entitys_component(turn_holder, Tracked).time_spent
    time_progressed = next_entity_time - get_time_of_last_turn()

    # add the difference to the time
    add_time(time_progressed)
    set_time_of_last_turn(get_time())

    # check if we need to set new round
    if get_time_in_round() + time_progressed >= TIME_PER_ROUND:
        next_round(time_progressed)
    else:
        set_time_in_round(get_time_in_round() + time_progressed)

    # log new turn holder
    name = existence.get_name(turn_holder)
    logging.debug(f"-> Current time is {get_time()}. We are {get_time_in_round()} TU`s into round {get_round()}.")
    logging.debug(f"-> It is now '{name}'s turn.")


def next_round(time_progressed: int):
    """
    Move to the next round and trigger end of round events
    """
    # trigger end of round actions
    publisher.publish(EndRoundEvent())

    # add progressed time and minus time_in_round to keep the remaining time
    set_time_in_round((get_time_in_round() + time_progressed) - TIME_PER_ROUND)

    # increment rounds
    increment_round()

    logging.info(f"It is now _round {get_round()}.")


def increment_round():
    """
    Increment the round by 1
    """
    store.round += 1


def add_time(time_to_add: int):
    """
    Add to the current time
    """
    store.time += time_to_add


############# GET ###################

def get_turn_holder() -> int:
    """
    Get the entity who has the current turn
    """
    return store.turn_holder


def get_turn_queue() -> Dict[int, int]:
    """
    Get the turn queue
    """
    return store.turn_queue


def get_time_in_round() -> int:
    """
    Get current time in the current round
    """
    return store.round_time


def get_time() -> int:
    """
    Get the current time
    """
    return store.time


def get_time_of_last_turn() -> int:
    """
    Get the time of the last turn
    """
    return store.time_of_last_turn


def get_round() -> int:
    """
    Get the current round
    """
    return store.round


def _get_pretty_queue() -> List[Tuple[str, int]]:
    queue = []
    for entity, time in get_turn_queue().items():
        name = existence.get_name(entity)
        queue.append((name, time))
    return queue


def _get_next_entity_in_queue() -> int:
    queue = get_turn_queue()
    next_entity = min(queue, key=queue.get)
    return next_entity


############# SET ###################

def set_turn_holder(active_entity: int):
    """
    Get the entity who has the current turn
    """
    store.turn_holder = active_entity


def set_time_in_round(time: int):
    """
    Set current time in the current round
    """
    store.round_time = time


def set_turn_queue(queue: Dict[int, int]):
    """
    Set the turn queue
    """
    store.turn_queue = queue


def set_time_of_last_turn(time: int):
    """
    Set the time of the last turn
    """
    store.time_of_last_turn = time


