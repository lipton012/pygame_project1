import pygame
import sys
import os
pygame.init()


worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

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
        for i in range(1, 7):
            img = pygame.image.load(f'main_dog/{i}.png')
            img = pygame.transform.scale(img, (100, 100))
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

        # moving up
        if self.movey < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving down
        if self.movey > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

backdrop = pygame.image.load('data/homes_wall1.jpg')
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
            # if event.key == ord('q'):
            #     pygame.quit()
            #     try:
            #         sys.exit()
            #     finally:
            #         main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)


    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)