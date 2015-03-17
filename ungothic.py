from ungothic.application import application
from ungothic.game_state import GameState

__author__ = 'TriD'


application.push_state(GameState())
application.start()
