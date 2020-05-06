import pygame
from Extensions.color import color
from Extensions.scenes import scenes
from Extensions.image import image
from project.Player import Player
from project.Enemy import Enemy
from project.PortalHeaven import PortalHeaven
from project.PortalHell import PortalHell
from project.Weapon import Weapon

class Main:

    def __init__(self, win):
        self.color = color()
        self.window = win
        # Background init
        self.backgroundImage = image("backgrounds/mainMap.png", [800, 512])
        self.player = Player(self.window, 10, 50) # Player with value 'speed' and 'moveSmoothness'
        self.portalHeaven = PortalHeaven(self.window)
        self.portalHell = PortalHell(self.window)

        self.enemy = Enemy(self.window, 2, 5, self.player)

        self.Weapon = Weapon(self.window, "bow")

    def draw(self, clock, fps):
        self.backgroundImage.draw(self.window)
        self.portalHeaven.draw()
        self.portalHell.draw()
        self.enemy.draw()
        self.player.draw()
        self.Weapon.draw()
        self.Weapon.setPosition(self.player.getPosition())

        if self.player.collision.checkState() == True:
            print(self.player.collision.checkState())

        pygame.display.update()
