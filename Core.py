import pygame
from Extensions.scenes import scenes
from project.Main import Main

class Core:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.Main = Main(self.win)
        self.scene = scenes(self.Main, self.win)
        pygame.init()

    def run(self, title, fps):
        run = True
        pygame.display.set_caption(title)
        clock = pygame.time.Clock()
        while run:
            clock.tick(fps)
            self.draw(clock, fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()

    def draw(self, clock, fps):
        # Set draw function from starting scene
        self.scene.update(clock, fps)
        pygame.display.update()

Scene = Core(800, 512)
Scene.run('Beyond-The-Grave', 60)
