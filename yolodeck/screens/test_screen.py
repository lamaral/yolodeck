from yolodeck.screens.base_screen import BaseScreen
from yolodeck.buttons.clock_button import ClockButton


class TestScreen(BaseScreen):
    def __init__(self, key_no):
        super().__init__(key_no)

    def initialize(self):
        with self._renderer as r:
            r\
                .text('OUTPUT \nNOT FOUND')\
                .color('red')\
                .center_vertically()\
                .center_horizontally()\
                .font_size(85)\
                .text_align('center')\
                .end()
        return

    def screen_buttons(self):
        self.register_button(14, ClockButton)
