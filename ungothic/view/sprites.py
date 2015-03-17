from sdl2uipy import Image

__author__ = 'TriD'


class SpriteManager(object):
    def __init__(self):
        self.sprites = {
            'castle_bg': Image.from_file('res/images/castle.jpg'),
            'button_characters': Image.from_file('res/images/button_characters.png')
        }

    def __getitem__(self, item):
        return self.sprites[item]