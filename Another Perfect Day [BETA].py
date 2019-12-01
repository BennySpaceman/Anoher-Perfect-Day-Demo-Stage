import pygame
from time import sleep

pygame.init()

display_width = 1280
display_height = 720
hero_width = 84
hero_height = 138
speed = 5
hero_x = 1000
hero_y = 347
first_badguy_x = 350
first_badguy_y = display_height - 688
second_badguy_x = 1070
second_badguy_y = 562
third_badguy_x = 1070
third_badguy_y = 562

Game_Name = 'Another perfect day [BETA]'
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_icon(pygame.image.load('Game icon.png'))
pygame.display.set_caption(Game_Name)

first_badguy_climb = [pygame.image.load('Bad guy/First/Bad guy climb 1.png'),
                      pygame.image.load('Bad guy/First/Bad guy climb 2.png')]

first_badguy_stand_right = [pygame.image.load('Bad guy/First/Bad guy smoke 1.png'),
                            pygame.image.load('Bad guy/First/Bad guy smoke 2.png')]

first_badguy_run_left = [pygame.image.load('Bad guy/First/Bad guy run left(1).png'),
                         pygame.image.load('Bad guy/First/Bad guy run left(2).png'),
                         pygame.image.load('Bad guy/First/Bad guy run left(3).png'),
                         pygame.image.load('Bad guy/First/Bad guy run left(4).png')]

first_badguy_run_right = [pygame.image.load('Bad guy/First/Bad guy run right(1).png'),
                          pygame.image.load('Bad guy/First/Bad guy run right(2).png'),
                          pygame.image.load('Bad guy/First/Bad guy run right(3).png'),
                          pygame.image.load('Bad guy/First/Bad guy run right(4).png')]

second_badguy_run_left = [pygame.image.load('Bad guy/Second/Second bad guy run left(1).png'),
                          pygame.image.load('Bad guy/Second/Second bad guy run left(2).png'),
                          pygame.image.load('Bad guy/Second/Second bad guy run left(3).png'),
                          pygame.image.load('Bad guy/Second/Second bad guy run left(4).png')]

third_badguy_run_left = [pygame.image.load('Bad guy/Third/Third bad guy run left (1).png'),
                         pygame.image.load('Bad guy/Third/Third bad guy run left (2).png'),
                         pygame.image.load('Bad guy/Third/Third bad guy run left (3).png'),
                         pygame.image.load('Bad guy/Third/Third bad guy run left (4).png')]

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

hero_climb = [pygame.image.load('Hero/Hero climb (1).png'),
              pygame.image.load('Hero/Hero climb (2).png')]

background = pygame.transform.scale(pygame.image.load('Warehouse Level (v.2.0).png'),
                                    (display_width, display_height))

