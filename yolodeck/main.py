#!/usr/bin/env python3

import logging
import sys
import threading

from StreamDeck.DeviceManager import DeviceManager

from yolodeck.screen_manager import ScreenManager
from yolodeck.screens.simple_screen import SimpleScreen


def main():
    root = logging.getLogger('yolodeck')
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    root.addHandler(info_handler)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(formatter)
    root.addHandler(error_handler)

    streamdeck = DeviceManager().enumerate()[0]

    screen_manager = ScreenManager(streamdeck)

    main_screen = SimpleScreen(0)
    screen_manager.set_active_screen(main_screen)

    # Wait until all application threads have terminated (for this example,
    # this is when all deck handles are closed).
    for t in threading.enumerate():
        if t is threading.current_thread():
            continue

        if t.is_alive():
            try:
                t.join()
            except KeyboardInterrupt as ex:
                screen_manager.close()
                streamdeck.close()


if __name__ == "__main__":
    main()
