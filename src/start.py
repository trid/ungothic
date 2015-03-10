__author__ = 'TriD'

import sdl2uipy

sdl2uipy.video_init()

image = sdl2uipy.Image.from_file('../res/images/castle.jpg')

while True:
    image.draw(0, 0)
    sdl2uipy.flip_screen()
    event = sdl2uipy.get_event()
    if event.type == sdl2uipy.EventType.EVENT_TYPE_QUIT:
        break
