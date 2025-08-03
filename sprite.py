import pygame
from camera import camera

sprites = []
loaded = {}

class Sprite:
    def __init__(self, image):
        # If: Uses images in memory
        # Else: Loads new images not in memory
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))