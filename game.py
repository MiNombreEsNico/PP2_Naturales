import pygame
import sys
from config import screen_width, screen_height
from const import button, img_start, font_button
from pygame.locals import QUIT

# Inicializar Pygame
pygame.init()

# Crear ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fishing Game")

# Imprimir la ruta de la imagen de fondo para depuración
print("Image path:", img_start)

# Cargar imagen de fondo
try:
    background = pygame.image.load(img_start)
except FileNotFoundError:
    print(f"Error: No se encontró la imagen en la ruta {img_start}")
    pygame.quit()
    sys.exit()

# Función para dibujar el botón
def draw_button():
    pygame.draw.rect(screen, (0, 128, 0), button)  # Dibujar el botón (verde)
    text_surface = font_button.render("Start", True, (255, 255, 255))  # Texto del botón
    screen.blit(text_surface, (button.x + 50, button.y + 25))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # Detectar clic en el botón
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                print("Iniciar el juego...")  # Aquí iría el cambio a la pantalla de juego

    # Dibujar fondo
    screen.blit(background, (0, 0))

    # Dibujar el botón de inicio
    draw_button()

    # Actualizar la pantalla
    pygame.display.update()
