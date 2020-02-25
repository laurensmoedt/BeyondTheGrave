import pygame

class scenes:

    def __init__(self, scene, win):
        self.scene = scene
        self.win = win

    def _setupScene(self, clock, fps):
        running = True
        while running:
            self.win.fill((0, 0, 0))
            self.scene.draw(clock, fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            clock.tick(fps)
            pygame.display.update()
            
    def update(self, clock, fps):
        self._setupScene(clock, fps)
