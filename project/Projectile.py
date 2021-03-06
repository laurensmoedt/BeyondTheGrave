import pygame
import math
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision

class Projectile(pygame.sprite.Sprite):
    def __init__(self, win, pos, bulletspeed):
        super().__init__()
        self.name = 'projectile'
        self.pos = pos
        self.currentPos = pygame.Vector2(0,0)

        self.image = pygame.Surface([8, 3])
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=(self.pos))

        self.width = self.rect.width
        self.height = self.rect.height

        self.floating_point_x = self.pos.x
        self.floating_point_y = self.pos.y

        self.mousepos = pygame.mouse.get_pos()
        self.target = pygame.Vector2(self.mousepos)

        x_diff = self.target.x - self.rect.x
        y_diff = self.target.y - self.rect.y
        shootingAngle = math.atan2(y_diff, x_diff);

        velocity = bulletspeed
        self.change_x = math.cos(shootingAngle) * velocity
        self.change_y = math.sin(shootingAngle) * velocity

        # Rotate projectile with an angle in correct direction
        mouseX, mouseY = pygame.mouse.get_pos()
        rel_x, rel_y = mouseX - self.pos.x, mouseY - self.pos.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.image, int(angle))

        # Add collision to projectile
        self.collision = collision(self, 'square')
        self.collision.setCollision(True, 'moving')

    def getPosition(self):
        return self.currentPos

    def update(self):
        # The floating point x and y hold our more accurate location.
        self.floating_point_x += self.change_x
        self.floating_point_y += self.change_y

        # The rect.x and rect.y are converted to integers.
        self.rect.x = int(self.floating_point_x)
        self.rect.y = int(self.floating_point_y)

        self.currentPos = pygame.Vector2(self.rect.left, self.rect.top)

        self.collision._setPositionMoving()

        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 512:
            self.kill()

    def draw(self):
         super()._draw(self.win)
         self.update()
