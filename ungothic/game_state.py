from ungothic.state import State
from ungothic.view.ui.button import Button

__author__ = 'TriD'


class GameState(State):
    def __init__(self):
        super(GameState, self).__init__()
        self.characters_button = Button(0, 0, 'button_characters', self.show_characters)

    def on_push(self):
        super(GameState, self).on_push()

    def on_pop(self):
        super(GameState, self).on_pop()

    def update(self):
        super(GameState, self).update()

    def show_characters(self):
        pass