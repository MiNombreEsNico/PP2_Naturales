import pygame
import sys
from config import screen_width, screen_height
from const import img_start, img_game, font_button, button_sound
from const import *
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

        # Aquí iría la lógica del juego
        
        # Dibujar fondo y botón
        screen.blit(background, (0, 0))
        draw_button()

        # Actualizar la pantalla
        pygame.display.update()

# Escena del juego
def game_scene():
    background = pygame.image.load(img_game)  # Cargar imagen de fondo para la escena del juego
    
    #Carga de imagenes
    apple_img = pygame.image.load(apple)
    banana_img = pygame.image.load(banana)
    bottle_img = pygame.image.load(bottle)
    carrot_img = pygame.image.load(carrot)
    clownfish_img = pygame.image.load(clownfish)
    crab_img = pygame.image.load(crab)
    fish2_img = pygame.image.load(fish2)
    fisherman_img = pygame.image.load(fisherman)
    fish1_img = pygame.image.load(fish1)
    hippocampus_img = pygame.image.load(hippocampus)
    pear_img = pygame.image.load(pear)
    soda_can_img = pygame.image.load(soda_can)
    strawberry_img = pygame.image.load(strawberry)
    turtle_img = pygame.image.load(turtle)
    
    # Cambia el tamaño de las imagenes (ancho, alto)
    apple_img = pygame.transform.scale(apple_img, (40, 40))
    banana_img = pygame.transform.scale(banana_img, (70, 60))
    bottle_img = pygame.transform.scale(bottle_img, (60, 40))
    carrot_img = pygame.transform.scale(carrot_img, (60, 50))
    clownfish_img = pygame.transform.scale(clownfish_img, (60, 60))
    crab_img = pygame.transform.scale(crab_img, (100, 75))
    fish2_img = pygame.transform.scale(fish2_img, (85, 65))
    fisherman_img = pygame.transform.scale(fisherman_img, (400, 400))
    fish1_img = pygame.transform.scale(fish1_img, (80, 70))
    hippocampus_img = pygame.transform.scale(hippocampus_img, (80, 60))
    pear_img = pygame.transform.scale(pear_img, (60, 50))
    soda_can_img = pygame.transform.scale(soda_can_img, (50, 40))
    strawberry_img = pygame.transform.scale(strawberry_img, (50, 40))
    turtle_img = pygame.transform.scale(turtle_img, (100, 100))
    
    # Posición inicial de los elementos
    apple_pos = [718,312] 
    banana_pos = [30,250]
    bottle_pos = [190,285]
    carrot_pos = [125,322]
    clownfish_pos = [308,400]
    crab_pos = [500,530]
    fish2_pos = [600,390]
    fisherman_pos = [150,-55]
    fish1_pos = [190,350]
    hippocampus_pos = [500,450]
    pear_pos = [400, 450]
    soda_can_pos = [400,300]
    strawberry_pos = [500,350]
    turtle_pos = [600,250]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Aquí iría la lógica del juego

        # Dibujar fondo del juego
        screen.blit(background, (0, 0))
        
        # Dibujar los elementos
        screen.blit(apple_img, apple_pos)
        screen.blit(banana_img, banana_pos)
        screen.blit(bottle_img, bottle_pos)
        screen.blit(carrot_img, carrot_pos)
        screen.blit(clownfish_img, clownfish_pos)
        screen.blit(crab_img, crab_pos)
        screen.blit(fish2_img, fish2_pos)
        screen.blit(fisherman_img, fisherman_pos)
        screen.blit(fish1_img, fish1_pos)
        screen.blit(hippocampus_img, hippocampus_pos)
        screen.blit(pear_img, pear_pos)
        screen.blit(soda_can_img, soda_can_pos)
        screen.blit(strawberry_img, strawberry_pos)
        screen.blit(turtle_img, turtle_pos)

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
