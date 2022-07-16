from yolodeck.rendering import Renderer


class BaseButton:
    def __init__(self, key_no, **kwargs):
        self._screen_manager = None
        self._renderer = None
        self._key_no = key_no
        self.settings = kwargs

    def set_screen_manager(self, screen_manager):
        self._screen_manager = screen_manager
        self._renderer = Renderer(self._key_no, screen_manager)

    def clear_screen_manager(self):
        self._screen_manager = None

    def screen_manager(self):
        return self._screen_manager

    def dispose(self):
        pass

    def initialize(self):
        pass

    def pressed(self):
        pass

    def released(self):
        pass
