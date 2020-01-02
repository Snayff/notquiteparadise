import pygame


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
        if event.key == pygame.K_UP or event.key == pygame.K_KP8 or event.key == pygame.K_k:
            self.input_values["up"] = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2 or event.key == pygame.K_j:
            self.input_values["down"] = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4 or event.key == pygame.K_h:
            self.input_values["left"] = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6 or event.key == pygame.K_l:
            self.input_values["right"] = True
        elif event.key == pygame.K_KP7 or event.key == pygame.K_y:
            self.input_values["up_left"] = True
        elif event.key == pygame.K_KP9 or event.key == pygame.K_u:
            self.input_values["up_right"] = True
        elif event.key == pygame.K_KP1 or event.key == pygame.K_b:
            self.input_values["down_left"] = True
        elif event.key == pygame.K_KP3 or event.key == pygame.K_n:
            self.input_values["down_right"] = True

    def set_intent(self, intent):
        pass