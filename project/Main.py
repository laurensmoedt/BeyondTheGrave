import pygame
from Extensions.color import color
from Extensions.scenes import scenes
from project.Player import Player
from project.Wall import Wall

class Main:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background color init
        self.backgroundColor = self.color.custom('#70A9A1')
        self.player = Player(self.window, 10, 30) # Player with value 'speed' and 'moveSmoothness'
        self.Wall = Wall(self.window)

    def draw(self, clock, fps):
        self.window.fill(self.backgroundColor)
        self.player.draw()
        self.Wall.draw()
        print(self.player.collision.checkState())

        pygame.display.update()
