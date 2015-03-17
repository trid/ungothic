from ungothic.application import application
from ungothic.state import State
from ungothic.view.ui.button import Button

__author__ = 'TriD'


class GameState(State):
    def __init__(self):
        super(GameState, self).__init__()
        characters_button_image = application.view.sprite_manager['button_characters']
        self.characters_button = Button(0, 0, characters_button_image, self.show_characters)

    def on_push(self):
        super(GameState, self).on_push()
        application.view.ui_manager.add_item(self.characters_button)

    def on_pop(self):
        super(GameState, self).on_pop()
        application.view.ui_manager.remove_item(self.characters_button)

    def update(self):
        super(GameState, self).update()

    def show_characters(self):
        pass