import pygame

pygame.init()
click = pygame.mouse.get_pressed()

if click[0] == 1:
    print('Click!')