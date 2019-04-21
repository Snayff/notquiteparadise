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
        self.palette = Palette().entity_info
        self.font = Font().default
        self.gap_between_lines = int(self.font.size / 3)

        # panel info
        panel_width = int((BASE_WINDOW_WIDTH / 4) * 1)
        panel_height = int(BASE_WINDOW_HEIGHT / 2)
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = BASE_WINDOW_HEIGHT - panel_height
        panel_border = 2
        panel_background_colour = self.palette.background
        panel_border_colour = self.palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

    def draw(self, surface):
        """
        Draw the entity info

        Args:
            surface (Surface): Surface to draw to

        """
        # entity info
        entity = self.selected_entity
        icon = entity.icon

        # formatting info
        panel_centre_x = self.panel.width / 2
        icon_width, icon_height = icon.get_rect().size
        half_icon_width = icon_width / 2
        half_icon_height = icon_height / 2
        icon_x = panel_centre_x - half_icon_width
        icon_y = (self.panel.height / 8) - half_icon_height
        column_one_x = self.panel.width / 16
        column_two_x = panel_centre_x + column_one_x
        header_x = icon_x
        header_y = icon_y + icon_height
        font_colour = Colour().white
        panel_surface = self.panel.surface
        first_section_text = []
        second_section_column_one_text = []
        second_section_column_two_text = []
        header_text = []
        font = self.font
        font_size = self.font.size

        # what messages do we want to show?
        # TODO - move content out of draw
        header_text.append(f"{entity.name.capitalize()}")
        header_text.append(f"Current Health: {entity.combatant.hp}")

        first_section_text.append(f"PRIMARY")
        first_section_text.append(f"Vigour: {entity.combatant.primary_stats.vigour}")
        first_section_text.append(f"Clout: {entity.combatant.primary_stats.clout}")
        first_section_text.append(f"Subtlety: {entity.combatant.primary_stats.subtlety}")
        first_section_text.append(f"Bustle: {entity.combatant.primary_stats.bustle}")
        first_section_text.append(f"Exactitude: {entity.combatant.primary_stats.exactitude}")

        second_section_text_header = f"SECONDARY"
        second_section_column_one_text.append(f"Offense:")
        second_section_column_one_text.append(f"Base Damage: {entity.combatant.secondary_stats.base_damage}")
        second_section_column_one_text.append(f"Chance to Hit: {entity.combatant.secondary_stats.chance_to_hit}")
        second_section_column_one_text.append(f"")
        second_section_column_one_text.append(f"Utility:")
        second_section_column_one_text.append(f"Action Cost Change: "
                                              f"{entity.combatant.secondary_stats.action_cost_change}")
        second_section_column_one_text.append(f"Status Length: {entity.combatant.secondary_stats.status_length}")

        second_section_column_two_text.append(f"Defence:")
        second_section_column_two_text.append(f"Dodge speed: {entity.combatant.secondary_stats.dodge_speed}")
        second_section_column_two_text.append(f"Dodge toughness: "
                                              f"{entity.combatant.secondary_stats.dodge_toughness}")
        second_section_column_two_text.append(f"Dodge intelligence: "
                                              f"{entity.combatant.secondary_stats.dodge_intelligence}")
        second_section_column_two_text.append(f"Resist blunt: {entity.combatant.secondary_stats.resist_blunt}")
        second_section_column_two_text.append(f"Resist piece: {entity.combatant.secondary_stats.resist_pierce}")
        second_section_column_two_text.append(f"Resist elemental: "
                                              f"{entity.combatant.secondary_stats.resist_elemental}")

        # panel background
        self.panel.draw_background()

        # render the entity's icon
        self.panel.surface.blit(icon, (icon_x, icon_y))

        # render header
        adjusted_y = header_y
        for text in header_text:
            font.render_to(panel_surface, (header_x, adjusted_y), text, font_colour)
            adjusted_y += font_size + self.gap_between_lines

        # render the first section
        adjusted_y += font_size + self.gap_between_lines
        current_column = 0  # header of section
        for text in first_section_text:
            if current_column == 0:
                font.render_to(panel_surface, (header_x, adjusted_y), text, font_colour)
                current_column = 1
                # just added header so increment y
                adjusted_y += font_size + self.gap_between_lines
            elif current_column == 1:
                font.render_to(panel_surface, (column_one_x, adjusted_y), text, font_colour)
                current_column = 2
                # N.B. just moving column so don't increment y
            elif current_column == 2:
                font.render_to(panel_surface, (column_two_x, adjusted_y), text, font_colour)
                current_column = 1
                # now in second column so adjust y
                adjusted_y += font_size + self.gap_between_lines

        # render the second section
        # render the header
        adjusted_y += font_size + self.gap_between_lines
        font.render_to(panel_surface, (header_x, adjusted_y), second_section_text_header, font_colour)
        adjusted_y += font_size + self.gap_between_lines

        second_main_row_y = adjusted_y + font_size + self.gap_between_lines

        # render the first column of the second section
        adjusted_y = second_main_row_y
        for text in second_section_column_one_text:
            font.render_to(panel_surface, (column_one_x, adjusted_y), text, font_colour)
            adjusted_y += font_size + self.gap_between_lines

        # render the second column of the second section
        adjusted_y = second_main_row_y
        for text in second_section_column_two_text:
            font.render_to(panel_surface, (column_two_x, adjusted_y), text, font_colour)
            adjusted_y += font_size + self.gap_between_lines

        # panel border
        self.panel.draw_border()

        # draw all to provided surface
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

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
        ui_manager.update_panel_visibility("entity_info", self, visible)

