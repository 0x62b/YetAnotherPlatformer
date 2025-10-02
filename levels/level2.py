import pygame
from src.entities.platform import Platform
from src.entities.spike import Spike
from src.entities.crusher import Crusher
from src.entities.portal import Portal

LEVEL_HEIGHT = 3000

PLATFORM1 = Platform(100, 800, 130, 30)
PLATFORM2 = Platform(400, 900, 140, 30)
PLATFORM3 = Platform(600, 800, 170, 30)
PLATFORM4 = Platform(800, 800, 110, 30)
PLATFORM5 = Platform(1100, 900, 170, 30)
PLATFORM6 = Platform(1300, 900, 130, 30)
PLATFORM7 = Platform(0, 500, 100, 30)
PLATFORM8 = Platform(300, 600, 90, 30)
PLATFORM9 = Platform(500, 600, 190, 30)
PLATFORM10 = Platform(800, 500, 160, 30)
PLATFORM11 = Platform(1100, 600, 170, 30)
PLATFORM12 = Platform(1400, 500, 150, 30)
PLATFORM13 = Platform(200, 300, 70, 30)
PLATFORM14 = Platform(400, 300, 110, 30)
PLATFORM15 = Platform(700, 200, 90, 30)
PLATFORM16 = Platform(1000, 300, 150, 30)
PLATFORM17 = Platform(1200, 400, 170, 30)
PLATFORM18 = Platform(1500, 300, 140, 30)

PLATFORM19 = Platform(-100, 1200, 160, 30)
PLATFORM20 = Platform(80, 1200, 110, 30)
PLATFORM21 = Platform(300, 1100, 170, 30)
PLATFORM22 = Platform(600, 1100, 90, 30)
PLATFORM23 = Platform(800, 1200, 150, 30)
PLATFORM24 = Platform(1100, 1200, 140, 30)
PLATFORM25 = Platform(-200, 1400, 130, 30)
PLATFORM26 = Platform(100, 1500, 90, 30)
PLATFORM27 = Platform(300, 1500, 190, 30)
PLATFORM28 = Platform(600, 1500, 160, 30)
PLATFORM29 = Platform(900, 1400, 170, 30)
PLATFORM30 = Platform(1200, 1500, 150, 30)

PLATFORM31 = Platform(-300, 1800, 70, 30)
PLATFORM32 = Platform(0, 1800, 130, 30)
PLATFORM33 = Platform(200, 1700, 90, 30)
PLATFORM34 = Platform(500, 1800, 150, 30)
PLATFORM35 = Platform(700, 1800, 150, 30)
PLATFORM36 = Platform(1000, 1900, 140, 30)
PLATFORM37 = Platform(-200, 2000, 160, 30)
PLATFORM38 = Platform(0, 2100, 120, 30)
PLATFORM39 = Platform(300, 2000, 170, 30)
PLATFORM40 = Platform(500, 2000, 90, 30)
PLATFORM41 = Platform(800, 2000, 150, 30)
PLATFORM42 = Platform(1000, 2000, 130, 30)

PLATFORM43 = Platform(-100, 2400, 130, 30)
PLATFORM44 = Platform(200, 2400, 90, 30)
PLATFORM45 = Platform(400, 2400, 180, 30)
PLATFORM46 = Platform(700, 2400, 140, 30)
PLATFORM47 = Platform(900, 2300, 170, 30)
PLATFORM48 = Platform(1300, 2300, 160, 30)
PLATFORM49 = Platform(200, 2700, 70, 30)
PLATFORM50 = Platform(400, 2700, 130, 30)
PLATFORM51 = Platform(800, 2600, 100, 30)
PLATFORM52 = Platform(1000, 2700, 150, 30)
PLATFORM53 = Platform(1200, 2700, 170, 30)
PLATFORM54 = Platform(1500, 2800, 140, 30)

PORTAL_X = 1000
PORTAL_Y = 2600

START_POS = (400, 700)

platforms = pygame.sprite.Group(
    PLATFORM1, PLATFORM2, PLATFORM3, PLATFORM4, PLATFORM5, PLATFORM6,
    PLATFORM7, PLATFORM8, PLATFORM9, PLATFORM10, PLATFORM11, PLATFORM12,
    PLATFORM13, PLATFORM14, PLATFORM15, PLATFORM16, PLATFORM17, PLATFORM18,
    PLATFORM19, PLATFORM20, PLATFORM21, PLATFORM22, PLATFORM23, PLATFORM24,
    PLATFORM25, PLATFORM26, PLATFORM27, PLATFORM28, PLATFORM29, PLATFORM30,
    PLATFORM31, PLATFORM32, PLATFORM33, PLATFORM34, PLATFORM35, PLATFORM36,
    PLATFORM37, PLATFORM38, PLATFORM39, PLATFORM40, PLATFORM41, PLATFORM42,
    PLATFORM43, PLATFORM44, PLATFORM45, PLATFORM46, PLATFORM47, PLATFORM48,
    PLATFORM49, PLATFORM50, PLATFORM51, PLATFORM52, PLATFORM53, PLATFORM54
)

spikes = pygame.sprite.Group(
    Spike(1200, 380, 20, 20),
    Spike(300, 580, 20, 20),
    Spike(800, 480, 20, 20),
    Spike(800, 480, 20, 20),
    Spike(500, 580, 20, 20),
    Spike(1000, 280, 20, 20),
    Spike(1000, 280, 20, 20),
    Spike(0, 1780, 20, 20),
    Spike(400, 1080, 20, 20),
    Spike(800, 1180, 20, 20),
    Spike(200, 2680, 20, 20),
    Spike(400, 1480, 20, 20),
    Spike(600, 1480, 20, 20),
    Spike(0, 1780, 20, 20),
    Spike(200, 1680, 20, 20),
    Spike(400, 1980, 20, 20),
    Spike(100, 1780, 20, 20),
    Spike(300, 1980, 20, 20),
    Spike(500, 1980, 20, 20),
    Spike(100, 1780, 20, 20),
    Spike(400, 2380, 20, 20),
    Spike(700, 2380, 20, 20),
    Spike(500, 2680, 20, 20),
    Spike(700, 2380, 20, 20),
    Spike(1000, 2680, 20, 20)
)

crushers = pygame.sprite.Group(
    Crusher(633, 772, 22, 28, 152, 2),
    Crusher(519, 568, 18, 32, 144, 3),
    Crusher(1092, 273, 22, 27, 166, 2),
    Crusher(1234, 371, 18, 29, 104, 5),
    Crusher(286, 1068, 20, 32, 130, 2),
    Crusher(943, 1171, 22, 29, 152, 3),
    Crusher(788, 1774, 18, 26, 136, 4),
    Crusher(74, 2070, 20, 30, 88, 2),
    Crusher(927, 2272, 22, 28, 118, 3),
    Crusher(1352, 2666, 18, 34, 128, 4)
)

voiders = pygame.sprite.Group(
    
)

enemies = pygame.sprite.Group(
    spikes,
    crushers
)