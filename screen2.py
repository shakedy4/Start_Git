import pygame
import consts
import random

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("The Flag!")


def draw_window(color):
    window.fill(color)
    pygame.display.update()


def draw_grass():
    window.blit(consts.GRASS_PIC, (300, 100))
    pygame.display.update()


def draw_soldier():
    window.blit(consts.SOLDIER_PIC, (0, 0))
    pygame.display.update()


def draw_night_soldier():
    window.blit(consts.NIGHT_SOLDIER_PIC, (100, 0))
    pygame.display.update()


def draw_mine():
    window.blit(consts.MINE_PIC, (400, 100))
    pygame.display.update()


run = True
clock = pygame.time.Clock()
draw_window(consts.GREEN_BACKGROUND)
while run:
    # clock.tick(consts.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_grass()
    draw_soldier()
    draw_mine()
    draw_night_soldier()
    pygame.display.update()

pygame.quit()
