import pygame

pygame.init()

Game_Name = 'Ванильный питон'
win = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(pygame.image.load('Mascot.png'))
pygame.display.set_caption(Game_Name)
hero_run_right = [pygame.image.load('Hero/Hero run right(1).png'),
                  pygame.image.load('Hero/Hero run right(2).png'),
                  pygame.image.load('Hero/Hero run right(3).png'),
                  pygame.image.load('Hero/Hero run right(4).png')]

hero_run_left = [pygame.image.load('Hero/Hero run left(1).png'),
                 pygame.image.load('Hero/Hero run left(2).png'),
                 pygame.image.load('Hero/Hero run left(3).png'),
                 pygame.image.load('Hero/Hero run left(4).png')]

hero_stands_left = [pygame.image.load('Hero/Hero stand left.png'),
                    pygame.image.load('Hero/Hero smoke left.png')]

hero_stands_right = [pygame.image.load('Hero/Hero stand right.png'),
                     pygame.image.load('Hero/Hero smoke right.png')]

background = pygame.transform.scale(pygame.image.load('Background.png'), (1280, 720))
clock = pygame.time.Clock()

width = 55
height = 115
speed = 5
x = 50
y = 720 - height - 50

game_running = True
left = False
right = True
isRunning = False
isJump = False
jumpCount = 10
animCount = 0
smokeAnimCount = 0


def f_hero_stands_left():
    global smokeAnimCount
    if not isJump and not isRunning and left:
        win.blit(pygame.transform.scale(hero_stands_left[smokeAnimCount // 10], (35, 115)), (x, y))
        smokeAnimCount += 1


def f_hero_stands_right():
    global smokeAnimCount
    if not isJump and not isRunning and right:
        win.blit(pygame.transform.scale(hero_stands_right[smokeAnimCount // 10], (35, 115)), (x, y))
        smokeAnimCount += 1


def f_hero_run_left():
    global animCount
    if not isJump and isRunning and left:
        win.blit(pygame.transform.scale(hero_run_left[animCount // 5], (55, 115)), (x, y))
        animCount += 1


def f_hero_run_right():
    global animCount
    if not isJump and isRunning and right:
        win.blit(pygame.transform.scale(hero_run_right[animCount // 5], (55, 115)), (x, y))
        animCount += 1


def f_hero_jump_left():
    if isJump and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump left.png'), (68, 108)), (x, y))


def f_hero_jump_right():
    if isJump and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump right.png'), (68, 108)), (x, y))


def game_quit():
    global game_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False


def draw_window():
    global isRunning
    global animCount
    global smokeAnimCount

    win.blit(background, (0, 0))

    if animCount + 1 >= 20:
        animCount = 0
    if smokeAnimCount + 1 >= 20:
        smokeAnimCount = 0

    f_hero_stands_left()
    f_hero_stands_right()
    f_hero_run_left()
    f_hero_run_right()
    f_hero_jump_left()
    f_hero_jump_right()

    for bla in pygame.event.get():
        if bla.type == pygame.KEYUP:
            if bla.key == pygame.K_RIGHT or bla.key == pygame.K_d:
                isRunning = False
            if bla.key == pygame.K_LEFT or bla.key == pygame.K_a:
                isRunning = False
    pygame.display.update()


def jump():
    global jumpCount
    global isJump
    global y
    global x
    if jumpCount >= -10:
        if jumpCount < 0:
            y += (jumpCount ** 2) / 3
        else:
            y -= (jumpCount ** 2) / 3
        jumpCount -= 1
    else:
        isJump = False
        jumpCount = 10


while game_running:
    clock.tick(120)
    game_quit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and x > 5) or (keys[pygame.K_a] and x > 5):
        x -= speed
        left = True
        right = False
        isRunning = True
    if (keys[pygame.K_RIGHT] and x < (1280 - width - 5)) or (keys[pygame.K_d] and x < (1280 - width - 5)):
        x += speed
        left = False
        right = True
        isRunning = True

    if not isJump:
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            isJump = True
    else:
        jump()
    draw_window()
pygame.quit()
