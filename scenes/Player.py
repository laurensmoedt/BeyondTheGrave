import pygame
from Extensions.actor import actor
from Extensions.image import image

class Player(actor):

    def __init__(self, win):
        self.win = win

    def draw(self):
        super()._draw(self.win)
