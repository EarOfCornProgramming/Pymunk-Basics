import pygame
import pymunk

pygame.init()

display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 100

def convert_coordinates(point):
    return int(point[0]), int(600-point[1])

class Ball():
    def __init__(self, x, color, category, mask, velocity):
        self.color = color
        self.body = pymunk.Body()
        self.body.position = x, 500
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, 15)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.filter = pymunk.ShapeFilter(categories=category, mask=mask)
        space.add(self.body, self.shape)
    
    def draw(self):
        pos = self.body.position
        pygame.draw.circle(display, self.color, convert_coordinates(pos), 15)

class Platform():
    def __init__(self, y, color, category):
        self.color = color
        self.y = y
        self.body = pymunk.Body(pymunk.Body.STATIC)
        self.body.position = 0, y
        self.shape = pymunk.Segment(self.body, [0, 0], [600, 0], 10)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.filter = pymunk.ShapeFilter(categories=category)
        space.add(self.shape)
    
    def draw(self):
        a = convert_coordinates(self.body.local_to_world(self.shape.a))
        b = convert_coordinates(self.body.local_to_world(self.shape.b))
        pygame.draw.line(display, self.color, a, b, 10)
        
def game():
    ball_1 = Ball(150, (255, 0, 0), 1, 21, (0, 0))
    ball_2 = Ball(300, (0, 255, 0), 2, 22, (100, 0))
    ball_3 = Ball(450, (0, 0, 255), 4, 31, (0, 0))
    platform1 = Platform(300, (0, 0, 0), 8)
    platform2 = Platform(100, (255, 165, 0), 16)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        ball_1.draw()
        ball_2.draw()
        ball_3.draw()
        platform1.draw()
        platform2.draw()

        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()






















