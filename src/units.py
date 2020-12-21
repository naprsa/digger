import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    max_speed = 10

    def __init__(self, game, x, y) -> None:
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("src/assets/digger/digger_front.png")
        # self.image = pg.Surface((TILESIZE, TILESIZE))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.current_speed = 0
        self.last_direction = None
        self.lifes = 3

    def change_image_direction(self, dx=0, dy=0):
        if dx < 0:
            self.image = pg.image.load("src/assets/digger/digger_l.png")
        elif dx > 0:
            self.image = pg.image.load("src/assets/digger/digger_r.png")
        elif dy < 0:
            self.image = pg.image.load("src/assets/digger/digger_u.png")
        elif dy > 0:
            self.image = pg.image.load("src/assets/digger/digger_d.png")
        else:
            self.image = pg.image.load("src/assets/digger/digger_front.png")

    def move(self, dx=0, dy=0):
        self.change_image_direction(dx, dy)
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Background(pg.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pg.image.load("src/assets/stuff/bg.png")
        self.rect = self.image.get_rect()
