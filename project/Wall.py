import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision

class Wall(actor):

    def __init__(self, win):
        self.win = win
        self.image = image("Wall.png", [256, 256])
        super().__init__(self.image)
        super().setPosition([400, 250])

        #collision
        self.collision = collision(self, 'square')
        self.collision.setCollision(True)

    def draw(self):
        super()._draw(self.win)
        self.collision.checkState()
