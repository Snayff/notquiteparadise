
from scripts.ui.templates.panel import Panel


class SkillContainer(Panel):
    def __init__(self, x, y, width, height, background_colour, border_size, border_colour, skill_icon, skill_number):
        super().__init__(x, y, width, height, background_colour, border_size, border_colour)

        self.skill_icon = skill_icon
        self.skill_number = skill_number

    def draw_skill_icon(self):
        """
        Draw the skill icon
        """
        if self.skill_icon:
            self.surface.blit(self.skill_icon, (0, 0))

    def draw_skill_key(self):
        """
        Draw the use key for the skills
        """
        from scripts.global_singletons.managers import ui_manager
        font = ui_manager.Font.skill_bar
        text_x = int(self.width - (font.size / 1.8))
        text_y = int(self.height - font.size * 1.2)
        text = str(self.skill_number)
        text_colour = ui_manager.Palette.skill_bar.text_default

        font.render_to(self.surface, (text_x, text_y), text, text_colour)

    def draw_self_on_other_surface(self, surface):
        """
        Draw the skill parent_widget on another surface

        Args:
            surface:
        """
        surface.blit(self.surface, (self.x, self.y))


