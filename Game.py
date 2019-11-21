
import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Untitled Game 1')

white = (255, 255, 255)
black = (0, 0, 0)

x = 50
y = 50
width = 40
height = 60
speed = 5

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
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
    win.fill(black)
    pygame.draw.rect(win, white, (x, y, width, height))
    pygame.display.update()
pygame.quit()

