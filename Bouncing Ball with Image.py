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
body = pymunk.Body()
body.position = 400, 600
shape = pymunk.Circle(body, ball_radius)
shape.density = 1
shape.elasticity = 1
space.add(body, shape)

segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape = pymunk.Segment(segment_body, (0, 250), (800, 50), 5)
segment_shape.elasticity = 1
space.add(segment_shape)

image = pygame.image.load("basketball.png")
image = pygame.transform.scale(image, (ball_radius*2, ball_radius*2))

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        display.fill((255, 255, 255))
        x, y = convert_coordinates(body.position)
        # pygame.draw.circle(display, (255, 0, 0), (int(x), int(y)), ball_radius)
        display.blit(image, (int(x)-ball_radius, int(y)-ball_radius))
        pygame.draw.line(display, (0, 0, 0), (0, 550), (800, 750), 5)

        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

game()
pygame.quit()






















