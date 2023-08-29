import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

star_points = [(165, 151), (200, 20), (235, 151), (371, 144), (257, 219),
               (306, 346), (200, 260), (94, 346), (143, 219), (29, 144)]

for i in range(len(star_points)):
  star_points[i] = (star_points[i][0] / 10 + 50, star_points[i][1] / 10 + 70)

while True:
  pygame.draw.rect(DISPLAYSURF, blue, pygame.Rect(30, 30, 250, 25))
  pygame.draw.rect(DISPLAYSURF, white, pygame.Rect(30, 55, 250, 25))
  pygame.draw.rect(DISPLAYSURF, blue, pygame.Rect(30, 80, 250, 25))
  pygame.draw.rect(DISPLAYSURF, white, pygame.Rect(30, 105, 250, 25))
  pygame.draw.rect(DISPLAYSURF, blue, pygame.Rect(30, 130, 250, 25))

  pygame.draw.polygon(DISPLAYSURF, red, ((30, 30), (30, 155), (150, 92)))
  pygame.draw.polygon(DISPLAYSURF, white, star_points, 0)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
