from scripts.ui_elements.templates.panel import Panel


class SkillContainer(Panel):
    def __init__(self, x, y, width, height, background_colour, border_size, border_colour, skill_icon):
        super().__init__(x, y, width, height, background_colour, border_size, border_colour)

        self.skill_icon = skill_icon

    def draw_skill_icon(self):
        """
        Draw the skill icon
        """
        if self.skill_icon:
            self.surface.blit(self.skill_icon, (self.x, self.y))

    def draw_self_on_other_surface(self, surface):
        """
        Draw the skill container on another surface

        Args:
            surface:
        """
        surface.blit(self.surface, (self.x, self.y))