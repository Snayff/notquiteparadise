import pygame

from scripts.core.constants import InputIntents


class ValueMethods:
    """
    Methods for handling Input values and converting them to intents

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.new_input_manager import InputManager
        self.manager = manager  # type: InputManager

    def reset_intents(self):
        """
        Reset all input intents to false
        """
        for field in self.manager.Intent.fields:
            if field.type is bool:
                setattr(self.manager.Intent, field.name, False)

    def check_directions(self, event):
        """
        get directional input from the keyboard

        Args:
            event (pygame.event):
        """
        # TODO - refer to key mapping to enable key rebinding
        if event.key == pygame.K_UP or event.key == pygame.K_KP8 or event.key == pygame.K_k:
            self.set_intent(InputIntents.UP)
        elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2 or event.key == pygame.K_j:
            self.set_intent(InputIntents.DOWN)
        elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4 or event.key == pygame.K_h:
            self.set_intent(InputIntents.LEFT)
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6 or event.key == pygame.K_l:
            self.set_intent(InputIntents.RIGHT)
        elif event.key == pygame.K_KP7 or event.key == pygame.K_y:
            self.set_intent(InputIntents.UP_LEFT)
        elif event.key == pygame.K_KP9 or event.key == pygame.K_u:
            self.set_intent(InputIntents.UP_RIGHT)
        elif event.key == pygame.K_KP1 or event.key == pygame.K_b:
            self.set_intent(InputIntents.DOWN_LEFT)
        elif event.key == pygame.K_KP3 or event.key == pygame.K_n:
            self.set_intent(InputIntents.DOWN_RIGHT)

    def set_intent(self, intent: InputIntents):
        """
        Set an intent to true. Intent must exist in InputIntents and name must match (except case).

        Args:
            intent ():
        """
        setattr(self.manager.Intentm, intent.name.lower(), True)