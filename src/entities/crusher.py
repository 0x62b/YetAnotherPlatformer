import pygame
from src.constants import BLACK

class Crusher(pygame.sprite.Sprite):
    # 把玩家立即压扁了
    def __init__(self, x, y, size_x, size_y, range, speed):
        super().__init__()
        self.image = pygame.Surface([size_x, size_y])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.range = range
        self.speed = speed

        self.pos = 0

    def update(self):
        if abs(self.pos) >= self.range:
            self.speed = -self.speed
        self.pos += self.speed
        self.rect.x += self.speed