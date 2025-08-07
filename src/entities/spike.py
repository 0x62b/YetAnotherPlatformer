import pygame

BLACK = (0, 0, 0)

class Spike(pygame.sprite.Sprite):
    # 把玩家立即刺死了
    def __init__(self, x, y, size_x, size_y):
        super().__init__()
        self.image = pygame.Surface([size_x, size_y], pygame.SRCALPHA)
        
        points = [
            (size_x // 2, 0),
            (0, size_y),
            (size_x, size_y)
        ]
        pygame.draw.polygon(self.image, BLACK, points)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y