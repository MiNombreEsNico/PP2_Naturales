import pygame
import sys
from config import screen_width, screen_height
from const import img_start, img_game, font_button, button_sound
from pygame.locals import QUIT

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Crear ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("¡Salva el mar!")

# Definir el botón
button_rect = pygame.Rect((screen_width // 2 - 224, screen_height // 2), (436, 101))

# Función para dibujar el botón
def draw_button():
    pygame.draw.rect(screen, (0, 151, 178), button_rect, border_radius=50)  # Dibujar el botón (azul claro)
    text_surface = font_button.render("Empezar juego", True, (255, 255, 255))  # Texto del botón
    
    # Obtener las dimensiones del texto
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    
    # Calcular la posición centrada del texto
    text_x = button_rect.x + (button_rect.width - text_width) // 2
    text_y = button_rect.y + (button_rect.height - text_height) // 2
    
    # Dibujar el texto centrado en el botón
    screen.blit(text_surface, (text_x, text_y))

# Reproducir sonido del botón
def play_button_sound():
    sound = pygame.mixer.Sound(button_sound)
    sound.play()

# Escena de inicio
def start_scene():
    background = pygame.image.load(img_start)  # Cargar imagen de fondo para la escena de inicio

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Detectar clic en el botón
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    play_button_sound()  # Reproducir el sonido del botón
                    print("Iniciar el juego...")
                    return "game_scene"  # Cambia a la escena del juego

        # Dibujar fondo y botón
        screen.blit(background, (0, 0))
        draw_button()

        # Actualizar la pantalla
        pygame.display.update()

# Escena del juego
def game_scene():
    background = pygame.image.load(img_game)  # Cargar imagen de fondo para la escena del juego

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Aquí iría la lógica del juego

        # Dibujar fondo del juego
        screen.blit(background, (0, 0))

        # Actualizar la pantalla
        pygame.display.update()

        # Puedes usar una condición para regresar a la pantalla de inicio o a otra escena
        # if algún evento:
        #     return "start_scene"

# Controlador principal de escenas
def main():
    current_scene = "start_scene"  # Comienza con la pantalla de inicio

    while True:
        if current_scene == "start_scene":
            current_scene = start_scene()  # Llama a la escena de inicio
        elif current_scene == "game_scene":
            current_scene = game_scene()  # Cambia a la escena del juego

# Ejecutar el juego
if __name__ == "__main__":
    main()
