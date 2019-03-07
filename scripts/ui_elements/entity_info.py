from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT
from scripts.ui_elements.templates.panel import Panel


class SelectedEntityInfo:
    """
    Handle the information for the selected entity and the associated panel
    """
    def __init__(self):
        self.selected_entity = None
        self.visible = False

        # setup the panel
        panel_width = BASE_WINDOW_WIDTH / 5
        panel_height = int(BASE_WINDOW_HEIGHT / 3) * 2
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = 0
        panel_border = 2
        panel_background_colour = Palette().entity_info.background
        panel_border_colour = Palette().entity_info.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

    def set_selected_entity(self, entity):
        """
        Set the selected entity  and make panel visible

        Args:
            entity(tuple): x y position of tile in game map
        """
        self.selected_entity = entity
        if entity is not None:
            self.set_visibility(True)
        else:
            self.set_visibility(False)

    def set_visibility(self, visibility):
        """
        Set the visibility of the selected entity info

        Args:
            visibility (bool): Visible or not
        """
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("entity_info", self.panel, visibility)

    def draw(self, surface):
        """
        Draw the entity info

        Args:
            surface (Surface): Surface to draw to

        """
        # panel background
        self.panel.surface.fill(Colour().black)
        self.panel.draw_rect()

        # entity info


        # panel border
        self.panel.draw_panel_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))