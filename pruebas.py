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
    top_stick_union1 = (base_stick_union[0], base_stick_union[1] - 350)
    top_stick_union2 = (top_stick_union1[0] + 180, top_stick_union1[1])
    stick_head_union = (top_stick_union2[0], top_stick_union2[1] + 50)

    pygame.draw.line(screen, WHITE, (base_stick_union[0] + 100, base_stick_union[1] + 100), base_stick_union, 3) # support stick
    pygame.draw.line(screen, WHITE, (base_stick_union[0] - 100, base_stick_union[1] + 100), base_stick_union, 3) # support stick

    pygame.draw.line(screen, WHITE, base_stick_union, top_stick_union1, 3) # long vertical stick
    pygame.draw.line(screen, WHITE, top_stick_union1, top_stick_union2, 3) # horizontal stick to the right

    pygame.draw.line(screen, WHITE, top_stick_union2, stick_head_union, 3) # stick where the head is attached

    radius = 40
    pygame.draw.circle(screen, WHITE, (stick_head_union[0], stick_head_union[1] + radius + 3), radius, width=3) # head

    height = 110
    torso_start = (stick_head_union[0], stick_head_union[1] + radius* 2 + 3)
    torso_end = (stick_head_union[0], stick_head_union[1] + radius* 2 + 3 + height)
    pygame.draw.line(screen, WHITE, torso_start, torso_end, width=3) # torso

    shoulder = (torso_start[0], torso_start[1] + (height // 3))
    arm_length = 30
    pygame.draw.line(screen, WHITE, shoulder, (shoulder[0] - arm_length, shoulder[1] + arm_length), width=3) # left arm
    pygame.draw.line(screen, WHITE, shoulder, (shoulder[0] + arm_length, shoulder[1] + arm_length), width=3) # right arm

    leg_length = 60
    pygame.draw.line(screen, WHITE, torso_end, (torso_end[0] - leg_length + 20, torso_end[1] + leg_length), width=3) # left leg
    pygame.draw.line(screen, WHITE, torso_end, (torso_end[0] + leg_length - 20, torso_end[1] + leg_length), width=3) # right leg

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