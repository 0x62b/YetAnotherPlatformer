import pygame
from src.constants import WHITE, BLACK

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([80, 150])
        self.image.fill((100, 200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
