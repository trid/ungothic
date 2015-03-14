import sdl2uipy

__author__ = 'TriD'


class EventManager(object):
    def __init__(self, application):
        self.listeners = {}
        self.application = application

    def update(self):
        while True:
            event = sdl2uipy.get_event()
            if not event:
                return
            if event.type == sdl2uipy.EventType.QUIT:
                self.application.running = False
            if event.type == sdl2uipy.EventType.MOUSEBUTTON_UP:
                for listener in self.listeners.get(sdl2uipy.EventType.MOUSEBUTTON_UP, ()):
                    listener(event.mouse_button.button, event.mouse_button.x, event.mouse_button.y)

    def add_listener(self, message, listener):
        if message not in self.listeners:
            self.listeners[message] = []
        self.listeners[message].append(listener)

    def remove_listener(self, message, listener):
        self.listeners.get(message, []).remove(listener)