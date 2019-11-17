import logging
from scripts.core.constants import InputStates, VisualInfo, ICON_SIZE, PrimaryStatTypes, SecondaryStatTypes
from scripts.ui.basic.fonts import Font
from scripts.ui.basic.palette import Palette
from scripts.ui.templates.frame import Frame
from scripts.ui.templates.text_box import TextBox
from scripts.ui.templates.ui_element import UIElement
from scripts.ui.templates.widget_style import WidgetStyle


class EntityInfo(UIElement):
    """
    Hold text relating to the game's events, to display to the player.
    """
    def __init__(self):
        # state and info
        self.selected_entity = None

        # size and position
        width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        x = VisualInfo.BASE_WINDOW_WIDTH - width
        y = VisualInfo.BASE_WINDOW_HEIGHT - height

        # create style
        palette = Palette().entity_info
        font = Font().entity_info
        font_colour = palette.text_default
        bg_colour = palette.background
        border_colour = palette.border
        border_size = 2

        base_style1 = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        base_style2 = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        base_style3 = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        base_style4 = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                 font_colour=font_colour, border_size=border_size)
        base_style5 = WidgetStyle(font=font, background_colour=bg_colour, border_colour=border_colour,
                                  font_colour=font_colour, border_size=border_size)

        children = []
        edge = 5

        # create child widgets
        frame_x = (width / 2) - (ICON_SIZE / 2)  # find centre and then move half the width of the icon to the left
        frame_y = edge
        frame = Frame(base_style1, frame_x, frame_y, ICON_SIZE, ICON_SIZE, [], "icon_frame")
        
        info_y = frame_y + ICON_SIZE + edge
        info_height = base_style1.font.size * 6  # size * 2 is same as a line's height, need 3 lines
        info_text_box = TextBox(base_style2, edge, info_y, width - (edge * 2), info_height - (edge * 2),  [],
                                "current_info")

        primary_y = info_y + info_height + edge
        text_height = (height - primary_y - (edge * 2)) / 2
        primary_text_box = TextBox(base_style3, edge, primary_y, width - (edge * 2), text_height - (edge * 2),
                                   [], "primary_stats")
        secondary_y = primary_y + text_height + edge
        secondary_text_box = TextBox(base_style4, edge, secondary_y, width - (edge * 2), text_height - (edge * 2),
                                     [], "secondary_stats")

        # add children
        children.append(frame)
        children.append(info_text_box)
        children.append(primary_text_box)
        children.append(secondary_text_box)

        # complete base class init
        super().__init__(base_style5, x, y, width, height, children)

        # confirm init complete
        logging.debug(f"EntityInfo initialised.")

    def update(self):
        """
        If dirty update entity's icon, info and stats
        """
        if self.is_dirty:
            self.update_icon()
            self.update_current_info()
            self.update_primary_stats()
            self.update_secondary_stats()
            self.update_affliction_info()

        super().update()

    def draw(self, main_surface):
        """
        Draw the text log.

        Args:
            main_surface ():
        """
        super().draw(self.surface)

        # blit to the main surface
        main_surface.blit(self.surface, (self.rect.x, self.rect.y))

    def handle_input(self, input_key, input_state: InputStates = InputStates.PRESSED):
        """
        Process received input

        Args:
            input_key (): input received. Mouse, keyboard, gamepad.
            input_state (): pressed or released
        """
        pass

    def set_selected_entity(self, entity):
        """
        Update the info held for the new entity

        Args:
            entity ():
        """
        self.selected_entity = entity
        self.is_dirty = True

    def update_icon(self):
        """
        Update the entity icon
        """
        for child in self.children:
            if child.name == "icon_frame":
                child.base_style.background_image = self.selected_entity.icon
                break

    def update_current_info(self):
        """
        Update the current info text box
        """
        for child in self.children:
            if child.name == "current_info":
                entity = self.selected_entity
                child.add_text(f"{entity.name.capitalize()}")
                child.add_text(f"Current Health: {entity.combatant.hp}")
                child.add_text(f"Current Stamina: {entity.combatant.stamina}")
                child.update_text_shown()
                break

    def update_primary_stats(self):
        """
        Update the primary stats text box
        """
        for child in self.children:
            if child.name == "primary_stats":
                stats = self.selected_entity.combatant.primary_stats

                for stat in PrimaryStatTypes:
                    try:
                        stat_value = getattr(stats, stat.name.lower())
                        name = stat.name.title()
                        name = name.replace("_", " ")

                        child.add_text(f"{name}: {stat_value}")

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"Attribute {stat} not found for EntityInfo.")

                child.update_text_shown()
                break

    def update_secondary_stats(self):
        """
        Update the secondary stats text box
        """
        for child in self.children:
            if child.name == "secondary_stats":
                stats = self.selected_entity.combatant.secondary_stats

                for stat in SecondaryStatTypes:
                    try:
                        stat_value = getattr(stats, stat.name.lower())
                        name = stat.name.title()
                        name = name.replace("_", " ")

                        child.add_text(f"{name}: {stat_value}")

                    # in case it fails to pull expected attribute
                    except AttributeError:
                        logging.warning(f"Attribute {stat} not found for EntityInfo.")

                child.update_text_shown()
                break

    def update_affliction_info(self):
        """
        Update the affliction info text box
        """
        pass

        # from scripts.global_singletons.managers import world
        # afflictions = world.Affliction.get_afflictions_for_entity(entity)
        # affliction_info = []
        # for affliction in afflictions:
        #     affliction_info.append(affliction.name + ":" + str(affliction.duration))
        # second_section_column_one_text.append(f"")
        # second_section_column_one_text.append(f"Afflicted by: {affliction_info}")