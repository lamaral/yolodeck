import logging

from StreamDeck.ImageHelpers import PILHelper


class ScreenManager:
    def __init__(self, streamdeck):
        self._logger = logging.getLogger('yolodeck')
        self._streamdeck = streamdeck
        self._streamdeck.open()
        self._streamdeck.set_brightness(30)
        self._streamdeck.set_key_callback(self.key_callback)
        self._logger.info(
            "Opened '{}' device (serial number: '{}', fw: '{}')".format(
                streamdeck.deck_type(), streamdeck.get_serial_number(),
                streamdeck.get_firmware_version()
            )
        )
        self.screens = []

    def set_active_screen(self, screen):
        self._logger.info("Setting active screen: %s", type(screen).__name__)
        for screen_itr in self.screens:
            screen_itr.suspend()
        self.screens.append(screen)
        self.get_active_screen().render(self)

    def get_active_screen(self):
        if not self.screens:
            return None
        return self.screens[-1]

    def pop_active_screen(self):
        if len(self.screens) == 1:
            return
        popped_screen = self.screens.pop()
        popped_screen.dispose()
        self._logger.info("Exiting screen: %s", type(popped_screen).__name__)
        self.get_active_screen().render(self)

    def key_callback(self, deck, key, state):
        if state:
            self.get_active_screen().pressed(key)
        else:
            self.get_active_screen().released(key)

    def update_key_image(self, key_no, img):
        native_img = PILHelper.to_native_format(self._streamdeck, img)
        self._streamdeck.set_key_image(key_no, native_img)

    def reset_screen(self):
        keys = self._streamdeck.key_count()
        for key_no in range(keys):
            self._streamdeck.set_key_image(key_no, None)

    def close(self):
        for screen in self.screens:
            screen.dispose()
        self.reset_screen()
