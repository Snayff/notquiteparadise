from scripts.core.constants import TargetTypes


class SkillQuery():
    def __init__(self, manager):
        self.manager = manager

    def can_use_skill(self, entity, target_pos, skill):
        """
        Confirm entity can use skill on targeted position
        Args:
            entity (Entity):
            target_pos (tuple(int, int)):
            skill (Skill):

        Returns:
            bool: True if can use the skill. Else False.
        """
        from scripts.global_instances.managers import world_manager

        target_x, target_y = target_pos
        blocking_entity_at_location = world_manager.entity_query.get_blocking_entity_at_location(target_x,
                                                                                                 target_y)
        tile = world_manager.game_map.get_tile(target_x, target_y)

        # do we need an entity?
        if skill.required_target_type == TargetTypes.ENTITY:
            # is there an entity to target?
            if blocking_entity_at_location:
                # is the entity within range?
                distance_to_entity = world_manager.entity_query.get_chebyshev_distance_between_entities(entity,
                                                                                                         blocking_entity_at_location)
                if distance_to_entity > skill.range:
                    return False
            else:
                return False

        # get info about the tile and the skill requirements
        is_required_type = skill.is_required_target_type(tile)
        has_tags = skill.has_required_tags(tile)

        # check we have everything we need and if so use the skill
        if is_required_type and has_tags:
            if skill.user_can_afford_cost():
                return True

        return False

    