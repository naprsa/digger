import pygame as pg
import os
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(os.path.join(filename), "rt") as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.groups = game.all_sprites, game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.destroyable = False


class GroundBlock(Block):
    def __init__(self, game,  *args, **kwargs):
        super(GroundBlock, self).__init__(game, *args, **kwargs)
        self.image.fill(YELLOW)
        self.destroyable = True

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left side
        y = min(0, y)  # top side
        x = max(-(self.width - WIDTH), x)  # right side
        y = max(-(self.height - HEIGHT), y)  # bottom side
        self.camera = pg.Rect(x, y, self.width, self.height)
