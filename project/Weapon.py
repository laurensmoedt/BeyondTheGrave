import pygame
from Extensions.actor import actor
from Extensions.image import image
from project.Projectile import Projectile

class Weapon(actor):


    def __init__(self, win, name):
        self.win = win
        self.image = image("weapons/bow.png", [32, 32])
        super().__init__(self.image)

        self.pos = super().getPosition()
        self.targetRadius = 10

    # def fire(self, fromPos, toPos, bulletSpeed):
    #     self.pos = self.projectile.setPosition(fromPos)
    #
    #     self.targetPos = toPos
    #
    #     move = toPos - fromPos
    #     move_length = move.length()
    #
    #     if move:
    #         move.normalize_ip()
    #     move = move * bulletSpeed
    #
    #     fromPos += move
    #     super().setPosition(self.pos)

    def draw(self):
        super()._draw(self.win)
