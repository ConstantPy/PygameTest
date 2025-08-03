import pygame

camera = pygame.Rect(0, 0, 0, 0)

def create_screen(width, height, title):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    pygame_icon = pygame.image.load('images/DJIcon.png')
    pygame.display.set_icon(pygame_icon)

    camera.width = width
    camera.height = height

    return screen