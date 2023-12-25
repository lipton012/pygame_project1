import pygame
from pygame.locals import *

green = (0, 255, 0)
blue = (0, 0, 128)
screen = pygame.display.set_mode((500,500),HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Prizrak_v1')
background_colour = (255,255,255)
screen.fill(background_colour)
print(pygame.font.get_fonts())
pygame.init()
font =pygame.font.Font(pygame.font.get_default_font(), 30)
text = font.render('Start', True, green, blue)
imp = pygame.image.load("background.jpg").convert()
# screen.blit(imp, (0, 0))
screen.blit(pygame.transform.scale(imp, (500, 500)), (0, 0))
pygame.display.flip()




running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False