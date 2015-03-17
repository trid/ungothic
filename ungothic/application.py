from ungothic.event_manager import EventManager
from ungothic.view.view import View

__author__ = 'TriD'


class Application(object):
    def __init__(self):
        self.running = True
        self.event_manager = EventManager(self)
        self.view = View(self)
        self.states = []

    def start(self):
        while self.running:
            self.event_manager.update()
            self.view.draw()

    def push_state(self, state):
        self.states.append(state)
        state.on_push()

    def pop_state(self):
        state = self.states.pop()
        state.on_pop()


application = Application()