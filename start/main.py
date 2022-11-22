import pygame as pg

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60


pg.init()

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pg.time.Clock()

is_running = True
while is_running:
    clock.tick(FPS)

    # обработка событий


    # обработка состояния игры


    # отрисовка
    

    pg.display.flip()