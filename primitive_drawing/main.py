import pygame

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    @property
    def coord(self):
        return self.x, self.y

class Rectangle:
    def __init__(self, start_point: Point, width: int, height: int):
        self.point = start_point
        self.width = width
        self.height = height

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class Circle(pygame.sprite.Sprite):
    def __init__(self, p, radius, dx, dy, color):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((2*radius, 2*radius))
        self.rect = self.image.get_rect(center=p.coord)
        
        self.radius = radius
        
        self.dx = dx
        self.dy = dy
        
        self.color = color
    
    def move(self):
        self.rect.move_ip(self.dx, self.dy)


    def collision(self, other):
        if self.rect.left < other.left or self.rect.right > other.right:
            self.dx *= -1
        
        if self.rect.bottom > other.bottom or self.rect.top < other.top:
            self.dy *= -1
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

from random import randint

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

#rect = Rectangle(Point(15, 15), 100, 100)
cirlce = Circle(Point(400, 400), 100, randint(0, 10), randint(0, 10), (127, 25, 13))
#triangle = Triangle(Point(10, 10), Point(100, 100), Point(45, 100))
is_running = True
while is_running:
    clock.tick(30)

    #обработать все входящие события
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

    #изменить состояние мира

    cirlce.collision(screen.get_rect())
    cirlce.move()

    #отрисовать новый мир
    screen.fill((127,127, 14))
    cirlce.draw(screen)
   # pygame.draw.rect(screen, (127, 127, 127), (rect.point.x, rect.point.y, rect.height, rect.width))
    #шабон для вывода прямугольника на экран

    #pygame.draw.circle(screen, cirlce.color, (cirlce.p.x, cirlce.p.y), cirlce.radius)
    #шаблон для вывода круга на экран

    #pygame.draw.polygon(screen, (155, 155, 12), [(triangle.p1.x, triangle.p1.y), (triangle.p2.x, triangle.p2.y), (triangle.p3.x, triangle.p3.y)])
    #шаблон для вывода треугольника на экран




    pygame.display.flip()
