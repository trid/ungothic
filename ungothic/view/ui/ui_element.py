__author__ = 'TriD'


class UIElement(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = True

    def click(self, button, x, y):
        if not self.visible:
            return False
        if x < self.x or x > self.x + self.w:
            return False
        if y < self.y or y > self.y + self.h:
            return False
        return True

    def draw(self):
        raise NotImplementedError()