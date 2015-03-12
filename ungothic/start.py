from ungothic.view import SpriteManager
import sdl2uipy

__author__ = 'TriD'


sdl2uipy.video_init()

spriteManage = SpriteManager()
image = spriteManage['castle_bg']

while True:
    image.draw(0, 0)
    sdl2uipy.flip_screen()
    event = sdl2uipy.get_event()
    if event.type == sdl2uipy.EventType.QUIT:
        break
