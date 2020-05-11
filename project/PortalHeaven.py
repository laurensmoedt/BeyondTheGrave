import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision
from project.Player import Player

class PortalHeaven(actor):

    def __init__(self, win):
        self.win = win
        self.image = image("portals/Heaven_Portal.png", [64, 128])
        super().__init__(self.image)
        super().setPosition([289, -16])

        #collision
        self.collision = collision(self, 'square')
        self.collision.setCollision(True, 'stationary')

    def draw(self):
        super()._draw(self.win)
