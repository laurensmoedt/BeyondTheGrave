import pygame
from Extensions.color import color
from Extensions.scenes import scenes
from Extensions.image import image
from project.Player import Player
from project.Enemy import Enemy
from project.PortalHeaven import PortalHeaven
from project.PortalHell import PortalHell
from project.Weapon import Weapon
from project.Projectile import Projectile

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

        self.weapon = Weapon(self.window, "bow")

        #projectile sprite list
        self.projectiles = pygame.sprite.Group()

    def shoot(self):
        self.projectile = Projectile(self.window, self.player.pos, 15)
        self.projectile.position = self.player.pos
        self.projectiles.add(self.projectile)

    def draw(self, clock, fps):
        self.backgroundImage.draw(self.window)
        self.portalHeaven.draw()
        self.portalHell.draw()
        self.enemy.draw()
        self.player.draw()
        self.weapon.draw()
        self.weapon.setPosition(self.player.getPosition())

        # player collision with anything that has collision
        if self.enemy.collision.checkState() == True:
            print(self.enemy.collision.checkState())

        # projectiles
        if self.player.shot == True:
            self.shoot()
        self.projectiles.draw(self.window)
        self.projectiles.update()

        self.player.collision.updateMovingObjects()


        pygame.display.update()
