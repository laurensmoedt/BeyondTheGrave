import pygame
from Extensions.actor import actor
from Extensions.image import image

class Player(actor):

    def __init__(self, win, speed, moveSmoothness):
        self.win = win
        self.playerImage = image('maik.png', [32, 32])
        super().__init__(self.playerImage)
        super().setPosition([100, 100])

        self.pos = pygame.Vector2(0, 0)
        self.set_target((0, 0))
        self.speed = speed
        self.targetRadius = moveSmoothness

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.set_target(pygame.mouse.get_pos())

        move = self.target - self.pos
        move_length = move.length()

        if move:
            move.normalize_ip()
        if move_length < self.speed: # player stops moving if target is reached
            self.pos = self.target
        elif move_length > self.targetRadius:
            move = move * self.speed
        else:
            move = move * (move_length / self.targetRadius * self.speed) # slows down Player if player is close tho the target

        self.pos += move
        super().setPosition(self.pos)

    def draw(self):
        super()._draw(self.win)
        self.movement()
