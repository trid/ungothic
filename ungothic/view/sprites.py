from sdl2uipy import Image

__author__ = 'TriD'


class SpriteManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SpriteManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.sprites = {
            'castle_bg': Image.from_file('../res/images/castle.jpg')
        }

    def __getitem__(self, item):
        return self.sprites[item]