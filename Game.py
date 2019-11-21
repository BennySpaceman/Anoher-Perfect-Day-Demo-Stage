
import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))
Game_Name = 'Untitled Game 1'

pygame.display.set_caption(Game_Name)

white = (255, 255, 255)
black = (0, 0, 0)


width = 40
height = 60
speed = 5
x = 50
y = 720-height

isJump = False
jumpCount = 10

img = pygame.image.load('IMG_0470.gif')

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and x > 0) or (keys[pygame.K_a] and x > 0):
        x -= speed
    if (keys[pygame.K_RIGHT] and x < (1280-width)) or (keys[pygame.K_d] and x < (1280-width)):
        x += speed
    if not(isJump):
        # if (keys[pygame.K_UP] and y > 0) or (keys[pygame.K_w] and y > 0):
        #     y -= speed
        # if (keys[pygame.K_DOWN] and y < (720-height)) or (keys[pygame.K_s] and y < (720-height)):
        #     y += speed
        if keys[pygame.K_SPACE]:
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
    win.fill(black)
    pygame.draw.rect(win, white, (x, y, width, height))
    pygame.display.update()
pygame.quit()

