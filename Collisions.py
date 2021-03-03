import pygame
import pymunk
import random

pygame.init()

display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
FPS = 50

def convert_coordinates(point):
    return int(point[0]), 600-int(point[1])

class Ball():
    def __init__(self, x, y, collision_type, up = 1):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.body.velocity = random.uniform(-100, 100), random.uniform(-100, 100)
        # self.body.velocity = 0, up*100
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)
    def draw(self):
        if self.shape.collision_type != 2:
            pygame.draw.circle(display, (255, 0, 0), convert_coordinates(self.body.position), 10)
        else:
            pygame.draw.circle(display, (0, 0, 255), convert_coordinates(self.body.position), 10)
    def change_to_blue(self, arbiter, space, data):
        self.shape.collision_type = 2

def game():
    balls = [Ball(random.randint(0, 600), random.randint(0, 600), i+3) for i in range(100)]
    balls.append(Ball(400, 400, 2))
    
    handlers = [space.add_collision_handler(2, i+3) for i in range(100)]
    for i, handler in enumerate(handlers):
        handler.separate = balls[i].change_to_blue

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        [ball.draw() for ball in balls]
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()






















