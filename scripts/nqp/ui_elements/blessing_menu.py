from __future__ import annotations

import logging
import random
from typing import TYPE_CHECKING

import pygame
from pygame_gui.core import ObjectID
from pygame_gui.core import UIElement as PygameUiElement
from pygame_gui.elements import UIImage, UITextBox, UIVerticalScrollBar, UIButton
from scripts.engine.core import utility
import scripts.engine.core.matter
from scripts.engine.widgets.window import Window
from scripts.engine.internal.constant import ASSET_PATH, GAP_SIZE, ICON_SIZE, GameState
from scripts.engine.internal.action import Skill, SkillModifier
from scripts.engine.internal.data import store
from scripts.engine.core.component import Knowledge
from scripts.engine.core import state
from scripts.nqp.actions.blessing import MoveFast, NoMove, AttackMove, Aftershock, SaltTheWound, KeepAnEvenKeel

if TYPE_CHECKING:
    from typing import List, Optional, Tuple, Union, Type

    from pygame_gui import UIManager

class BlessingMenu(Window):
    """
    A menu for adding blessings.
    """

    def __init__(self, rect: pygame.Rect, manager: UIManager, blessings: List[SkillModifier]):

        # assigned blessings
        self.blessings = blessings

        # sections
        self.sections: List[PygameUiElement] = []
        self.section_base_positions: List[int] = []

        # button tracking
        self.apply_buttons: List[Tuple[Type[Skill], SkillModifier, UIButton]] = []

        # complete base class init
        super().__init__(rect, manager, object_id=ObjectID("#blessing_menu", "@menu_window"))
        #self.set_dimensions((rect.width, rect.height))

        # setup scroll bar
        self.scrollbar_width = 50
        self.scrollbar_size = 0.3
        self.scrollbar = UIVerticalScrollBar(
            pygame.Rect((rect.width - self.scrollbar_width, 0), (self.scrollbar_width, rect.height)),
            self.scrollbar_size,
            manager,
            self,
            self,
            "#scrollbar",
        )

        # block mouse clicks outside of menu
        self.set_blocking(True)

        # show self
        self.show()

        # confirm init complete
        logging.debug(f"Blessing menu initialized.")

    def _shift_children(self, target_y):
        for i, child in enumerate(self.sections):
            child.set_relative_position((child.relative_rect.x, self.section_base_positions[i] - target_y))

    def update(self, time_delta: float):
        super().update(time_delta)
        new_y_portion = self.scrollbar.scroll_position / self.scrollbar.bottom_limit / (1 - self.scrollbar_size)
        if self.sections != []:
            if (
                self.section_base_positions[-1] + self.sections[-1].relative_rect.height
                > self.rect.height - self.section_base_positions[0]
            ):
                new_y = new_y_portion * (
                    self.section_base_positions[-1]
                    + self.sections[-1].relative_rect.height
                    - (self.rect.height - self.section_base_positions[0])
                    + 30 # the +30 accounts for a bug in window sizes from pygame_gui
                )
                self._shift_children(new_y)

        for button in self.apply_buttons:
            if button[2].check_pressed():
                player = scripts.engine.core.matter.get_player()
                knowledge = scripts.engine.core.matter.get_entitys_component(player, Knowledge)
                knowledge.add_blessing(button[0], button[1])
                state.set_new(GameState.GAME_MAP)
                self.kill()

    def show(self):
        """
        fill in later
        """
        super().show()

        self.visible = True

        # clear to refresh first
        self.cleanse()

        if 1:
            info: List[Tuple[str, Union[str, pygame.Surface]]] = []

            current_y = 0
            width = self.rect.width - self.scrollbar_width

            for blessing in self.blessings:
                current_y = self._create_blessing_section(current_y, blessing)

            #info.append(("text", "Please select a blessing."))
            #info.append(("image", section_break_image))

            # create the box for the info
            #self._create_sections(info)

            # refresh scrollbar
            self.scrollbar.redraw_scrollbar()

    def _create_blessing_section(self, current_y, blessing):
        # get the break image
        section_break_image = utility.get_image(
            ASSET_PATH / "ui/menu_window_n_repeat.png", (self.rect.width - self.scrollbar_width, 13)
        )

        width = self.rect.width - self.scrollbar_width

        # blessing name
        rect = pygame.Rect((0, current_y), (width, 0))
        ui_text = UITextBox(
            html_text=blessing.name,
            relative_rect=rect,
            manager=self.ui_manager,
            wrap_to_height=True,
            layer_starting_height=1,
            container=self.get_container(),
        )
        self.sections.append(ui_text)
        self.section_base_positions.append(ui_text.relative_rect.y)
        current_y += ui_text.rect.height + GAP_SIZE

        # blessing description
        rect = pygame.Rect((0, current_y), (width, 0))
        ui_text = UITextBox(
            html_text=blessing.description,
            relative_rect=rect,
            manager=self.ui_manager,
            wrap_to_height=True,
            layer_starting_height=1,
            container=self.get_container(),
        )
        self.sections.append(ui_text)
        self.section_base_positions.append(ui_text.relative_rect.y)
        current_y += ui_text.rect.height + GAP_SIZE

        # button section
        player = scripts.engine.core.matter.get_player()
        knowledge = scripts.engine.core.matter.get_entitys_component(player, Knowledge)
        for skill in knowledge.skills.values():
            if knowledge.can_add_blessing(skill, blessing):
                # blessing can be applied to this skill, so add a button for it
                apply_button = UIButton(
                    relative_rect=pygame.Rect((5, current_y), (width - 10, 40)),
                    text=skill.__name__,
                    manager=self.ui_manager,
                    container=self.get_container(),
                )
                self.sections.append(apply_button)
                self.section_base_positions.append(apply_button.relative_rect.y)
                self.apply_buttons.append((skill, blessing, apply_button))
                current_y += apply_button.rect.height + GAP_SIZE

        # create rect and image element
        image_rect = pygame.Rect((0, current_y), (section_break_image.get_width(), section_break_image.get_height()))
        ui_image = UIImage(
            relative_rect=image_rect,
            image_surface=section_break_image,
            manager=self.ui_manager,
            container=self.get_container(),
        )
        self.sections.append(ui_image)
        self.section_base_positions.append(ui_image.relative_rect.y)

        # update position
        current_y += section_break_image.get_height() + GAP_SIZE

        return current_y

    def cleanse(self):
        """
        Cleanse existing section info.
        """
        # kill the box and clear the reference
        for element in self.sections:
            element.kill()
        self.sections = []

    def _create_sections(self, info: List[Tuple[str, Union[str, pygame.Surface]]]):
        """
        Create sections for the information about the tile
        """
        sections = []
        section_base_positions = []
        current_y = 0
        current_text_block = ""

        # draw info
        x = 0
        width = self.rect.width - self.scrollbar_width
        text_height = 0  # box will resize height anyway

        # loop each image provided and use as header for each group of info
        for type_str, text_or_image in info:
            # build current text block
            if type_str == "text":
                assert isinstance(text_or_image, str)  # handle mypy error
                current_text_block += text_or_image + "<br>"

            elif type_str == "image":
                assert isinstance(text_or_image, pygame.Surface)  # handle mypy error
                # if we have text in the previous block, show it
                if current_text_block:
                    ## Display text
                    rect = pygame.Rect((x, current_y), (width, text_height))
                    ui_text = UITextBox(
                        html_text=current_text_block,
                        relative_rect=rect,
                        manager=self.ui_manager,
                        wrap_to_height=True,
                        layer_starting_height=1,
                        container=self.get_container(),
                    )
                    sections.append(ui_text)
                    section_base_positions.append(ui_text.relative_rect.y)

                    # update position
                    current_y += ui_text.rect.height + GAP_SIZE

                    # clear to prevent any carry over
                    ui_text = None
                    current_text_block = ""

                ##  Display image
                # draw info
                image_width = text_or_image.get_width()
                image_height = text_or_image.get_height()

                # if image is the icon_path then draw centre, otherwise draw left
                if image_width == ICON_SIZE:
                    draw_x = int((self.rect.width / 2) - (image_width / 2))
                else:
                    draw_x = 0

                # create rect and image element
                image_rect = pygame.Rect((draw_x, current_y), (image_width, image_height))
                ui_image = UIImage(
                    relative_rect=image_rect,
                    image_surface=text_or_image,
                    manager=self.ui_manager,
                    container=self.get_container(),
                )
                sections.append(ui_image)
                section_base_positions.append(ui_image.relative_rect.y)

                # update position
                current_y += image_height + GAP_SIZE

                # clear to prevent any carry over
                ui_image = None

        # we've left the loop, clean up left over text
        if current_text_block:
            ## Display text
            rect = pygame.Rect((x, current_y), (width, text_height))
            ui_text = UITextBox(
                html_text=current_text_block,
                relative_rect=rect,
                manager=self.ui_manager,
                wrap_to_height=True,
                layer_starting_height=1,
                container=self.get_container(),
            )
            sections.append(ui_text)
            section_base_positions.append(ui_text.relative_rect.y)

        # update main sections list
        self.sections = sections
        self.section_base_positions = section_base_positions

    def process_close_button(self):
        state.set_new(GameState.GAME_MAP)
        # post game event
        #event_hub.post(ExitMenuEvent(UIElement.ACTOR_INFO))
