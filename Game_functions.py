import pygame

pygame.init()


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
    global isRunning
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                isRunning = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                isRunning = False


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