import pygame
from src.entities.platform import Platform
from src.entities.spike import Spike
from src.entities.crusher import Crusher
from src.entities.portal import Portal

LEVEL_HEIGHT = 3000
LEVEL_WIDTH = 1700

PLATFORM1 = Platform(100, 800, 140, 30)
PLATFORM2 = Platform(300, 900, 118, 30)
PLATFORM3 = Platform(600, 800, 176, 30)
PLATFORM4 = Platform(900, 700, 102, 30)
PLATFORM5 = Platform(1100, 800, 158, 30)
PLATFORM6 = Platform(1400, 800, 142, 30)
PLATFORM7 = Platform(0, 500, 122, 30)
PLATFORM8 = Platform(300, 600, 104, 30)
PLATFORM9 = Platform(500, 600, 194, 30)
PLATFORM10 = Platform(800, 600, 148, 30)
PLATFORM11 = Platform(1100, 500, 182, 30)
PLATFORM12 = Platform(1400, 500, 156, 30)
PLATFORM13 = Platform(200, 200, 82, 30)
PLATFORM14 = Platform(400, 300, 120, 30)
PLATFORM15 = Platform(700, 200, 100, 30)
PLATFORM16 = Platform(1000, 200, 140, 30)
PLATFORM17 = Platform(1200, 300, 160, 30)
PLATFORM18 = Platform(1500, 300, 150, 30)
PLATFORM19 = Platform(0, 1100, 150, 30)
PLATFORM20 = Platform(100, 1200, 122, 30)
PLATFORM21 = Platform(300, 1100, 180, 30)
PLATFORM22 = Platform(600, 1000, 100, 30)
PLATFORM23 = Platform(800, 1100, 160, 30)
PLATFORM24 = Platform(1100, 1100, 140, 30)
PLATFORM25 = Platform(0, 1400, 124, 30)
PLATFORM26 = Platform(100, 1500, 102, 30)
PLATFORM27 = Platform(400, 1500, 198, 30)
PLATFORM28 = Platform(600, 1500, 152, 30)
PLATFORM29 = Platform(900, 1500, 178, 30)
PLATFORM30 = Platform(1200, 1400, 164, 30)
PLATFORM31 = Platform(-100, 1700, 88, 30)
PLATFORM32 = Platform(-100, 1800, 126, 30)
PLATFORM33 = Platform(200, 1800, 98, 30)
PLATFORM34 = Platform(500, 1800, 136, 30)
PLATFORM35 = Platform(700, 1900, 162, 30)
PLATFORM36 = Platform(1000, 1800, 148, 30)
PLATFORM37 = Platform(-200, 2000, 154, 30)
PLATFORM38 = Platform(0, 2100, 118, 30)

platforms = pygame.sprite.Group(
    PLATFORM1, PLATFORM2, PLATFORM3, PLATFORM4, PLATFORM5, PLATFORM6,
    PLATFORM7, PLATFORM8, PLATFORM9, PLATFORM10, PLATFORM11, PLATFORM12,
    PLATFORM13, PLATFORM14, PLATFORM15, PLATFORM16, PLATFORM17, PLATFORM18,
    PLATFORM19, PLATFORM20, PLATFORM21, PLATFORM22, PLATFORM23, PLATFORM24,
    PLATFORM25, PLATFORM26, PLATFORM27, PLATFORM28, PLATFORM29, PLATFORM30,
    PLATFORM31, PLATFORM32, PLATFORM33, PLATFORM34, PLATFORM35, PLATFORM36,
    PLATFORM37, PLATFORM38
)

spikes = pygame.sprite.Group(
    Spike(1200, 800, 20, 20),
    Spike(300, 600, 20, 20),
    Spike(800, 600, 20, 20),
    Spike(900, 500, 20, 20),
    Spike(400, 300, 20, 20),
    Spike(1000, 300, 20, 20),
    Spike(1000, 200, 20, 20),
    Spike(100, 1200, 20, 20),
    Spike(300, 1100, 20, 20),
    Spike(800, 1100, 20, 20),
    Spike(100, 1500, 20, 20),
    Spike(400, 1500, 20, 20),
    Spike(700, 1500, 20, 20),
    Spike(0, 800, 20, 20),
    Spike(200, 800, 20, 20),
    Spike(500, 900, 20, 20),
    Spike(100, 1100, 20, 20),
    Spike(300, 400, 20, 20),
    Spike(500, 200, 20, 20),
    Spike(200, 400, 20, 20),
    Spike(400, 900, 20, 20),
    Spike(700, 600, 20, 20)
)

crushers = pygame.sprite.Group(
    Crusher(600, 780, 20, 30, 140, 2),
    Crusher(550, 600, 20, 30, 160, 3),
    Crusher(1100, 500, 20, 30, 140, 2),
    Crusher(1300, 300, 20, 30, 120, 4),
    Crusher(300, 1100, 20, 30, 140, 2),
    Crusher(900, 1400, 20, 30, 140, 3),
    Crusher(800, 1800, 20, 30, 120, 4),
    Crusher(100, 2100, 20, 30, 80, 2)
)

voiders = pygame.sprite.Group(
    # none for floating level
)

enemies = pygame.sprite.Group(
    spikes,
    crushers
)

PORTAL_X = 1800
PORTAL_Y = 0

START_POS = (420, 712)