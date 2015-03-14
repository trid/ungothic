import sdl2uipy
from ungothic.view import SpriteManager

__author__ = 'TriD'


class View(object):
    def __init__(self):
        sdl2uipy.video_init()
        self.sprite_manager = SpriteManager()

    def draw(self):
        self.sprite_manager['castle_bg'].draw(0, 0)
        sdl2uipy.flip_screen()
