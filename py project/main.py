import pygame
import sys
import input_box
import console
import random
import os

#инициализация пугейма
pygame.init()

#всякая чушь чисто для себя (ну или поржать)
ver="1.0.0"
random_text={0: "",
             1: "Also try Mondealy Mod Installer!",
             2: "I used pygame!",
             3: "",
             4: "",
             5: "Also try Banana Farmer 3000!",
             6: "Also try real life!"}

random_text_num=random.randint(0, 6)

#инициализация окна
screen=pygame.display.set_mode((640, 680))
pygame.display.set_caption(f"Shell Emulator {ver} {random_text[random_text_num]}")
console_layer = pygame.Surface((640, 680))

#цвета
bg_col=(9, 12, 40)
gray=(200, 200, 200)

penis=0

#хер его знает, зачем я сделал для выхода отдельную функцию
def kill_this_fucking_program():
    pygame.quit()
    sys.exit()

#основная функция программы, бла бла бла
def main():
    global penis
    clock = pygame.time.Clock()
    screen.blit(console_layer, (0, 0 + penis))
    console_output = console.ConsoleOutput(25, 18, 90, 600, 575)
    inputbox = input_box.InputBox(10, 50, 615, 30, 25)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==5:
                    penis-=25
                if event.button==4:
                    if penis!=0:
                        penis+=25


            inputbox.handle_event(event)


        screen.fill(bg_col)
        inputbox.draw(screen)
        console_output.draw(screen)
        pygame.display.flip()
        clock.tick(60)


    kill_this_fucking_program()

if __name__ == '__main__':
    main()
