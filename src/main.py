import sys
import pygame as pg
from settings import SIZE
from units import Player, Background


clock = pg.time.Clock()

pg.init()
pg.display.set_caption("Digger")
screen = pg.display.set_mode(SIZE)


# Groups
all_objects = pg.sprite.Group()

# Game objects
player = Player()
bg = Background()

all_objects.add(bg)
all_objects.add(player)


def main():

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
        screen.fill((0, 0, 0))
        all_objects.update()
        all_objects.draw(screen)
        pg.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
