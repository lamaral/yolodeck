import logging

from yolodeck.buttons.base_button import BaseButton


class BaseScreen(BaseButton):
    def __init__(self, key_no):
        self._logger = logging.getLogger('yolodeck')
        self._screen_manager = None
        self.buttons = {}
        self.screen_buttons()
        super().__init__(key_no)

    def suspend(self):
        for key_no, button in self.buttons.items():
            button.suspend()

    def resume(self):
        for key_no, button in self.buttons.items():
            button.resume()

    def dispose(self):
        for key_no, button in self.buttons.items():
            button.dispose()

    def register_button(self, key_no, button_class):
        self.buttons[key_no] = button_class(key_no)

    def screen_buttons(self):
        pass

    def render(self, screen_manager):
        self._logger.info("Rendering screen: %s", type(self).__name__)
        self._screen_manager = screen_manager
        screen_manager.reset_screen()
        for key_no, button in self.buttons.items():
            button.set_screen_manager(screen_manager)
            try:
                button.initialize()
            except Exception as ex:
                self._logger.error(
                    "Key %s (%s) initialize() raised an unhandled exception: "
                    "%s",
                    key_no, type(self).__name__, str(ex))

    def pressed(self, key_no):
        if key_no not in self.buttons:
            return
        if issubclass(type(self.buttons[key_no]), BaseScreen):
            return
        self._logger.info("Key %s pressed on %s", key_no, type(self).__name__)
        try:
            self.buttons[key_no].pressed()
        except Exception as ex:
            self._logger.error(
                "Key %s (%s) pressed() raised an unhandled exception: %s",
                key_no, type(self).__name__, str(ex))

    def released(self, key_no):
        if key_no not in self.buttons:
            return
        if issubclass(type(self.buttons[key_no]), BaseScreen):
            self._screen_manager.set_active_screen(self.buttons[key_no])
            return
        self._logger.info("Key %s released on %s", key_no,
                          type(self).__name__)
        try:
            self.buttons[key_no].released()
        except Exception as ex:
            self._logger.error(
                "Key %s (%s) released() raised an unhandled exception: %s",
                key_no, type(self).__name__, str(ex))
        self._screen_manager.pop_active_screen()
