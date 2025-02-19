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
        self.game_state = None

    def guess_letter(self, letter):

        letter = letter.lower()
        if self.game_state == False or self.game_state == True or letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)
        if letter not in self.word_to_guess:
            self.n_mistakes += 1
            if self.n_mistakes == 6:
                self.game_state = False
                self.defeat = True
        else:
            all_found = all(l in self.guessed_letters for l in self.word_to_guess)
            if all_found:
                self.game_state = True 

    def end_msg(self):
        if self.game_state:
            return "You win!"
        elif self.game_state == False:
            return "You lose"
        return None

