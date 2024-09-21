import pygame
import sys
import input_box
import console
import random
import os

pygame.init()

ver="0.0.7"
random_text={0: "",
             1: "Also try Mondealy Mod Installer!",
             2: "I used pygame!",
             3: "",
             4: "",
             5: "Also try Banana Farmer 3000!",
             6: "Also try real life!"}

random_text_num=random.randint(0, 6)

screen=pygame.display.set_mode((640, 480))
pygame.display.set_caption(f"Shell Emulator {ver} {random_text[random_text_num]}")

bg_col=(9, 12, 40)
gray=(200, 200, 200)

def kill_this_fucking_program():
    pygame.quit()
    sys.exit()

def main():
    clock = pygame.time.Clock()
    console_output = console.ConsoleOutput(25, 18, 90, 600, 375)
    inputbox = input_box.InputBox(10, 50, 615, 30, 25)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            inputbox.handle_event(event)

        screen.fill(bg_col)
        console_output.draw(screen)
        inputbox.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    kill_this_fucking_program()

if __name__ == '__main__':
    main()