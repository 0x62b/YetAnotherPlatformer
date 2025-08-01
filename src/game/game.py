import pygame
from src.entities.player import Player
from src.game.camera import Camera
from src.constants import WIDTH, HEIGHT, WHITE

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
        """Load a specific level and initialize game objects"""
        self.current_level = level_number
        
        if level_number == 1:
            from levels.level1 import platforms as level1_platforms
            self.platforms = level1_platforms
        elif level_number == 2:
            from levels.level2 import platforms as level2_platforms
            self.platforms = level2_platforms
        
        # Create player with platforms reference
        self.player = Player(100, 300, self.platforms)
        
        # Recreate sprites group
        
        self.sprites = pygame.sprite.Group(self.player)
        for platform in self.platforms:
            self.sprites.add(platform)
    
    def handle_events(self):
        """Handle pygame events"""
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
        """Update game state"""
        self.sprites.update()
        self.camera.update(self.player)
    
    def render(self):
        """Render the game"""
        self.screen.fill(WHITE)
        
        for sprite in self.sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite.rect))
        
        pygame.display.update()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
        
        pygame.quit()
