import pygame
import minefield
import screen2
import solider
import consts

pygame.display.set_caption("The Flag!")

minefield.unite_screen()

pygame.init()
run = True
clock = pygame.time.Clock()

screen2.draw_night_screen()
# screen2.draw_screen()

while run:
    # clock.tick(consts.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()



