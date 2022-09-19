import pygame
import minefield
import screen2
import solider
import consts


def main():
    pygame.display.set_caption("The Flag!")

    minefield.unite_screen()
    soldier_rect = pygame.Rect(0, 0, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)
    screen2.grass_indexes()
    screen2.draw_screen(soldier_rect)

    # screen2.draw_first_message()

    # clock = pygame.time.Clock()
    run = True

    while run:
        # clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen2.draw_night_screen(soldier_rect)
                    pygame.time.wait(1000)
            keys_pressed = pygame.key.get_pressed()
            solider.solider_movement(keys_pressed, soldier_rect)

        if solider.is_on_flag(soldier_rect):
            print("on flag")
            run = False

        if solider.is_on_mine(soldier_rect):
            print("on mine")
            run = False

        screen2.draw_screen(soldier_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
