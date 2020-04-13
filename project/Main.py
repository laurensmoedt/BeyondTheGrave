import pygame
from Extensions.color import color
from Extensions.scenes import scenes
from Extensions.image import image
from project.Player import Player
from project.Enemy import Enemy
from project.PortalHeaven import PortalHeaven
from project.PortalHell import PortalHell

class Main:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background init
        self.backgroundImage = image("backgrounds/mainMap.png", [800, 512])
        self.player = Player(self.window, 10, 50) # Player with value 'speed' and 'moveSmoothness'
        self.portalHeaven = PortalHeaven(self.window)
        self.portalHell = PortalHell(self.window)

        self.enemy = Enemy(self.window, 2, 20, self.player)

    def draw(self, clock, fps):
        self.backgroundImage.draw(self.window)
        self.portalHeaven.draw()
        self.portalHell.draw()
        self.player.draw()
        self.enemy.draw()

        if self.player.collision.checkState() == True:
            print(self.player.collision.checkState())

        pygame.display.update()
