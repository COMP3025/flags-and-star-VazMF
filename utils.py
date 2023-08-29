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


def draw_star(screen, position, size, angle_degrees=0, color=WHITE):
    x, y = position
    half_size = size // 2

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

    pygame.draw.polygon(screen, color, points, 0)


def draw_crescent_moon(screen, position, size, color):
    pygame.draw.circle(screen, WHITE, (position[0] - size // 4, position[1]), size // 2)

    pygame.draw.circle(screen, color, position, size // 2)
