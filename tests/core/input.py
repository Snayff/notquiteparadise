import unittest
import mock
from scripts.core.input import check_mouse_input


class TestMouseInput(unittest.TestCase):
    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_left_click(self, mock_pygame_get_pressed):
        # mock the mouse button
        mock_pygame_get_pressed.return_value = (True, False, False)
        input_values = {"left_click": False}

        check_mouse_input(input_values)

        self.assertTrue(input_values["left_click"])

    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_no_left_click(self, mock_pygame_get_pressed):
        mock_pygame_get_pressed.return_value = (False, False, False)
        input_values = {"left_click": False}

        check_mouse_input(input_values)

        self.assertFalse(input_values["left_click"])

    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_middle_click(self, mock_pygame_get_pressed):
        mock_pygame_get_pressed.return_value = (False, True, False)
        input_values = {"middle_click": False}

        check_mouse_input(input_values)

        self.assertTrue(input_values["middle_click"])

    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_no_middle_click(self, mock_pygame_get_pressed):
        mock_pygame_get_pressed.return_value = (False, False, False)
        input_values = {"middle_click": False}

        check_mouse_input(input_values)

        self.assertFalse(input_values["middle_click"])

    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_right_click(self, mock_pygame_get_pressed):
        mock_pygame_get_pressed.return_value = (False, False, True)
        input_values = {"right_click": False}

        check_mouse_input(input_values)

        self.assertTrue(input_values["right_click"])

    @mock.patch("pygame.mouse.get_pressed")
    def test_check_mouse_input_for_no_right_click(self, mock_pygame_get_pressed):
        mock_pygame_get_pressed.return_value = (False, False, False)
        input_values = {"right_click": False}

        check_mouse_input(input_values)

        self.assertFalse(input_values["right_click"])