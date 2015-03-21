import sdl2uipy
from ungothic.view import get_sprite_manager
from ungothic.view.ui_manager import UIManager

__author__ = 'TriD'


class View(object):
    def __init__(self, application):
        sdl2uipy.video_init()
        self.application = application
        self.ui_manager = UIManager(self)

    def draw(self):
        get_sprite_manager()['castle_bg'].draw(0, 0)
        self.ui_manager.draw()
        sdl2uipy.flip_screen()
