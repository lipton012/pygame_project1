import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 20)
objects = []
window = pygame.display.set_mode((1280, 768))

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
        window.blit(self.buttonSurface, self.buttonRect)

def show_level():
    print('Button Pressed')
    image = pygame.image.load("main_hero.png").convert_alpha()
    image = pygame.transform.scale(image, (200, 200))
    background = pygame.image.load('homes_wall1.jpg')
    window.blit(background, (0, 0))
    while True:
        # screen.fill((0, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.blit(image, (0, 0))
        pygame.display.update()




customButton = Button(500, 600, 200, 70, 'Start', show_level)


clock = pygame.time.Clock()
pygame.display.set_caption("Barbos adventure")
background = pygame.image.load('background.jpg').convert()
background = pygame.transform.smoothscale(background, window.get_size())
window.blit(background, (0, 0))
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for object in objects:
        object.process()


    pygame.display.flip()

pygame.quit()
exit()