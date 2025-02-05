import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del Ahorcado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente de texto
font = pygame.font.Font(None, 36)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    base_stick_union = (200, 400)
    top_stick_union = (base_stick_union[0], base_stick_union[1] - 350)

    pygame.draw.line(screen, WHITE, (base_stick_union[0] + 100, base_stick_union[1] + 100), base_stick_union, 3)
    pygame.draw.line(screen, WHITE, (base_stick_union[0] - 100, base_stick_union[1] + 100), base_stick_union, 3)

    pygame.draw.line(screen, WHITE, base_stick_union, top_stick_union, 3)

    pygame.display.flip()
'''
# Palabra a adivinar
palabra = "PYTHON"
letras_adivinadas = []

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letra = event.unicode.upper()
                if letra not in letras_adivinadas:
                    letras_adivinadas.append(letra)

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar la palabra oculta
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra + " "
        else:
            palabra_oculta += "_ "
    text = font.render(palabra_oculta, True, BLACK)
    screen.blit(text, (50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

# Finalización de Pygame
pygame.quit()
sys.exit()
'''