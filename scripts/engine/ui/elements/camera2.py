from __future__ import annotations
from typing import TYPE_CHECKING, Type

from pygame import SRCALPHA, Surface
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIImage, UIPanel
from scripts.engine import world
from scripts.engine.component import Aesthetic, Position
from scripts.engine.core.constants import RenderLayer, TILE_SIZE
from scripts.engine.world_objects.tile import Tile

if TYPE_CHECKING:
    from typing import Union, Optional, Any, Tuple, Dict, List


class Camera2(UIPanel):
    """
    Represent the map on screen
    """
    def __init__(self, rect: Rect, manager: UIManager):
        player = world.get_player()
        pos = world.get_entitys_component(player, Position)

        self.display_width = rect.width  # draw space
        self.display_height = rect.height
        self.start_x = int(pos.x - (self.display_width / 2) / TILE_SIZE)  # world space
        self.start_y = int(pos.y - (self.display_height / 2) / TILE_SIZE)

        self._tiles_in_view = []
        self.is_dirty = True

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, element_id="camera")

        blank_surf = Surface((rect.width, rect.height), SRCALPHA)
        self.gamemap = UIImage(relative_rect=Rect((0, 0), rect.size), image_surface=blank_surf, manager=manager,
                               container=self.get_container(), object_id="#gamemap")

    @property
    def end_x(self) -> int:
        return round(self.start_x + self.display_width // TILE_SIZE) - 1

    @property
    def end_y(self) -> int:
        return round(self.start_y + self.display_height // TILE_SIZE)

    def handle_events(self, event):
        pass

    def update(self, time_delta: float):
        super().update(time_delta)


        player = world.get_player()
        position = world.get_entitys_component(player, Position)
        self.start_x = int(position.x - (self.display_width / 2) / TILE_SIZE)
        self.start_y = int(position.y - (self.display_height / 2) / TILE_SIZE)


        # create new surface for the game map
        map_width = self.gamemap.rect.width
        map_height = self.gamemap.rect.height
        margin = TILE_SIZE * 2
        map_surf = Surface((map_width + margin, map_height + margin), SRCALPHA)

        # draw tiles
        for tile in self._get_tiles_in_view():
            draw_pos = self.world_to_draw_position((tile.x, tile.y))
            map_surf.blit(tile.sprite, draw_pos)

        # draw entities
        for entity, (pos, aesthetic) in world.get_components([Position, Aesthetic]):
            # if part of entity in camera view
            for offset in pos.offsets:
                src_area = Rect(offset[0] * TILE_SIZE, offset[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                position = (pos.x + offset[0], pos.y + offset[1])
                draw_position = (aesthetic.draw_x + offset[0], aesthetic.draw_y + offset[1])
                if self.start_x <= position[0] < self.end_x and self.start_y <= position[1] < self.end_y:
                    tile = world.get_tile(position)
                    if tile.is_visible or True:
                        map_surf.blit(aesthetic.current_sprite, self.world_to_draw_position(draw_position), src_area)

        # set the image in the UI Image
        #self.gamemap.set_image_clip(Rect((TILE_SIZE * 2, TILE_SIZE * 2), (map_width, map_height)))
        self.gamemap.set_image(map_surf)

    def world_to_draw_position(self, pos: Tuple[float, float]) -> Tuple[int, int]:
        """
        Convert from the world_objects position to the screen position
        """
        draw_x = int((pos[0] - self.start_x) * TILE_SIZE)
        draw_y = int((pos[1] - self.start_y) * TILE_SIZE)

        return draw_x, draw_y

    def _get_tiles_in_view(self) -> List[Tile]:
        """
        Return the tiles in view. Refreshes them if is_dirty.
        """
        if self.is_dirty:
            tiles = []
            for x in range(self.start_x, self.end_x):
                for y in range(self.start_y, self.end_y):
                    tile = world.get_tile((x, y))
                    if tile.is_visible:
                        tiles.append(tile)
            self._tiles_in_view = tiles

        return self._tiles_in_view
