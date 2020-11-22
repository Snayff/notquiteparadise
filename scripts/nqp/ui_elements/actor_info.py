from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import pygame
from pygame_gui.core import UIElement as PygameUiElement
from pygame_gui.elements import UIImage, UITextBox, UIVerticalScrollBar
from snecs.typedefs import EntityID

from scripts.engine.core import utility, world
from scripts.engine.internal.component import Aesthetic, Afflictions, Identity, Resources, Traits
from scripts.engine.internal.constant import (
    ASSET_PATH,
    GameEvent,
    GAP_SIZE,
    ICON_SIZE,
    INFINITE,
    PrimaryStat,
    SecondaryStat,
    UIElement,
)
from scripts.engine.core.utility import get_class_members
from scripts.engine.widgets.window import Window

if TYPE_CHECKING:
    from typing import List, Optional, Tuple, Union
    from pygame_gui import UIManager


class ActorInfo(Window):
    """
    Full detail about an npc entity.
    """

    def __init__(self, rect: pygame.Rect, manager: UIManager):

        # sections
        self.selected_entity: Optional[EntityID] = None
        self.sections: List[PygameUiElement] = []

        # complete base class init
        super().__init__(rect, manager, object_id="actor_info")

        # setup scroll bar
        self.scrollbar_width = 50
        self.scrollbar = UIVerticalScrollBar(
            pygame.Rect((rect.width - self.scrollbar_width, 0), (self.scrollbar_width, rect.height)),
            0.5,
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
        logging.debug(f"Actor Info initialised.")

    ############## GET / SET ########################

    def set_entity(self, entity: EntityID):
        """
        Set the selected entity to show the info for that entity.
        """
        self.selected_entity = entity

    ############### ACTIONS #########################

    def show(self):
        """
        Show the entity info. Builds the sections required, after clearing any existing.
        """
        super().show()

        self.visible = True
        entity = self.selected_entity

        # clear to refresh first
        self.cleanse()

        if entity:

            info: List[Tuple[str, Union[str, pygame.Surface]]] = []
            section_break_image = utility.get_image(
                ASSET_PATH / "ui/menu_window_n_repeat.png", (self.rect.width - self.scrollbar_width, 13)
            )

            # get aesthetic
            aesthetic = world.get_entitys_component(entity, Aesthetic)
            info.append(("image", aesthetic.sprites.icon))

            # get identity
            identity = world.get_entitys_component(entity, Identity)
            info.append(("text", identity.name))

            # get resources
            resources = world.get_entitys_component(entity, Resources)
            if resources:
                info.append(("text", f"Health: {resources.health}"))
                info.append(("text", f"Stamina: {resources.stamina}"))
                info.append(("image", section_break_image))

            # get stats
            stats = world.create_combat_stats(entity)
            if stats:
                primary_stats = utility.get_class_members(PrimaryStat)
                for name in primary_stats:
                    try:
                        stat_value = getattr(stats, name.lower())

                        name = name.title()
                        name = name.replace("_", " ")
                        info.append(("text", f"{name}: {stat_value}"))

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"ActorInfo: attribute {name} not found in primary stats.")

                secondary_stats = get_class_members(SecondaryStat)
                for name in secondary_stats:
                    # FIXME - HEALTH and STAMINA not found
                    try:
                        stat_value = getattr(stats, name.lower())

                        name = name.title()
                        name = name.replace("_", " ")
                        info.append(("text", f"{name}: {stat_value}"))

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"ActorInfo: attribute {name} not found in secondary stats.")

                info.append(("image", section_break_image))

            #  get traits
            traits = world.get_entitys_component(entity, Traits)
            if traits:
                names = ""
                for name in traits.names:
                    # if more than one trait add a separator
                    if len(names) > 1:
                        names += ", "
                    names += f"{name}"
                info.append(("text", names))
                info.append(("image", section_break_image))

            # get afflictions
            afflictions = world.get_entitys_component(entity, Afflictions)
            if afflictions:
                for affliction in afflictions.active:
                    # get duration
                    if affliction.duration == INFINITE:
                        duration = "∞"
                    else:
                        duration = affliction.duration
                    affliction_icon = utility.get_image(affliction.icon_path, (32, 32))
                    info.append(("image", affliction_icon))
                    info.append(("text", f"{affliction.key.title()}: {duration}"))

                # if no afflictions, say so
            if not afflictions:
                info.append(("text", "Not afflicted."))

            # create the box for the info
            self._create_sections(info)

            # refresh scrollbar
            self.scrollbar.redraw_scrollbar()

    def cleanse(self):
        """
        Cleanse existing section info.
        """
        # kill the box and clear the reference
        for element in self.sections:
            element.kill()
        self.sections = []

    def process_close_button(self):
        event = pygame.event.Event(GameEvent.EXIT_MENU, menu=UIElement.ACTOR_INFO)
        pygame.event.post(event)

    ############## CREATE ########################

    def _create_sections(self, info: List[Tuple[str, Union[str, pygame.Surface]]]):
        """
        Create sections for the information about the tile
        """
        sections = []
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

        # update main sections list
        self.sections = sections
