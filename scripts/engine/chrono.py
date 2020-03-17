from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from scripts.engine import entity
from scripts.engine.component import Resources, Identity
from scripts.engine.core.constants import TIME_PER_ROUND
from scripts.engine.core.event_core import publisher
from scripts.engine.core.store import store
from scripts.engine.event import EndRoundEvent

if TYPE_CHECKING:
    from typing import Dict

# TODO What do we need from the turn queue?
#  Add all entities that are within X range of the player;
#  Add new entities to the queue as they get into range;
#  Amend an entities position in the queue;


############ ACTIONS ##################

def build_new_turn_queue():
    """
    Build a new turn queue for all entities
    """
    logging.debug(f"Building a new turn queue...")

    get_component = entity.get_component

    # create a turn queue from the entities list
    new_queue = {}
    for ent, resource in get_component(Resources):
        new_queue[ent] = resource.time_spent
    set_turn_queue(new_queue)

    # get the next entity in the queue
    turn_queue = get_turn_queue()
    new_turn_holder = min(turn_queue, key=turn_queue.get)
    set_turn_holder(new_turn_holder)

    # log result
    queue = []
    for ent, time in get_turn_queue().items():
        name = entity.get_name(ent)
        queue.append((name, time))

    logging.debug(f"-> Queue built. {queue}")


def next_turn():
    """
    Proceed to the next turn, setting the next entity to act as the turn holder.
    """
    logging.info(f"Moving to the next turn...")

    if not store.turn_queue:
        build_new_turn_queue()

    turn_holder = get_turn_holder()

    # update time using last action and when new turn holder can act
    resources = entity.get_entitys_component(turn_holder, Resources)
    time_progressed = resources.time_spent - get_time_of_last_turn()
    add_time(time_progressed)
    set_time_of_last_turn(get_time())

    # check if we need to set new round
    if get_time_in_round() + time_progressed > TIME_PER_ROUND:
        next_round(time_progressed)
    else:
        set_time_in_round(get_time_in_round() + time_progressed)

    # log result
    identity = entity.get_entitys_component(turn_holder, Identity)
    if identity:
        name = identity.name
    else:
        name = "(not found!)"
    logging.debug(f"-> It is now '{name}'`s turn.")


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


