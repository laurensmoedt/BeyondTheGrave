import pygame
from scenes.secMenu import secMenu
from Extensions.button import button
from Extensions.text import text
from Extensions.color import color
from Extensions.scenes import scenes

class mainMenu:

    def __init__(self, win):
        self.color = color()
        self.window = win
        middleX, middleY = (self.window.get_width() / 2), (self.window.get_height() / 2)
        self.scenes = scenes(secMenu(self.window), self.window)
        # Background color init
        self.backgroundColor = self.color.custom('#70A9A1')
        # Button inialization
        self.UIButton = button([(0, 0, 0), (255, 255, 255)], [150, 50])
        self.UIButton.text = 'Start'
        self.UIButton.position = [self.window.get_width() / 2 - (self.UIButton.width / 2), self.window.get_height() / 2 - (self.UIButton.height / 2)]
        # Text inialization
        self.UIText = text((150, 50, 30), 32, [100, 30])
        self.UIText.text = 'Name of game'
        self.UIText.position = [middleX - (self.UIText.width / 2), 100]

    def draw(self, clock, fps):
        self.window.fill(self.backgroundColor)
        self.UIButton.draw(self.window)
        if self.UIButton.getClick(): self.scenes.update(clock, fps)
        self.UIText.draw(self.window)
