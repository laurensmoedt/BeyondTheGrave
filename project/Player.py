import pygame
from Extensions.actor import actor
from Extensions.image import image
from Extensions.collision import collision
from project.Weapon import Weapon
from project.Projectile import Projectile

class Player(actor):

    def __init__(self, win, speed, moveSmoothness):
        self.win = win
        self.playerImage = image("characters/maik.png", [32, 32])
        super().__init__(self.playerImage)
        super().setPosition([390, 290])
        self.rect = self.playerImage.get_rect();

        startPos = super().getPosition()
        self.pos = pygame.Vector2(startPos)
        self.pos -= self.playerImage.getWidth()/2, self.playerImage.getHeight()
        self.set_target(startPos)
        self.speed = speed
        self.targetRadius = moveSmoothness

        self.collision = collision(self, 'square')
        self.collision.setCollision(True)

        #self.weapon = Weapon(self.win, "bow")
        #sprite lists
        # self.all_sprites = pygame.sprite.Group()
        # self.projectiles = pygame.sprite.Group()

    def shoot(self):
        projectile = Projectile(self, 1,1)
        # self.all_sprites.add(projectile)
        # self.projectiles.add(projectile)

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)
        self.target -= self.playerImage.getWidth()/2, self.playerImage.getHeight()

    def update(self):
        for event in pygame.event.get():
            #key_events for weapon fired
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot()
            #key_events for player movement
            if pygame.mouse.get_pressed()[2]:
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
        super().setPosition(self.pos)

    def draw(self):
        super()._draw(self.win)
        self.update()
