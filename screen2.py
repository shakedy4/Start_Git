import pygame
import consts
import random
import minefield
import solider


# coloring window
def draw_window(color):
    consts.WINDOW.fill(color)
    # pygame.display.update()


# draws 20 random grasses
def grass_indexes(field):
    grasses = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            if field[row][col] == consts.GRASS:
                grasses.append([col, row])
    return grasses


def draw_grass(grasses):
    for grass in range(0, len(grasses)):
        consts.WINDOW.blit(consts.GRASS_PIC,
                           (grasses[grass][0] * consts.STEP, grasses[grass][1] * consts.STEP))


def draw_mines(mines):
    for mine in range(0, len(mines), 3):
        consts.WINDOW.blit(consts.MINE_PIC, (mines[mine][0] * consts.STEP, mines[mine][1] * consts.STEP))


def draw_flag():
    consts.WINDOW.blit(consts.FLAG_PIC, (920, 420))


def draw_night_tabel():
    for row in range(25):
        pygame.draw.lines(consts.WINDOW, consts.NIGHT_TABLE,
                          True, [(0, 20 * row), (1000, 20 * row)])
    for col in range(50):
        pygame.draw.aalines(consts.WINDOW, consts.NIGHT_TABLE,
                            True, [(20 * col, 0), (20 * col, 500)])


def draw_screen(soldier_rect):
    draw_window(consts.GREEN_BACKGROUND)
    draw_grass(grass_indexes(minefield.get_field()))
    draw_flag()
    solider.draw_soldier(soldier_rect)
    # pygame.display.update()


def draw_night_screen(soldier_rect):
    draw_window(consts.NIGHT_BACKGROUND)
    draw_night_tabel()
    draw_mines(minefield.mines_indexes())
    solider.draw_soldier(soldier_rect)
    pygame.display.update()


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    consts.WINDOW.blit(text_img, location)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE, consts.WIN_COLOR, consts.LOSE_LOCATION)
    pygame.display.update()


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.update()


def draw_first_message():
    draw_message(consts.FIRST_MESSAGE, consts.FIRST_FONT_SIZE, (255, 255, 255), consts.FIRST_LOCATION)
    pygame.display.update()
