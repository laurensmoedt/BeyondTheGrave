import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision

class Player(actor):

    def __init__(self, win, speed, moveSmoothness):
        self.win = win
        self.playerImage = image("characters/maik.png", [32, 32])
        super().__init__(self.playerImage)
        super().setPosition([390, 290])

        startPos = super().getPosition()
        self.pos = pygame.Vector2(startPos)
        self.pos -= self.playerImage.getWidth()/2, self.playerImage.getHeight()
        self.set_target(startPos)
        self.speed = speed
        self.targetRadius = moveSmoothness

        self.collision = collision(self, 'square')
        self.collision.setCollision(True)

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)
        self.target -= self.playerImage.getWidth()/2, self.playerImage.getHeight()

    def movement(self):
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                self.set_target(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEMOTION:
                    self.set_target(pygame.mouse.get_pos())

        move = self.target - self.pos
        move_length = move.length()

        if move:
            move.normalize_ip()
        if move_length > self.targetRadius:
            move = move * self.speed
        else:
            move = move * (move_length / self.targetRadius * self.speed) # slows down Player if player is close to the target

        self.pos += move
        newPos = super().setPosition(self.pos)

    def draw(self):
        super()._draw(self.win)
        self.movement()
        self.collision.checkState()
