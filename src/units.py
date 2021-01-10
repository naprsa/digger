import pygame as pg
from settings import *

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

class Player(pg.sprite.Sprite):
    max_speed = 10

    def __init__(self, game, x, y) -> None:
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.image = pg.image.load("src/assets/digger/digger_front.png")
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.lives = 3

    def get_keys(self):
        keys = pg.key.get_pressed()
        self.vel = vec(0, 0)
        if keys[pg.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        elif keys[pg.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
        elif keys[pg.K_UP]:
            self.vel.y = -PLAYER_SPEED
        elif keys[pg.K_DOWN]:
            self.vel.y = PLAYER_SPEED
        if keys[pg.K_SPACE]:
            print("Fire")

    def get_player_image(self):
        img = PLAYER_IMAGE_SET['front']
        if self.vel.x > 0:
            img = PLAYER_IMAGE_SET['right']
        elif self.vel.x < 0:
            img = PLAYER_IMAGE_SET['left']
        elif self.vel.y > 0:
            img = PLAYER_IMAGE_SET['down']
        elif self.vel.y < 0:
            img = PLAYER_IMAGE_SET['up']
        return img

    def update_player_image(self):
        self.image = pg.image.load(self.get_player_image()).convert_alpha()

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collide_with_blocks(self, self.game.blocks, 'x', destroyable=False)
        self.rect.y = self.pos.y
        collide_with_blocks(self, self.game.blocks, 'y', destroyable=False)
        self.update_player_image()


class Mob(pg.sprite.Sprite):
    speed = 150

    def __init__(self, game, x, y) -> None:
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y,) * TILESIZE
        self.rect.center = self.pos
        self.rot = 0
        self.vel = vec(0, 0)
        self.acceleration = vec(0, 0)

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acceleration = vec(self.speed, 0).rotate(-self.rot)
        self.acceleration += self.vel * -1
        self.vel += self.acceleration * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acceleration * self.game.dt ** 2
        self.rect.centerx = self.pos.x
        collide_with_blocks(self, self.game.blocks, 'x', destroyable=False)
        self.rect.centery = self.pos.y
        collide_with_blocks(self, self.game.blocks, 'y', destroyable=False)
