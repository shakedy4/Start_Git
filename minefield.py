import consts
import random
import pygame
import screen2

pygame.display.set_caption("The Flag")

field = []


# creating an empty matrix
def empty_screen():
    row_to_append = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            row_to_append.append(consts.EMPTY)
        field.append(row_to_append)
        row_to_append = []


def put_flag():
    for row in range(consts.SCREEN_ROWS - consts.FLAG_HEIGHT - 1, consts.SCREEN_ROWS - 1):
        for col in range(consts.SCREEN_COLS - consts.FLAG_WIDTH, consts.SCREEN_COLS):
            field[row][col] = consts.FLAG


def put_soldier():
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            field[row][col] = consts.SOLDIER


# putting 20 mines on random places
def put_mines():
    mines_count = 0
    while mines_count < 20:
        row = random.randint(0, consts.SCREEN_ROWS - 1)
        col = random.randint(0, consts.SCREEN_COLS - 3)
        if field[row][col] == consts.EMPTY:
            mines_count += 1
            for i in range(consts.MINE_WIDTH):
                field[row][col + i] = consts.MINE


def unite_screen():
    empty_screen()
    put_flag()
    put_soldier()
    put_mines()


# returns a list of the mines' indexes
def mines_indexes():
    mines = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            if field[row][col] == consts.MINE:
                mines.append([row, col])
    return mines


# returns a list of the flag's indexes
def flag_indexes():
    flags = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            if field[row][col] == consts.FLAG:
                flags.append([row, col])
    return flags

# for i in range(consts.SCREEN_ROWS):
#     for j in range(consts.SCREEN_COLS):
#         print(field[i][j], end=" ")
#     print(" ")
#
# print(mines_indexes())
# print(flag_indexes())

