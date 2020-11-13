from __future__ import annotations

from typing import Type

import pygame

from scripts.engine import utility, world
from scripts.engine.component import Position
from scripts.engine.core import queries
from scripts.engine.core.constants import GameEvent, InteractionEvent

__all__ = ["process_event"]


def process_event(event: pygame.event):
    """
    Passes an interaction event to the right function.
    """
    if event.type == InteractionEvent.MOVEMENT:
        # print(f"Caught MOVE: {event.origin}, {event.target}, {event.direction}, {event.new_pos}")
        _check_for_proximity(event)
        _process_win_condition(event)


############################ MOVEMENT ########################

def _check_for_proximity(event: pygame.event):
    """
    Check for any entities with a reaction to proximity and trigger that reaction.
    """

    new_x = event.new_pos[0]
    new_y = event.new_pos[1]

    # loop all entities sharing same position that have a reaction
    for entity, (position, reaction) in queries.position_and_reaction:
        if position.x == new_x and position.y == new_y:
            if "proximity" in reaction.reactions:
                data = reaction.reactions["proximity"]
                effect = world.create_effect(event.origin, event.target, data)
                effect.evaluate()
                # FIXME - wrong tags when trying to apply affect - other_entity



def _process_win_condition(event: pygame.event):
    """
    Checking if the win condition has been met. Post event if it is.
    """
    player = world.get_player()

    # only progress if its the player as only the player can win
    if not player == event.target:
        return

    player_pos = world.get_entitys_component(player, Position)

    for entity, (position, _) in queries.position_and_win_condition:
        if player_pos.x == position.x and player_pos.y == position.y:
            event = pygame.event.Event(GameEvent.WIN_CONDITION_MET)
            pygame.event.post(event)
            break


def _process_interventions(event: pygame.event):
    """
    Consider taking possible interventions and then take them.
    """
    # TODO - update in line with judge_actions to use skills
    # TODO - reactivate the interventions
    pass

    # skill_name = event.skill_name
    # entity = event.entity
    # position = world.get_entitys_component(entity, Position)
    # interventions = world.choose_interventions(entity, skill_name)
    #
    # for god_entity_id, intervention_name in interventions:
    #     # create use skill event with direction of centre
    #     if world.can_use_skill(god_entity_id, intervention_name):
    #         skill = world.get_known_skill(god_entity_id, intervention_name)
    #         tile = world.get_tile((position.x, position.y))
    #         world.use_skill(god_entity_id, skill, tile, Direction.CENTRE)
