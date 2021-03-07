from __future__ import annotations

import logging
from typing import Optional, Tuple

import pygame
from snecs.typedefs import EntityID

import scripts.engine.core.matter
from scripts.engine.core import query, world
from scripts.engine.core.component import Aesthetic, Afflictions, Opinion, Position, Reaction
from scripts.engine.internal.constant import (
    Direction,
    EventType,
    ReactionTrigger,
    ReactionTriggerType,
    SpriteCategory,
    SpriteCategoryType,
)
from scripts.engine.internal.definition import EffectData, ReactionData
from scripts.engine.internal.event import (
    AffectCooldownEvent,
    AffectStatEvent,
    AfflictionEvent,
    ChangeMapEvent,
    DamageEvent,
    event_hub,
    MoveEvent,
    Subscriber,
    UseSkillEvent,
    WinConditionMetEvent,
)

__all__ = ["InteractionEventSubscriber"]

from scripts.engine.world_objects.tile import Tile


class InteractionEventSubscriber(Subscriber):
    """
    Handle interaction events.
    """

    def __init__(self):
        super().__init__("interaction_subscriber")
        self.subscribe(EventType.INTERACTION)

    def process_event(self, event):

        if isinstance(event, UseSkillEvent):
            # hacky way to prevent Move causing attack animation to play
            if event.skill_name != "Move":
                _set_sprite(event.origin, SpriteCategory.ATTACK)

        elif isinstance(event, MoveEvent):
            _handle_proximity_reaction_trigger(event)
            _process_win_condition(event)
            _process_map_condition(event)

            _handle_reaction_trigger(event.origin, ReactionTrigger.MOVE)
            _handle_reaction_trigger(event.target, ReactionTrigger.MOVED)

            # is it a move other or a move self?
            if event.target == event.origin:
                _set_sprite(event.target, SpriteCategory.MOVE, event.new_pos)
            else:
                _set_sprite(event.target, SpriteCategory.HIT)

        elif isinstance(event, DamageEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.DEAL_DAMAGE)
            _handle_reaction_trigger(event.target, ReactionTrigger.TAKE_DAMAGE)

            if event.remaining_hp <= 0:
                _handle_reaction_trigger(event.origin, ReactionTrigger.KILL)
                _handle_reaction_trigger(event.target, ReactionTrigger.DIE)

                _set_sprite(event.target, SpriteCategory.DEAD)

            else:
                _set_sprite(event.target, SpriteCategory.HIT)

        elif isinstance(event, AffectStatEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFECT_STAT)
            _handle_reaction_trigger(event.target, ReactionTrigger.STAT_AFFECTED)

            _set_sprite(event.target, SpriteCategory.HIT)

        elif isinstance(event, AffectCooldownEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFECT_COOLDOWN)
            _handle_reaction_trigger(event.target, ReactionTrigger.COOLDOWN_AFFECTED)

            _set_sprite(event.target, SpriteCategory.HIT)

        elif isinstance(event, AfflictionEvent):
            _handle_reaction_trigger(event.origin, ReactionTrigger.CAUSED_AFFLICTION)
            _handle_reaction_trigger(event.target, ReactionTrigger.AFFLICTED)

            _set_sprite(event.target, SpriteCategory.HIT)


# interaction_subscriber = InteractionEventSubscriber()


