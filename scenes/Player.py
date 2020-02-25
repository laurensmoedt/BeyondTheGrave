import pygame
from Extensions.actor import actor
from Extensions.image import image

class Player(actor):
    
    def __init__(self, win):
        self.win = win
        self.playerImage = image('maik.png', [32, 32])
        super().__init__(self.playerImage)
        super().setPosition([100, 100])

    def draw(self):
        super()._draw(self.win)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    super().setVelocity((4, 0))
                elif event.key == pygame.K_a:
                    super().setVelocity((-4, 0))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    super().setVelocity((0, 0))
                    break
