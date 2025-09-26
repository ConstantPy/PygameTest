import pygame
from components.sprite import Sprite
from core.input import is_key_pressed
from core.camera import camera

from components.physics import Body, triggers
from components.entity import Entity
from components.label import Label
from core.area import area

movement_speed = 1
sprint_mod = 2

class Player:
    def __init__(self):
        self.loc_label = Entity(Label("Montserrat-Medium.ttf", 
                                         "X: 0 - Y: 0")).get(Label)
        self.area_label = Entity(Label("Montserrat-Medium.ttf", 
                                       area.name)).get(Label)

        self.loc_label.entity.y = camera.height - 50

        self.loc_label.entity.x = 10
        self.area_label.entity.x = 10

        from core.engine import engine
        engine.active_objs.append(self)

    def update(self):
        self.loc_label.set_text(f"X: {self.entity.x} - Y: {self.entity.y}")
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        if is_key_pressed(pygame.K_w):
            self.entity.y -= movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_w):
                self.entity.y -= sprint_mod
        if is_key_pressed(pygame.K_s):
            self.entity.y += movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_s):
                self.entity.y += sprint_mod
        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_ESCAPE):
            from core.engine import engine
            engine.switch_to("Menu")

        if is_key_pressed(pygame.K_a):
            self.entity.x -= movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_a):
                self.entity.x -= sprint_mod
        if is_key_pressed(pygame.K_d):
            self.entity.x += movement_speed
            if is_key_pressed(pygame.K_LSHIFT) and is_key_pressed(pygame.K_d):
                self.entity.x += sprint_mod
        if not body.is_position_valid():
            self.entity.x = previous_x
        camera.x = self.entity.x - int(camera.width/2) + int(sprite.image.get_width()/2)
        camera.y = self.entity.y - int(camera.height/2) + int(sprite.image.get_height()/2)

        # print(sprite.image.get_width(), sprite.image.get_height())
        
        for t in triggers:
            if body.is_colliding_with(t):
                t.on()
