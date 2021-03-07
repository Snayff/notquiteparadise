import math
import os
from typing import Iterable, List, Optional, Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

import scripts.engine.core.matter
from scripts.engine.core import query, state, utility, world
from scripts.engine.core.component import Aesthetic, Position
from scripts.engine.core.ui import ui
from scripts.engine.internal.constant import (
    EventType,
    GameState,
    Height,
    InputEventType,
    InputIntent,
    TargetingMethod,
    TILE_SIZE,
    UIElement,
)
from scripts.nqp import command
from scripts.nqp.ui_elements.tile_info import TileInfo

__all__ = ["targeting"]


class Targeting:
    def __init__(self):
        self.hovered_tile = None
        self.valid_line_of_sight = False
        self.possible_los_tiles = None

    def process_events(self, camera):
        """
        For processing local events based on camera data.
        Updates the current hovered tile based on mouse position and updates the TILE_INFO GUI element.
        """

        mx, my = pygame.mouse.get_pos()
        mx /= camera._desired_width / camera._base_width
        my /= camera._desired_height / camera._base_height

        hover_pos = (int(camera.start_x + mx / TILE_SIZE), int(camera.start_y + my / TILE_SIZE))
        try:
            new_hover = world.get_tile(hover_pos)
            if (new_hover is self.hovered_tile) == False:
                if new_hover.is_visible:
                    if not ui.has_element(UIElement.TILE_INFO):
                        tile_info: TileInfo = TileInfo(
                            command.get_element_rect(UIElement.TILE_INFO), ui.get_gui_manager()
                        )
                        ui.register_element(UIElement.TILE_INFO, tile_info)

                    tile_info = ui.get_element(UIElement.TILE_INFO)
                    tile_info.set_selected_tile_pos(hover_pos)
                    tile_info.cleanse()
                    ui.set_element_visibility(UIElement.TILE_INFO, True)
                else:
                    ui.set_element_visibility(UIElement.TILE_INFO, False)
            self.hovered_tile = new_hover
        except IndexError:
            pass

    def process_click(self):
        """
        Process a click. This is currently just used during targeting to trigger the cast event since the camera tracks what tiles are targetable.
        TODO: Move targeting logic out of the camera.
        """

        state.set_skill_target_valid(False)
        if self.hovered_tile and self.hovered_tile.is_visible:
            if state.get_current() == GameState.TARGETING:
                active_skill_name = state.get_active_skill()
                player = scripts.engine.core.matter.get_player()
                skill = scripts.engine.core.matter.get_known_skill(player, active_skill_name)

                # set the skill target for the skill cast if the hovered tile is a valid target during line of sight targeting
                if (skill.targeting_method == TargetingMethod.DIRECTION) and self.valid_line_of_sight:
                    state.set_active_skill_target((self.hovered_tile.x, self.hovered_tile.y))
                    state.set_skill_target_valid(True)

                # cancel event triggering if the hovered target is invalid in the target mode
                if skill.targeting_method == TargetingMethod.TILE:
                    position = scripts.engine.core.matter.get_entitys_component(player, Position)
                    dif = (position.x - self.hovered_tile.x, position.y - self.hovered_tile.y)
                    if (
                        (dif not in skill.target_directions)
                        or (not self.hovered_tile.is_visible)
                        or (not world.tile_has_tags(player, self.hovered_tile, skill.target_tags))
                    ):
                        return

            event = pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.TILE_CLICK, tile_pos=(self.hovered_tile.x, self.hovered_tile.y)
            )
            pygame.event.post(event)

    def render(self, camera, target_surf: pygame.Surface):
        # targeting mode related indicator rendering
        if state.get_current() == GameState.TARGETING:
            player = scripts.engine.core.matter.get_player()
            position = scripts.engine.core.matter.get_entitys_component(player, Position)
            active_skill_name = state.get_active_skill()
            skill = scripts.engine.core.matter.get_known_skill(player, active_skill_name)

            # if this is a directional attack
            if skill.targeting_method == TargetingMethod.TILE:
                for direction in skill.target_directions:
                    target_x = position.x + direction[0]
                    target_y = position.y + direction[1]
                    tile = world.get_tile((target_x, target_y))
                    if tile.is_visible and world.tile_has_tags(player, tile, skill.target_tags):
                        option_r = pygame.Rect(
                            (target_x - camera.start_x) * TILE_SIZE,
                            (target_y - camera.start_y) * TILE_SIZE,
                            TILE_SIZE,
                            TILE_SIZE,
                        )
                        pygame.draw.rect(target_surf, (60, 70, 120), option_r, 1)

            # if this is a line of sight attack
            elif skill.targeting_method == TargetingMethod.DIRECTION:
                # regenerate possible targets if targeting mode was just entered
                if self.possible_los_tiles == None:
                    self.possible_los_tiles = []
                    state.set_skill_target_valid(False)
                    for y in range(skill.range * 2 + 1):
                        for x in range(skill.range * 2 + 1):
                            test_pos = (position.x - skill.range + x, position.y - skill.range + y)
                            valid, _ = self.check_valid_line_of_sight(test_pos)
                            if valid:
                                self.possible_los_tiles.append(test_pos)

                # check if current hovered tile is a valid target
                self.valid_line_of_sight = False
                self.valid_line_of_sight, tile_path = self.check_valid_line_of_sight(
                    (self.hovered_tile.x, self.hovered_tile.y)
                )

                # render indicators
                for tile_pos in self.possible_los_tiles:
                    highlight_r = pygame.Rect(
                        (tile_pos[0] - camera.start_x) * TILE_SIZE,
                        (tile_pos[1] - camera.start_y) * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE,
                    )
                    pygame.draw.rect(target_surf, (60, 70, 120), highlight_r, 1)
                if self.valid_line_of_sight:
                    for tile_pos in tile_path:
                        highlight_r = pygame.Rect(
                            (tile_pos[0] - camera.start_x) * TILE_SIZE,
                            (tile_pos[1] - camera.start_y) * TILE_SIZE,
                            TILE_SIZE,
                            TILE_SIZE,
                        )
                        pygame.draw.rect(target_surf, (50, 150, 200), highlight_r, 1)

        # empty targeting data if not in targeting mode
        else:
            self.possible_los_tiles = None

        if self.hovered_tile and self.hovered_tile.is_visible:
            hover_r = pygame.Rect(
                (self.hovered_tile.x - camera.start_x) * TILE_SIZE,
                (self.hovered_tile.y - camera.start_y) * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )
            pygame.draw.rect(target_surf, (200, 200, 0), hover_r, 1)

        target_surf.blit(pygame.transform.scale(target_surf, target_surf.get_size()), (0, 0))

    def check_valid_line_of_sight(self, pos: Tuple[int, int]) -> Tuple[bool, List]:
        """
        Checks if a tile is in the line of sight from the player and returns the visible path to the target tile.
        """
        # get base info and init
        player = scripts.engine.core.matter.get_player()
        position = scripts.engine.core.matter.get_entitys_component(player, Position)
        active_skill_name = state.get_active_skill()
        skill = scripts.engine.core.matter.get_known_skill(player, active_skill_name)
        valid_line_of_sight = False
        target_tile = world.get_tile(pos)
        tile_path = []

        # check if the endpoint is even valid
        if target_tile.is_visible and world.tile_has_tags(player, target_tile, skill.target_tags):

            # init some values for search
            current_pos = [position.x, position.y]
            tile_path = [current_pos.copy()]
            target_pos = list(pos)

            # get list of possible search directions
            directions_for_steps = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
            # this set is for distance calculations
            # the 0.81 reduces the weight of diagonal movement so it isn't chosen too often
            directions_for_math = [
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1),
                (-0.81, -0.81),
                (0.81, 0.81),
                (0.81, -0.81),
                (-0.81, 0.81),
            ]

            valid = True

            # iteratively search for the bordering tile that's closest to the target
            while current_pos != target_pos:
                closest = [
                    current_pos.copy(),
                    math.sqrt((target_pos[0] - current_pos[0]) ** 2 + (target_pos[1] - current_pos[1]) ** 2),
                ]
                for i, direction in enumerate(directions_for_steps):
                    check_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
                    math_check_pos = [
                        current_pos[0] + directions_for_math[i][0],
                        current_pos[1] + directions_for_math[i][1],
                    ]
                    dis = math.sqrt((math_check_pos[0] - target_pos[0]) ** 2 + (math_check_pos[1] - target_pos[1]) ** 2)
                    if dis < closest[1]:  # type: ignore
                        closest = [check_pos.copy(), dis]
                tile = world.get_tile(closest[0])  # type: ignore

                # check if tile step meets targeting criteria
                if (not tile.is_visible) or (not world.tile_has_tags(player, tile, skill.cast_tags)):
                    valid = False

                current_pos = closest[0].copy()  # type: ignore
                tile_path.append(current_pos.copy())

            # determine if the final path was valid based on skill range and previous calculations
            if (len(tile_path) - 1 <= skill.range) and valid:
                valid_line_of_sight = True

        return (valid_line_of_sight, tile_path)


if "GENERATING_SPHINX_DOCS" not in os.environ:  # when building in CI these fail
    targeting = Targeting()
else:
    targeting = ""  # type: ignore
