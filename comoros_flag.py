import math
import sys

import pygame
from pygame.locals import QUIT
from utils import draw_star, draw_crescent_moon

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

green = (0, 151, 57)
red = (239, 51, 64)
blue = (0, 61, 165)
white = (255, 255, 255)
yellow = (255, 209, 0)


while True:
    pygame.draw.rect(DISPLAYSURF, yellow, pygame.Rect(30, 30, 250, 31.2))
    pygame.draw.rect(DISPLAYSURF, white, pygame.Rect(30, 61, 250, 31.2))
    pygame.draw.rect(DISPLAYSURF, red, pygame.Rect(30, 92, 250, 31.2))
    pygame.draw.rect(DISPLAYSURF, blue, pygame.Rect(30, 123, 250, 33))

    pygame.draw.polygon(DISPLAYSURF, green, ((30, 30), (30, 155), (150, 92)))

    draw_crescent_moon(screen=DISPLAYSURF, position=(80, 95), size=60, color=green)

    draw_star(
        screen=DISPLAYSURF, position=(80, 70), size=10, angle_degrees=16, color=white
    )
    draw_star(
        screen=DISPLAYSURF, position=(80, 85), size=10, angle_degrees=16, color=white
    )
    draw_star(
        screen=DISPLAYSURF, position=(80, 100), size=10, angle_degrees=16, color=white
    )
    draw_star(
        screen=DISPLAYSURF, position=(80, 115), size=10, angle_degrees=16, color=white
    )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
