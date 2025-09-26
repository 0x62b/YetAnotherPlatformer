import pygame
from src.entities.player import Player
from src.entities.portal import Portal
from src.game.camera import Camera
from src.constants import WIDTH, HEIGHT, WHITE
from src.utils import Utils

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('stick figure thingy')
        self.clock = pygame.time.Clock()
        
        self.current_level = 1
        self.player = None
        self.camera = Camera(WIDTH, HEIGHT)
        self.sprites = pygame.sprite.Group()
        self.platforms = None
        
        self.load_level(1)
        
    def load_level(self, level_number):
        if (self.player):
            self.player.kill()
        self.current_level = level_number
        
        level = Utils.get_level(level_number)

        self.platforms = level.platforms
        self.enemies = level.enemies
        
        self.portal = Portal(level.PORTAL_X, level.PORTAL_Y)
        self.player = Player(level.START_POS[0], level.START_POS[1], self.platforms, self.portal, self)
        
        self.player.vel_x = 0
        self.player.vel_y = 0
        
        self.sprites = pygame.sprite.Group(self.player, self.portal)
        for platform in self.platforms:
            self.sprites.add(platform)
        for enemy in self.enemies:
            self.sprites.add(enemy)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.load_level(1)
                elif event.key == pygame.K_2:
                    self.load_level(2)
                elif event.key == pygame.K_3:
                    self.load_level(3)
                elif event.key == pygame.K_4:
                    self.load_level(4)
        return True
    
    def update(self):
        self.sprites.update()
        self.camera.update(self.player)
    
    def render(self):
        self.screen.fill(WHITE)
        
        for sprite in self.sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite.rect))
        
        pygame.display.update()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60) # 60 fps
        
        pygame.quit()
