import unittest
from kivy.clock import mainthread  # Import mainthread decorator for Kivy tests
from kivy.tests.common import GraphicUnitTest  # Import GraphicUnitTest for Kivy UI tests
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from main import MainApp  # Import your MainApp class

class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.app = MainApp()
        self.app.build()
        self.text_input = self.app.solution

    def tearDown(self):
        pass

    def test_on_button_press(self):
        # Test button press with valid input
        self.text_input.text = "123"
        button = Button(text="4")
        self.app.on_button_press(button)
        self.assertEqual(self.text_input.text, "1234")

        # Test button press with operator after number
        self.text_input.text = "123"
        operator_button = Button(text="+")
        self.app.on_button_press(operator_button)
        self.assertEqual(self.text_input.text, "123+")

        # Test button press with C (clear) button
        self.text_input.text = "123"
        clear_button = Button(text="C")
        self.app.on_button_press(clear_button)
        self.assertEqual(self.text_input.text, "")

    def test_on_solution(self):
        # Test solution for valid expression
        self.text_input.text = "2 + 2"
        solution_button = Button(text="=")
        self.app.on_solution(solution_button)
        self.assertEqual(self.text_input.text, "4")

        # Test solution for division by zero
        self.text_input.text = "5 / 0"
        self.app.on_solution(solution_button)
        self.assertEqual(self.text_input.text, "Error: Cannot Divide by Zero")

        # Test solution for invalid expression
        self.text_input.text = "2 * (3 + 4))"
        self.app.on_solution(solution_button)
        self.assertEqual(self.text_input.text, "Error: Invalid Expression")

if __name__ == "__main__":
    unittest.main()
