import random
import time
import sys
import os
import pygame

objects = []
frame = 1
worldx = 960
worldy = 800
fps = 60
ani = 4
qw = 1
game_score = 0
pygame.init()
f = pygame.font.SysFont('arial', 30)


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, name, size):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 7):
            if name == "player":
                img = pygame.image.load(f'data/main_dog/{i}.png')
            else:
                img = pygame.image.load(f'data/bad_hero.png')
            img = pygame.transform.scale(img, size)
            img.convert_alpha()  # optimise alpha

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

        if self.rect.x + self.movex < worldx - 100 and self.rect.x + self.movex > 0:
            self.rect.x = self.rect.x + self.movex
        # print(self.rect.y + self.movey < worldy - 180 and self.rect.y + self.movey > 0)

        if self.rect.y + self.movey < worldy - 100 and self.rect.y + self.movey > 0:
            self.rect.y = self.rect.y + self.movey

        # self.rect.x = self.rect.x + self.movex
        # self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        if self.movex == 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Ball(pygame.sprite.Sprite):
    image = load_image("bone.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.rect.y = random.randint(50, 750)
        self.image = pygame.transform.scale(self.image, (75, 40))
        self.image.convert_alpha()


    def update(self):
        global game_score
        if pygame.sprite.collide_mask(self, player):
            game_score += 1
            self.kill()


def next_frame():
    global frame
    frame = 2


def show_screen1():
    customButton = Button(500, 600, 200, 70, 'Start', next_frame)
    pygame.display.set_caption("Barbos adventure")
    background = pygame.image.load('data/background.jpg').convert()
    background = pygame.transform.smoothscale(background, screen.get_size())
    screen.blit(background, (0, 0))
    for object in objects:
        object.process()
    # background_colour = (255,255,255)
    # screen.fill(background_colour)


def show_screen2(event):
    if event.type == pygame.KEYDOWN:

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


def show_screen3():
    global your
    background = pygame.image.load('data/background2.jpg')
    background = pygame.transform.scale(background, (960, 800))
    screen.blit(background, (0, 0))
    res = []
    rfile = open('records.txt', 'r')
    for e in rfile:
        for i in range(len(e)):
            if e[i] == ' ':
                res.append(float(e[0:i]))



    text_surface = font.render(f'Рекорд: {min(res)} барбосьих секунд', False, (230, 230, 230))
    screen.blit(text_surface, (400, 0))
    text_surface2 = font.render(f'Ваш результат: {your} барбосьих секунд', False, (230, 230, 230))
    screen.blit(text_surface2, (400, 100))

def show_screen4():
    background = pygame.image.load('data/background2.jpg')
    background = pygame.transform.scale(background, (960, 800))
    screen.blit(background, (0, 0))

    text_surface = font.render(f'GAME OVER', False, (230, 230, 230))
    screen.blit(text_surface, (430, 400))



def show_enemy():
    global qw
    if qw == 1:
        enemy.control(10, 0)  # right
        qw = qw + 1


    elif enemy.rect.x == 10 and enemy.rect.y == 100:  # движение призрака
        enemy.control(10, 10)  # right
    elif enemy.rect.x == 770 and enemy.rect.y == 100:
        enemy.control(-10, 10)  # down
    elif enemy.rect.x == 770 and enemy.rect.y == 200:
        enemy.control(-10, -10)  # left
    elif enemy.rect.x == 20 and enemy.rect.y == 200:
        enemy.control(10, 10)  # down
    elif enemy.rect.x == 20 and enemy.rect.y == 300:
        enemy.control(10, -10)  # right
    elif enemy.rect.x == 770 and enemy.rect.y == 300:
        enemy.control(-10, 10)  # down
    elif enemy.rect.x == 770 and enemy.rect.y == 400:
        enemy.control(-10, -10)  # left
    elif enemy.rect.x == 10 and enemy.rect.y == 400:
        enemy.control(10, -10)  # up



pygame.init()
screen = pygame.display.set_mode([worldx, worldy])
font = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()
backdropbox = screen.get_rect()
backdrop = pygame.image.load('data/homes_wall1.jpg')

all_sprites = pygame.sprite.Group()
player = Player("player", (125, 125))
player.rect.x = 400  # go to x
player.rect.y = 400  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10
enemy = Player("enemy", (150, 300))
enemy.rect.x = 10  # go to x
enemy.rect.y = 100  # go to y
# player_list = pygame.sprite.Group()
player_list.add(enemy)

for i in range(20):
    Ball()

running = True
x = time.perf_counter()
z = 0
all_stats = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # show_screen2(event)
        if frame == 1:
            show_screen1()

        elif frame == 2:
            show_screen2(event)

        else:
            show_screen3()

    if frame == 2:
        show_enemy()
        screen.blit(backdrop, backdropbox)
        player.update()
        player_list.draw(screen)
        enemy.update()
        all_sprites.draw(screen)
        all_sprites.update()
        sc_text = f.render(str(game_score), 1, (128, 128, 128))
        screen.blit(sc_text, (20, 10))
        if game_score == 20:
            tic = round(time.perf_counter() - x, 2)
            with open(r"records.txt", "a") as file:
                file.write(f'{tic} \n')
            all_stats.append(tic)
            your = min(all_stats)
            player.rect.x = 4000  # go to x
            player.rect.y = 4000
            frame = 3
        if pygame.sprite.collide_mask(player, enemy):
            z = 1
        if z == 1:
            show_screen4()


    # screen.blit(backdrop, backdropbox)
    # player.update()
    # player_list.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
exit()
