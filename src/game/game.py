import pygame
from src.entities.player import Player
from src.game.camera import Camera
from src.constants import WIDTH, HEIGHT, WHITE
import utils

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
        self.current_level = level_number
        self.level = utils.Utils.get_level(self.current_level)
        self.platforms = self.level.platforms
        
        self.player = Player(100, 300, self.platforms)

        self.sprites = pygame.sprite.Group(self.player)
                
        for enemy in self.level.enemies:
            self.sprites.add(enemy)

        for platform in self.platforms:
            self.sprites.add(platform)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.load_level(1)
                elif event.key == pygame.K_2:
                    self.load_level(2)
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
        
        pygame.quit()
