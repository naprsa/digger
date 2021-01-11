from kivy.graphics import Rectangle
from kivy.vector import Vector as vec


def collides(e1, e2):
    r1x = e1.pos[0]
    r1y = e1.pos[1]
    r2x = e2.pos[0]
    r2y = e2.pos[1]
    r1w = e1.size[0]
    r1h = e1.size[1]
    r2w = e2.size[0]
    r2h = e2.size[1]

    if r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y:
        return True
    else:
        return False


class Entity:
    def __init__(self):
        self._pos = vec(0, 0)
        self._size = (50, 50)
        self._source = "bullshit.png"
        self._instruction = Rectangle(
            pos=self._pos, size=self._size, source=self._source
        )

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = vec(value)
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source


class Camera(Entity):
    def __init__(self, game, pos, size, speed=0):
        super(Camera, self).__init__()
        self.game = game
        self.pos = vec(pos)
        self.size = size
        self.camera = Rectangle(pos=self.pos, size=self.size)
        self.source = None

    # def apply(self, entity):
    #     return entity.rect.move(self.camera.topleft)

    # def update(self, target):
    #     x = -target.rect.x + int(WIDTH / 2)
    #     y = -target.rect.y + int(HEIGHT / 2)
    #
    #     # limit scrolling to map size
    #     x = min(0, x)  # left side
    #     y = min(0, y)  # top side
    #     x = max(-(self.width - WIDTH), x)  # right side
    #     y = max(-(self.height - HEIGHT), y)  # bottom side
    #     self.camera = pg.Rect(x, y, self.width, self.height)
