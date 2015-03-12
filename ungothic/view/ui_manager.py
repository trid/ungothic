__author__ = 'TriD'


class UIManager(object):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def draw(self):
        for item in self.items:
            item.draw()

    def get_mouse_message(self, button, x, y):
        for item in self.items:
            item.click(button, x, y)