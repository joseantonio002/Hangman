import pygame


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class HangmanAnimation():
    def __init__(self):
        self.state = 0 # base state (no body parts)

    def __draw_base(self, screen):
        # draw outside rectangle
        pygame.draw.rect(screen, WHITE, pygame.Rect(100, 100, 50, 50))

    def draw_current_state(self, screen):
        self.__draw_base(screen)

    def reset_animation(self):
        pass

    def next_state(self):
        pass    