import pygame
from time import sleep

pygame.init()

display_width = 1280
display_height = 720
hero_width = 84
hero_height = 138
speed = 5
hero_x = 80
hero_y = 562
first_badguy_x = 350
first_badguy_y = 32
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

background = pygame.transform.scale(pygame.image.load('Warehouse Level.png'),
                                    (display_width, display_height))

clock = pygame.time.Clock()
GG_gun_sound = pygame.mixer.Sound('GG_gun_sound.ogg')
BG_gun_sound = pygame.mixer.Sound('BG_gun_sound.ogg')

game_over = False
absolute_death = False
logo_running = True
menu_running = True
credits_running = True
intro_running = True
game_running = True
outro_running = True
game_finished = False
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
got_a_card = False
door_allow = False
part_two_is_running = False
first_badguy_is_dead = False
second_badguy_is_dead = False
third_badguy_is_dead = False
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
first_bg_cd = 0
second_bg_cd = 0
third_bg_cd = 0
finish_counter = 0
GG_cd = 0
game_over_timer = -1

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
        display_name.blit(pygame.transform.scale(pygame.image.load('Bullet GG.png'), (8, 4)),
                          (self.bullet_x, self.bullet_y))


class BgBulletClass:
    def __init__(self, bullet_x, bullet_y, bullet_facing):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.bullet_facing = bullet_facing
        self.bullet_speed = 12 * bullet_facing

    def draw(self, display_name):
        display_name.blit(pygame.transform.scale(pygame.image.load('Bullet BG.png'), (8, 4)),
                          (self.bullet_x, self.bullet_y))


