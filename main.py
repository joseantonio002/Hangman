'''
https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

'''
import pygame
from pygame.locals import *
import sys
 
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

# Font
FONT = pygame.font.Font(None, 36)
WIDTH, HEIGHT = 800, 600


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.width, self.height = WIDTH, HEIGHT
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height))
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.draw.rect(self._display_surf, (255,0,0), pygame.Rect(200, 50, 400, 250))
        text = FONT.render('_ ' * 10, True, BLACK)
        screen.blit(text, (50, 50))

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
    theApp = App()
    theApp.on_execute()
