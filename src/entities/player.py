import pygame
from ..utils import Utils
from src.constants import GRAVITY, PLAYER_SPEED, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms, portal, game):
        super().__init__()

        self.game = game
        self.level = Utils.get_level(self.game.current_level)

        self.platforms = platforms
        self.portal = portal
        self.sheet = pygame.transform.scale(pygame.image.load('assets/spritesheet.png').convert(), (64, 128))

        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.can_jump = True

    def respawn(self):
        self.vel_x = 0
        self.vel_y = 0
        self.rect.x = self.level.START_POS[0]
        self.rect.y = self.level.START_POS[1]
        self.on_ground = True
        self.jump_count = 0
        self.can_jump = True
        
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        for hit in hits:
            self.rect.bottom = hit.rect.top    

    def get_image(self, x, y):
        image = pygame.Surface([64, 128])
        image.blit(self.sheet, (0, 0), (x, y, 64, 128))
        image.set_colorkey((255, 255, 255))
        return image

    def update(self):
        self.vel_y += GRAVITY

        keys = pygame.key.get_pressed()
        
        self.vel_x = 0
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED

        if keys[pygame.K_UP]:
            if self.can_jump:
                if self.on_ground:
                    self.vel_y = -10
                    self.jump_count = 1
                    self.on_ground = False
                    self.can_jump = False
                elif self.jump_count == 1:
                    self.vel_y = -10
                    self.jump_count = 2
                    self.can_jump = False
        else:
            self.can_jump = True
        
        self.rect.x += self.vel_x
        
        # platform
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        for hit in hits:
            if self.vel_x > 0:
                self.rect.right = hit.rect.left
            elif self.vel_x < 0:
                self.rect.left = hit.rect.right
        
        # crusher
        hits = pygame.sprite.spritecollide(self, self.level.crushers, False)
        for hit in hits:
            self.can_jump = False
            if self.vel_x > 0:
                self.rect.right = hit.rect.left
            elif self.vel_x < 0:
                self.rect.left = hit.rect.right
            self.rect.x += hit.speed

            if pygame.sprite.spritecollide(self, self.platforms, False):
                self.respawn()
                return
        
        self.rect.y += self.vel_y
        self.on_ground = False

        # platform
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        for hit in hits:
            if self.vel_y > 0:
                self.rect.bottom = hit.rect.top
                self.vel_y = 0
                self.on_ground = True
                self.jump_count = 0
            elif self.vel_y < 0:
                self.rect.top = hit.rect.bottom
                self.vel_y = 0

        # crusher
        hits = pygame.sprite.spritecollide(self, self.level.crushers, False)
        for hit in hits:
            self.can_jump = False
            if self.vel_y > 0:
                self.rect.bottom = hit.rect.top
                self.vel_y = 0
                self.on_ground = True
                self.jump_count = 0
            elif self.vel_y < 0:
                self.rect.top = hit.rect.bottom
                self.vel_y = 0
                self.rect.x += hit.speed

            if pygame.sprite.spritecollide(self, self.platforms, False):
                self.respawn()
                return

        # portal
        hits = pygame.sprite.spritecollide(self, pygame.sprite.Group(self.portal), False)
        for hit in hits:
            if hit == self.portal:
                self.game.load_level(self.game.current_level + 1)

        # enemies
        hits = pygame.sprite.spritecollide(self, self.level.enemies, False)
        for hit in hits:
            if hit in self.level.spikes:
                self.respawn()
            elif hit in self.level.voiders:
                self.vel_x = 0
                self.vel_y = 100

        if self.rect.y > self.level.LEVEL_HEIGHT:
            self.respawn()