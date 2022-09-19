import pygame
import consts
import minefield

soldier_rect = pygame.Rect(0, 0, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)


# returning soldiers index
def get_soldier_index():
    soldier_index = []
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            soldier_index.append([(soldier_rect.x + j), soldier_rect.y + i])
    return soldier_index


# returning soldiers feet index
def get_soldier_feet_index():
    feet_x = soldier_rect.x
    feet_y = soldier_rect.y + consts.STEP * (consts.SOLDIER_HEIGHT - 1)
    return [feet_x, feet_y]


# solider movement
def solider_movement(keys_pressed, solider_rect):
    if keys_pressed[pygame.K_LEFT] \
            and solider_rect - consts.STEP < consts.WINDOW_WIDTH:
        solider_rect.x -= consts.STEP  # left
    if keys_pressed[pygame.K_RIGHT] \
            and solider_rect + consts.STEP < consts.WINDOW_WIDTH:
        solider_rect.x += consts.STEP  # right
    if keys_pressed[pygame.K_UP] \
            and solider_rect - consts.STEP < consts.WINDOW_HEIGHT:
        solider_rect.y -= consts.STEP  # up
    if keys_pressed[pygame.K_DOWN] \
            and solider_rect + consts.STEP < consts.WINDOW_HEIGHT:
        solider_rect.y += consts.STEP  # down


# checking if solider on a mine
def is_on_mine():
    left_leg = get_soldier_feet_index()
    right_leg = [left_leg[0] + consts.STEP, left_leg[1]]
    if left_leg in minefield.mines_indexes() \
            and right_leg in minefield.mines_indexes():
        return True
    else:
        return False


# checking if solider is on flag
def is_on_flag():
    for index in range(len(get_soldier_index())):
        if index in get_soldier_index():
            return True
    return False

