import logging


class ScreenManager:
    def __init__(self, streamdeck):
        self._logger = logging.getLogger('yolodeck')
        self._streamdeck = streamdeck
        self._streamdeck.open()
        self._streamdeck.set_brightness(30)
        self._logger.info(
            "Opened '{}' device (serial number: '{}', fw: '{}')".format(
                streamdeck.deck_type(), streamdeck.get_serial_number(),
                streamdeck.get_firmware_version()
            )
        )
        self.screens = []

    def reset_screen(self):
        keys = self._streamdeck.key_count()
        for key_no in range(keys):
            self._streamdeck.set_key_image(key_no, None)

    def close(self):
        for screen in self.screens:
            screen.dispose()
        self.reset_screen()
