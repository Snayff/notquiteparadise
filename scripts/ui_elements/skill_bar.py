from scripts.core.colours import Palette, Colour
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
        self.skills_shown_in_skill_bar = 5
        self.skill_icon_size = 64
        self.icon_x = 10

        # init the containers
        self.skill_containers = []
        x = self.icon_x
        size = self.skill_icon_size
        bg_colour = Colour().white
        bor_colour = self.palette.skill_border
        bor_size = 1

        for y in range(0,self.skills_shown_in_skill_bar):
            y *= size
            skill_container = SkillContainer(x, y, size, size, bg_colour, bor_size, bor_colour, None)
            self.skill_containers.append(skill_container)

        # panel info
        panel_width = int(((BASE_WINDOW_WIDTH / 4) * 1) /2 ) # half the size of the message log
        panel_height = int(BASE_WINDOW_HEIGHT / 2)
        panel_x = BASE_WINDOW_WIDTH - panel_width
        panel_y = 0
        panel_border = 2
        panel_background_colour = self.palette.background
        panel_border_colour = self.palette.border
        self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
                           panel_border_colour)

        # set panel to be rendered
        from scripts.core.global_data import ui_manager
        ui_manager.update_panel_visibility("skill_bar", self, True)

    def draw(self, surface):
        """
        Draw the skill bar, and skill containers

        Args:
            surface:
        """
        # panel background
        self.panel.draw_background()

        # skill containers
        for skill_container in self.skill_containers:
            skill_container.draw_background()
            skill_container.draw_skill_icon()
            skill_container.draw_border()
            skill_container.draw_self_on_other_surface(self.panel.surface)

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

    def update_skill_icons_to_show(self):
        """
        Get the player's known skills to show in the skill bar.
        """

        # update info
        from scripts.core.global_data import entity_manager
        player = entity_manager.player

        if player:
            for counter, skill in enumerate(player.actor.known_skills):
                self.skill_containers[counter].skill_icon = skill.icon
