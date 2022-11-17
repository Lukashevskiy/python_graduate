class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        ...

class Rectangle:
    def __init__(self, start_point: Point, width: int, height: int):
        self.point = start_point
        self.width = width
        self.height = height
    
    def draw(self, screen):
        ...

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw(self, screen):
        ...

class Circle:
    def __init__(self, p, radius):
        self.p = p
        self.radius = radius

    def draw(self, screen):
        ...



import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

rect = Rectangle(Point(15, 15), 100, 100)
cirlce = Circle(Point(400, 400), 100)
triangle = Triangle(Point(10, 10), Point(100, 100), Point(45, 100))
is_running = True
while is_running:
    clock.tick(60)

    #обработать все входящие события
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

    #изменить состояние мира



    #отрисовать новый мир
    pygame.draw.rect(screen, (127, 127, 127), (rect.point.x, rect.point.y, rect.height, rect.width))
    #шабон для вывода прямугольника на экран

    pygame.draw.circle(screen, (14, 15, 111), (cirlce.p.x, cirlce.p.y), cirlce.radius)
    #шаблон для вывода круга на экран

    pygame.draw.polygon(screen, (155, 155, 12), [(triangle.p1.x, triangle.p1.y), (triangle.p2.x, triangle.p2.y), (triangle.p3.x, triangle.p3.y)])
    #шаблон для вывода треугольника на экран

    # screen.fill((127,127, 14))

    pygame.display.flip()
