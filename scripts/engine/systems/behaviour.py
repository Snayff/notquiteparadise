from __future__ import annotations

__all__ = ["process_interventions"]


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
