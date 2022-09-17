import consts
import random


def empty_screen():
    row_to_append = []
    for row in range(consts.SCREEN_ROWS):
        for col in range(consts.SCREEN_COLS):
            row_to_append.append(consts.EMPTY)
        consts.FIELD.append(row_to_append)
        row_to_append = []


def put_flag():
    for row in range(consts.SCREEN_ROWS - consts.FLAG_HEIGHT - 1, consts.SCREEN_ROWS - 1):
        for col in range(consts.SCREEN_COLS - consts.FLAG_WIDTH, consts.SCREEN_COLS):
            consts.FIELD[row][col] = consts.FLAG


def put_solider():
    for row in range(consts.SOLIDER_WIDTH):
        for col in range(consts.SOLIDER_HEIGHT):
            consts.FIELD[row][col] = consts.SOLIDER


def put_mines():
    mines_count = 0
    while mines_count < 20:
        row = random.randint(0, consts.SCREEN_ROWS-1)
        col = random.randint(0, consts.SCREEN_COLS)
        if consts.FIELD[row][col] == consts.EMPTY:
            mines_count += 1
            for i in range(consts.MINE_WIDTH):
                consts.FIELD[row][col + i] = consts.MINE


def unite_screen():
    empty_screen()
    put_flag()
    put_solider()
    put_mines()


unite_screen()
for i in range(len(consts.FIELD)):
    for j in range(len(consts.FIELD[i])):
        print(consts.FIELD[i][j], end=" ")
    print(" ")
