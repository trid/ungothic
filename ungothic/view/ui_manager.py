from sdl2uipy import EventType

__author__ = 'TriD'


class UIManager(object):
    def __init__(self, view):
        self.items = []
        self.view = view
        view.application.event_manager.add_listener(EventType.MOUSEBUTTON_UP, self.get_mouse_message)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def draw(self):
        for item in self.items:
            if item.visible:
                item.draw()

    def get_mouse_message(self, button, x, y):
        for item in self.items:
            item.click(button, x, y)