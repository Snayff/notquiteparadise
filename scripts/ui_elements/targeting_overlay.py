import pygame

from scripts.core.colours import Palette
from scripts.core.constants import TILE_SIZE, LoggingEventTypes
from scripts.core.fonts import Font
from scripts.core.skill import Skill
from scripts.events.logging_events import LoggingEvent


class TargetingOverlay:
    """
    The targeting overlay showing possible targets

    Attributes:
        skill_being_targeted (Skill): the skill in use

    """

    def __init__(self):
        # data
        self.skill_being_targeted = None
        self.tiles_to_highlight = []
        self.selected_tile = None  # TODO - update the entity info panel in line with this

        # drawing info
        self.palette = Palette().targeting_overlay
        self.font = Font().targeting_overlay
        self.select_border_width = 5
        self.highlight_border_width = 3

        self.is_dirty = True

    def update(self):
        pass
        # TODO - update the selected tile when mouse or controller or keyboard moves

    def draw(self, surface):
        """
        Draw the targeting overlay

        Args:
            surface:
        """
        self.draw_range_highlight(surface)
        self.draw_selected_tile(surface)

    def draw_range_highlight(self, surface):
        """
        Draw the highlights on top of the tiles_to_highlight
        Args:
            surface:
        """
        tile_colour = self.palette.highlighted_range_border
        rect = pygame.rect.Rect(0, 0, TILE_SIZE, TILE_SIZE)

        # draw highlight on all tiles listed, except the one selected
        for tile in self.tiles_to_highlight:
            if tile != self.selected_tile:
                # amend rect position to reflect tile sizes
                rect.x = tile.x * TILE_SIZE
                rect.y = tile.y * TILE_SIZE
                pygame.draw.rect(surface, tile_colour, rect, self.highlight_border_width)
                # TODO - move to debug
                self.font.render_to(surface, (rect.x, rect.y), f"{tile.x},{tile.y}", Palette().debug_font_colour)

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
        Update the tile currently selected
        Args:
            tile:
        """
        self.selected_tile = tile

    def update_tiles_to_highlight(self):
        """
        build list of valid tiles within range
        """
        self.tiles_to_highlight = []

        from scripts.core.global_data import entity_manager
        player = entity_manager.player
        centre_x = player.x
        centre_y = player.y
        from scripts.core.global_data import world_manager
        skill_range = self.skill_being_targeted.range
        game_map = world_manager.game_map

        # +1 to make the range inclusive
        for x in range(-skill_range, skill_range + 1):
            for y in range(-skill_range, skill_range + 1):
                current_x = x + centre_x
                current_y = y + centre_y

                # check in bounds, in fov and is targetable
                in_bounds = game_map.is_tile_in_bounds(current_x, current_y)
                in_fov = world_manager.is_tile_in_fov(current_x, current_y)

                if in_bounds and in_fov:
                    tile = game_map.get_tile(current_x, current_y)
                    if current_x != tile.x or current_y != tile.y:
                        tile2 = game_map.get_tile(current_x, current_y)

                    self.tiles_to_highlight.append(tile)

                    from scripts.core.global_data import game_manager
                    log_string = f"Added tile({tile.x}, {tile.y})."
                    game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, log_string))

    def set_visibility(self, visible):
        """
        Set the visibility of the targeting overlay

        Args:
            visible (bool): Visible or not
        """
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("targeting_overlay", self,  visible)
