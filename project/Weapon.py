import pygame
from Extensions.actor import actor
from Extensions.image import image
from project.Projectile import Projectile

class Weapon(actor):


    def __init__(self, win, name):
        self.win = win
        self.image = image("weapons/bow.png", [16, 16])
        super().__init__(self.image)



    def draw(self):
        super()._draw(self.win)
