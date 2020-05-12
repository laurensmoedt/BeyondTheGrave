import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision
from project.Player import Player

class Enemy(actor):

    def __init__(self, win, speed, moveSmoothness, target):
        self.win = win
        self.enemyImage = image("characters/maik.png", [32, 32])
        super().__init__(self.enemyImage, 'enemy')
        super().setPosition([190, 290])

        startPos = super().getPosition()
        self.pos = pygame.Vector2(startPos)
        self.pos -= self.enemyImage.getWidth()/2, self.enemyImage.getHeight()

        self.speed = speed
        self.targetRadius = moveSmoothness

        self.target = target
        self.targetPos = self.target.getPosition()
        self.set_target(self.targetPos)

        self.collision = collision(self, 'square')
        self.collision.setCollision(True, 'moving')

    def set_target(self, pos):
        self.targetPos = pygame.Vector2(pos)
        self.targetPos -= self.enemyImage.getWidth()/2, self.enemyImage.getHeight()

    def movement(self):
        self.collision._setPositionMoving()

        self.targetPos = self.target.getPosition()

        move = self.targetPos - self.pos
        move_length = move.length()

        if move:
            move.normalize_ip()
        if move_length > self.targetRadius:
            move = move * self.speed
        else:
            move = move * (move_length / self.targetRadius * self.speed) # slows down Player if player is close to the target

        self.pos += move
        super().setPosition(self.pos)

    def draw(self):
        super()._draw(self.win)
        self.movement()
