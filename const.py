import pygame
import os
import sys

# Función para obtener rutas de archivos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
width = 800
height = 600

# Botón
button = pygame.Rect((width // 2 - 224, height // 2), (436, 101))

# Tipografías
font = pygame.font.Font(resource_path("assets/fonts/MoreSugar-Regular.ttf"), 26)
font_button = pygame.font.Font(resource_path("assets/fonts/OpenSans-Bold.ttf"), 43)

# Backgrounds
img_start = resource_path("assets/img/background/home.png")
img_game = resource_path("assets/img/background/fishing_game.png")
# img_end = resource_path("assets/img/End.png")

# Música
background_sound = resource_path("assets/music/background.mp3")

# Sonidos
fishing_rod = resource_path("assets/sound/fishing_rod.mp3")
splash = resource_path("assets/sound/splash.ogg")
button_sound = resource_path("assets/sound/button.wav")

# Personajes/Elementos
apple = resource_path("assets/img/entities/apple.png")
banana = resource_path("assets/img/entities/banana.png")
bottle = resource_path("assets/img/entities/bottle.png")
carrot = resource_path("assets/img/entities/carrot.png")
clownfish = resource_path("assets/img/entities/clownfish.png")
crab = resource_path("assets/img/entities/crab.png")
fish2 = resource_path("assets/img/entities/fish2.png")
fisherman = resource_path("assets/img/entities/fisherman.png")
fish1 = resource_path("assets/img/entities/fish1.png")
hippocampus = resource_path("assets/img/entities/hippocampus.png")
pear = resource_path("assets/img/entities/pear.png")
soda_can = resource_path("assets/img/entities/soda_can.png")
strawberry = resource_path("assets/img/entities/strawberry.png")
turtle = resource_path("assets/img/entities/turtle.png")

# Posiciones iniciales de las imágenes
bottle_pos = [190, 285]
carrot_pos = [125, 322]
clownfish_pos = [308, 400]
crab_pos = [550, 566]
fish2_pos = [600, 390]
fisherman_pos = [0, 0]
fish1_pos = [0, 0]
hippocampus_pos = [0, 0]
pear_pos = [0, 0]
soda_can_pos = [0, 0]
strawberry_pos = [0, 0]
turtle_pos = [0, 0]

# Velocidades de las imágenes (en píxeles por frame)
#apple_vel = [1, 0]  # Mueve a la derecha
#banana_vel = [0, 1]  # Mueve hacia abajo
#bottle_vel = [1, 1]  # Mueve diagonalmente

apple_vel = [0, 0]
banana_vel = [0, 0]
bottle_vel = [0, 0]
carrot_vel = [0, 0]
clownfish_vel = [0, 0]
crab_vel = [0, 0]
fish2_vel = [0, 0]
fisherman_vel = [0, 0]
fish1_vel = [0, 0]
hippocampus_vel = [0, 0]
pear_vel = [0, 0]
soda_can_vel = [0, 0]
strawberry_vel = [0, 0]
turtle_vel = [0, 0]