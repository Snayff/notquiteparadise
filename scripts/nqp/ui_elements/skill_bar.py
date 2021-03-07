from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pygame
import pygame_gui
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

import scripts.engine.core.entity
from scripts.engine.core import utility, world
from scripts.engine.core.component import Knowledge
from scripts.engine.internal import library
from scripts.engine.internal.constant import (
    EventType,
    GAP_SIZE,
    ICON_SIZE,
    InputEventType,
    InputIntent,
    RenderLayer,
    SKILL_BUTTON_SIZE,
)
from scripts.engine.widgets.panel import Panel

if TYPE_CHECKING:
    from typing import List

__all__ = ["SkillBar"]


class SkillBar(Panel):
    """
    Display and hold the info for the skills in the skill bar.
    """

    def __init__(self, rect: Rect, manager: UIManager):
        self.button_events = {
            "skill_0": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL0
            ),
            "skill_1": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL1
            ),
            "skill_2": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL2
            ),
            "skill_3": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL3
            ),
            "skill_4": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL4
            ),
            "skill_5": pygame.event.Event(
                EventType.INPUT, subtype=InputEventType.SKILL_BAR_CLICK, skill_intent=InputIntent.SKILL5
            ),
        }

        self.buttons: List[UIButton] = []

        self.button_start_x = GAP_SIZE
        self.button_start_y = GAP_SIZE
        self.button_width = SKILL_BUTTON_SIZE
        self.button_height = SKILL_BUTTON_SIZE
        self.space_between_buttons = GAP_SIZE

        # complete base class init
        super().__init__(
            rect,
            RenderLayer.UI_BASE,
            manager,
            object_id=ObjectID("#skill_bar", "@gui"),
            anchors={"left": "left", "right": "right", "top": "bottom", "bottom": "bottom"},
        )

        self._init_buttons()
        self.refresh_skills()

        # confirm init complete
        logging.debug(f"SkillBar initialised.")

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)

        # only progress for user events
        if event.type != pygame.USEREVENT:
            return

        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

            # Find out which button we are clicking
            button = event.ui_element

            # post the new event
            if button in self.buttons:
                # get the id
                ids = event.ui_object_id.split(".")
                button_id = ids[-1]  # get last element
                new_event = self.button_events[button_id]
                pygame.event.post(new_event)

                logging.debug(f"SkillBar button '{ids}' was pressed.")

    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        # extract values for performance
        start_x = self.button_start_x
        y = self.button_start_y
        info = self.button_events
        width = self.button_width
        height = self.button_height
        gap = self.space_between_buttons
        manager = self.ui_manager

        count = 0
        for name in info.keys():
            x = start_x + ((width + gap) * count)

            button = UIButton(
                relative_rect=Rect((x, y), (width, height)),
                text=f"{count + 1}",
                manager=manager,
                container=self,
                object_id=f"{name}",
            )

            self.buttons.append(button)

            count += 1

    def refresh_skills(self):
        """
        Reload the player skills and assign the correct images. All buttons set to blank if player doesnt exist.
        """
        blank_icon = pygame.Surface((ICON_SIZE, ICON_SIZE), pygame.SRCALPHA, 32)
        blank_icon = blank_icon.convert_alpha()

        try:
            player = scripts.engine.core.entity.get_player()
            knowledge = scripts.engine.core.entity.get_entitys_component(player, Knowledge)
            amount_known_skills = len(knowledge.skill_order)

            for count, button in enumerate(self.buttons):
                if count <= amount_known_skills - 1:
                    icon = utility.get_image(library.SKILLS[knowledge.skill_order[count]].icon_path)
                else:
                    icon = blank_icon

                self._set_skill_image(button, icon)

        except ValueError:
            # no player, load blank images
            for button in self.buttons:
                self._set_skill_image(button, blank_icon)

    @staticmethod
    def _set_skill_image(button: UIButton, surface: pygame.Surface):
        """
        Set the image for the skill
        """
        button.normal_image = surface
        button.hovered_image = surface
        button.selected_image = surface
        button.rebuild()
