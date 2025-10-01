import pygame
from src.entities.platform import Platform
from src.entities.spike import Spike
from src.entities.crusher import Crusher
from src.entities.portal import Portal

LEVEL_HEIGHT = 3000

PLATFORM1 = Platform(100, 850, 150, 30)
PLATFORM2 = Platform(350, 900, 120, 30)
PLATFORM3 = Platform(600, 820, 180, 30)
PLATFORM4 = Platform(850, 780, 100, 30)
PLATFORM5 = Platform(1100, 830, 160, 30)
PLATFORM6 = Platform(1400, 870, 140, 30)
PLATFORM7 = Platform(50, 550, 120, 30)
PLATFORM8 = Platform(300, 600, 100, 30)
PLATFORM9 = Platform(550, 620, 200, 30)
PLATFORM10 = Platform(800, 580, 150, 30)
PLATFORM11 = Platform(1100, 560, 180, 30)
PLATFORM12 = Platform(1400, 530, 160, 30)
PLATFORM13 = Platform(150, 280, 80, 30)
PLATFORM14 = Platform(400, 320, 120, 30)
PLATFORM15 = Platform(700, 250, 100, 30)
PLATFORM16 = Platform(950, 290, 140, 30)
PLATFORM17 = Platform(1250, 340, 160, 30)
PLATFORM18 = Platform(1500, 310, 150, 30)

PLATFORM19 = Platform(-200, 1150, 150, 30)
PLATFORM20 = Platform(50, 1200, 120, 30)
PLATFORM21 = Platform(300, 1120, 180, 30)
PLATFORM22 = Platform(550, 1080, 100, 30)
PLATFORM23 = Platform(800, 1130, 160, 30)
PLATFORM24 = Platform(1100, 1170, 140, 30)
PLATFORM25 = Platform(-150, 1450, 120, 30)
PLATFORM26 = Platform(100, 1500, 100, 30)
PLATFORM27 = Platform(350, 1520, 200, 30)
PLATFORM28 = Platform(600, 1480, 150, 30)
PLATFORM29 = Platform(900, 1460, 180, 30)
PLATFORM30 = Platform(1200, 1430, 160, 30)

PLATFORM31 = Platform(-300, 1780, 80, 30)
PLATFORM32 = Platform(-50, 1820, 120, 30)
PLATFORM33 = Platform(200, 1750, 100, 30)
PLATFORM34 = Platform(450, 1790, 140, 30)
PLATFORM35 = Platform(750, 1840, 160, 30)
PLATFORM36 = Platform(1000, 1810, 150, 30)
PLATFORM37 = Platform(-250, 2050, 150, 30)
PLATFORM38 = Platform(0, 2100, 120, 30)
PLATFORM39 = Platform(250, 2020, 180, 30)
PLATFORM40 = Platform(500, 1980, 100, 30)
PLATFORM41 = Platform(750, 2030, 160, 30)
PLATFORM42 = Platform(1050, 2070, 140, 30)

PLATFORM43 = Platform(-100, 2350, 120, 30)
PLATFORM44 = Platform(150, 2400, 100, 30)
PLATFORM45 = Platform(400, 2420, 200, 30)
PLATFORM46 = Platform(650, 2380, 150, 30)
PLATFORM47 = Platform(950, 2360, 180, 30)
PLATFORM48 = Platform(1250, 2330, 160, 30)
PLATFORM49 = Platform(200, 2680, 80, 30)
PLATFORM50 = Platform(450, 2720, 120, 30)
PLATFORM51 = Platform(750, 2650, 100, 30)
PLATFORM52 = Platform(1000, 2690, 140, 30)
PLATFORM53 = Platform(1300, 2740, 160, 30)
PLATFORM54 = Platform(1550, 2710, 150, 30)

PORTAL_X = 800
PORTAL_Y = 2500

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
    Spike(1150, 810, 20, 20),
    Spike(320, 580, 20, 20),
    Spike(820, 560, 20, 20),
    Spike(860, 560, 20, 20),
    Spike(420, 300, 20, 20),
    Spike(970, 270, 20, 20),
    Spike(1010, 270, 20, 20),
    Spike(70, 1180, 20, 20),
    Spike(350, 1100, 20, 20),
    Spike(850, 1110, 20, 20),
    Spike(130, 1480, 20, 20),
    Spike(400, 1500, 20, 20),
    Spike(650, 1460, 20, 20),
    Spike(-30, 1800, 20, 20),
    Spike(220, 1730, 20, 20),
    Spike(470, 1770, 20, 20),
    Spike(20, 2080, 20, 20),
    Spike(270, 2000, 20, 20),
    Spike(520, 1960, 20, 20),
    Spike(170, 2380, 20, 20),
    Spike(420, 2400, 20, 20),
    Spike(670, 2360, 20, 20),
    Spike(470, 2700, 20, 20),
    Spike(770, 2630, 20, 20),
    Spike(1020, 2670, 20, 20)
)

crushers = pygame.sprite.Group(
    Crusher(610, 790, 20, 30, 140, 2),
    Crusher(560, 590, 20, 30, 160, 3),
    Crusher(1110, 530, 20, 30, 140, 2),
    Crusher(1260, 310, 20, 30, 120, 4),
    Crusher(310, 1090, 20, 30, 140, 2),
    Crusher(910, 1430, 20, 30, 140, 3),
    Crusher(760, 1810, 20, 30, 120, 4),
    Crusher(50, 2070, 20, 30, 80, 2),
    Crusher(960, 2330, 20, 30, 140, 3),
    Crusher(1310, 2710, 20, 30, 120, 4)
)

voiders = pygame.sprite.Group(
    # none for floating level
)

enemies = pygame.sprite.Group(
    spikes,
    crushers
)