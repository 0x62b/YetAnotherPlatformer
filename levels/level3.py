import pygame
from src.entities.platform import Platform
from src.entities.voider import Voider
from src.entities.crusher import Crusher
from src.entities.spike import Spike

LEVEL_HEIGHT = 2200

LEFT_WALL = Platform(0, 0, 50, LEVEL_HEIGHT)
RIGHT_WALL = Platform(2950, 0, 50, LEVEL_HEIGHT)
TOP_WALL = Platform(0, 0, 3000, 50)
BOTTOM_WALL = Platform(0, LEVEL_HEIGHT-200, 3000, 50)

PLATFORM0 = Platform(300, 300, 500, 30)
PLATFORM1 = Platform(100, 400, 600, 30)
PLATFORM2 = Platform(900, 550, 800, 30)
PLATFORM3 = Platform(1800, 700, 900, 30)
PLATFORM4 = Platform(400, 850, 1000, 30)
PLATFORM5 = Platform(1600, 1000, 700, 30)
PLATFORM6 = Platform(300, 1150, 500, 30)
PLATFORM7 = Platform(1200, 1275, 1200, 30)
PLATFORM8 = Platform(200, 1400, 600, 30)
PLATFORM9 = Platform(1500, 1550, 1000, 30)
PLATFORM10 = Platform(800, 1700, 800, 30)
PLATFORM11 = Platform(400, 1850, 600, 30)
PLATFORM12 = Platform(1800, 1950, 900, 30)

PORTAL_X = 2700
PORTAL_Y = 100

START_POS = (100, 2000)

SPIKE1 = Spike(350, 270, 40, 40)
SPIKE2 = Spike(950, 520, 40, 40)
SPIKE3 = Spike(1850, 670, 40, 40)
SPIKE4 = Spike(600, 820, 40, 40)
SPIKE5 = Spike(1700, 970, 40, 40)
SPIKE6 = Spike(400, 1120, 40, 40)
SPIKE7 = Spike(1300, 1245, 40, 40)
SPIKE8 = Spike(300, 1370, 40, 40)
SPIKE9 = Spike(1700, 1520, 40, 40)

CRUSHER1 = Crusher(700, 270, 80, 80, 300, 4)
CRUSHER2 = Crusher(1700, 520, 80, 80, 200, 5)
CRUSHER3 = Crusher(900, 820, 80, 80, 400, 3)
CRUSHER4 = Crusher(1800, 1120, 80, 80, 350, 4)

VOIDER1 = Voider(600, 270)
VOIDER2 = Voider(1800, 520)
VOIDER3 = Voider(800, 820)
VOIDER4 = Voider(1700, 1120)
VOIDER5 = Voider(400, 1370)
VOIDER6 = Voider(2000, 1520)

platforms = pygame.sprite.Group(
    LEFT_WALL, RIGHT_WALL, TOP_WALL, BOTTOM_WALL,
    PLATFORM1, PLATFORM2, PLATFORM3, PLATFORM4, PLATFORM5, PLATFORM6,
    PLATFORM7, PLATFORM8, PLATFORM9, PLATFORM10, PLATFORM11, PLATFORM12
)

spikes = pygame.sprite.Group(
    SPIKE1, SPIKE2, SPIKE3, SPIKE4, SPIKE5, SPIKE6, SPIKE7, SPIKE8, SPIKE9
)

crushers = pygame.sprite.Group(
    CRUSHER1, CRUSHER2, CRUSHER3, CRUSHER4
)

voiders = pygame.sprite.Group(
    VOIDER1, VOIDER2, VOIDER3, VOIDER4, VOIDER5, VOIDER6
)

enemies = pygame.sprite.Group(
    spikes, crushers, voiders
)