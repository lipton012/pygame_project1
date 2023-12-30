import pygame
import sys
import os
pygame.init()

# screen = pygame.display.set_mode((1280, 768))
# image = pygame.image.load("main_hero.png").convert_alpha()
# image = pygame.transform.scale(image, (200,200))
# backdrop = pygame.image.load('homes_wall1.jpg')
# screen.blit(backdrop, (0, 0))
# while True:
#     # screen.fill((0, 255, 255))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()
#
#     screen.blit(image, (0, 0))
#     pygame.display.update()

worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

# BLUE = (25, 25, 200)
# BLACK = (23, 23, 23)
# WHITE = (254, 254, 254)
# ALPHA = (0, 255, 0)

key = pygame.image.load('key_image.png')

key = pygame.transform.scale(key, (200, 200))
world.blit(key, (0, 0))
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load('main_hero.png')
            img = pygame.transform.scale(img, (200, 200))
            img.convert_alpha()  # optimise alpha
            # img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        if self.rect.x + self.movex < worldx - 180 and self.rect.x + self.movex > 0:
            self.rect.x = self.rect.x + self.movex
        # print(self.rect.y + self.movey < worldy - 180 and self.rect.y + self.movey > 0)

        if self.rect.y + self.movey < worldy - 180 and self.rect.y + self.movey > 0:
            self.rect.y = self.rect.y + self.movey

        # self.rect.x = self.rect.x + self.movex
        # self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

backdrop = pygame.image.load('homes_wall1.jpg')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)


    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)