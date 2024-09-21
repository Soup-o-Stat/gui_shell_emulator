import pygame
import console
import emulator

console_output=console.ConsoleOutput
emulator_obj=emulator.Emulator

input_history=[]
history_step=0

class InputBox:
    def __init__(self, x, y, w, h, font_size):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = (100, 100, 100)
        self.color_active = (255, 255, 255)
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.font = pygame.font.Font(None, font_size)
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.min_w = w

    def handle_event(self, event):
        global history_step
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text!='':
                        emulator.Emulator.read_command(self, self.text)
                        self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pass
                elif event.key==pygame.K_UP:
                    if len(input_history)>0 and (len(input_history)-history_step)>0:
                        history_step += 1
                        self.text=str(input_history[len(input_history)-history_step])
                    else:
                        pass
                elif event.key==pygame.K_DELETE:
                    self.text=''
                elif event.key==pygame.K_DOWN:
                    if (len(input_history)-history_step)<len(input_history)-1:
                        history_step -= 1
                        self.text=str(input_history[len(input_history)-history_step])
                    else:
                        pass
                else:
                    self.text += event.unicode

        self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2, border_radius=10)