import logging
import pygame
import pygame_gui
from pygame_gui.core import UIWindow
from pygame_gui.elements import UIImage, UITextBox
from scripts.engine.core.constants import PrimaryStatTypes, SecondaryStatTypes
from scripts.engine.utilities import get_class_members
from scripts.engine.components import Aesthetic, Identity, Resources


class EntityInfo(UIWindow):
    """
    Hold text relating to the game's events, to display to the player.
    """

    def __init__(self, rect: pygame.Rect, manager: pygame_gui.ui_manager.UIManager):
        self.gui_manager = manager

        # sections
        self.selected_entity = None
        self.entity_image = None
        self.core_info = None
        self.primary_stats = None
        self.secondary_stats = None
        # TODO: add affliction info

        # data
        self.gap_between_sections = 2
        self.indent = 3
        self.entity_image_height = 32
        self.entity_image_width = 32
        self.core_info_height = 80
        self.primary_stats_height = 100
        self.secondary_stats_height = 100

        # complete base class init
        super().__init__(rect, manager, ["entity_info"])

        # confirm init complete
        logging.debug(f"Entity Info initialised.")

    def update(self, time_delta: float):
        """
        Update based on current state and data. Run every frame.
        """
        super().update(time_delta)

    def handle_events(self, event):
        """
        Handle events created by this UI widget
        """
        pass

    def set_entity(self, entity: int):
        """
        Set the selected entity to show the info for that entity.
        """
        self.selected_entity = entity

    def show(self):
        """
        Show the entity info. Builds the sections required, after clearing any existing.
        """
        if self.selected_entity:
            # clear to refresh first
            self.cleanse()

            # create the various boxes for the info
            self.entity_image = self.create_entity_image_section()
            self.core_info = self.create_core_info_section()
            self.primary_stats = self.create_primary_stats_section()
            self.secondary_stats = self.create_secondary_stats_section()

    def cleanse(self):
        """
        Cleanse existing section info.
        """
        # kill the boxes and clear the references
        if self.entity_image:
            self.entity_image.kill()
            self.entity_image = None
        if self.core_info:
            self.core_info.kill()
            self.core_info = None
        if self.primary_stats:
            self.primary_stats.kill()
            self.primary_stats = None
        if self.secondary_stats:
            self.secondary_stats.kill()
            self.secondary_stats = None

    def create_entity_image_section(self):
        """
        Create the image section.

        Returns:
            UIImage:
        """
        image_width = self.entity_image_width
        image_height = self.entity_image_height
        centre_draw_x = int((self.rect.width / 2) - (image_width / 2))
        rect = pygame.Rect((centre_draw_x, self.indent), (image_width, image_height))

        # TODO - moving to the top causes import issues. Resolve this!
        from scripts.managers.world_manager.world_manager import world
        aesthetic = world.Entity.get_entitys_component(self.selected_entity, Aesthetic)
        image = pygame.transform.scale(aesthetic.sprites.icon, (image_width, image_height))

        entity_image = UIImage(relative_rect=rect, image_surface=image, manager=self.gui_manager,
                               container=self.get_container(), object_id="#entity_image")
        return entity_image

    def create_core_info_section(self):
        """
        Create the core info section.

        Returns:
            UITextBox:
        """
        entity = self.selected_entity
        # TODO - moving to the top causes import issues. Resolve this!
        from scripts.managers.world_manager.world_manager import world
        identity = world.Entity.get_entitys_component(entity, Identity)
        resources = world.Entity.get_entitys_component(entity, Resources)
        text = f"{identity.name.capitalize()}" + "<br>"
        text += f"Current Health: {resources.health}" + "<br>"
        text += f"Current Stamina: {resources.stamina}" + "<br>"

        x = self.indent
        y = (self.gap_between_sections * 2) + self.indent + self.entity_image_height
        width = self.rect.width - (self.indent * 2)
        height = self.core_info_height

        rect = pygame.Rect((x, y), (width, height))
        core_info = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#core_info",
                              container=self.get_container())
        return core_info

    def create_primary_stats_section(self):
        """
        Create the primary stats section.

        Returns:
            UITextBox:
        """
        text = ""
        # TODO - moving to the top causes import issues. Resolve this!
        from scripts.managers.world_manager.world_manager import world
        stats = world.Entity.get_combat_stats(self.selected_entity)

        all_stats = get_class_members(PrimaryStatTypes)
        for name in all_stats:
            try:
                stat_value = getattr(stats, name.lower())

                name = name.title()
                name = name.replace("_", " ")

                text += f"{name}: {stat_value}" + "<br>"

            # in case it fails to pull expected attribute
            except AttributeError:
                logging.warning(f"Attribute {name} not found for EntityInfo.")

        x = self.indent
        y = (self.gap_between_sections * 3) + self.indent + self.entity_image_height + self.core_info_height
        width = self.rect.width - (self.indent * 2)
        height = self.primary_stats_height
        rect = pygame.Rect((x, y), (width, height))
        primary_stats = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                                  wrap_to_height=False, layer_starting_height=1, object_id="#primary_stats",
                                  container=self.get_container())
        return primary_stats

    def create_secondary_stats_section(self):
        """
        Create the secondary stats section.

        Returns:
            UITextBox:
        """
        text = ""
        # TODO - moving to the top causes import issues. Resolve this!
        from scripts.managers.world_manager.world_manager import world
        stats = world.Entity.get_combat_stats(self.selected_entity)

        all_stats = get_class_members(SecondaryStatTypes)
        for name in all_stats:
            try:
                stat_value = getattr(stats, name.lower())

                name = name.title()
                name = name.replace("_", " ")

                text += f"{name}: {stat_value}" + "<br>"

            # in case it fails to pull expected attribute
            except AttributeError:
                logging.warning(f"Attribute {name} not found for EntityInfo.")

        x = self.indent
        y = (self.gap_between_sections * 3) + self.indent + self.entity_image_height + self.core_info_height + \
            self.primary_stats_height
        width = self.rect.width - (self.indent * 2)
        height = self.secondary_stats_height
        rect = pygame.Rect((x, y), (width, height))
        secondary_stats = UITextBox(html_text=text, relative_rect=rect, manager=self.gui_manager,
                              wrap_to_height=False, layer_starting_height=1, object_id="#secondary_stats",
                              container=self.get_container())
        return secondary_stats