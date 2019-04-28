import pygame

from scripts.ui_elements.palette import Palette
from scripts.core.constants import BASE_WINDOW_HEIGHT, BASE_WINDOW_WIDTH
from scripts.core.fonts import Font
from scripts.ui_elements.templates.panel import Panel
from scripts.ui_elements.templates.skill_container import SkillContainer


class SkillBar:
    """
    Get and hold the info for the skill section
    """

    def __init__(self):
        # setup info
        self.font = Font().skill_bar
        self.palette = Palette().skill_bar
        self.max_skills_in_bar = 5
        self.skill_icon_size = 64

        # panel info
        panel_width = int(self.skill_icon_size * 1.5)
        panel_height = int(BASE_WINDOW_HEIGHT / 2)
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = 0
        panel_border = 2
        panel_background_colour = self.palette.background
        panel_border_colour = self.palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # init the containers
        self.skill_containers = []
        self.icon_x = int(panel_width / 4) - 5  # centre of the skill bar
        self.gap_between_skill_icons = int((panel_height - (self.max_skills_in_bar * self.skill_icon_size)) /
                                           self.max_skills_in_bar)

        size = self.skill_icon_size
        bg_colour = self.palette.background
        bor_colour = self.palette.skill_border
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

        # set self to be rendered
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("skill_bar", self, True)

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

    def update_skill_icons_to_show(self):
        """
        Get the player's known skills to show in the skill bar.
        """

        # update info
        from scripts.core.global_data import world_manager
        player = world_manager.player

        # if the player has been init'd update skill bar
        if player:
            for counter, skill in enumerate(player.actor.known_skills):
                # catch any images not the right size and resize them
                if skill.icon.get_size() != (self.skill_icon_size, self.skill_icon_size):
                    icon = pygame.transform.smoothscale(skill.icon, (self.skill_icon_size, self.skill_icon_size))
                else:
                    icon = skill.icon

                self.skill_containers[counter].skill_icon = icon

    def get_skill_index_from_skill_clicked(self, relative_x, relative_y):
        """
        Return the index of the skill clicked in the skill bar

        Args:
            relative_x:
            relative_y:

        Returns:
            int: -1 if nothing, else 0-4.

        Notes:
            The skills in the skill bar are pulled, in order, from the player's known skills.
        """
        for container in self.skill_containers:
            if container.rect.collidepoint(relative_x, relative_y):
                skill_index = self.skill_containers.index(container)
                return skill_index

        return -1