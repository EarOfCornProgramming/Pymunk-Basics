import pygame
import pymunk

pygame.init()

display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, -1000
FPS = 80

def convert_coordinates(point):
    return point[0], 800-point[1]


ball_radius = 30
image = pygame.image.load("basketball.png")
image = pygame.transform.scale(image, (ball_radius*2, ball_radius*2))
class Ball():
    def __init__(self, x=400):
        self.body = pymunk.Body()
        self.body.position = x, 600
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    def draw(self):
        x, y = convert_coordinates(self.body.position)
        # pygame.draw.circle(display, (255, 0, 0), (int(x), int(y)), ball_radius)
        display.blit(image, (int(x)-ball_radius, int(y)-ball_radius))


class Floor():
    def __init__(self):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (0, 250), (800, 50), 5)
        self.shape.elasticity = 1
        space.add(self.shape)
    def draw(self):
        pygame.draw.line(display, (0, 0, 0), (0, 550), (800, 750), 5)


def game():
    ball = Ball()
    ball_2 = Ball(200)
    floor = Floor()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255, 255, 255))
        ball.draw()
        ball_2.draw()
        floor.draw()
        
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()






















