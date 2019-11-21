import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))
Game_Name = 'Ванильный питон'

pygame.display.set_caption(Game_Name)

white = (255, 255, 255)
black = (0, 0, 0)

background = pygame.image.load('Background.png')
hero = pygame.image.load('Hero — копия.png')

clock = pygame.time.Clock()

width = 35
height = 114
speed = 5
x = 50
y = 720-height-5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

# img = pygame.image.load('IMG_0470.gif')


def draw_window():
    # win.fill(white)
    # global animCount
    win.blit(background, (0, 0))
    win.blit(hero, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and x > 5) or (keys[pygame.K_a] and x > 5):
        x -= speed
        left = True
        right = False
    if (keys[pygame.K_RIGHT] and x < (1280-width-5)) or (keys[pygame.K_d] and x < (1280-width-5)):
        x += speed
        left = False
        right = True
    if not isJump:
        # if (keys[pygame.K_UP] and y > 0) or (keys[pygame.K_w] and y > 0):
        #     y -= speed
        # if (keys[pygame.K_DOWN] and y < (720-height)) or (keys[pygame.K_s] and y < (720-height)):
        #     y += speed
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount ** 2) / 3
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    draw_window()
pygame.quit()
