from ungothic.view.ui.ui_element import UIElement

__author__ = 'TriD'


class Panel(UIElement):
    def __init__(self, x, y, w, h):
        super(Panel, self).__init__(x, y, w, h)
        self.items = []

    def click(self, button, x, y):
        res = super(Panel, self).click(button, x, y)
        for item in self.items:
            item.click(button, x + self.x, y + self.y)

    def add_item(self, item):
        self.items.append(item)
        item.x = item.x + self.x
        item.y = item.y + self.y

    def remove_item(self, item):
        self.items.remove(item)

    def draw(self):
        for item in self.items:
            item.draw()