from hangmanView import HangmanView
from hangmanModel import HangmanModel
import pygame
from pygame.locals import *
import sys


class HangmanController:
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
        self._hangman_view.reset_surface()
        #print(self._hangman_model.word_to_guess)
        self._hangman_view.show_end_message(self._hangman_model.end_msg(), self._hangman_model.defeat)
        self._hangman_view.draw_hangman_stickman(self._hangman_model.n_mistakes)
        self._hangman_view.show_word_to_guess(self._hangman_model.word_to_guess, self._hangman_model.guessed_letters, self._hangman_model.defeat)
        self._hangman_view.show_wrong_letters(self._hangman_model.word_to_guess, self._hangman_model.guessed_letters)
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