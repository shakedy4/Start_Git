import pygame
import consts
import random
import minefield


# coloring window
def draw_window(color):
    consts.WINDOW.fill(color)
    pygame.display.update()


# draws 20 random grasses
def draw_grass():
    for i in range(0, 20):
        ran1 = random.randint(1, consts.WINDOW_WIDTH - 40)
        ran2 = random.randint(0, consts.WINDOW_HEIGHT - 40)
        consts.WINDOW.blit(consts.GRASS_PIC, [ran1, ran2])
        pygame.display.update()


def draw_soldier(x, y):
    consts.WINDOW.blit(consts.SOLDIER_PIC, (x * consts.STEP, y * consts.STEP))
    pygame.display.update()


def draw_night_soldier(x, y):
    consts.WINDOW.blit(consts.NIGHT_SOLDIER_PIC, (x * consts.STEP, y * consts.STEP))
    pygame.display.update()


def draw_mines():
    mines = minefield.mines_indexes()
    for mine in range(0, len(mines), 3):
        consts.WINDOW.blit(consts.MINE_PIC, (mines[mine][0] * consts.STEP, mines[mine][1] * consts.STEP))
        pygame.display.update()


def draw_flag():
    consts.WINDOW.blit(consts.FLAG_PIC, (920, 420))
    pygame.display.update()


def draw_night_tabel():
    for row in range(25):
        pygame.draw.lines(consts.WINDOW, consts.NIGHT_TABLE,
                          True, [(0, 20 * row), (1000, 20 * row)])
    for col in range(50):
        pygame.draw.aalines(consts.WINDOW, consts.NIGHT_TABLE,
                            True, [(20 * col, 0), (20 * col, 500)])
    pygame.display.update()


def draw_screen():
    draw_window(consts.GREEN_BACKGROUND)
    draw_grass()
    draw_flag()


def draw_night_screen():
    draw_window(consts.NIGHT_BACKGROUND)
    draw_night_tabel()
    draw_mines()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    consts.WINDOW.blit(text_img, location)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE, consts.WIN_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION)
def draw_first_message():
    draw_message(consts.FIRST_MESSAGE, consts.FIRST_FONT_SIZE, consts.WIN_COLOR, consts.FIRST_LOCATION)
