import os
import pygame

# screen related:
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
GREEN_BACKGROUND = (81, 224, 16)
NIGHT_BACKGROUND = (14, 38, 0)
FPS = 60
GRASS_PIC = pygame.image.load(os.path.join('pictures', 'grass.png'))
SOLDIER_PIC = pygame.image.load(os.path.join('pictures', 'soldier.png'))
NIGHT_SOLDIER_PIC = pygame.image.load(os.path.join('pictures', 'soldier_night.png'))
MINE_PIC = pygame.image.load(os.path.join('pictures', 'mine.png'))
FLAG_PIC = pygame.image.load(os.path.join('pictures', 'flag.png'))

# SLOT_WINDOW_WIDTH = WINDOW_WIDTH / SCREEN_COLS
# SLOT_WINDOW_HEIGHT = WINDOW_HEIGHT / SCREEN_ROWS
# SCREEN_COLOR = (81, 224, 16)
# SCREEN_COLOR_MINE = (14, 38, 0)
# GRASS_PICTURES = r"C:\Users\yarin\Downloads\pics_files\grass.png"
# SOLDIER_PICTURE = r"C:\Users\yarin\Downloads\pics_files\soldier.png"
# PINK = (255, 20, 147)
# FLAG_PICTURE = r"C:\Users\yarin\Downloads\pics_files\flag.png"
# SOLDIER_MINE_PICTURE = r"C:\Users\yarin\Downloads\pics_files\soldier_nigth.png"
# MINE_PICTURE = r"C:\Users\yarin\Downloads\pics_files\mine.png"
