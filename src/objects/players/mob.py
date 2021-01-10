import pygame as pg
from .base import AbstractPerson, collide_with_blocks
import src.settings as settings

vec = pg.math.Vector2


class Mob(AbstractPerson):

    image_set = settings.MOB_IMG_SET

    def __init__(self, game, x, y) -> None:
        super(Mob, self).__init__(game, x, y, self.image_set)
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 50
        self.acc = vec(0, 0)

    def update(self):
        self.target = self.game.player.pos - self.pos
        print(int(abs(self.target.x)), int(abs(self.target.y)), int(self.target.x), int(self.target.y))
        if abs(self.target.x) > abs(self.target.y):
            if self.target.x > 0:
                self.move("right")
            if self.target.x < 0:
                self.move("left")
        if abs(self.target.x) < abs(self.target.y):
            if self.target.y > 0:
                self.move("down")
            if self.target.y < 0:
                self.move("up")
        else:
            self.move("stop")
        self.acc += self.vel
        self.vel = self.acc * self.game.dt

        self.pos += self.vel * self.game.dt
        self.rect.centerx = self.pos.x
        collide_with_blocks(self, self.game.blocks, 'x', destroyable=False)
        self.rect.centery = self.pos.y
        collide_with_blocks(self, self.game.blocks, 'y', destroyable=False)