from datetime import datetime
from time import sleep

from yolodeck.buttons.base_button import BaseButton


class DummyButton(BaseButton):

    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)

    def initialize(self):
        with self._renderer as r:
            now = datetime.now()
            r.text('DUMMY') \
                .center_horizontally() \
                .center_vertically(-100) \
                .font_size(120) \
                .end()
