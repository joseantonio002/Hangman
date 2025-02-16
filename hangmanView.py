import pygame

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

color_light = (170,170,170)  
color_dark = (100,100,100) 

smallfont = pygame.font.SysFont('Corbel',35) 
text = smallfont.render('quit' , True , color) 

WIDTH, HEIGHT = 800, 600

class HangmanView():
    def __init__(self):
        self.width, self.height = WIDTH, HEIGHT
        self._display_surf = pygame.display.set_mode((self.width, self.height))
        self._FONT = pygame.font.Font(None, 45)

    def show_end_message(self, msg, defeat):
        '''
        Shows message when you win or lose
        msg (str or None): message to show (win or lose), if msg is None dont show anything
        victory (bool): if True change the color of the text to victory color if False change it to defeat color
        '''
        if msg is not None:
            color_msg = GREEN
            if defeat:
                color_msg = RED
            text = self._FONT.render(msg, True, color_msg)
            text_width = text.get_width()
            center_x = (self.width // 2) - (text_width // 2)
            self._display_surf.blit(text, (center_x, 10))

    def show_word_to_guess(self, word_to_guess, guessed_letters, defeat):
        """
        Show word to guess, if a letter is not guessed yet it will show "_"
        If the game is over it will show the full word, with the letters not guessed in red
        """
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters or defeat:
                display_word += letter + " "
            else:
                display_word += "_ "

        display_word = display_word.strip()

        text_surface = self._FONT.render(display_word, True, WHITE)
        text_width = text_surface.get_width()

        start_x = (self.width // 2) - (text_width // 2)

        # Render each letter individually to handle color changes
        x_offset = 0
        for letter in display_word.split():
            if letter == "_":
                color = WHITE
            else:
                if defeat and letter not in guessed_letters:
                    color = RED
                else:
                    color = WHITE

            letter_surface = self._FONT.render(letter, True, color)
            self._display_surf.blit(letter_surface, (start_x + x_offset, 360))
            x_offset += letter_surface.get_width() + 5  # Add a small space between letters    

    def show_wrong_letters(self, word_to_guess, guessed_letters):
        """
        Show wrong words
        """
        # Filtrar las letras incorrectas
        wrong_letters = [letter.upper() for letter in guessed_letters if letter not in word_to_guess]

        wrong_letters_str = "  ".join(wrong_letters)
        text_surface = self._FONT.render(wrong_letters_str, True, WHITE)
        text_width = text_surface.get_width()

        start_x = (self.width // 2) - (text_width // 2)

        self._display_surf.blit(text_surface, (start_x, 430))

    def draw_button(self, mouse):
        y_pos = 480
        if self.width/2 <= mouse[0] <= self.width/2+140 and y_pos <= mouse[1] <= y_pos/2+40: 
            pygame.draw.rect(self._display_surf, color_light, [self.width/2, y_pos, 140, 40]) 
        else: 
            pygame.draw.rect(self._display_surf, color_dark, [self.width/2, y_pos, 140, 40]) 

    def __draw_gallow(self):
        """
        Draw gallows poles
        """
        pygame.draw.rect(self._display_surf, WHITE, pygame.Rect(100, 50, 600, 300), width=1)
        base_stick_union = (265, 300)
        top_stick_union1 = (base_stick_union[0], base_stick_union[1] - 230)
        top_stick_union2 = (top_stick_union1[0] + 140, top_stick_union1[1])
        stick_head_union = (top_stick_union2[0], top_stick_union2[1] + 40)

        pygame.draw.line(self._display_surf, WHITE, (base_stick_union[0] + 45, base_stick_union[1] + 45), base_stick_union, 3) # support stick
        pygame.draw.line(self._display_surf, WHITE, (base_stick_union[0] - 45, base_stick_union[1] + 45), base_stick_union, 3) # support stick

        pygame.draw.line(self._display_surf, WHITE, base_stick_union, top_stick_union1, 3) # long vertical stick
        pygame.draw.line(self._display_surf, WHITE, top_stick_union1, top_stick_union2, 3) # horizontal stick to the right

        pygame.draw.line(self._display_surf, WHITE, top_stick_union2, stick_head_union, 3) # stick where the head is attached

    def draw_hangman_stickman(self, n_mistakes):
        """
        Draw the hangman stickman based on the number of mistakes
        """
        self.__draw_gallow()