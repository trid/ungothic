from ungothic.view.ui.ui_element import UIElement

__author__ = 'TriD'


class Button(UIElement):
    def __init__(self, x, y, image, callback=None):
        w = image.get_width()
        h = image.get_height()
        self.callback = callback
        self.image = image
        super(Button, self).__init__(x, y, w, h)

    def click(self, button, x, y):
        if super(Button, self).click(button, x, y) and self.callback:
            self.callback()
            return True
        return False

    def draw(self):
        self.image.draw(self.x, self.y)