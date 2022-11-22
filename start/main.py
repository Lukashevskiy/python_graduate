import pygame as pg
from random import randint

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60


pg.init()

x, y, r = randint(100, 1600), randint(100, 620), randint(10, 100)
color = (randint(100, 255), 0, 0)

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pg.time.Clock()

is_running = True
while is_running:
    clock.tick(FPS)

    # обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
            break

    # обработка состояния игры


    # отрисовка
    screen.fill((0, 155, 0))
    pg.draw.circle(screen, color, (x, y), r)
    pg.display.flip()