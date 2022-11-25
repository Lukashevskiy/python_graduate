import pygame as pg
from random import randint



WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60

class Circle:

    def __init__(self):
        self.x = randint(100, 1180)
        self.y = randint(100, 610)

        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)
        
        self.radius = randint(10, 20)
        
        self.color = (randint(100, 255), 0, 0) 

    def update(self):
        self.x = (self.x + self.dx)
        self.y = (self.y + self.dy)


    def check_collision(self, other):
        if self.x + self.radius >= other.right or self.x - self.radius <= other.left:
            self.dx *= -1
        if self.y + self.radius >= other.bottom or self.y - self.radius <= other.top:
            self.dy *= -1 

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)



pg.init()


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
clock = pg.time.Clock()

circles = [Circle() for _ in range(100)]

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
            if event.key == pg.K_q:
                is_running = False

    # обработка состояния игры
    for circle in circles:
        circle.update()
        circle.check_collision(screen.get_rect())
        
    # отрисовка
    screen.fill((0, 155, 0))
    for circle in circles:
        circle.draw(screen)
    pg.display.flip()