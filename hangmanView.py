import pygame

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

color_light = (170,170,170)  
color_dark = (100,100,100) 

WIDTH, HEIGHT = 800, 600

class HangmanView():
    def __init__(self):
        self.width, self.height = WIDTH, HEIGHT
        self._display_surf = pygame.display.set_mode((self.width, self.height))
        self._FONT = pygame.font.Font(None, 45)
        # button variables:
        self.button_width, self.button_height = 140, 40
        self.button_x, self.button_y = (self.width // 2) - self.button_width // 2, 480
        self.is_button_clicked = False


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
        wrong_letters = [letter.upper() for letter in guessed_letters if letter not in word_to_guess]

        wrong_letters_str = "  ".join(wrong_letters)
        text_surface = self._FONT.render(wrong_letters_str, True, WHITE)
        text_width = text_surface.get_width()

        start_x = (self.width // 2) - (text_width // 2)

        self._display_surf.blit(text_surface, (start_x, 430))

    def __mouse_over_button(self, mouse):
        """
        Given the mouse coordinates returns True if the button was pressed or False otherwise
        """
        if self.button_x <= mouse[0] <= self.button_x + self.button_width and self.button_y <= mouse[1] <= self.button_y + self.button_height:
            return True
        return False

    def check_click_button(self, mouse):
        """
        In case of a MOUSEBUTTONDOWN event checks if the restart button was clicked
        """
        if self.__mouse_over_button(mouse):
            self.is_button_clicked = True

    def check_unclick_button(self, mouse):
        """
        In case of a MOUSEBUTTONUP event checks if the restart button was unclicked and returns True in that case, returns False otherwise
        """
        if self.is_button_clicked:
            if self.__mouse_over_button(mouse):
                print("restart y cancelar animación")
                self.is_button_clicked = False
                return True
            else:
                self.is_button_clicked = False
        return False

    def draw_button(self, mouse):
        if self.__mouse_over_button(mouse):
            pygame.draw.rect(self._display_surf, color_dark, [self.button_x, self.button_y, self.button_width, self.button_height])
            if self.is_button_clicked:
                pygame.draw.rect(self._display_surf, (50, 50, 50), [self.button_x, self.button_y, self.button_width, self.button_height], 5)
        else:
            pygame.draw.rect(self._display_surf, color_light, [self.button_x, self.button_y, self.button_width, self.button_height])

        text_surface = self._FONT.render("Restart", True, WHITE)
        text_rect = text_surface.get_rect(center=(self.button_x + self.button_width/2, self.button_y + self.button_height/2))
        self._display_surf.blit(text_surface, text_rect)

    def __draw_gallow(self):
        """
        Draw gallows poles
        """
        pygame.draw.rect(self._display_surf, WHITE, pygame.Rect(100, 50, 600, 300), width=1)
        self.base_stick_union = (265, 300)
        self.top_stick_union1 = (self.base_stick_union[0], self.base_stick_union[1] - 230)
        self.top_stick_union2 = (self.top_stick_union1[0] + 140, self.top_stick_union1[1])
        self.stick_head_union = (self.top_stick_union2[0], self.top_stick_union2[1] + 40)

        pygame.draw.line(self._display_surf, WHITE, (self.base_stick_union[0] + 45, self.base_stick_union[1] + 45), self.base_stick_union, 3) # support stick
        pygame.draw.line(self._display_surf, WHITE, (self.base_stick_union[0] - 45, self.base_stick_union[1] + 45), self.base_stick_union, 3) # support stick

        pygame.draw.line(self._display_surf, WHITE, self.base_stick_union, self.top_stick_union1, 3) # long vertical stick
        pygame.draw.line(self._display_surf, WHITE, self.top_stick_union1, self.top_stick_union2, 3) # horizontal stick to the right

        pygame.draw.line(self._display_surf, WHITE, self.top_stick_union2, self.stick_head_union, 3) # stick where the head is attached

    def draw_hangman_stickman(self, n_mistakes):
        """
        Draw the hangman stickman based on the number of mistakes
        """
        if n_mistakes >= 0:
          self.__draw_gallow()
        if n_mistakes >= 1:
            radius = 20
            pygame.draw.circle(self._display_surf, WHITE, (self.stick_head_union[0], self.stick_head_union[1] + radius + 3), radius, width=3) 
        if n_mistakes >= 2:
            height = 55
            torso_start = (self.stick_head_union[0], self.stick_head_union[1] + radius* 2 + 3)
            torso_end = (self.stick_head_union[0], self.stick_head_union[1] + radius* 2 + 3 + height)
            pygame.draw.line(self._display_surf, WHITE, torso_start, torso_end, width=3) # torso
        if n_mistakes >= 3:
            shoulder = (torso_start[0], torso_start[1] + (height // 3))
            arm_length = 15
            pygame.draw.line(self._display_surf, WHITE, shoulder, (shoulder[0] - arm_length, shoulder[1] + arm_length), width=3) # left arm
        if n_mistakes >= 4:
            pygame.draw.line(self._display_surf, WHITE, shoulder, (shoulder[0] + arm_length, shoulder[1] + arm_length), width=3) # right arm
        if n_mistakes >= 5:
            leg_length = 30
            pygame.draw.line(self._display_surf, WHITE, torso_end, (torso_end[0] - leg_length + 20, torso_end[1] + leg_length), width=3) # left leg
        if n_mistakes == 6:
            pygame.draw.line(self._display_surf, WHITE, torso_end, (torso_end[0] + leg_length - 20, torso_end[1] + leg_length), width=3) # right leg
        