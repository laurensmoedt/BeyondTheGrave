import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision

class PortalHell(actor):

    def __init__(self, win):
        self.win = win
        self.image = image("portals/Hell_Portal.png", [64, 128])
        super().__init__(self.image, 'portalHell')
        super().setPosition([447, -16])

        #collision
        self.collision = collision(self, 'square')
        self.collision.setCollision(True, 'stationary')

    def draw(self):
        super()._draw(self.win)
