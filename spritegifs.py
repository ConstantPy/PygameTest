import pygame
import gif_pygame
from core.camera import camera

gif_path = "content/gif"

loaded = {}

class SpriteAnimated:
    def __init__(self, gif, is_ui = False):
        from core.engine import engine
        global spritesanimated

        if gif in loaded:
            self.gif = loaded[gif]
        else:
            self.gif = gif_pygame.load(gif_path + "/" + gif)
            loaded[gif] = self.gif

        self.loaded_width, self.loaded_height = loaded.get(gif).get_width(), loaded.get(gif).get_height()
        self.gif_surfaces = self.gif.get_surfaces()
        self.gif_surfaces
        gif_rect = self.gif.blit_ready()
        self.anim_loaded = len(loaded)
        for i in self.gif_surfaces:
            pygame.draw.rect(gif_rect, "green", [0, 0, self.loaded_width, self.loaded_height], 2)

        if is_ui:
            engine.ui_drawables.append(self)
        else:
            engine.animateds.append(self)

        self.is_ui = is_ui

    def delete(self):
        from core.engine import engine
        engine.animateds.remove(self)

    def draw(self, screen):
        pos = (self.entity.x - camera.x, self.entity.y - camera.y) \
                if not self.is_ui else \
                (self.entity.x, self.entity.y)
        screen.blit(self.gif.blit_ready(), pos)