def f_hero_stands_left():
    global smokeAnimCount

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and not isRunning and left\
            and not game_over:
        win.blit(pygame.transform.scale(hero_stands_left[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_stands_right():
    global smokeAnimCount

    if not isClimbUp and not isClimbDown and not isSitting and \
            not isShooting and not isJump and not isRunning and right and not game_over:
        win.blit(pygame.transform.scale(hero_stands_right[smokeAnimCount // 10],
                                        (hero_width, hero_height)), (hero_x, hero_y))
        smokeAnimCount += 1


def f_hero_run_left():
    global animCount

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and isRunning and left\
            and not game_over:
        win.blit(pygame.transform.scale(hero_run_left[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_run_right():
    global animCount

    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and not isJump and isRunning and right\
            and not game_over:
        win.blit(pygame.transform.scale(hero_run_right[animCount // 5], (hero_width, hero_height)), (hero_x, hero_y))
        animCount += 1


def f_hero_jump_left():
    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and isJump and left and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_jump_right():
    if not isClimbUp and not isClimbDown and not isSitting and not isShooting and isJump and right and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero jump right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_left():
    if not isClimbUp and not isClimbDown and not isSitting and isShooting and left and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero shoot left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_shoot_right():
    if not isClimbUp and not isClimbDown and not isSitting and isShooting and right and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero shoot right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_sit_left():
    if isSitting and left and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero sit left.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_sit_right():
    if isSitting and right and not game_over:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero sit right.png'),
                                        (hero_width, hero_height)), (hero_x, hero_y))


def f_hero_climb():
    global climbAnim

    if isClimbUp or isClimbDown and not game_over:
        win.blit(pygame.transform.scale(hero_climb[climbAnim // 10], (84, 147)), (hero_x, hero_y))
        climbAnim += 1


def f_hero_dead_left():
    if game_over and left:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero dead left.png'), (195, 138)), (hero_x, hero_y+39))


def f_hero_dead_right():
    if game_over and right:
        win.blit(pygame.transform.scale(pygame.image.load('Hero/Hero dead right.png'), (195, 138)), (hero_x, hero_y+39))


def draw_hero():
    global isRunning, animCount, smokeAnimCount, climbAnim, finish_counter

    if climbAnim + 1 >= 20:
        climbAnim = 0

    if animCount + 1 >= 20:
        animCount = 0

    if smokeAnimCount + 1 >= 20:
        smokeAnimCount = 0

    if not game_finished:
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
        f_hero_dead_left()
        f_hero_dead_right()
    else:
        if 81 > finish_counter > 40:
            f_hero_stands_right()
            finish_counter -= 1
        if 41 > finish_counter > 0:
            pygame.draw.rect(win, (0, 0, 0), (1135, 340, 70, 150))
            f_hero_stands_right()
            finish_counter -= 1

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
        if not first_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy shoot right.png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
        if not second_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Second/Second bad guy shoot right.png'),
                                            (84, 138)), (second_badguy_x, second_badguy_y))
        if not third_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy shoot left.png'),
                                            (84, 138)), (third_badguy_x, third_badguy_y))
        if first_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad dead right.png'),
                                            (171, 138)), (first_badguy_x - 130, first_badguy_y + 12))
        if second_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Second/Second bad guy dead.png'),
                                            (138, 138)), (second_badguy_x - 130, second_badguy_y + 12))
        if third_badguy_is_dead:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/Third/Third bad guy dead.png'),
                                            (138, 138)), (third_badguy_x + 60, second_badguy_y + 12))
        first_bg_shoot()
        if hero_y == 562:
            second_bg_shoot()
            third_bg_shoot()

        for i in bg_bullets:
            i.draw(win)


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
    global game_running, isRunning, isShooting, isSitting, facing, isJump, combat_theme, hero_action, GG_cd

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE and not isSitting and not isJump and part_two_is_running:
                if not GG_cd:
                    isShooting = True
                    GG_gun_sound.play().set_volume(0.12)
                    if right:
                        facing = 1
                        bullets.append(BulletClass(hero_x + 70, hero_y + 45, facing))

                    if left:
                        facing = -1
                        bullets.append(BulletClass(hero_x + 10, hero_y + 45, facing))
                    GG_cd = 10

            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not isJump and \
                    not isClimbUp and not isClimbDown:
                isSitting = True

            if event.key == pygame.K_f:
                hero_action = True

        if event.type == pygame.KEYUP and not game_over:
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
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        print_text('Game is paused. Press ENTER to continue.', 400, 400, 20)
        p_keys = pygame.key.get_pressed()

        if p_keys[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
            paused = False

        pygame.display.update()
        clock.tick(15)


def first_bg_shoot():
    global first_bg_cd, bg_bullets
    if not first_badguy_is_dead and not game_over:
        if not first_bg_cd:
            new_bullet = BgBulletClass(first_badguy_x + 74, first_badguy_y + 35, 1)
            new_bullet.draw(win)
            first_bg_cd = 60
            bg_bullets.append(new_bullet)
            BG_gun_sound.play().set_volume(0.12)

        else:
            first_bg_cd -= 1


def second_bg_shoot():
    global second_bg_cd, bg_bullets
    if not second_badguy_is_dead and not game_over:
        if not second_bg_cd:
            new_bullet = BgBulletClass(second_badguy_x + 74, second_badguy_y + 30, 1)
            new_bullet.draw(win)
            second_bg_cd = 60
            bg_bullets.append(new_bullet)
            BG_gun_sound.play().set_volume(0.12)

        else:
            second_bg_cd -= 1


def third_bg_shoot():
    global third_bg_cd, bg_bullets
    if not third_badguy_is_dead and not game_over:
        if not third_bg_cd:
            new_bullet = BgBulletClass(third_badguy_x, third_badguy_y + 30, -1)
            new_bullet.draw(win)
            third_bg_cd = 60
            bg_bullets.append(new_bullet)
            BG_gun_sound.play().set_volume(0.12)

        else:
            third_bg_cd -= 1


def music_change_check():
    global combat_theme

    if combat_theme:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Combat theme.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.12)
        combat_theme = False


def show_logo():
    global logo_running

    pygame.mixer.music.load('Logo sound.mp3')
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.25)
    logo = pygame.image.load('Full VIMO Logo.png')

    while logo_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))
        win.blit(logo, (0, 0))
        pygame.display.update()
        clock.tick(15)
        sleep(3)
        break


