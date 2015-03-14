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