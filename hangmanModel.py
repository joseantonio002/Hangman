import pygame
from random_word import RandomWords

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class HangmanModel():
    def __init__(self):
        self.guessed_letters = []
        self.defeat = False
        self.n_mistakes = 0
        self.random_word_generator = RandomWords()
        self.word_to_guess = self.random_word_generator.get_random_word()
        self.game_state = None # None, False (defeat), True (victory)

    def restart(self):
        self.guessed_letters = []
        self.defeat = False
        self.n_mistakes = 0
        self.word_to_guess = self.random_word_generator.get_random_word()

    def __check_win(self):
        return True if for l in word l in self.guessed_letters else False

    def guess_letter(self, letter):
        self.guessed_letters.append(letter)
        if letter not in self.word_to_guess:
            self.n_mistakes += 1

        if self.__check_win():
            self.game_state = True

        if self.n_mistakes > 6:
            self.game_state = 
