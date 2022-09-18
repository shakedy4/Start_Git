import pygame
import consts

solider_rect = pygame.rect(0, 0, consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT)


# drawing solider
def drawing_solider():
    """
    Yarin
    """
    pass


# putting solider on (0,0)
def putting_solider():
    """
    Yarin
    """
    pass


# returning solider's index
def get_solider_index():
    return set(solider_rect.x, solider_rect.y)


# returning solider's feet index
def get_solider_feet_index():



# solider movement
def solider_movement(keys_pressed, solider_rect):
    if keys_pressed[pygame.K_LEFT] \
            and solider_rect - consts.STEP < consts.WINDOW_WIDTH:
        solider_rect.x -= consts.STEP  # left
    if keys_pressed[pygame.K_RIGHT] \
            and solider_rect + consts.STEP < consts.WINDOW_WIDTH:
        solider_rect.x += consts.STEP  # right
    if keys_pressed[pygame.K_UP] \
            and solider_rect - consts.STEP < consts.WINDOW_HIGHT:
        solider_rect.y -= consts.STEP  # up
    if keys_pressed[pygame.K_DOWN] \
            and solider_rect + consts.STEP < consts.WINDOW_HIGHT:
        solider_rect.y += consts.STEP  # down


# checking if solider on a mine
def is_on_mine():
    pass


# checking if solider is on flag
def is_on_flag():
    pass
