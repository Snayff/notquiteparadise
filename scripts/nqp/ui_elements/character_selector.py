from __future__ import annotations

import logging
from typing import Callable, Optional, TYPE_CHECKING, Union

import pygame
import pygame_gui
from pygame import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIButton, UIDropDownMenu, UIImage, UIPanel, UITextBox

from scripts.engine.internal import library
from scripts.engine.internal.constant import GameEvent, GAP_SIZE, RenderLayer, TILE_SIZE, TraitGroup
from scripts.engine.internal.definition import ActorData
from scripts.engine.core.utility import build_sprites_from_paths


from scripts.engine.widgets.panel import Panel

if TYPE_CHECKING:
    from typing import Dict, List

__all__ = ["CharacterSelector"]


class CharacterSelector(Panel):
    """
    A menu widget. Used to hold a collection of text, images, buttons etc. Expects to have buttons and provides
    functionality to handle the clicks
    """

    def __init__(self, rect: Rect, manager: UIManager):

        self.button_events: Dict[str, Union[pygame.event.Event, Callable]] = {
            "confirm": self._post_confirm_event,
        }

        # containers for created widgets
        self.buttons: List[UIButton] = []
        self.drop_downs: List[UIDropDownMenu] = []
        self.text_boxes: List[UITextBox] = []
        self.ui_image: Optional[UIImage] = None

        # complete base class init
        super().__init__(rect, RenderLayer.BOTTOM, manager, object_id="character_selector")

        self._init_buttons()
        self._init_drop_downs()
        self._refresh_info()

        # confirm init complete
        logging.debug(f"CharacterSelector initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def process_event(self, event):
        super().process_event(event)

        # only progress for user events
        if event.type != pygame.USEREVENT:
            return

        # handle button presses
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

            # Find out which button we are clicking
            button = event.ui_element

            # post the new event
            if button in self.buttons:
                # get the id
                ids = event.ui_object_id.split(".")
                button_id = ids[-1]  # get last element
                new_event = self.button_events[button_id]

                # post a blank event or process the func
                if isinstance(new_event, pygame.event.EventType):
                    pygame.event.post(new_event)
                else:
                    new_event()

                logging.debug(f"CharacterSelector button '{button_id}' pressed.")

        # handle new selection in drop downs
        if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            self._refresh_info()

    def _init_buttons(self):
        """
        Init the buttons for the menu
        """
        manager = self.ui_manager

        # set button dimensions
        max_width = self.rect.width
        max_height = self.rect.height
        height = int(max_height / 12)
        width = int(max_width / 6)
        x = -width  # anchor top right
        y = 0

        button = UIButton(
            relative_rect=Rect((x, y), (width, height)),
            anchors={"left": "right", "right": "right", "top": "top", "bottom": "bottom"},
            manager=manager,
            container=self,
            text="Embark",
            tool_tip_text="Confirm your selection and embark on your adventure.",
            object_id="confirm",
        )

        self.buttons.append(button)

    def _init_drop_downs(self):
        """
        Initialise the drop downs for the menu
        """
        people = []
        savvy = []
        homeland = []

        manager = self.ui_manager
        max_width = self.rect.width
        max_height = self.rect.height
        num_drop_downs = 3
        gap = GAP_SIZE
        width = int((max_width / num_drop_downs) - (gap * num_drop_downs + 2))
        height = int(max_height / 12)
        start_x = 0
        start_y = int(max_height / 2)  # anchored to the bottom left
        max_expansion = int(start_y - height)

        # get traits
        for key, trait in library.TRAITS.items():
            if trait.group == TraitGroup.PEOPLE:
                people.append(key)
            elif trait.group == TraitGroup.SAVVY:
                savvy.append(key)
            elif trait.group == TraitGroup.HOMELAND:
                homeland.append(key)

        # bundle trait lists with group name
        all_traits = [(people, TraitGroup.PEOPLE), (savvy, TraitGroup.SAVVY), (homeland, TraitGroup.SAVVY)]

        # create drop downs
        count = 0
        for traits, trait_group in all_traits:
            x = start_x + (count * (width + gap))
            rect = Rect((x, start_y), (width, height))
            drop_down = UIDropDownMenu(
                options_list=traits,
                starting_option=traits[0],
                relative_rect=rect,
                manager=manager,
                container=self,
                object_id=trait_group,
                expansion_height_limit=max_expansion,
            )

            count += 1
            self.drop_downs.append(drop_down)

    def _refresh_info(self):
        """
        Update the image and text in line with drop down selections
        """
        # image dimensions
        image_width = TILE_SIZE * 4
        image_height = TILE_SIZE * 4
        image_x = int((self.rect.width / 2) - (image_width / 2))
        image_y = int(self.rect.height / 10)
        image_rect = Rect((image_x, image_y), (image_width, image_height))

        # clear ui image if it exists
        if self.ui_image:
            self.ui_image.kill()
            self.ui_image = None

        # clear text box if it exists
        if self.text_boxes:
            for text_box in self.text_boxes:
                text_box.kill()
            self.text_boxes = []

        # get info from traits
        sprite_paths = []
        info = {}
        info_rects = []
        text_size = 4
        col = "#ffffff"
        for drop_down in self.drop_downs:
            trait = library.TRAITS[drop_down.selected_option]
            sprite_paths.append(trait.sprite_paths)
            info[trait.name] = [
                f"<font face=barlow color={col} size={text_size}>"
                # f"{trait.name} <br>",
                f"{trait.description} <br>",
                f"<br>",
                f"Clout: {trait.clout} <br>",
                f"Vigour: {trait.vigour} <br>",
                f"Skullduggery: {trait.skullduggery} <br>",
                f"Bustle: {trait.bustle} <br>",
                f"Exactitude: {trait.exactitude} <br>",
                f"Permanent Afflictions: {trait.permanent_afflictions} <br>",
                f"</font",
            ]

            # info dimensions
            drop_down_rect = drop_down.rect
            info_width = drop_down_rect.width
            info_height = int((self.rect.height - drop_down_rect.y) - drop_down_rect.height)
            info_x = drop_down_rect.x
            info_y = drop_down_rect.y + drop_down_rect.height
            info_rects.append(Rect((info_x, info_y), (info_width, info_height)))

        # sort and build into sprites
        sprite_paths.sort(key=lambda path: path.render_order, reverse=True)
        sprites = build_sprites_from_paths(sprite_paths, (image_width, image_height))

        # create UI image
        ui_image = UIImage(
            relative_rect=image_rect,
            image_surface=sprites.idle,
            manager=self.ui_manager,
            container=self,
        )
        self.ui_image = ui_image

        # create the text boxes
        count = 0
        for name, details in info.items():
            text_box = UITextBox(
                html_text=" ".join(details),
                relative_rect=info_rects[count],
                manager=self.ui_manager,
                object_id="name",
                container=self,
            )
            count += 1
            self.text_boxes.append(text_box)

    def _post_confirm_event(self):
        """
        Post the confirm event to be picked up elsewhere. Includes the selected data.
        """
        # get trait names
        traits = []
        for drop_down in self.drop_downs:
            traits.append(drop_down.selected_option)

        # get player data
        player_data = ActorData(
            key="player",
            possible_names=["player"],
            description="Player desc",
            position_offsets=[(0, 0)],
            trait_names=traits,
        )

        # fire event
        new_event = pygame.event.Event(GameEvent.START_GAME, player_data=player_data)
        pygame.event.post(new_event)
