import pygame

objects = []
frame = 1
worldx = 960
worldy = 720
fps = 40
ani = 4
qw = 1


class Button:
    def __init__(self, x, y, width, height, button_text='Button', onclick_function=None, one_press=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclick_function
        self.onePress = one_press

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(button_text, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mouse_pos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
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
                img = pygame.image.load(f'zip/main_dog/{i}.png')
            else:
                img = pygame.image.load(f'bad_hero.png')
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
        if 0 < self.rect.x + self.movex < worldx - 100:
            self.rect.x = self.rect.x + self.movex

        if 0 < self.rect.y + self.movey < worldy - 100:
            self.rect.y = self.rect.y + self.movey

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


def next_frame():
    global frame
    frame = 2


def show_screen1():
    Button(500, 600, 200, 70, 'Start', next_frame)
    pygame.display.set_caption("Barbos adventure")
    background = pygame.image.load('background.jpg').convert()
    background = pygame.transform.smoothscale(background, screen.get_size())
    screen.blit(background, (0, 0))
    for item in objects:
        item.process()


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
    background = pygame.image.load('background2.jpg')
    background = pygame.transform.scale(background, (960, 720))
    screen.blit(background, (0, 0))
    results = []
    record = 65
    user_result = 10
    records = open("records.txt", "r")
    for result in records:
        results.append(result)
    print(results)

    text_surface = font.render(f'Рекорд: {record}', False, (230, 230, 230))
    screen.blit(text_surface, (400, 0))
    text_surface2 = font.render(f'Ваш результат: {user_result}', False, (230, 230, 230))
    screen.blit(text_surface2, (400, 100))


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
backdrop = pygame.image.load('zip/data/homes_wall1.jpg')

player = Player("player", (100, 100))  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10
enemy = Player("enemy", (100, 200))
enemy.rect.x = 10  # go to x
enemy.rect.y = 100  # go to y
player_list.add(enemy)

running = True
while running:
    for event_game in pygame.event.get():
        if event_game.type == pygame.QUIT:
            running = False

        if frame == 1:
            show_screen1()

        elif frame == 2:
            show_screen2(event_game)

        else:
            show_screen3()

    if frame == 2:
        show_enemy()
        screen.blit(backdrop, backdropbox)
        player.update()
        enemy.update()
        player_list.draw(screen)


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
exit()