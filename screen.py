import pygame
import consts
import random


#
# size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
# screen = pygame.display.set_mode(size)
# def Background_deletion(image):
#     """
#     :param image:picture with a pink background
#     :return:Image with a transparent background
#     """
#     image.set_colorkey(consts.PINK)
#
# def Random_grass():
#     """
#
#     :return: Prints 20 random grass images
#     """
#     for i in range(20):
#         grass_image = pygame.image.load(consts.GRASS_PICTURES).convert()
#         Background_deletion(grass_image)
#         ran1 = random.randint(1, 950)  # The length of the image is 50, so download 50 so that it will not exceed
#         ran2 = random.randint(20, 500)
#         # The height of the image is 20, therefore we start from 20, which will not exceed
#         screen.blit(grass_image, [ran1, ran2])
#         pygame.display.flip()
#
# def play():
#     pygame.init()
#     # size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
#     # screen = pygame.display.set_mode(size)
#     pygame.display.set_caption("The Flag")
#     screen.fill(consts.SCREEN_COLOR)
#     Random_grass()
#     flag_image = pygame.image.load(consts.FLAG_PICTURE).convert()
#     Background_deletion(flag_image)
#     screen.blit(flag_image, [920, 420])
#     player_image = pygame.image.load(consts.SOLDIER_PICTURE).convert()
#     Background_deletion(player_image)
#     screen.blit(player_image, [0, 0])
#     pygame.display.flip()
#     finish = False
#     while not finish:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 finish = True
#
#     pygame.quit()
#


