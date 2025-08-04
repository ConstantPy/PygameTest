import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera
from entity import active_objs

class Player:
    def __init__(self):
        active_objs.append(self)

    def update(self):
        sprite = self.entity.get(Sprite)

        movement_speed = 1
        sprint_mod = 1.5

        if is_key_pressed(pygame.K_p):
            print(self.entity.x,self.entity.y)
        if is_key_pressed(pygame.K_w):
            self.entity.y -= movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_w):
                self.entity.y -= sprint_mod
        if is_key_pressed(pygame.K_a):
            self.entity.x -= movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_a):
                self.entity.x -= sprint_mod
        if is_key_pressed(pygame.K_s):
            self.entity.y += movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_s):
                self.entity.y += sprint_mod
        if is_key_pressed(pygame.K_d):
            self.entity.x += movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_d):
                self.entity.x += sprint_mod

        camera.x = self.entity.x - camera.width/2 + sprite.image.get_width()/2
        camera.y = self.entity.y - camera.height/2 + sprite.image.get_height()/2

