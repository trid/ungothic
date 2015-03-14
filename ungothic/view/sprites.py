from sdl2uipy import Image

__author__ = 'TriD'


class SpriteManager(object):
    def __init__(self):
        self.sprites = {
            'castle_bg': Image.from_file('res/images/castle.jpg')
        }

    def __getitem__(self, item):
        return self.sprites[item]