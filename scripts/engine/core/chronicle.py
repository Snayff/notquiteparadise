from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from snecs.typedefs import EntityID

from scripts.engine.core import query, system, world
from scripts.engine.internal import library
from scripts.engine.internal.component import Tracked
from scripts.engine.internal.data import store

if TYPE_CHECKING:
    from typing import Dict, List, Optional, Tuple


############ ACTIONS ##################


def rebuild_turn_queue(entity_to_exclude: Optional[EntityID] = None):
    """
    Build a new turn queue that includes all timed entities. entity_to_exclude is one that should not be added
    to the queue. Usually used in relation to deletion.
    """
    logging.debug(f"Building a new turn queue...")

    # create a turn queue from the entities list
    new_queue = {}

    for entity, (
        is_active,
        tracked,
    ) in query.active_and_tracked:
        if entity != entity_to_exclude:
            assert isinstance(tracked, Tracked)
            new_queue[entity] = tracked.time_spent

    # did we actually allocate to anyone?
    if not new_queue:
        # add player to queue
        new_queue[world.get_player()] = get_time()

    set_turn_queue(new_queue)

    # get the next entity in the queue and set as new turn holder
    set_turn_holder(_get_next_entity_in_queue())

    # log result
    logging.debug(f"-> New queue built: {_get_pretty_queue()}")


def next_turn(entity_to_exclude: Optional[EntityID] = None):
    """
    Proceed to the next turn, setting the next entity to act as the turn holder and updating the passage of time.
    Update game state to reflect turn holder.
    """
    logging.info(f"Moving to the next turn...")

    # update the queue
    rebuild_turn_queue(entity_to_exclude)

    # get next entity in queue
    turn_holder = get_turn_holder()

    # whats the difference between current time and when they last acted?
    tracked = world.get_entitys_component(turn_holder, Tracked)
    if tracked:
        next_entity_time = tracked.time_spent
    else:
        next_entity_time = get_time_of_last_turn()  # turn holder should always have Tracked but handle if they dont

    time_progressed = next_entity_time - get_time_of_last_turn()

    # add the difference to the time
    _add_time(time_progressed)
    set_time_of_last_turn(get_time())

    # check if we need to set new round
    if get_time_in_round() + time_progressed >= library.GAME_CONFIG.default_values.time_per_round:
        next_round(time_progressed)
    else:
        set_time_in_round(get_time_in_round() + time_progressed)

    # update visibility
    # TODO - implement scheduling so this doesnt need to be called here
    system.process_activations()  # must be first otherwise wrong entities active
    system.process_light_map()
    system.process_fov()
    system.process_tile_visibility()

    # log new turn holder
    name = world.get_name(turn_holder)
    logging.debug(f"-> Current time is {get_time()}. We are {get_time_in_round()} TU`s into round {get_round()}.")
    logging.debug(f"-> '{name}' is now the turn holder.")


def next_round(time_progressed: int):
    """
    Move to the next round and trigger end of round events, like cooldown and affliction reduction.
    """
    # TODO - create end of round event and handle there.
    system.reduce_skill_cooldowns()
    system.reduce_affliction_durations()
    system.reduce_lifespan_durations()

    # add progressed time and minus time_in_round to keep the remaining time
    set_time_in_round((get_time_in_round() + time_progressed) - library.GAME_CONFIG.default_values.time_per_round)

    # increment rounds
    _increment_round_number()

    logging.info(f"It is now round {get_round()}.")


def _increment_round_number():
    """
    Increment the round by 1
    """
    store.round += 1


def _add_time(time_to_add: int):
    """
    Add to the current time
    """
    store.time += time_to_add


############# GET ###################


def get_turn_holder() -> EntityID:
    """
    Get the entity who has the current turn
    """
    return store.turn_holder


def get_turn_queue() -> Dict[EntityID, int]:
    """
    Get the turn queue
    """
    return store.turn_queue


def get_time_in_round() -> int:
    """
    Get current time in the current round
    """
    # FIXME - returning negative value for projectiles
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
        name = world.get_name(entity)
        queue.append((name, time))
    return queue


def _get_next_entity_in_queue() -> EntityID:
    queue = get_turn_queue()
    next_entity = min(queue, key=queue.get)  # type: ignore
    return next_entity


############# SET ###################


def set_turn_holder(active_entity: EntityID):
    """
    Get the entity who has the current turn
    """
    store.turn_holder = active_entity


def set_time_in_round(time: int):
    """
    Set current time in the current round
    """
    store.round_time = time


def set_turn_queue(queue: Dict[EntityID, int]):
    """
    Set the turn queue
    """
    store.turn_queue = queue


def set_time_of_last_turn(time: int):
    """
    Set the time of the last turn
    """
    store.time_of_last_turn = time


def end_turn(entity: EntityID, time_spent: int):
    """
    Spend an entities time, progress time, move to next acting entity in queue.
    """
    if entity == get_turn_holder():
        world.spend_time(entity, time_spent)
        next_turn()
    else:
        logging.warning(f"Tried to end {world.get_name(entity)}'s turn but they're not turn holder.")
