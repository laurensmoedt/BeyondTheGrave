import pygame
from Extensions.actor import actor
from Extensions.image import image

class Projectile(actor):


    def __init__(self, win, x, y):
        self.win = win
        self.image = image("weapons/arrow.png", [16, 4])
        super().__init__(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

    def draw(self):
        super()._draw(self.win)
