import pygame as pg
from random import randint
from enum import Enum
from typing import Tuple
N, M = 30, 60

SIZE_N = 10
SIZE_M = 10

class LifeState(Enum):
    alive: Tuple[int] = (255, 255, 255)
    murder: Tuple[int] = (0, 0, 0)


W_HEIGHT, W_WIDTH = (SIZE_N + 1) * N + 1, (SIZE_M + 1) * M + 1

class Rectangle(pg.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = pg.Surface((SIZE_M, SIZE_N))
        
        self.life_status = LifeState.alive
        if randint(0, 10) < 5:
            self.life_status = LifeState.murder

        self.change_color(self.life_status.value)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self, new_color):
        self.image.fill(new_color)
        
    def update(self):
        self.change_color(self.life_status.value)
pg.init()

rectangle_group = pg.sprite.Group()

for y in range(SIZE_N//2 + 1, W_HEIGHT, SIZE_N + 1):
    for x in range(SIZE_N//2 + 1, W_WIDTH, SIZE_M + 1):
        rectangle_group.add(Rectangle(x, y))

screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()

is_running = True
change_color = False
while is_running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                change_color = True

    if change_color:
        change_color = False
        for rect in rectangle_group.sprites():
            if randint(0, 10) < 5:
                rect.life_status = LifeState.murder
            else:
                rect.life_status = LifeState.alive

    rectangle_group.update()
    screen.fill((150, 150, 150))
    rectangle_group.draw(screen)

    pg.display.flip()