def show_menu():
    global menu_running

    pygame.mixer.music.load('Main Theme.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
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
        play_demo_button.draw(575, 420, 'Start demo', show_intro, 70)
        credits_button.draw(700, 510, 'Credits', show_credits, 70)
        exit_button.draw(825, 600, 'Exit', quit, 70)

        pygame.display.update()
        clock.tick(60)


def show_credits():
    global credits_running

    back_button = Button(140, 60)

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
        print_text('Charachters and artist - Malachin Arseniy', 700, 340, 25)
        print_text('Composer - Ivanov Michail', 700, 380, 25)
        print_text('Level artist - Vlasov Daniil', 700, 420, 25)
        print_text('Brand designer - Vlasov Daniil', 700, 460, 25)

        print_text('Special thanks to', 500, 550, 30)
        print_text('ABTOZAK Group ', 495, 590, 40)
        print_text('for writing Game`s Main Theme', 420, 640, 30)

        back_button.draw(1100, 625, 'Back', show_menu, 50)

        pygame.display.update()
        clock.tick(60)


def show_intro():
    global intro_running

    start_button = Button(150, 60)

    while intro_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        win.fill((0, 0, 0))

        print_text('Japan, Akita, year 2031', 25, 25, 30)
    
        print_text('There was a powerful electromagnetic pulse during massive hackers attack on Akita`s', 80, 100, 25)
        print_text('government. The whole Japan lost power more than a month. During this time, huge amounts of', 25, 125, 25)
        print_text('information were erased, hospitals lost life supporting systems, prison inmates could leave ', 25, 150, 25)
        print_text('their cells and nobody could leave the country border by planes or trains.', 25, 175, 25)

        print_text('A year later, a special task force Neuron was created by APD (Akita Police Department),', 80, 250, 25)
        print_text('whose goal is eliminating potential hackers, as well as to prevent terrorist acts.', 25, 275, 25)
        
        print_text('Lloyd Davis is a prisoned hacker from UCA (United Cities of America), who was offered', 80, 350, 25)
        print_text('to become a Neuron operative in exchange for early release.', 25, 375, 25)
        
        print_text('Davis first mission is to eliminate defendants of Japanese-italian hackers group Medjed', 80, 450, 25)
        print_text('which commit suspicious acts in suburban warehouse...', 25, 475, 25)

        start_button.draw(1100, 625, 'Start', game_cycle, 50)

        pygame.display.update()        
        clock.tick(60)


def show_outro():
    global outro_running

    menu_button = Button(400, 60)

    while outro_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))

        print_text('Thanks for playing!', 700, 100, 50)

        menu_button.draw(900, 625, 'Back to the menu', show_menu, 50)

        pygame.display.update()
        clock.tick(60)


def check_bullet_hit():
    global bullets, first_badguy_is_dead, second_badguy_is_dead, third_badguy_is_dead
    for bullet in bullets:
        if not first_badguy_is_dead:
            if first_badguy_x + 40 > bullet.bullet_x > first_badguy_x and \
                    first_badguy_y + 138 > bullet.bullet_y > first_badguy_y:
                bullets.pop(bullets.index(bullet))
                first_badguy_is_dead = True

        if not second_badguy_is_dead:
            if second_badguy_x + 40 > bullet.bullet_x > second_badguy_x and \
                    second_badguy_y + 138 > bullet.bullet_y > second_badguy_y:
                bullets.pop(bullets.index(bullet))
                second_badguy_is_dead = True

        if not third_badguy_is_dead:
            if third_badguy_x + 84 > bullet.bullet_x > third_badguy_x + 40 and \
                    third_badguy_y + 138 > bullet.bullet_y > third_badguy_y:
                bullets.pop(bullets.index(bullet))
                third_badguy_is_dead = True


def show_deathScreen():
    global absolute_death

    restart_button = Button(405, 100)
    menu_button = Button(250, 100)

    while absolute_death:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        win.fill((0, 0, 0))

        print_text('You are dead...', 70, 30, 150)

        restart_button.draw(440, 300, 'Restart', game_cycle, 100)
        menu_button.draw(520, 500, 'Menu', show_menu, 100)

        pygame.display.update()
        clock.tick(60)


