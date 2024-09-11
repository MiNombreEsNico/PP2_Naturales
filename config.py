import pygame
import sys
import os

pygame.init()

# Tamaño de ventana
width = 800
height = 600

button = pygame.Rect((width // 2 - 224, height // 2), (436, 101))

def resourse_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