def _process_opinions(causing_entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Adjust opinion of entity for any other entities that have an attitude towards the reaction trigger.
    """
    for entity, (opinion,) in query.opinion:
        assert isinstance(opinion, Opinion)
        if reaction_trigger in opinion.attitudes:
            if causing_entity in opinion.opinions:
                opinion.opinions[causing_entity] += opinion.attitudes[reaction_trigger]
            else:
                opinion.opinions[causing_entity] = opinion.attitudes[reaction_trigger]

            logging.debug(
                f"{scripts.engine.core.matter.get_name(entity)}`s opinion of {scripts.engine.core.matter.get_name(causing_entity)} is now "
                f"{opinion.opinions[causing_entity]} due to {reaction_trigger}."
            )


def _handle_affliction(entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Check for any afflictions triggered by the interaction and trigger that interaction.
    """
    if scripts.engine.core.matter.entity_has_component(entity, Afflictions):
        afflictions = scripts.engine.core.matter.get_entitys_component(entity, Afflictions)
        for affliction in afflictions.active:
            if reaction_trigger in affliction.triggers:
                scripts.engine.core.matter.trigger_affliction(affliction)


def _handle_reaction_trigger(entity: EntityID, reaction_trigger: ReactionTriggerType):
    """
    Check for any entities with a reaction to the trigger and handle that reaction.
    """
    # loop all entities sharing same position that have a reaction
    for reacting_entity, (reaction,) in query.reaction:
        assert isinstance(reaction, Reaction)

        if reaction_trigger in reaction.reactions:
            data = reaction.reactions[reaction_trigger]
            _process_opinions(entity, reaction_trigger)
            _handle_affliction(entity, reaction_trigger)
            _handle_reaction(reacting_entity, entity, data)


def _handle_reaction(observer: EntityID, triggering_entity: EntityID, data: ReactionData):
    """
    Process a reaction, checking opinion is sufficient and rolling for chance to trigger.
    """
    diff_mod = 0.5  # the amount of the opinion difference to consider
    required_opinion = data.required_opinion

    # if we dont have a required opinion or have enough opinion carry on
    if required_opinion is None or not scripts.engine.core.matter.entity_has_component(observer, Opinion):
        opinion_diff = 0

    else:
        opinion = scripts.engine.core.matter.get_entitys_component(observer, Opinion)
        current_opinion = opinion.opinions[triggering_entity]

        # reverse if negative to make it simpler
        if required_opinion < 0:
            required_opinion = -required_opinion
            current_opinion = -current_opinion

        if required_opinion < current_opinion:
            opinion_diff = current_opinion - required_opinion

        else:
            # has opinion and doesnt meet requirement
            return

    # roll for chance to react
    from scripts.engine.core import utility

    roll = utility.roll()
    modified_chance = int(data.chance + (opinion_diff * diff_mod))  # the greater the opinion diff the more chance

    # if roll was unsuccessful return now
    if roll > modified_chance:
        return

    # we need position to react to so check we have one (this also prevents triggering on gods)
    if scripts.engine.core.matter.entity_has_component(triggering_entity, Position):
        # get tile of the acting entity
        position = scripts.engine.core.matter.get_entitys_component(triggering_entity, Position)
        target_tile = world.get_tile((position.x, position.y))

        _apply_reaction(observer, triggering_entity, target_tile, data)

        # reacted so reduce opinion towards 0
        if required_opinion is None or not scripts.engine.core.matter.entity_has_component(observer, Opinion):
            return

        # check if negative value
        if 0 >= opinion.opinions[triggering_entity]:
            opinion.opinions[triggering_entity] = min(0, opinion.opinions[triggering_entity] + required_opinion)
        else:
            opinion.opinions[triggering_entity] = max(0, opinion.opinions[triggering_entity] - required_opinion)


def _apply_reaction(observer: EntityID, triggering_entity: EntityID, target_tile: Tile, data: ReactionData):
    """
    Create the skill or effect from the reaction and apply it.
    """
    if isinstance(data.reaction, EffectData):
        effect = scripts.engine.core.matter.create_effect(observer, triggering_entity, data.reaction)
        effect.evaluate()
    else:  # skill data
        from scripts.engine.internal.data import store

        skill = store.skill_registry[data.reaction]
        scripts.engine.core.matter.use_skill(observer, skill, target_tile, Direction.CENTRE)


def _set_sprite(entity: EntityID, sprite_category: SpriteCategoryType, new_pos: Optional[Tuple[int, int]] = None):
    """
    Sets an entities sprite
    """
    if scripts.engine.core.matter.entity_has_component(entity, Aesthetic):
        aesthetic = scripts.engine.core.matter.get_entitys_component(entity, Aesthetic)
        animation = getattr(aesthetic.sprites, sprite_category)
        if animation:
            aesthetic.set_current_sprite(sprite_category)
        else:
            logging.warning(f"{scripts.engine.core.matter.get_name(entity)} doesn`t have {sprite_category} sprite so left as idle.")

        if new_pos:
            aesthetic.target_draw_x, aesthetic.target_draw_y = new_pos


############### NON-GENERIC REACTION HANDLING ##########################


def _handle_proximity_reaction_trigger(event: pygame.event):
    """
    Special case of _handle_reaction_trigger. Checks for overlapping positions. Check for any entities with a
    reaction to proximity and handle that reaction.
    """
    # loop all entities sharing same position that have a reaction
    for entity, (position, reaction) in query.position_and_reaction:
        assert isinstance(position, Position)
        assert isinstance(reaction, Reaction)
        for coord in position.coordinates:
            if coord == event.new_pos:
                if ReactionTrigger.PROXIMITY in reaction.reactions:
                    data = reaction.reactions[ReactionTrigger.PROXIMITY]
                    _handle_reaction(entity, event.origin, data)


def _process_win_condition(event: pygame.event):
    """
    Checking if the win condition has been met. Post event if it is.
    """
    player = scripts.engine.core.matter.get_player()

    # only progress if its the player as only the player can win
    if not player == event.target:
        return

    player_pos = scripts.engine.core.matter.get_entitys_component(player, Position)

    for entity, (position, _) in query.position_and_win_condition:
        assert isinstance(position, Position)
        if player_pos.x == position.x and player_pos.y == position.y:
            # post game event
            event_hub.post(WinConditionMetEvent())
            break


def _process_map_condition(event: pygame.event):
    """
    Checking if the map change condition has been met. Post event if it is.
    """
    player = scripts.engine.core.matter.get_player()

    # only progress if its the player as only the player can change the map
    if not player == event.target:
        return

    player_pos = scripts.engine.core.matter.get_entitys_component(player, Position)

    for entity, (position, _) in query.position_and_map_condition:
        assert isinstance(position, Position)
        if player_pos.x == position.x and player_pos.y == position.y:
            # post game event
            event_hub.post(ChangeMapEvent())
            break
