from scripts.core.colours import Palette, Colour
from scripts.core.constants import BASE_WINDOW_WIDTH, BASE_WINDOW_HEIGHT
from scripts.core.fonts import Font
from scripts.ui_elements.templates.panel import Panel


class SelectedEntityInfo:
    """
    Handle the information for the selected entity and the associated panel
    """
    def __init__(self):
        self.selected_entity = None
        self.visible = False
        self.font = Font().default
        self.gap_between_lines = int(self.font.size / 3)

        # setup the panel
        panel_width = int((BASE_WINDOW_WIDTH / 4) * 1)
        panel_height = int((BASE_WINDOW_HEIGHT / 5) * 2)
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = BASE_WINDOW_HEIGHT - panel_height
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

    def set_visibility(self, visible):
        """
        Set the visibility of the selected entity info

        Args:
            visible (bool): Visible or not
        """
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("entity_info", self.panel, visible)

    def draw(self, surface):
        """
        Draw the entity info

        Args:
            surface (Surface): Surface to draw to

        """
        # panel background
        self.panel.draw_background()

        # entity info
        font = self.font
        font_size = self.font.size
        adjusted_x = self.panel.width / 4
        adjusted_y = self.panel.height / 8
        font_colour = Colour().white
        panel_surface = self.panel.surface
        entity = self.selected_entity
        messages = []

        # what messages do we want to show?
        messages.append(f"{entity.name.capitalize()}")
        messages.append(f"")
        messages.append(f"Hp: {entity.combatant.hp}")
        messages.append(f"Power: {entity.combatant.power}")
        messages.append(f"Defence: {entity.combatant.defence}")

        # render the message_list
        for message in messages:
            font.render_to(panel_surface, (adjusted_x, adjusted_y), message, font_colour)
            adjusted_y += font_size + self.gap_between_lines

        # panel border
        self.panel.draw_panel_border()

        # draw all to provided surface
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))