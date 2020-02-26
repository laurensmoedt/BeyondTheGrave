import pygame
from Extensions.color import color
from Extensions.scenes import scenes
from scenes.Player import Player

class mainMenu:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background color init
        self.backgroundColor = self.color.custom('#70A9A1')
        self.player = Player(self.window)

    def draw(self, clock, fps):
        self.window.fill(self.backgroundColor)
        self.player.draw()
