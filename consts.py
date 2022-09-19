import os
import pygame

SCREEN_ROWS = 25
SCREEN_COLS = 50
EMPTY = "EMPTY"
MINE = "MINE"
FLAG = "FLAG"
SOLDIER = "SOLDIER"
SOLDIER_HEIGHT = 4
SOLDIER_WIDTH = 2
FLAG_HEIGHT = 3
FLAG_WIDTH = 4
MINE_WIDTH = 3
STEP = 20
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
GREEN_BACKGROUND = (0, 128, 0)
NIGHT_BACKGROUND = (0, 0, 0)
NIGHT_TABLE = (14, 38, 0)
FPS = 60
GRASS_PIC = pygame.image.load(os.path.join('pictures', 'grass.png'))
SOLDIER_PIC = pygame.image.load(os.path.join('pictures', 'soldier.png'))
NIGHT_SOLDIER_PIC = pygame.image.load(os.path.join('pictures', 'soldier_night.png'))
MINE_PIC = pygame.image.load(os.path.join('pictures', 'mine.png'))
FLAG_PIC = pygame.image.load(os.path.join('pictures', 'flag.png'))
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

