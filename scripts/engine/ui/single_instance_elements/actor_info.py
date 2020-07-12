from __future__ import annotations

import logging
import pygame
from typing import List, Optional, Tuple, Union
from pygame_gui import UIManager, UI_BUTTON_PRESSED
from pygame_gui.core import UIElement as PygameUiElement
from pygame_gui.elements import UIImage, UIPanel, UITextBox, UIVerticalScrollBar, UIWindow
from snecs.typedefs import EntityID
from scripts.engine import state, utility, world
from scripts.engine.component import Aesthetic, Afflictions, Identity, Resources, Traits
from scripts.engine.core.constants import EventType, GAP_SIZE, ICON_SIZE, INFINITE, PrimaryStat, SecondaryStat, \
    UIElement
from scripts.engine.utility import get_class_members


class ActorInfo(UIWindow):
    """
    Full detail about an npc entity.
    """
    # TODO - change to window
    # TODO  - change state when selected

    def __init__(self, rect: pygame.Rect, manager: UIManager):

        # sections
        self.selected_entity: Optional[EntityID] = None
        self.sections: List[PygameUiElement] = []

        # complete base class init
        super().__init__(rect, manager, element_id="actor_info")

        # setup scroll bar
        self.scrollbar_width = 50
        self.scrollbar = UIVerticalScrollBar(pygame.Rect((rect.width - self.scrollbar_width, 0),
                                                         (self.scrollbar_width, rect.height)), 0.5, manager,
                                             self.get_container(), self, "#scrollbar")

        # block mouse clicks outside of menu
        self.set_blocking(True)

        # show self
        self.show()

        # confirm init complete
        logging.debug(f"Actor Info initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI element. Method must exist, even if stubbed.
        """
        pass

    def process_event(self, event: pygame.event.Event) -> bool:
        """
        Handles resizing & closing windows. Gives UI Windows access to pygame events. Derived
        windows should super() call this class if they implement their own process_event method.

        NOTE: Copied from pygame_gui UIWindow to allow overwriting use of close button.

        """
        consumed_event = False

        if self.is_blocking and event.type == pygame.MOUSEBUTTONDOWN:
            consumed_event = True

        if (self is not None and
                event.type == pygame.MOUSEBUTTONDOWN and
                event.button in [pygame.BUTTON_LEFT,
                                 pygame.BUTTON_MIDDLE,
                                 pygame.BUTTON_RIGHT]):
            scaled_mouse_pos = self.ui_manager.calculate_scaled_mouse_position(event.pos)

            edge_hovered = (self.edge_hovering[0] or self.edge_hovering[1] or
                            self.edge_hovering[2] or self.edge_hovering[3])
            if (self.is_enabled and
                    event.button == pygame.BUTTON_LEFT and
                    edge_hovered):
                self.resizing_mode_active = True
                self.start_resize_point = scaled_mouse_pos
                self.start_resize_rect = self.rect.copy()
                consumed_event = True
            elif self.hover_point(scaled_mouse_pos[0], scaled_mouse_pos[1]):
                consumed_event = True

        if (self is not None and event.type == pygame.MOUSEBUTTONUP and
                event.button == pygame.BUTTON_LEFT and self.resizing_mode_active):
            self.resizing_mode_active = False

        if (event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED
                and event.ui_element == self.close_window_button):
            self.process_close_button()

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
            # TODO - replace with non-placeholder image
            section_break_image = utility.get_image("assets/ui/menu_window_n_repeat.png",
                                                    (self.rect.width - self.scrollbar_width, 13))

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
                    info.append(("text", f"{affliction.name.title()}: {duration}"))

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
        """
        Override close button to post an Exit Menu event.
        """
        event = pygame.event.Event(EventType.EXIT_MENU, menu=UIElement.ACTOR_INFO)
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
                current_text_block += text_or_image + "<br>"

            elif type_str == "image":

                # if we have text in the previous block, show it
                if current_text_block:
                    ## Display text
                    rect = pygame.Rect((x, current_y), (width, text_height))
                    ui_text = UITextBox(html_text=current_text_block, relative_rect=rect, manager=self.ui_manager,
                                        wrap_to_height=True, layer_starting_height=1,
                                        container=self.get_container())
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

                # if image is the icon then draw centre, otherwise draw left
                if image_width == ICON_SIZE:
                    draw_x = int((self.rect.width / 2) - (image_width / 2))
                else:
                    draw_x = 0

                # create rect and image element
                image_rect = pygame.Rect((draw_x, current_y), (image_width, image_height))
                ui_image = UIImage(relative_rect=image_rect, image_surface=text_or_image, manager=self.ui_manager,
                                   container=self.get_container())
                sections.append(ui_image)

                # update position
                current_y += image_height + GAP_SIZE

                # clear to prevent any carry over
                ui_image = None

        # we've left the loop, clean up left over text
        if current_text_block:
            ## Display text
            rect = pygame.Rect((x, current_y), (width, text_height))
            ui_text = UITextBox(html_text=current_text_block, relative_rect=rect, manager=self.ui_manager,
                                wrap_to_height=True, layer_starting_height=1,
                                container=self.get_container())
            sections.append(ui_text)



        # update main sections list
        self.sections = sections


