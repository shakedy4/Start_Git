import pygame
import consts

soldier_rect = pygame.Rect(0, 0, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)


# drawing solider
def drawing_soldier():
    """
    Yarin
    """
    pass


# putting solider on (0,0)
def putting_soldier():
    """
    Yarin
    """
    pass


# returning soldiers index
def get_soldier_index():
    return [soldier_rect.x, soldier_rect.y]


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
    left_leg_x = get_soldier_feet_index()[0]
    left_leg_y = get_soldier_feet_index()[1]
    right_leg_x = left_leg_x + consts.STEP
    right_leg_y = left_leg_y
    if consts.FIELD[left_leg_y][left_leg_x] == consts.MINE \
            and consts.FIELD[right_leg_y][right_leg_x] == consts.MINE:
        return True
    else:
        return False


# checking if solider is on flag
def is_on_flag():
    pass



