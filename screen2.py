import pygame
import consts
import random

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("The Flag!")


def draw_window(color):
    window.fill(color)
    pygame.display.update()


def draw_grass():
    """
    :return: Prints 20 random grass images
    """
    for i in range(0, 20):
        # grass_image = pygame.image.load(consts.GRASS_PIC).convert()
        ran1 = random.randint(1, 950)  # The length of the image is 50, so download 50 so that it will not exceed
        ran2 = random.randint(0, 500)
        window.blit(consts.GRASS_PIC, [ran1, ran2])
        # pygame.display.flip()
        pygame.display.update()


def draw_soldier():
    window.blit(consts.SOLDIER_PIC, (0, 0))
    pygame.display.update()


def draw_night_soldier():
    window.blit(consts.NIGHT_SOLDIER_PIC, (100, 0))
    pygame.display.update()


run = True
clock = pygame.time.Clock()
draw_window(consts.GREEN_BACKGROUND)
draw_grass()
while run:
    # clock.tick(consts.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_soldier()
    pygame.display.update()

pygame.quit()
