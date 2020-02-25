import pygame
from Extensions.color import color
from scenes.Player import Player
from Extensions.image import image
from Extensions.actor import actor

class secMenu:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background color init
        self.backgroundColor = self.color.red
        self.player = Player(self.window)

    def draw(self, clock, fps):
        self.window.fill(self.backgroundColor)
        self.player.draw()
