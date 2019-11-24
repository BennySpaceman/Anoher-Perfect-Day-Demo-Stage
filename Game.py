import pygame

pygame.init()

display_width = 1280
display_height = 720
hero_width = 84
hero_height = 138
speed = 5
hero_x = 50
hero_y = display_height - hero_height - 20
badguy_x = 120
badguy_y = display_height - 690

Game_Name = 'Ванильный питон'
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_icon(pygame.image.load('Mascot.png'))
pygame.display.set_caption(Game_Name)
badguy_stand_right = pygame.transform.scale(pygame.image.load('Bad guy/Bad guy stand right.png'), (51, 138))
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

background = pygame.transform.scale(pygame.image.load('Warehouse level.png'), (display_width, display_height))
pygame.mixer.music.load('Soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)
clock = pygame.time.Clock()

game_running = True
left = False
right = True
isRunning = False
isJump = False
isShooting = False
isSitting = False
jumpCount = 10
animCount = 0
smokeAnimCount = 0
facing = 1


class BulletClass:
    def __init__(self, bullet_x, bullet_y, bullet_facing):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.bullet_facing = bullet_facing
        self.bullet_speed = 12 * bullet_facing

    def draw(self, display_name):
        display_name.blit(pygame.transform.scale(pygame.image.load('Bullet GG.png'), (5, 3)),
                          (self.bullet_x, self.bullet_y))


def f_hero_stands_left():
    global smokeAnimCount
    if not isSitting and not isShooting and not isJump and not isRunning and left:
        win.blit(pygame.transform.scale(hero_stands_left[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_stands_right():
    global smokeAnimCount
    if not isSitting and not isShooting and not isJump and not isRunning and right:
        win.blit(pygame.transform.scale(hero_stands_right[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_run_left():
    global animCount
    if not isSitting and not isShooting and not isJump and isRunning and left:
        win.blit(pygame.transform.scale(hero_run_left[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_run_right():
    global animCount
    if not isSitting and not isShooting and not isJump and isRunning and right:
        win.blit(pygame.transform.scale(hero_run_right[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_jump_left():
    if not isSitting and not isShooting and isJump and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_jump_right():
    if not isSitting and not isShooting and isJump and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_left():
    if not isSitting and isShooting and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero shoot left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_right():
    if not isSitting and isShooting and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero shoot right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_sit_left():
    if isSitting and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero sit left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_sit_right():
    if isSitting and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero sit right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def draw_hero():
    global isRunning, animCount, smokeAnimCount

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
    f_hero_shoot_left()
    f_hero_shoot_right()
    f_hero_sit_left()
    f_hero_sit_right()
    for i in bullets:
        i.draw(win)


def draw_badguy():
    win.blit(badguy_stand_right, (badguy_x, badguy_y))


def jump():
    global jumpCount, isJump, hero_y, hero_x
    if not isSitting:
        if jumpCount >= -10:
            if jumpCount < 0:
                hero_y += (jumpCount ** 2) / 1.8
            else:
                hero_y -= (jumpCount ** 2) / 1.8
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


def key_events():
    global game_running, isRunning, isShooting, isSitting, facing, isJump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            if event.key == pygame.K_SPACE:
                isShooting = True
                if right:
                    facing = 1
                if left:
                    facing = -1
                bullets.append(BulletClass(round(hero_x + hero_width // 2), round(hero_y + hero_height - 92), facing))
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                isSitting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                isRunning = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                isRunning = False
            if event.key == pygame.K_SPACE:
                isShooting = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                isSitting = False


def print_text(message, x, y, font_color=(255, 255, 255), font_type='bahnschrift.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))


def pause():
    global game_running
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
        print_text('Game is paused. Press ENTER to continue.', 400, 400)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        clock.tick(15)


bullets = []

while game_running:
    clock.tick(60)
    key_events()

    for bullet in bullets:
        if display_width > bullet.bullet_x > 0:
            bullet.bullet_x += bullet.bullet_speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        pause()
    if not isSitting:
        if (keys[pygame.K_LEFT] and hero_x > 5) or (keys[pygame.K_a] and hero_x > 5):
            hero_x -= speed
            left = True
            right = False
            isRunning = True
        if (keys[pygame.K_RIGHT] and hero_x < (display_width - hero_width - 5)) or \
                (keys[pygame.K_d] and hero_x < (display_width - hero_width - 5)):
            hero_x += speed
            left = False
            right = True
            isRunning = True

    if not isJump:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            isJump = True
    else:
        jump()
    win.blit(background, (0, 0))
    draw_hero()
    draw_badguy()
    pygame.display.update()

pygame.quit()