def check_bg_bullet_hit():
    global bg_bullets, game_over, game_over_timer
    if not isSitting:
        for bullet in bg_bullets:
            if hero_x + 40 > bullet.bullet_x > hero_x and hero_y + hero_height > bullet.bullet_y > hero_y:
                bg_bullets.pop(bg_bullets.index(bullet))
                game_over = True
                game_over_timer = 120


def second_part():
    global start_combat_timer, first_badguy_x, first_badguy_y, start_combat, badguyLadderCount, \
        first_badguy_animCount, second_badguy_animCount, second_badguy_x, third_badguy_x, \
        third_badguy_animCount, part_two_is_running, combat_theme, door_allow

    if start_combat:
        if 351 > start_combat_timer > 320:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy transmitter(1).png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            start_combat_timer -= 1

        if 321 > start_combat_timer > 240:
            win.blit(pygame.transform.scale(pygame.image.load('Bad guy/First/Bad guy transmitter(2).png'),
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            start_combat_timer -= 1

        if 241 > start_combat_timer > 204:
            first_badguy_x -= 3
            win.blit(pygame.transform.scale(first_badguy_run_left[first_badguy_animCount // 5],
                                            (84, 138)), (first_badguy_x, first_badguy_y))
            first_badguy_animCount += 1

            if first_badguy_animCount + 1 > 20:
                first_badguy_animCount = 0

            start_combat_timer -= 1
            pygame.draw.rect(win, (0, 0, 0), (1080, 525, 70, 140))

        if 205 > start_combat_timer > 184:
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
            first_badguy_x += 4
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
        start_combat, start_combat_timer, combat_theme, door_allow, got_a_card, game_finished, finish_counter, GG_cd, \
        game_over_timer, absolute_death, game_over

    absolute_death = False
    game_over = False

    pygame.mixer.music.stop()
    pygame.mixer.music.load('Soundtrack.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)

    while game_running:
        key_events()
        music_change_check()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for bullet in bullets:
            if display_width > bullet.bullet_x > 0:
                bullet.bullet_x += bullet.bullet_speed
            else:
                bullets.pop(bullets.index(bullet))

        for bullet in bg_bullets:
            if display_width > bullet.bullet_x > 0:
                bullet.bullet_x += bullet.bullet_speed
            else:
                bg_bullets.pop(bg_bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()

        if not isSitting and not isClimbUp and not isClimbDown and not isShooting and not game_over:
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

        if GG_cd:
            GG_cd -= 1

        if game_over_timer > 0:
            game_over_timer -= 1
        elif game_over_timer == 0:
            absolute_death = True
        win.blit(background, (0, 0))
        print_text(str(hero_x), 0, 0, 20)
        if got_a_card:
            print_text('You got a card', 400, 400, 70)
        if game_finished:
            print_text("You've completed the game", 200, 600, 70)
        if absolute_death:
            print_text("You are dead", 400, 200, 70)
        check_bullet_hit()
        check_bg_bullet_hit()
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

            if hero_x > 170 and hero_x + hero_width < 280 and hero_y == 347 and door_allow:
                ladderCounterUp = 63
                isClimbUp = True

            if hero_x > 170 and hero_x + hero_width < 280 and hero_y == 32:
                ladderCounterDown = 63
                isClimbDown = True

            if hero_x > 1100 and hero_x + hero_width < 1300 and hero_y == 347:
                if not got_a_card:
                    print_text('Oh, shit', 1000, 275, 20)
                    print_text('I need a keycard', 1000, 300, 20)
                else:
                    finish_counter = 80
                    game_finished = True

                if not door_allow:
                    start_combat = True
                    start_combat_timer = 350
                    combat_theme = True

            if hero_x > 800 and hero_x + hero_width < 950 and hero_y == 562 and part_two_is_running:
                got_a_card = True

        pygame.display.update()
        clock.tick(60)


bullets = []
bg_bullets = []

show_logo()
show_menu()

pygame.quit()
