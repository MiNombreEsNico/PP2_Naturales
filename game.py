import pygame
import sys
from config import screen_width, screen_height
from const import button, img_start, font_button, button_sound
from pygame.locals import QUIT

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Crear ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("¡Salva el mar!")

# Imprimir la ruta de la imagen de fondo para depuración
print("Image path:", img_start)

# Cargar imagen de fondo
try:
    background = pygame.image.load(img_start)
except FileNotFoundError:
    print(f"Error: No se encontró la imagen en la ruta {img_start}")
    pygame.quit()
    sys.exit()

# Función para dibujar el botón 0, 151, 178
def draw_button():
    # Quiero que el texto del boton este centrado
    button = pygame.Rect((screen_width // 2 - 224, screen_height // 2), (436, 101))
    pygame.draw.rect(screen, (0, 151, 178), button, border_radius=50,)  # Dibujar el botón (azul claro)
    text_surface = font_button.render("Empezar juego", True, (255, 255, 255))  # Texto del botón
     # Obtener las dimensiones del texto
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    
    # Calcular la posición centrada del texto
    text_x = button.x + (button.width - text_width) // 2
    text_y = button.y + (button.height - text_height) // 2
    
    # Dibujar el texto centrado en el botón
    screen.blit(text_surface, (text_x, text_y))


# Reproducir sonido del botón
def play_button_sound():
    sound = pygame.mixer.Sound(button_sound)
    sound.play()

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
                play_button_sound()  # Reproducir el sonido del botón
                print("Iniciar el juego...")  # Aquí iría el cambio a la pantalla de juego

    # Dibujar fondo
    screen.blit(background, (0, 0))

    # Dibujar el botón de inicio
    draw_button()

    # Actualizar la pantalla
    pygame.display.update()
