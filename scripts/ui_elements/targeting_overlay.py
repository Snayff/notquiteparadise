
import logging
import pygame


from scripts.global_singletons.data_library import library
from scripts.ui_elements.palette import Palette
from scripts.core.constants import TILE_SIZE,  SkillShapes
from scripts.core.fonts import Font
from scripts.skills.skill import Skill


class TargetingOverlay:
    """
    The targeting overlay showing possible targets

    Attributes:
        skill_being_targeted (Skill): the skill in use

    """

    def __init__(self):
        # data
        self.skill_being_targeted = None
        self.tiles_in_range_and_fov = []
        self.tiles_in_skill_effect_range = []
        self.selected_tile = None
        self.is_visible = True

        # drawing info
        self.palette = Palette().targeting_overlay
        self.font = Font().targeting_overlay
        self.select_border_width = 5
        self.highlight_border_width = 3

        logging.debug(f"TargetingOverlay initialised.")

    def draw(self, surface):
        """
        Draw the targeting overlay

        Args:
            surface:
        """
        self.draw_range_highlight(surface)
        self.draw_effect_highlight(surface)
        self.draw_selected_tile(surface)

    def draw_range_highlight(self, surface):
        """
        Draw the highlights on top of the tiles_in_range_and_fov

        Args:
            surface:
        """
        tile_colour = self.palette.highlighted_range_border
        rect = pygame.rect.Rect(0, 0, TILE_SIZE, TILE_SIZE)

        # draw highlight on all tiles listed, except the one selected
        for tile in self.tiles_in_range_and_fov:
            if tile != self.selected_tile:
                # amend rect position to reflect tile sizes
                rect.x = tile.x * TILE_SIZE
                rect.y = tile.y * TILE_SIZE
                pygame.draw.rect(surface, tile_colour, rect, self.highlight_border_width)

    def draw_effect_highlight(self, surface):
        """
        Draw the highlights on top of the tiles_in_skill_effect_range

        Args:
            surface:
        """
        tile_colour = self.palette.highlighted_effect_border
        rect = pygame.rect.Rect(0, 0, TILE_SIZE, TILE_SIZE)

        # draw highlight on all tiles listed, except the one selected
        for tile in self.tiles_in_skill_effect_range:
            if tile != self.selected_tile:
                # amend rect position to reflect tile sizes
                rect.x = tile.x * TILE_SIZE
                rect.y = tile.y * TILE_SIZE
                pygame.draw.rect(surface, tile_colour, rect, self.highlight_border_width)

    def draw_selected_tile(self, surface):
        """
        Draw the highlight on the selected_tile.
        Args:
            surface:
        """
        tile_colour = self.palette.selected_tile_border
        rect = pygame.rect.Rect(0, 0, TILE_SIZE, TILE_SIZE)
        rect.x = self.selected_tile.x * TILE_SIZE
        rect.y = self.selected_tile.y * TILE_SIZE

        pygame.draw.rect(surface, tile_colour, rect, self.select_border_width)

    def set_skill_being_targeted(self, skill):
        """
        Set the skill that the player is currently targeting

        Args:
            skill:
        """
        self.skill_being_targeted = skill

    def set_selected_tile(self, tile):
        """
        Update the tile currently selected. Must be in the highlighted range.

        Args:
            tile:
        """
        if tile in self.tiles_in_range_and_fov:
            self.selected_tile = tile

    def update_tiles_in_range_and_fov(self):
        """
        Update list of valid tiles within range based on currently selected skill's range.
        """
        # if there is a skill being targeted
        if self.skill_being_targeted:

            # clear current tiles
            self.tiles_in_range_and_fov = []

            from scripts.global_singletons.managers import world_manager
            player = world_manager.player
            skill_data = library.get_skill_data(self.skill_being_targeted.skill_tree_name,
                                                self.skill_being_targeted.name)
            skill_range = skill_data.range

            # get the tiles in range
            coords = world_manager.Skill.create_shape(SkillShapes.SQUARE, skill_range)
            tiles_in_range = world_manager.Map.get_tiles(player.x, player.y, coords)
            tiles_in_range_and_fov = []

            # only take tiles in range and FOV
            for tile in tiles_in_range:
                if world_manager.FOV.is_tile_in_fov(tile.x, tile.y):
                    tiles_in_range_and_fov.append(tile)

            self.tiles_in_range_and_fov = tiles_in_range_and_fov

    def update_tiles_in_skill_effect_range(self):
        """
        Update the list of Tiles for those effected by the skill effect range. Based on selected skill.
        """
        # TODO - set to only calculate on skill selection
        #  currently recalcing constantly

        # if there is a skill being targeted
        if self.skill_being_targeted:

            # clear current tiles
            self.tiles_in_skill_effect_range = []

            # get the skill data
            data = library.get_skill_data(self.skill_being_targeted.skill_tree_name, self.skill_being_targeted.name)

            from scripts.global_singletons.managers import world_manager
            coords = world_manager.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world_manager.Map.get_tiles(self.selected_tile.x, self.selected_tile.y, coords)

            self.tiles_in_skill_effect_range = effected_tiles