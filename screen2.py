import pygame
import consts
import random

pygame.display.set_caption("The Flag!")


def draw_window(color):
    consts.WINDOW.fill(color)
    pygame.display.update()


def draw_grass():
    """
    :return: Prints 20 random grass images
    """
    for i in range(0, 20):
        # grass_image = pygame.image.load(consts.GRASS_PIC).convert()
        ran1 = random.randint(1, 950)  # The length of the image is 50, so download 50 so that it will not exceed
        ran2 = random.randint(0, 500)
        consts.WINDOW.blit(consts.GRASS_PIC, [ran1, ran2])
        # pygame.display.flip()
        pygame.display.update()


def draw_soldier(x , y):
    consts.WINDOW.blit(consts.SOLDIER_PIC, (x, y))
    pygame.display.update()

def draw_flag():
    consts.WINDOW.blit(consts.FLAG_PIC, (920, 420))
    pygame.display.update()

def draw_night_soldier(x, y):
    consts.WINDOW.blit(consts.NIGHT_SOLDIER_PIC, (x, y))
    pygame.display.update()


# run = True
# clock = pygame.time.Clock()
# draw_window(consts.GREEN_BACKGROUND)
# draw_grass()
# while run:
#     # clock.tick(consts.FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     draw_soldier()
#     draw_flag()
#     pygame.display.update()
#
# pygame.quit()
