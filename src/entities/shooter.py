import pygame
from src.constants import BLACK

class Shooter(pygame.sprite.Sprite):
    # 把玩家立即射死了
    def __init__(self, x, y):
        super().__init__()

    def update(self):
        pass