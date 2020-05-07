import pygame
import os

class image:

    global position
    _angle = 0

    def __init__(self, fileName, properties):
        self.fileName = fileName
        self.width = properties[0]
        self.height = properties[1]
        self.position = [0, 0]

    def _setupImage(self):
        image = pygame.image.load(os.path.join("project/assets/sprites", self.fileName))
        scaledImage = pygame.transform.scale(image, (self.width, self.height))
        if not self._angle is 0:
            rotatedImage = pygame.transform.rotate(scaledImage, self._angle)
            return rotatedImage
        else:
            return scaledImage

    def setAngle(self, angle):
        self._angle += angle

    def getAngle(self):
        return self._angle

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setScale2X(self):
        self.width *= 2
        self.height *= 2

    def setScale(self, scale):
        self.width *= scale
        self.height *= scale

    def draw(self, win):
        win.blit(self._setupImage(), (self.position[0], self.position[1]))
