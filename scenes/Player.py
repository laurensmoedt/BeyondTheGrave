import pygame
from Extensions.actor import actor
from Extensions.image import image

class Player(actor):

    def __init__(self, win):
        self.win = win
        self.playerImage = image('maik.png', [32, 32])
        super().__init__(self.playerImage)
        super().setPosition([100, 100])

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                super().setPosition(pygame.mouse.get_pos())

    def draw(self):
        super()._draw(self.win)
        self.movement()
