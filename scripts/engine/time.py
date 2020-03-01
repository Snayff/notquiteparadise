from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from scripts.engine import entity
from scripts.engine.components import Resources, Identity
from scripts.engine.core.constants import TIME_PER_ROUND
from scripts.engine.core.event_core import publisher
from scripts.engine.core.store import store
from scripts.engine.events import EndRoundEvent

if TYPE_CHECKING:
    from typing import Dict, Tuple


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

    # TODO - convert access to store to get or set
    # get the next entity in the queue
    new_turn_holder = min(store.turn_queue, key=store.turn_queue.get)
    store.turn_holder = new_turn_holder

    # log result
    queue = []
    get_identity = entity.get_identity
    for ent, time in get_turn_queue().items():
        identity = get_identity(ent)
        if identity:
            queue.append((identity.name, time))

    logging.debug(f"-> Queue built. {queue}")


def next_turn():
    """
    Proceed to the next turn, setting the next entity to act as the turn holder.
    """
    logging.debug(f"Moving to the next turn...")

    if not store.turn_queue:
        build_new_turn_queue()

    # get the next entity in the queue
    new_turn_holder = min(store.turn_queue, key=store.turn_queue.get)
    store.turn_holder = new_turn_holder

    # update time using last action and when new turn holder can act
    resources = entity.get_entitys_component(new_turn_holder, Resources)
    time_progressed = resources.time_spent - store.time_of_last_turn
    store.time += time_progressed
    store.time_of_last_turn = get_time()

    # check if we need to set new round
    if get_time_in_round() + time_progressed > TIME_PER_ROUND:
        next_round(time_progressed)
    else:
        set_time_in_round(get_time_in_round() + time_progressed)

    # log result
    identity = entity.get_entitys_component(new_turn_holder, Identity)
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

    logging.info(f"It is now _round {store.round}.")


def increment_round():
    """
    Increment the round by 1
    """
    store.round += 1


############# GET ###################

def get_turn_holder() -> int:
    """
    Get the entity who has the current turn
    """
    return store.turn_holder


def get_turn_queue() -> Dict[Tuple[int, int]]:
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
