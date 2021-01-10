import pygame as pg
import src.settings as settings
from .base import AbstractPerson, collide_with_blocks

vec = pg.math.Vector2


class Player(AbstractPerson):
    image_set = settings.PLAYER_IMAGE_SET


    def __init__(self, game, x, y) -> None:
        super(Player, self).__init__(game, x, y, self.image_set)
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.lives = 3
        self.speed = 200

    def get_keys(self):
        keys = pg.key.get_pressed()
        self.vel = vec(0, 0)
        if keys[pg.K_LEFT]:
            self.move('left')
        elif keys[pg.K_RIGHT]:
            self.move('right')
        elif keys[pg.K_UP]:
            self.move('up')
        elif keys[pg.K_DOWN]:
            self.move('down')
        if keys[pg.K_SPACE]:
            print("Fire")

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collide_with_blocks(self, self.game.blocks, 'x', destroyable=False)
        self.rect.y = self.pos.y
        collide_with_blocks(self, self.game.blocks, 'y', destroyable=False)
        self.update_image()