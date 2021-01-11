from .objects import Entity


class Wall(Entity):
    def __init__(self, pos):
        super(Wall, self).__init__()
        self.source = "assets/images/map/grass.png"
        self.pos = pos
