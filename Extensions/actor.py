import pygame
import os
from Extensions.image import image
from Extensions.animator import animator

class actor:

    global width, height

    def __init__(self, image, hasAnim = False):
        self.texture = image
        self.hasAnimation = hasAnim
        self.position = []
        self.dt = pygame.time.Clock().tick(60) / 1000
        if not hasAnim:
            self.width = self.texture.getWidth()
            self.height = self.texture.getHeight()
            if ('allSprites' in globals()) and ('animatedActor' in globals()):
                del globals()['allSprites']
                del globals()['animatedActor']
                del globals()['animDependency']
        else:
            self.allSprites, self.animatedActor = None, None
            self.animDependency = None
                        
    def setAngle(self, angle):
        self.texture.setAngle(angle)

    def getAngle(self):
        return self.texture.getAngle()

    def setPosition(self, position):
        if not self.hasAnimation:
            self.texture.position = position
        else: 
            self.position = position

    def getPosition(self):
        if not self.hasAnimation:
            return self.texture.position
        else:
            return self.position

    def setVelocity(self, velocityVector2):
        x, y = velocityVector2[0], velocityVector2[1]
        if self.hasAnimation:
            self.animatedActor.velocity.x = x
            self.animatedActor.velocity.y = y
        else:
            self.texture.position[0] += x
            self.texture.position[1] += y

    def setAnimation(self, dependency):
        self.animatedActor = animator((self.getPosition()[0], self.getPosition()[1]), [32, 32], self.texture)
        self.allSprites = pygame.sprite.Group(self.animatedActor)
        self.animDependency = dependency

    def _draw(self, win):
        if self.hasAnimation:
            self.allSprites.update(self.dt, self.animDependency)
            self.allSprites.draw(win)
        elif not self.hasAnimation:
            self.texture.draw(win)
        pygame.display.update()
