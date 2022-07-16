import threading
from datetime import datetime
from time import sleep

from yolodeck.buttons.base_button import BaseButton


class ClockButton(BaseButton):

    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.thread = None
        self.running = False

    def initialize(self):
        self.thread = threading.Thread(target=self._update_display)
        self.running = True
        self.thread.start()

    def _update_display(self):
        while self.running is True:
            with self._renderer as r:
                now = datetime.now()
                r.text(now.strftime("%H:%M")) \
                    .center_horizontally() \
                    .center_vertically(-100) \
                    .font_size(150) \
                    .end()
                r.text(now.strftime("%Y-%m-%d")) \
                    .center_horizontally() \
                    .center_vertically(100) \
                    .font_size(75) \
                    .end()
            sleep(1)

    def suspend(self):
        self.running = False

    def resume(self):
        self.running = True

    def dispose(self):
        self.running = False
        if self.thread:
            self.thread.join()
