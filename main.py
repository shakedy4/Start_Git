import pygame
import minefield
import screen2
import solider
import consts
import database
import time


def main():
    pygame.display.set_caption("The Flag!")

    minefield.unite_screen()
    soldier_rect = pygame.Rect(0, 0, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)
    screen2.grass_indexes()
    screen2.draw_screen(soldier_rect)
    numbers_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                    pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

    screen2.draw_first_message()
    pygame.time.wait(2000)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # enter
                    screen2.draw_night_screen(soldier_rect)
                    pygame.time.wait(1000)
                else:
                    press_time = time.time()
                    keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.KEYUP and \
                    event.key in numbers_keys:  # number 1-9:
                press_time = time.time() - press_time
                press_time = str(press_time)
                press_time = press_time[:5]
                press_time = float(press_time)
                print(press_time)
                if press_time > 1:
                    print("big")
                    database.num_press_more(keys_pressed, soldier_rect, minefield.get_field())
                elif press_time <= 1:
                    print("small")
                    database.num_press_less(keys_pressed, soldier_rect, minefield.get_field())
            keys_pressed = pygame.key.get_pressed()
            solider.solider_movement(keys_pressed, soldier_rect)  # soldier movement

        if solider.is_on_flag(soldier_rect, minefield.flag_indexes()):
            screen2.draw_win_message()
            pygame.time.wait(3000)
            run = False

        if solider.is_on_mine(soldier_rect, minefield.mines_indexes()):
            screen2.draw_lose_message()
            pygame.time.wait(3000)
            run = False

        screen2.draw_screen(soldier_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
