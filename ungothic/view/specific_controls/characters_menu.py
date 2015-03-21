from ungothic.view.sprites import get_sprite_manager
from ungothic.view.ui.button import Button
from ungothic.view.ui.panel import Panel

__author__ = 'TriD'


class CharactersMenu(Panel):
    def __init__(self, x, y, w, h):
        super(CharactersMenu, self).__init__(x, y, w, h)
        self.button_create = Button(0, 0, get_sprite_manager()['button_create'], None)
        self.add_item(self.button_create)
        self.visible = False