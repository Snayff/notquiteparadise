
import logging

from scripts.core.constants import VisualInfo
from scripts.ui.templates.panel import Panel
from scripts.ui.templates.skill_container import SkillContainer


class SkillBar:
    """
    Get and hold the info for the skill section
    """

    def __init__(self):
        # setup info
        self.max_skills_in_bar = 5
        self.skill_icon_size = 64
        self.is_visible = False

        # panel info
        panel_width = int(self.skill_icon_size * 1.5)
        panel_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        panel_x = VisualInfo.BASE_WINDOW_WIDTH - panel_width
        panel_y = 0
        panel_border = 2
        from scripts.global_singletons.managers import ui
        palette = ui.Palette.skill_bar
        panel_background_colour = palette.background
        panel_border_colour = palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # init the containers
        # TODO - separate to own function
        self.skill_containers = []
        self.icon_x = int(panel_width / 4) - 5  # centre of the skill bar
        self.gap_between_skill_icons = int((panel_height - (self.max_skills_in_bar * self.skill_icon_size)) /
                                           self.max_skills_in_bar)

        size = self.skill_icon_size
        bg_colour = palette.background
        bor_colour = palette.skill_border
        bor_size = 1
        skill_number = 1

        for y in range(0, self.max_skills_in_bar):
            # ensure gap between skills
            y = 10 + ((size * y) + self.gap_between_skill_icons)

            skill_container = SkillContainer(self.icon_x, y, size, size, bg_colour, bor_size, bor_colour, None,
                                             skill_number)
            skill_container.owner = self
            self.skill_containers.append(skill_container)

            # increment counter
            skill_number += 1

        logging.debug(f"SkillBar initialised.")

    def draw(self, surface):
        """
        Draw the skill bar, and skill containers

        Args:
            surface:
        """
        panel_surface = self.panel.surface

        # panel background
        self.panel.draw_background()

        # skill containers
        for container in self.skill_containers:
            # draw the panel as normal then move to the panel surface
            container.draw_background()
            container.draw_border()
            container.draw_skill_icon()
            container.draw_skill_key()
            container.draw_self_on_other_surface(panel_surface)

        # panel border
        self.panel.draw_border()

        # draw everything to the passed in surface
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))