pygame.mixer.music.load('Soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)
clock = pygame.time.Clock()

intro_running = True
menu_running = True
credits_running = True
game_running = True
left = False
right = True
isRunning = False
isJump = False
isShooting = False
isSitting = False
isClimbUp = False
isClimbDown = False
combat_theme = False
hero_action = False
start_combat = False
door_allow = False
part_two_is_running = False
jumpCount = 10
animCount = 0
smokeAnimCountBadGuy = 0
badguyLadderCount = 0
smokeAnimCount = 0
facing = 1
ladderCounterUp = 0
ladderCounterDown = 0
climbAnim = 0
start_combat_timer = 0
first_badguy_animCount = 0
second_badguy_animCount = 0
third_badguy_animCount = 0


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (32, 32, 32)
        self.active_clr = (71, 71, 71)

    def draw(self, x, y, message, action, font_size):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(win, self.active_clr, (x, y, self.width, self.height))

            if click[0] == 1:
                if action == quit:
                    pygame.quit()
                    quit()
                else:
                    action()

        else:
            pygame.draw.rect(win, self.inactive_clr, (x, y, self.width, self.height))

        print_text(message=message, x=x + 5, y=y, font_size=font_size)


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

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and not isRunning and left:
        win.blit(pygame.transform.scale(hero_stands_left[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_stands_right():
    global smokeAnimCount

    if not isClimbUp and not isClimbDown and not isSitting and \
            not isShooting and not isJump and not isRunning and right:
        win.blit(pygame.transform.scale(hero_stands_right[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_run_left():
    global animCount

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and isRunning and left:
        win.blit(pygame.transform.scale(hero_run_left[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_run_right():
    global animCount

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and isRunning and right:
        win.blit(pygame.transform.scale(hero_run_right[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_jump_left():
    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and isJump and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_jump_right():
    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and isJump and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_left():
    if not isClimbUp and not isClimbDown and not isSitting and isShooting and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero shoot left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_right():
    if not isClimbUp and not isClimbDown and not isSitting and isShooting and right:
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


def f_hero_climb():
    global climbAnim

    if isClimbUp or isClimbDown:
        win.blit(pygame.transform.scale(hero_climb[climbAnim // 10], (84, 147)), (hero_x, hero_y))
        climbAnim += 1


def draw_hero():
    global isRunning, animCount, smokeAnimCount, climbAnim

    if climbAnim + 1 >= 20:
        climbAnim = 0

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
    f_hero_climb()

    for i in bullets:
        i.draw(win)


def ladder_climb():
    global ladderCounterUp, ladderCounterDown, isClimbUp, isClimbDown, hero_y, hero_x, climbAnim

    if ladderCounterUp > 0:
        hero_y -= 5
        ladderCounterUp -= 1

    if ladderCounterUp == 0:
        isClimbUp = False

    if ladderCounterDown > 0:
        hero_y += 5
        ladderCounterDown -= 1

    if ladderCounterDown == 0:
        isClimbDown = False


def draw_badguys():
    global smokeAnimCountBadGuy

    if not start_combat and not part_two_is_running:
        win.blit(pygame.transform.scale(first_badguy_stand_right[smokeAnimCountBadGuy // 60], (84, 138)),
                 (first_badguy_x, first_badguy_y))
        smokeAnimCountBadGuy += 1

    if smokeAnimCountBadGuy + 1 > 120:
        smokeAnimCountBadGuy = 0

    if part_two_is_running:
        win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy shoot right.png'),
                                        (84, 138)), (first_badguy_x, first_badguy_y))
        win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Second/Second bad guy shoot right.png'),
                                        (84, 138)), (second_badguy_x, second_badguy_y))
        win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy shoot left.png'),
                                        (84, 138)), (third_badguy_x, third_badguy_y))


def jump():
    global jumpCount, isJump, hero_y, hero_x

    if not isSitting:
        if jumpCount >= -10:
            if jumpCount < 0:
                hero_y += (jumpCount ** 2) / 5
            else:
                hero_y -= (jumpCount ** 2) / 5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


def key_events():
    global game_running, isRunning, isShooting, isSitting, facing, isJump, combat_theme, hero_action

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

            if event.key == pygame.K_SPACE and not isSitting:
                isShooting = True
                if right:
                    facing = 1

                if left:
                    facing = -1
                bullets.append(BulletClass(round(hero_x + hero_width // 2), round(hero_y + hero_height - 92), facing))

            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not isJump:
                isSitting = True

            if event.key == pygame.K_f:
                hero_action = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                isRunning = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                isRunning = False

            if event.key == pygame.K_SPACE:
                isShooting = False

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                isSitting = False

            if event.key == pygame.K_f:
                hero_action = False


def print_text(message, x, y, font_size, font_color=(255, 255, 255), font_type='Boo City.ttf'):
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

        print_text('Game is paused. Press ENTER to continue.', 400, 400, 20)
        p_keys = pygame.key.get_pressed()

        if p_keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)


def music_change_check():
    global combat_theme

    if combat_theme:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Combat theme.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.25)
        combat_theme = False


def show_intro():
    global intro_running

    logo = pygame.transform.scale(pygame.image.load('VIMO Games Logo.png'), (400, 400))

    while intro_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))
        win.blit(logo, (460, 160))
        pygame.display.update()
        clock.tick(15)
        sleep(3)
        break


def show_menu():
    global menu_running

    menu_background = pygame.image.load('Menu.png')

    play_demo_button = Button(400, 70)
    credits_button = Button(275, 70)
    exit_button = Button(150, 70)

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(menu_background, (0, 0))
        play_demo_button.draw(575, 420, 'Start demo', game_cycle, 70)
        credits_button.draw(700, 510, 'Credits', show_credits, 70)
        exit_button.draw(825, 600, 'Exit', quit, 70)

        pygame.display.update()
        clock.tick(60)


def show_credits():
    global credits_running

    back_button = Button(125, 60)

    while credits_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))
        print_text('Another Perfect Day', 225, 5, 75)
        print_text('VIMO Game Studio Crew:', 400, 100, 40)
        print_text('Game director - Vlasov Daniil', 400, 170, 30)

        print_text('Programming division:', 100, 240, 40)
        print_text('Head programmer - Olyanin Danila', 100, 300, 25)
        print_text('Functions developer - Vlasov Daniil', 100, 340, 25)
        print_text('Functions developer - Malachin Arseniy', 100, 380, 25)
        print_text('Assistance in programming - Ivanov Michail', 100, 420, 25)

        print_text('Design division:', 700, 240, 40)
        print_text('Game designer - Vlasov Daniil', 700, 300, 25)
        print_text('Charachters artist - Malachin Arseniy', 700, 340, 25)
        print_text('Composer - Ivanov Michail', 700, 380, 25)
        print_text('Level artist - Vlasov Daniil', 700, 420, 25)
        print_text('Brand designer - Vlasov Daniil', 700, 460, 25)

        print_text('Special thanks to', 500, 550, 30)
        print_text('ABTOZAK Group ', 495, 590, 40)
        print_text('for writing Game`s Main Theme', 420, 640, 30)

        back_button.draw(1100, 625, 'Back', show_menu, 50)

        pygame.display.update()
        clock.tick(60)


def second_part():
    global start_combat_timer, first_badguy_x, first_badguy_y, start_combat, badguyLadderCount, \
        first_badguy_animCount, second_badguy_animCount, second_badguy_x, third_badguy_x, \
        third_badguy_animCount, part_two_is_running, combat_theme, door_allow

    if start_combat:
        if 351 > start_combat_timer > 320:
            print_text('1', 0, 200, font_size=60, font_color=(0, 0, 0))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy transmitter(1).png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            start_combat_timer -= 1

        if 321 > start_combat_timer > 240:
            print_text('2', 0, 200, font_size=60, font_color=(0, 0, 0))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy transmitter(2).png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            start_combat_timer -= 1

        if 241 > start_combat_timer > 204:
            print_text('3', 0, 200, font_size=60, font_color=(0, 0, 0))
            first_badguy_x -= 3
            win.blit(pygame.transform.scale(first_badguy_run_left[first_badguy_animCount // 5],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            first_badguy_animCount += 1

            if first_badguy_animCount + 1 > 20:
                first_badguy_animCount = 0

            start_combat_timer -= 1
            pygame.draw.rect(win, (0, 0, 0), (1080, 525, 70, 140))

        if 205 > start_combat_timer > 184:
            print_text('4', 0, 200, font_size=60, font_color=(0, 0, 0))
            first_badguy_x -= 3
            win.blit(pygame.transform.scale(first_badguy_run_left[first_badguy_animCount // 5],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            first_badguy_animCount += 1

            if first_badguy_animCount + 1 > 20:
                first_badguy_animCount = 0

            start_combat_timer -= 1
            pygame.draw.rect(win, (0, 0, 0), (1080, 525, 70, 140))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Second/Second bad guy left.png'),
                                            (84, 138)), (second_badguy_x, second_badguy_y))

        if 185 > start_combat_timer > 151:
            print_text('5', 0, 200, font_size=60, font_color=(0, 0, 0))
            first_badguy_y += 5
            second_badguy_x -= 5
            win.blit(pygame.transform.scale(first_badguy_climb[badguyLadderCount // 10],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            badguyLadderCount += 1

            if badguyLadderCount + 1 > 20:
                badguyLadderCount = 0

            pygame.draw.rect(win, (0, 0, 0), (1080, 525, 70, 140))
            win.blit(pygame.transform.scale(second_badguy_run_left[second_badguy_animCount // 5],
                                            (84, 138)), (second_badguy_x, second_badguy_y))
            second_badguy_animCount += 1

            if second_badguy_animCount + 1 > 20:
                second_badguy_animCount = 0

            start_combat_timer -= 1

        if 152 > start_combat_timer > 121:
            print_text('6', 0, 200, font_size=60, font_color=(0, 0, 0))
            first_badguy_y += 5
            second_badguy_x -= 5
            win.blit(pygame.transform.scale(first_badguy_climb[badguyLadderCount // 10],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            badguyLadderCount += 1

            if badguyLadderCount + 1 > 20:
                badguyLadderCount = 0

            pygame.draw.rect(win, (0, 0, 0), (1080, 525, 70, 140))
            win.blit(pygame.transform.scale(second_badguy_run_left[second_badguy_animCount // 5],
                                            (84, 138)), (second_badguy_x, second_badguy_y))
            second_badguy_animCount += 1

            if second_badguy_animCount + 1 > 20:
                second_badguy_animCount = 0

            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy left.png'),
                                            (84, 138)), (third_badguy_x, third_badguy_y))
            start_combat_timer -= 1

        if 122 > start_combat_timer > 60:
            print_text('7', 0, 200, font_size=60, font_color=(0, 0, 0))
            first_badguy_x += 5
            second_badguy_x -= 5
            third_badguy_x -= 5
            win.blit(pygame.transform.scale(first_badguy_run_right[first_badguy_animCount // 5],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            first_badguy_animCount += 1

            if first_badguy_animCount + 1 > 20:
                first_badguy_animCount = 0

            win.blit(pygame.transform.scale(second_badguy_run_left[second_badguy_animCount // 5],
                                            (84, 138)), (second_badguy_x, second_badguy_y))
            second_badguy_animCount += 1

            if second_badguy_animCount + 1 > 20:
                second_badguy_animCount = 0

            win.blit(pygame.transform.scale(third_badguy_run_left[third_badguy_animCount // 5],
                                            (84, 138)), (third_badguy_x, third_badguy_y))
            third_badguy_animCount += 1

            if third_badguy_animCount + 1 > 20:
                third_badguy_animCount = 0

            start_combat_timer -= 1

        if 61 > start_combat_timer > 0:
            print_text('8', 0, 200, font_size=60, font_color=(0, 0, 0))
            second_badguy_x -= 5
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy shoot right.png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            win.blit(pygame.transform.scale(second_badguy_run_left[second_badguy_animCount // 5], (84, 138)),
                     (second_badguy_x, second_badguy_y))
            second_badguy_animCount += 1

            if second_badguy_animCount + 1 > 20:
                second_badguy_animCount = 0

            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy shoot left.png'),
                                            (84, 138)), (third_badguy_x, third_badguy_y))
            start_combat_timer -= 1
        if start_combat_timer == 0:
            print_text('9', 0, 200, font_size=60, font_color=(0, 0, 0))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy shoot right.png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Second/Second bad guy shoot right.png'),
                                            (84, 138)), (second_badguy_x, second_badguy_y))
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy shoot left.png'),
                                            (84, 138)), (third_badguy_x, third_badguy_y))
            start_combat = False
            part_two_is_running = True
            door_allow = True


def game_cycle():
    global isClimbUp, isClimbDown, hero_x, hero_y, left, right, isRunning, isJump, ladderCounterUp, ladderCounterDown, \
        start_combat, start_combat_timer, combat_theme

    while game_running:
        clock.tick(60)
        key_events()
        music_change_check()

        for bullet in bullets:
            if display_width > bullet.bullet_x > 0:
                bullet.bullet_x += bullet.bullet_speed
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            pause()

        if not isSitting and not isClimbUp and not isClimbDown:
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
        print_text(str(hero_x), 0, 0, 20)
        print_text(str(hero_y), 0, 30, 20)
        draw_hero()
        ladder_climb()
        draw_badguys()
        second_part()

        if hero_action:
            if hero_x > 1050 and hero_x + hero_width < 1200 and hero_y == 562:
                pygame.draw.rect(win, (0, 0, 0), (800, 465, 430, 80))
                print_text("It's guard room", 820, 470, 20)
                print_text("I'd better not to enter this door", 820, 500, 20)

            if hero_x > 490 and hero_x + hero_width < 600 and hero_y == 562:
                ladderCounterUp = 43
                isClimbUp = True

            if hero_x > 490 and hero_x + hero_width < 600 and hero_y == 347:
                ladderCounterDown = 43
                isClimbDown = True

            if hero_x > 170 and hero_x + hero_width < 280 and hero_y == 347:
                ladderCounterUp = 63
                isClimbUp = True

            if hero_x > 170 and hero_x + hero_width < 280 and hero_y == 32:
                ladderCounterDown = 63
                isClimbDown = True

            if hero_x > 1100 and hero_x + hero_width < 1300 and hero_y == 347:
                print_text('Oh, shit', 1000, 275, 20)
                print_text('I need a keycard', 1000, 300, 20)
                if not door_allow:
                    start_combat = True
                    start_combat_timer = 350
                    combat_theme = True

        pygame.display.update()


bullets = []

show_intro()
show_menu()

pygame.quit()
