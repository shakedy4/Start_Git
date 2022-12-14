import pygame
import consts
import minefield


def draw_soldier(soldier_rect):
    consts.WINDOW.blit(consts.SOLDIER_PIC, (soldier_rect.x * consts.STEP, soldier_rect.y * consts.STEP))
    pygame.display.update()


def draw_night_soldier(soldier_rect):
    consts.WINDOW.blit(consts.NIGHT_SOLDIER_PIC, (soldier_rect.x * consts.STEP, soldier_rect.y * consts.STEP))
    pygame.display.update()


# returning soldiers index
def get_soldier_index(soldier_rect):
    soldier_index = []
    for i in range(consts.SOLDIER_HEIGHT):
        for j in range(consts.SOLDIER_WIDTH):
            soldier_index.append([(soldier_rect.x + j), soldier_rect.y + i])
    return soldier_index


# returning soldiers feet index
def get_soldier_feet_index(soldier_rect):
    feet_x = soldier_rect.x
    feet_y = soldier_rect.y + 1 * (consts.SOLDIER_HEIGHT - 1)
    return [feet_x, feet_y]


# checking if solider on a mine
def is_on_mine(soldier_rect, mines):
    left_leg = get_soldier_feet_index(soldier_rect)
    right_leg = [left_leg[0] + 1, left_leg[1]]
    if left_leg in mines and right_leg in mines:
        return True
    return False


# checking if solider is on flag
def is_on_flag(soldier_rect, flags):
    soldier_body = get_soldier_index(soldier_rect)
    for index in range(len(soldier_body)):
        if soldier_body[index] in flags:
            return True
    return False


# solider movement
def solider_movement(keys_pressed, soldier_rect):
    if keys_pressed[pygame.K_LEFT] \
            and 0 < soldier_rect.x * consts.STEP < consts.WINDOW_WIDTH:
        soldier_rect.x -= 1  # left
    if keys_pressed[pygame.K_RIGHT] \
            and 0 < soldier_rect.x * consts.STEP + consts.STEP * 2 < consts.WINDOW_WIDTH:
        soldier_rect.x += 1  # right
    if keys_pressed[pygame.K_UP] \
            and 0 < soldier_rect.y * consts.STEP < consts.WINDOW_HEIGHT:
        soldier_rect.y -= 1  # up
    if keys_pressed[pygame.K_DOWN] \
            and 0 < soldier_rect.y * consts.STEP + consts.STEP * 4 < consts.WINDOW_HEIGHT:
        soldier_rect.y += 1  # down

