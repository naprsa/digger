import pygame as pg
from src.settings import TILESIZE


vec = pg.math.Vector2


def collide_with_blocks(sprite, group, line, destroyable=False):
    if line == "x":
        hits_blocks = pg.sprite.spritecollide(sprite, group, destroyable)
        if hits_blocks:
            if sprite.vel.x > 0:
                sprite.pos.x = hits_blocks[0].rect.left - sprite.rect.width
            if sprite.vel.x < 0:
                sprite.pos.x = hits_blocks[0].rect.right
            sprite.vel.x = 0
            sprite.rect.x = sprite.pos.x

    if line == "y":
        hits_blocks = pg.sprite.spritecollide(sprite, group, destroyable)

        if hits_blocks:
            if sprite.vel.y > 0:
                sprite.pos.y = hits_blocks[0].rect.top - sprite.rect.height
            if sprite.vel.y < 0:
                sprite.pos.y = hits_blocks[0].rect.bottom
            sprite.vel.y = 0
            sprite.rect.y = sprite.pos.y


class AbstractPerson(pg.sprite.Sprite):

    def __init__(self, game, x, y, image_set) -> None:
        self.game = game
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.speed = 0
        self.image_set = image_set

    def update(self):
        pass

    def move(self, direction):
        if direction == "left":
            self.vel.x = -self.speed
        elif direction == "right":
            self.vel.x = self.speed
        elif direction == "up":
            self.vel.y = -self.speed
        elif direction == "down":
            self.vel.y = self.speed
        elif direction == "stop":
            self.vel = vec(0, 0)

    def get_image(self):
        img = self.image_set['front']
        if self.vel.x > 0:
            img = self.image_set['right']
        elif self.vel.x < 0:
            img = self.image_set['left']
        elif self.vel.y > 0:
            img = self.image_set['down']
        elif self.vel.y < 0:
            img = self.image_set['up']
        return img

    def update_image(self):
        self.image = pg.image.load(self.get_image()).convert_alpha()