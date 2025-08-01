import pygame
from src.constants import WIDTH

class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def apply(self, rect):
        return pygame.Rect(rect.x - self.offset_x, rect.y - self.offset_y, rect.width, rect.height)

    def update(self, target):
        self.offset_x = target.rect.centerx - self.width // 2
        self.offset_y = target.rect.centery - self.height // 2
