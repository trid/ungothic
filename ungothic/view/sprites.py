from sdl2uipy import Image
from sdl2uipy import video_was_init

__author__ = 'TriD'


__sprite_manager = None

class SpriteManager(object):
    def __init__(self):
        self.sprites = {
            'castle_bg': Image.from_file('res/images/castle.jpg'),
            'button_characters': Image.from_file('res/images/button_characters.png'),
            'button_create': Image.from_file('res/images/button_create.png')
        }

    def __getitem__(self, item):
        return self.sprites[item]


class VideoNotInitException(Exception):
    pass


def get_sprite_manager():
    global __sprite_manager
    if video_was_init():
        if __sprite_manager is None:
            __sprite_manager = SpriteManager()
        return __sprite_manager
    raise VideoNotInitException()