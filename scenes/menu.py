import pygame
from Extensions.color import color
from Extensions.scenes import scenes

class mainMenu:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background color init
        self.backgroundColor = self.color.custom('#70A9A1')

    def draw(self, clock, fps):
        self.window.fill(self.backgroundColor)
