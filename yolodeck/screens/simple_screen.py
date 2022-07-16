from yolodeck.screens.base_screen import BaseScreen
from yolodeck.screens.test_screen import TestScreen
from yolodeck.buttons.clock_button import ClockButton


class SimpleScreen(BaseScreen):
    def __init__(self, key_no):
        super().__init__(key_no)

    def screen_buttons(self):
        self.register_button(0, ClockButton)
        self.register_button(7, TestScreen)
