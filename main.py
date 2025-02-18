'''
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

Modelo: Gestiona las tareas (crear, editar, eliminar).
Vista: Muestra la lista de tareas en una interfaz gráfica.
Controlador: Recibe las acciones del usuario (como agregar una tarea) y actualiza el modelo y la vista.

'''
import pygame
from pygame.locals import *
import sys
from hangmanView import HangmanView
from hangmanModel import HangmanModel

class HangmangController:
    def __init__(self):
        self._running = True
 
    def on_init(self):
        pygame.init()
        self._running = True
        self._hangman_view = HangmanView()
        self._hangman_model = HangmanModel()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode.upper()
                self._hangman_model.guess_letter(letter)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._hangman_view.check_click_button(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._hangman_view.check_unclick_button(pygame.mouse.get_pos()):
                self._hangman_model.restart()
                
    def on_loop(self):
        self._hangman_view.show_end_message("You win!", False)
        self._hangman_view.draw_hangman_stickman(6)
        self._hangman_view.show_word_to_guess("pato", ["p", "o", "z", "x"], True)
        self._hangman_view.show_wrong_letters("pato", ["p", "o", "z", "x"])
        self._hangman_view.draw_button(pygame.mouse.get_pos()) 

    def on_render(self):
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = HangmangController()
    theApp.on_execute()



'''
    def on_loop(self):
        pygame.draw.rect(self._display_surf, (255,0,0), pygame.Rect(200, 50, 400, 250))
        text = self._FONT.render('A ' * 2 + '_ ', True, WHITE)
        text_width = text.get_width()
        center_x = (self.width // 2) - (text_width // 2)
        self._display_surf.blit(text, (center_x, 325))
        pygame.draw.rect(self._display_surf, (255,0,0), pygame.Rect(180, 380, 445, 100))
        pygame.draw.rect(self._display_surf, (255,0,0), pygame.Rect((self.width//2) - (200/2), 500, 200, 50))
'''