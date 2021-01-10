import sys, os
import pygame as pg
from objects.players import Player, Mob
from src.objects.world import Block
from src.objects.map import Map, Camera
import src.settings as settings


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(settings.CAPTION)
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pg.key.set_repeat(500, 100)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        # нужно сделать генератор, с вызовом следующей карты
        self.map = Map(os.path.join(settings.MAPS_DIR, "map2.txt"))
        self.player_img = pg.image.load(settings.PLAYER_IMAGE_SET['front']).convert_alpha()
        self.mob_img = pg.image.load(settings.MOB_IMG_SET['front']).convert_alpha()
        self.mob_img = pg.transform.scale(self.mob_img, (settings.TILESIZE, settings.TILESIZE))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile.isdigit():
                    Block(self, col, row, block_type=tile)
                if tile.lower() == "m":
                    Mob(self, col, row)
                if tile.lower() == "p":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(self.screen, settings.LIGHTGREY, (0, y), (settings.WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.pause()

    def pause(self):
        pass

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def run(self):
        self.game_over = False
        while not self.game_over:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()


def main():
    app = Game()
    app.new()
    app.run()
    app.show_go_screen()


if __name__ == "__main__":
    main()
