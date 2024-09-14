import pygame
import sys
import os
import const as const

pygame.init()



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

screen_width = 800
screen_height = 600

img_start = resource_path("assets/img/background/inicio.png")
# img_game = resource_path("assets/img/Juego.png")
# img_end = resource_path("assets/img/Final.png")