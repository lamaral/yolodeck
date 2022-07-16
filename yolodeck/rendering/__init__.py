from PIL import Image, ImageDraw, ImageOps

from yolodeck.rendering.text_renderer import TextRenderer


class Renderer:
    def __init__(self, key_no, screen_manager):
        self.img = None
        self._screen_manager = screen_manager
        self._key_no = key_no

    def __enter__(self):
        self.img = Image.new("RGB", (512, 512))
        return self

    def __exit__(self, type, value, traceback):
        self._screen_manager.update_key_image(
            self._key_no, self.img
        )

    def background_color(self, color):
        draw = ImageDraw.Draw(self.img)
        draw.rectangle((0, 0, self.img.width, self.img.height), fill=color)

    # def badge_count(self, count):
    #     return BadgeCountRenderer(self, count)
    #
    # def emoji(self, emoji_name):
    #     return EmojiRenderer(self, emoji_name)
    #
    # def image(self, filename):
    #     return ImageRenderer(self, filename)

    def text(self, text):
        return TextRenderer(self, text)

    def colorize(self, color):
        grayscale = self.img.convert('L')
        self.img = ImageOps.colorize(grayscale, black='black', white=color)
        return self
