import sys
import pygame as pg
from settings import *
from units import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 0, 4)

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            # if event.type == pg.QUIT:
            #     self.quit()
            # # if event.type == pg.KEYDOWN:
            # if event.type == pg.K_ESCAPE:
            #     self.quit()
            if event.type == pg.K_LEFT:
                self.player.move(dx=-1)
                self.player.image = pg.image.load("src/assets/digger/digger_l.png")
            elif event.type == pg.K_RIGHT:
                self.player.move(dx=1)
                self.player.image = pg.image.load("src/assets/digger/digger_r.png")
            elif event.type == pg.K_UP:
                self.player.move(dy=-1)
                self.image = pg.image.load("src/assets/digger/digger_u.png")
            elif event.type == pg.K_DOWN:
                self.player.move(dy=1)
                self.image = pg.image.load("src/assets/digger/digger_d.png")
            elif event.type == pg.K_SPACE:
                print("Fire")
            # else:
            #     self.image = pg.image.load("src/assets/digger/digger_front.png")

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def run(self):
        self.game_over = False
        while not self.game_over:
            self.dt = self.clock.tick(FPS) / 100
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
