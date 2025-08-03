import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera
from entity import active_objs

class Player:
    def __init__(self):
        active_objs.append(self)
        self.player_sprite_width = 0  # Initialize width
        self.player_sprite_height = 0  # Initialize height
        
    def sprite_dimensions(self):
        # trying to figure out how to pass the sprite_dimensions, I think the last two lines need to be returned as a tuple and the (player_sprite =) moved to the __init__ function?
        player_sprite = self.entity.get(Sprite).image
        self.player_sprite_width = player_sprite.get_width()
        self.player_sprite_height = player_sprite.get_height()

    def update(self):
        ### old code ignore for now
        # sprite = self.entity.get(Sprite)
        
        self.sprite_dimensions()

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

        # the old code at the start of this function had me referencing something akin to sprite.entity.get_width()? This looks a little cleaner
        camera.x = self.entity.x - camera.width/2 + self.player_sprite_width/2
        camera.y = self.entity.y - camera.height/2 + self.player_sprite_height/2
