import pygame
import pymunk

pygame.init()

display = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, -900)
FPS = 50

def convert_coordinates(point):
    return int(point[0]), int(600-point[1])

class Ball():
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.circle(display, (255, 0, 0), convert_coordinates(self.body.position), 10)

class String():
    def __init__(self, body1, attachment, identifier="body"):
        self.body1 = body1
        if identifier == "body":
            self.body2 = attachment
        elif identifier == "position":
            self.body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body2.position = attachment
        joint = pymunk.PinJoint(self.body1, self.body2)
        space.add(joint)
    def draw(self):
        pos1 = convert_coordinates(self.body1.position)
        pos2 = convert_coordinates(self.body2.position)
        pygame.draw.line(display, (0, 0, 0), pos1, pos2, 2)

def game():
    ball_1 = Ball(200, 450)
    ball_2 = Ball(100, 150)
    
    string_1 = String(ball_1.body, (300, 550), "position")
    string_2 = String(ball_1.body, ball_2.body)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        ball_1.draw()
        ball_2.draw()
        string_1.draw()
        string_2.draw()
        
        
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()






















