import pygame
import os
import sys

# Función para obtener rutas de archivos
def resourse_path(relative_path):
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
font = pygame.font.Font(resourse_path("assets/fonts/MoreSugar-Regular.ttf"), 26)
font_button = pygame.font.Font(resourse_path("assets/fonts/OpenSans-Bold.ttf"), 43)

# Backgrounds
img_start = resourse_path("assets/img/background/inicio.png")
# img_game = resourse_path("assets/img/Game.png")
# img_end = resourse_path("assets/img/End.png")

# Música
background_sound = resourse_path("assets/music/background.mp3")

# Sonidos
fishing_rod = resourse_path("assets/sound/fishing_rod.mp3")
splash = resourse_path("assets/sound/splash.mp3")

# Personajes/Elementos
apple = resourse_path("assets/img/entities/apple.png")
banana = resourse_path("assets/img/entities/banana.png")
bottle = resourse_path("assets/img/entities/bottle.png")
carrot = resourse_path("assets/img/entities/carrot.png")
clownfish = resourse_path("assets/img/entities/clownfish.png")
crab = resourse_path("assets/img/entities/crab.png")
fish2 = resourse_path("assets/img/fish2/fisherman.png")
fisherman = resourse_path("assets/img/entities/fisherman.png")
fish1 = resourse_path("assets/img/entities/fish1.png")
hippocampus = resourse_path("assets/img/entities/hippocampus.png")
pear = resourse_path("assets/img/entities/pear.png")
soda_can = resourse_path("assets/img/soda_can/fisherman.png")
strawberry = resourse_path("assets/img/strawberry/fisherman.png")
turtle = resourse_path("assets/img/entities/turtle.png")
