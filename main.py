import pygame
import minefield
import screen2
import solider
import consts
import time

pygame.display.set_caption("The Flag!")

minefield.unite_screen()


run = True
pygame.init()
screen2.draw_screen()
screen2.draw_first_message()
while run:
    # clock.tick(consts.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen2.draw_night_screen()
                pygame.time.wait(1000)
            else: pass
    screen2.draw_screen()
    pygame.display.update()

pygame.quit()



