import sys

import pygame as pg
from settings import *
from units import *
from maps import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.key.set_repeat(500, 100)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        # нужно сделать генератор, с вызовом следующей карты
        self.map = Map(os.path.join(MAPS_DIR, "map2.txt"))
        self.player_img = pg.image.load(PLAYER_IMAGE_SET['front']).convert_alpha()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        # self.bg = Background(self)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Block(self, col, row)
                if tile.lower() == "p":
                    print(col, row)
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_grid()
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
            self.dt = self.clock.tick(FPS) / 1000
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
