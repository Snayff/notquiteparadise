from __future__ import annotations

from scripts.engine import world
from scripts.engine.component import IsActive, Position, Tracked
from scripts.engine.core import queries
from scripts.engine.core.constants import MAX_ACTIVATION_DISTANCE

__all__ = ["process_interventions", "process_activations"]



def process_interventions():
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


def process_activations():
    """
    Allocate active component to  appropriate NPCs. Entity with no position or with position and close to player.
    """
    # all entities with no position must be active
    for entity, (_,) in queries.not_position:
        if not world.entity_has_component(entity, IsActive):
            world.add_component(entity, IsActive())

    # check entities in range of player
    player = world.get_player()
    player_pos: Position = world.get_entitys_component(player, Position)
    for entity, (pos,) in queries.position:
        # check if they're close enough that we care
        distance_x = abs(player_pos.x - pos.x)
        distance_y = abs(player_pos.y - pos.y)
        if max(distance_x, distance_y) < MAX_ACTIVATION_DISTANCE:
            # they're close, now check they arent already active
            if not world.entity_has_component(entity, IsActive):
                world.add_component(entity, IsActive())

                # update tracked to current time (otherwise they will be behind and act repeatedly)
                if world.entity_has_component(entity, Tracked):
                    tracked = world.get_entitys_component(entity, Tracked)
                    from scripts.engine import chronicle

                    tracked.time_spent = chronicle.get_time() + 1

        else:
            # not close enough, remove active
            if world.entity_has_component(entity, IsActive):
                world.remove_component(entity, IsActive)
