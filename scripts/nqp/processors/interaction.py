from __future__ import annotations

import pygame
from snecs.typedefs import EntityID

from scripts.engine.core import query, world
from scripts.engine.internal.component import Afflictions, Position, Reaction
from scripts.engine.internal.constant import GameEvent, InteractionEvent, InteractionTrigger, InteractionTriggerType

__all__ = ["process_event"]


def process_event(event: pygame.event):
    """
    Passes an interaction event to the right function.
    """
    if event.type == InteractionEvent.MOVE:
        # print(f"Caught MOVE: {event.origin}, {event.target}, {event.direction}, {event.new_pos}")
        _handle_proximity(event)
        _handle_affliction(event.target, InteractionTrigger.MOVE)
        _process_win_condition(event)

    elif event.type == InteractionEvent.DAMAGE:
        # print(f"Caught DAMAGE: {event.origin}, {event.target}, {event.amount}, {event.damage_type},
        # {event.remaining_hp}")
        _handle_affliction(event.origin, InteractionTrigger.DEAL_DAMAGE)
        _handle_affliction(event.target, InteractionTrigger.TAKE_DAMAGE)

        if event.remaining_hp <= 0:
            _handle_affliction(event.origin, InteractionTrigger.KILL)
            _handle_affliction(event.target, InteractionTrigger.DIE)

    elif event.type == InteractionEvent.AFFECT_STAT:
        # print(f"Caught AFFECT_STAT: {event.origin}, {event.target}, {event.stat}, {event.amount}")
        _handle_affliction(event.origin, InteractionTrigger.CAUSED_AFFECT_STAT)
        _handle_affliction(event.target, InteractionTrigger.AFFECTED_STAT)

    elif event.type == InteractionEvent.AFFECT_COOLDOWN:
        # print(f"Caught AFFECT_COOLDOWN: {event.origin}, {event.target}, {event.amount}")
        _handle_affliction(event.origin, InteractionTrigger.CAUSED_AFFECT_COOLDOWN)
        _handle_affliction(event.target, InteractionTrigger.AFFECTED_COOLDOWN)

    elif event.type == InteractionEvent.AFFLICTION:
        # print(f"Caught AFFLICTION: {event.origin}, {event.target}, {event.name}")
        _handle_affliction(event.origin, InteractionTrigger.CAUSED_AFFLICTION)
        _handle_affliction(event.target, InteractionTrigger.AFFLICTED)


############################ MOVEMENT ########################


def _handle_proximity(event: pygame.event):
    """
    Check for any entities with a reaction to proximity and trigger that reaction.
    """
    new_x = event.new_pos[0]
    new_y = event.new_pos[1]

    # loop all entities sharing same position that have a reaction
    for entity, (position, reaction) in query.position_and_reaction:
        assert isinstance(position, Position)
        assert isinstance(reaction, Reaction)
        if position.x == new_x and position.y == new_y:
            if InteractionTrigger.PROXIMITY in reaction.reactions:
                data = reaction.reactions[InteractionTrigger.PROXIMITY]
                effect = world.create_effect(event.origin, event.target, data)
                effect.evaluate()


def _process_win_condition(event: pygame.event):
    """
    Checking if the win condition has been met. Post event if it is.
    """
    player = world.get_player()

    # only progress if its the player as only the player can win
    if not player == event.target:
        return

    player_pos = world.get_entitys_component(player, Position)

    for entity, (position, _) in query.position_and_win_condition:
        assert isinstance(position, Position)
        if player_pos.x == position.x and player_pos.y == position.y:
            event = pygame.event.Event(GameEvent.WIN_CONDITION_MET)
            pygame.event.post(event)
            break


############################ GENERIC ########################


def _handle_affliction(entity: EntityID, interaction_trigger: InteractionTriggerType):
    """
    Check for any afflictions triggered by the interaction and trigger them.
    """
    if world.entity_has_component(entity, Afflictions):
        afflictions = world.get_entitys_component(entity, Afflictions)
        for affliction in afflictions.active:
            if interaction_trigger in affliction.triggers:
                world.trigger_affliction(affliction)


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
