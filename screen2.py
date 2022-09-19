import pygame
import consts
import random
import minefield
import solider

rnd_grass_indexes = []


# coloring window
def draw_window(color):
    consts.WINDOW.fill(color)
    # pygame.display.update()


# draws 20 random grasses
def grass_indexes():
    for i in range(0, 20):
        rnd_y = random.randint(1, consts.WINDOW_WIDTH - 40)
        rnd_x = random.randint(0, consts.WINDOW_HEIGHT - 40)
        rnd_grass_indexes.append([rnd_x, rnd_y])


def draw_grass():
    for grass in range(0, len(rnd_grass_indexes)):
        consts.WINDOW.blit(consts.GRASS_PIC,
                           (rnd_grass_indexes[grass][1], rnd_grass_indexes[grass][0]))


def draw_mines(mines):
    for mine in range(0, len(mines), 3):
        consts.WINDOW.blit(consts.MINE_PIC, (mines[mine][1] * consts.STEP, mines[mine][0] * consts.STEP))


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
    draw_grass()
    draw_flag()
    solider.draw_soldier(soldier_rect)
    pygame.display.update()


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
    pygame.time.wait(1000)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE, consts.WIN_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_first_message():
    draw_message(consts.FIRST_MESSAGE, consts.FIRST_FONT_SIZE, (255, 255, 255), consts.FIRST_LOCATION)
    # time.sleep(consts.SHOW_MESSAGE)
