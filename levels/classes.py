import pygame

GRAVITY = 0.3
PLAYER_SPEED = 5
WIDTH = 800
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms):
        super().__init__()

        self.platforms = platforms
        self.sheet = pygame.transform.scale(pygame.image.load('stickfigure.png').convert(), (64, 128))

        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def get_image(self, x, y):
        image = pygame.Surface([64, 128])
        image.blit(self.sheet, (0, 0), (x, y, 64, 128))
        image.set_colorkey((255, 255, 255))
        return image

    def update(self):
        self.vel_y += GRAVITY

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        elif keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        else:
            self.vel_x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = -10

        if self.rect.top > HEIGHT:
            self.vel_x = 0
            self.vel_y = 0
            self.rect.x = 100
            self.rect.y = 300

        hits = pygame.sprite.spritecollide(self, self.platforms, False)

        if hits:
            for hit in hits:
                overlap_left = hit.rect.right - self.rect.left
                overlap_right = self.rect.right - hit.rect.left
                overlap_top = hit.rect.bottom - self.rect.top
                overlap_bottom = self.rect.bottom - hit.rect.top
                
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                
                if min_overlap == overlap_bottom and self.vel_y > 0:
                    self.vel_y = 0
                    self.on_ground = True
                    self.rect.bottom = hit.rect.top
                elif min_overlap == overlap_top and self.vel_y < 0:
                    self.vel_y = 0
                    self.rect.top = hit.rect.bottom
                elif min_overlap == overlap_right and self.vel_x > 0:
                    self.vel_x = 0
                    self.rect.right = hit.rect.left
                elif min_overlap == overlap_left and self.vel_x < 0:
                    self.vel_x = 0
                    self.rect.left = hit.rect.right
        else:
            self.on_ground = False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def apply(self, rect):
        return pygame.Rect(rect.x - self.offset_x, rect.y - self.offset_y, rect.width, rect.height)

    def update(self, target):
        self.offset_x = max(0, min(target.rect.centerx - self.width // 2, WIDTH * 2 - self.width))
        self.offset_y = target.rect.centery - self.height // 2
