import pygame
import math

pygame.init()

YELLOW = (255, 211, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_ORANGE = (255, 140, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Estrela de 5 Pontas")


def draw_star(screen, position, size, angle_degrees=0):
    x, y = position
    half_size = size // 2
    angle = math.radians(72)

    outer_points = []
    inner_points = []
    for i in range(5):
        outer_x = x + half_size * math.cos(math.radians(i * 72 + angle_degrees))
        outer_y = y - half_size * math.sin(math.radians(i * 72 + angle_degrees))
        inner_x = x + (half_size // 2) * math.cos(
            math.radians((i * 72 + 36) + angle_degrees)
        )
        inner_y = y - (half_size // 2) * math.sin(
            math.radians((i * 72 + 36) + angle_degrees)
        )
        outer_points.append((outer_x, outer_y))
        inner_points.append((inner_x, inner_y))

    points = []
    for i in range(5):
        points.append(outer_points[i])
        points.append(inner_points[i])

    pygame.draw.polygon(screen, DARK_ORANGE, points, 8)
    pygame.draw.polygon(screen, YELLOW, points, 0)


running = True
angle = 160

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_star(screen=screen, position=(400, 300), size=400, angle_degrees=angle)
    pygame.display.flip()

pygame.quit()
