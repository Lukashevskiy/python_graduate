import pygame as pg
from random import randint



WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
FPS = 60


class Circle(pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        x = randint(100, 1180)
        y = randint(100, 610)

        self.velocity = 0
        while (self.velocity == 0):
            self.velocity = randint(-3, 3) 

        self.direction = pg.Vector2(1, 1).rotate(self.velocity)

        self.position = pg.Vector2(x, y)

        self.radius = randint(10, 20)
        
        self.color = (randint(100, 255), 0, 0) 
        
        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def recolize(self):
        self.color = (randint(100, 255), randint(100, 255), randint(100, 255)) 
        self.image.fill(self.color)

    def update(self, rect):
        self.position += (self.direction * self.velocity)
        self.rect.center = self.position

        self.check_collision(rect)

    def check_collision(self, other):
        x, y = self.position
        flag = False
        if (x + self.radius >= other.right):
            refl = (1, 0)
            flag = True
        elif (x - self.radius <= other.left):
            refl = (-1, 0)
            flag = True
        elif (y + self.radius >= other.bottom):
            refl = (0, 1)
            flag = True
        elif (y - self.radius <= other.top):  
            refl = (0, -1)
            flag = True
            
        if flag:
            self.direction.reflect_ip(pg.Vector2(refl))




pg.init()


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
screen_rect = screen.get_rect()
clock = pg.time.Clock()

# circles = [Circle() for _ in range(10000)]
circles = pg.sprite.Group([Circle() for _ in range(1000)])
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
    # for circle in range(len(circles)):
    #     circles[circle].update()
    #     circles[circle].check_collision(screen.get_rect())
    circles.update(screen_rect)
        # for j in range(len(circles) - 1):
        #     if j != circle:
        #         circles[circle].collision_circles(circles[j])
    # # отрисовка
    screen.fill((0, 155, 0))
    # for circle in circles:
    #     circle.draw(screen)
    circles.draw(screen)
    pg.display.flip()
