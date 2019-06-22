from scripts.global_instances.managers import ui_manager


def handle_player_turn_input(input_values):
    """

    Args:
        input_values:

    """

    # Skill usage
    if self.input_values["skill"] != -1:
        skill_number = self.input_values["skill"]
        # check we actually have that skill
        # Note: this might bite me later if we can assign to any skill slot and not have preceding ones filled
        if len(player.actor.known_skills) > skill_number:
            skill = player.actor.known_skills[skill_number]
            if skill:
                mouse_x, mouse_y = ui_manager.get_relative_scaled_mouse_pos("game_map")
                target_x, target_y = world_manager.Map.convert_xy_to_tile(mouse_x, mouse_y)

                # create a skill with a target, or activate targeting mode
                skill = player.actor.known_skills[skill_number]
                if world_manager.Skill.can_use_skill(player, (target_x, target_y), skill):
                    publisher.publish((UseSkillEvent(player, (target_x, target_y), skill)))
                else:
                    # can't use skill, is it due to being too poor?
                    if world_manager.Skill.can_afford_cost(player, skill.resource_type, skill.resource_cost):
                        publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))
                    else:
                        msg = f"It seems you're too poor to do that."
                        publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))
            else:
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, "There is nothing in that skill slot."))
        else:
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, "You haven't learnt that many skills yet."))



def handle_targeting_mode_input(input_values):
    """

    Args:
        input_values:
    """
    self.input_values = input_values
    player = world_manager.player
    mouse_x, mouse_y = ui_manager.get_scaled_mouse_pos()
    mouse_tile_x, mouse_tile_y = world_manager.Map.convert_xy_to_tile(mouse_x, mouse_y)

    # cancel out
    if self.input_values["cancel"]:
        previous_state = game_manager.previous_game_state
        publisher.publish(ChangeGameStateEvent(previous_state))

    # Selected tile
    direction_x = 0
    direction_y = 0

    if self.input_values["up"]:
        direction_x = 0
        direction_y = -1
    elif self.input_values["down"]:
        direction_x = 0
        direction_y = 1
    elif self.input_values["left"]:
        direction_x = -1
        direction_y = 0
    elif self.input_values["right"]:
        direction_x = 1
        direction_y = 0
    elif self.input_values["up_left"]:
        direction_x = -1
        direction_y = -1
    elif self.input_values["up_right"]:
        direction_x = 1
        direction_y = -1
    elif self.input_values["down_left"]:
        direction_x = -1
        direction_y = 1
    elif self.input_values["down_right"]:
        direction_x = 1
        direction_y = 1

    # get selected tile from ui
    selected_tile = ui_manager.targeting_overlay.selected_tile

    # if direction isn't 0 then we need to move selected_tile
    if direction_x != 0 or direction_y != 0:
        tile_x, tile_y = direction_x + selected_tile.x, direction_y + selected_tile.y
        tile = world_manager.Map.get_tile(tile_x, tile_y)
        ui_manager.targeting_overlay.set_selected_tile(tile)
        entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
        ui_manager.entity_info.set_selected_entity(entity)

    # if mouse moved update selected tile
    if self.input_values["mouse_moved"]:
        tile = world_manager.Map.get_tile(mouse_tile_x, mouse_tile_y)
        ui_manager.targeting_overlay.set_selected_tile(tile)
        entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
        ui_manager.entity_info.set_selected_entity(entity)

    # confirm usage
    skill_being_targeted = ui_manager.targeting_overlay.skill_being_targeted
    skill_number = self.input_values["skill"]
    # check the skill value has been set
    if self.input_values["skill"] != -1:

        if self.input_values["skill"] == player.actor.known_skills.index(skill_being_targeted) or self.input_values["confirm"]:
            # FIXME: confirm not triggering

            # if entity selected then use skill
            if world_manager.Entity.get_blocking_entity_at_location(selected_tile.x, selected_tile.y):
                publisher.publish((UseSkillEvent(player, (selected_tile.x, selected_tile.y), skill_being_targeted)))

        # pressed another skill so swap to that one
        elif self.input_values["skill"] != player.actor.known_skills.index(skill_being_targeted):
            skill = player.actor.known_skills[skill_number]
            publisher.publish(ChangeGameStateEvent(GameStates.TARGETING_MODE, skill))

    if self.input_values["left_click"]:
        # if entity selected then use skill
        if world_manager.Entity.get_blocking_entity_at_location(selected_tile.x, selected_tile.y):
            publisher.publish((UseSkillEvent(player, (selected_tile.x, selected_tile.y), skill_being_targeted)))