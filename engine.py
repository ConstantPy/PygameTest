import pygame
pygame.init()

engine = None

class Engine:
    def __init__(self, game_title):
        from core.camera import create_screen, update_screen
        global engine
        engine = self
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.active_objs = [] # Anything with an update() method which can be called 

        self.background_drawables = []
        self.drawables = [] # Anything to be drawn in the world
        self.ui_drawables = [] # Anything to be drawn over the world
        self.animateds = []
        
        self.screen = create_screen(game_title) # The rectangle in the window itself
        new_width = self.screen.get_width()
        new_height = self.screen.get_height()
        self.new_screen = update_screen(new_width, new_height)

        self.stages = {}
        self.current_stage = None

    def register(self, stage_name, func):
        self.stages[stage_name] = func

    def switch_to(self, stage_name):
        from core.area import area
        area = None
        self.reset()
        self.current_stage = stage_name
        func = self.stages[stage_name]
        print(f"Switching to {self.current_stage}")
        func()

    def run(self):
        from core.input import keys_down
        from core.camera import update_screen
        new_width = self.screen.get_width()
        new_height = self.screen.get_height()


        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    keys_down.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys_down.remove(event.key)
            
            self.new_screen = update_screen(new_width, new_height)

            # Update Code
            for a in self.active_objs:
                a.update()

            # Draw Code
            if self.screen is not None:
                self.screen.fill("black")
            del self.screen

            # Draw background items like the tiles
            for b in self.background_drawables:
                b.draw(self.screen) or b.draw(self.new_screen)

            # Draw the main objects
            for s in self.drawables:
                s.draw(self.screen) or s.draw(self.new_screen)

            # Draw the UI stuff
            for l in self.ui_drawables:
                l.draw(self.screen) or l.draw(self.new_screen)

            for k in self.animateds:
                k.draw(self.screen) or k.draw(self.new_screen)
                self.clock.tick(self.fps)

            pygame.display.flip()

            # Cap to 60 fps
            self.clock.tick(self.fps)

        pygame.quit()

    def reset(self):
        from components.physics import reset_physics
        reset_physics()
        self.active_objs.clear()
        self.drawables.clear()
        self.ui_drawables.clear()
        self.background_drawables.clear()
        self.animateds.clear()