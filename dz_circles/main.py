import pygame as pg
from random import randint

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60


pg.init()

def update_position():
    return randint(100, 1180), randint(100, 620)
    
xs = [randint(100, 1180) for i in range(100)] 
ys = [randint(100, 620) for i in range(100)] 
rs = [randint(10, 100) for i in range(100)]

colors = [(randint(100, 255), 0, 0) for i in range(100)]

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pg.time.Clock()

is_running = True

is_circle_change = False

while is_running:
    clock.tick(FPS)

    # обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
            break
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                is_circle_change = True

    # обработка состояния игры
    if is_circle_change:
        for i in range(100):
            xs[i], ys[i] = update_position()
        is_circle_change = False

    # отрисовка
    screen.fill((0, 155, 0))
    for x, y, r, color in zip(xs, ys, rs, colors):
        pg.draw.circle(screen, color, (x, y), r)
    pg.display.flip()