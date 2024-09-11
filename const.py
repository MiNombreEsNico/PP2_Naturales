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
fish2 = resource_path("assets/img/fish2/fisherman.png")
fisherman = resource_path("assets/img/entities/fisherman.png")
fish1 = resource_path("assets/img/entities/fish1.png")
hippocampus = resource_path("assets/img/entities/hippocampus.png")
pear = resource_path("assets/img/entities/pear.png")
soda_can = resource_path("assets/img/soda_can/fisherman.png")
strawberry = resource_path("assets/img/strawberry/fisherman.png")
turtle = resource_path("assets/img/entities/turtle.png")
