import pygame
import os

class animator(pygame.sprite.Sprite):
    
    def __init__(self, positions, size, path):
        super(animator, self).__init__()
        size = (size[0], size[1])
        self.rect = pygame.Rect(positions, size)
        self.images = self._loadImages(path)
        self.imagesRight = self.images
        self.imagesLeft = [pygame.transform.flip(image, True, False) for image in self.images]
        self.index = 0
        self.image = self.images[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animTime = 0.1
        self.currentTime = 0
        self.frames = len(self.images)
        self.currentFrame = 0

    def _loadImages(self, path):
        images = []
        fixedPath = 'scenes/assets/animations'
        for files in os.listdir(fixedPath + path):
            try:
                image = pygame.image.load('scenes/assets/animations' + path + os.sep + files).convert()
                images.append(image)
            except pygame.error: continue
        return images

    def updateTimeDepended(self, dt):
        if self.velocity.x > 0: self.images = self.imagesRight
        else: self.images = self.imagesLeft
        self.currentTime += dt
        if self.currentTime >= self.animTime:
            self.currentTime = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def updateFrameDepended(self):
        if self.velocity.x > 0: self.images = self.imagesRight
        else: self.images = self.imagesLeft
        self.currentFrame += 1
        if self.currentFrame >= self.frames:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.move_ip(*self.velocity)

    def update(self, dt, dependency):
        if dependency is 'time':
            self.updateTimeDepended(dt)
        elif dependency is 'frame':
            self.updateFrameDependent()
        else:
            raise NameError('The dependency value is incorrect. Use time or frame.') 
