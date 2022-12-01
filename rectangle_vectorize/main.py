import pygame as pg
from random import randint
from typing import List
from itertools import combinations

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60


class Circle(pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        x = randint(100, 1180)
        y = randint(100, 610)

        angle = randint(0, 360)
        self.velocity = 0
        while (self.velocity == 0):
            self.velocity = randint(-3, 3) 

        self.direction = pg.Vector2(1, 1).rotate(angle)

        self.radius = randint(10, 20)
        
        self.color = (randint(100, 255), 0, 0) 
        
        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(self.color)

        self.current_image = self.image.copy()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def recolize(self):
        self.color = (randint(100, 255), randint(100, 255), randint(100, 255)) 
        self.image.fill(self.color)

    def update(self, rect):
        self.rect.move_ip(self.direction * self.velocity)
        self.check_collision(rect)

    def check_collision(self, other):
        x, y = self.rect.center
        flag = False
        
        if (x + self.radius >= other.right):
            normal = (1, 0)
            flag = True
        elif (x - self.radius <= other.left):
            normal = (-1, 0)
            flag = True
        elif (y + self.radius >= other.bottom):
            normal = (0, 1)
            flag = True
        elif (y - self.radius <= other.top):  
            normal = (0, -1)
            flag = True
            
        if flag:
            self.direction.reflect_ip(pg.Vector2(normal))

    def reflect(self, norm):
        try:
            self.direction.reflect_ip(norm)
        except ValueError:
            print(norm)

def circle_collision(c1: Circle, c2: Circle):
    if c1.rect.colliderect(c2.rect):
        norm = (c1.direction - c2.direction)
        if 0 < norm.length_squared() < (c1.radius+c2.radius)**2:
            c1.reflect(norm)
            c2.reflect(norm)
            

pg.init()


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
screen_rect = screen.get_rect()
clock = pg.time.Clock()

# circles = [Circle() for _ in range(10000)]
circles: pg.sprite.Group = pg.sprite.Group([Circle() for _ in range(100)])
circles_sprite = circles.sprites()

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

    for c1, c2 in combinations(circles_sprite, 2):
        if c1.rect.colliderect(c2.rect):
            norm = (c1.direction - c2.direction)
            if 0 < norm.length() < c1.radius + c2.radius:
                norm = norm.normalize()
                c1.reflect(norm)
                c2.reflect(norm)
    
    circles.update(screen_rect)

    screen.fill((0, 155, 0))
    
    circles.draw(screen)
    
    pg.display.flip()
