import pygame as pg
import os
import src.settings as settings


class Map:
    def __init__(self, filename):
        self.data = []
        with open(os.path.join(filename), "rt") as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.tilesize = settings.TILESIZE
        self.width = self.tilewidth * self.tilesize
        self.height = self.tileheight * self.tilesize





class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(settings.WIDTH / 2)
        y = -target.rect.y + int(settings.HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left side
        y = min(0, y)  # top side
        x = max(-(self.width - settings.WIDTH), x)  # right side
        y = max(-(self.height - settings.HEIGHT), y)  # bottom side
        self.camera = pg.Rect(x, y, self.width, self.height)
