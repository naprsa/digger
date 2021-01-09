import pygame as pg
from settings import *

vec = pg.math.Vector2


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

    def collide_with_blocks(self, line):
        if line == "x":
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x

        if line == "y":
            hits = pg.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_blocks('x')
        self.rect.y = self.pos.y
        self.collide_with_blocks('y')
        self.update_player_image()


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
