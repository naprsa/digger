import pygame as pg
import src.settings as settings


class AbstractBlock(pg.sprite.Sprite):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.image = pg.Surface((settings.TILESIZE, settings.TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * settings.TILESIZE
        self.rect.y = y * settings.TILESIZE
        self.destroyable = False


class Block(AbstractBlock):

    def __init__(self, game, *args, block_type=0, **kwargs):
        super(Block, self).__init__(game, *args, **kwargs)
        self.groups = game.all_sprites, game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image.fill(settings.GREEN if block_type == 0 else settings.YELLOW)
        self.destroyable = False if block_type == 0 else True
