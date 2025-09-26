import pygame

camera = pygame.Rect(0, 0, 0, 0)

def create_screen(title):
    width = 1280
    height = 720

    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    pygame_icon = pygame.image.load('content/images/DJIcon.png')
    pygame.display.set_icon(pygame_icon)

    camera.width = width
    camera.height = height
    return screen
