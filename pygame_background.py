import pygame

pygame.init()
window = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Barbos adventure")
background = pygame.image.load('background.jpg').convert()
background = pygame.transform.smoothscale(background, window.get_size())

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()