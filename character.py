import pygame
from config import screen_height, screen_width
from const import *

class Character:
    def __init__(self):
        self.image = pygame.image.load(fisherman)  # Usa la imagen del pescador
        self.drawing_line = False
        self.image = pygame.transform.scale(self.image, (200, 300))  # Ajusta el tamaño
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 450))  # Posición inicial
        self.speed = 1 # Velocidad de movimiento
        self.flip = False  # Dirección del personaje
        
        # Variables del hilo de la caña
        self.fishing = False
        self.line_length = 0  # Longitud del hilo
        self.max_line_length = screen_height - self.rect.bottom  # Hasta dónde puede llegar
    
    def move(self, dx):
        self.rect.x += dx
        # Verifica colisión con los bordes
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        
        # Actualiza la dirección del sprite
        if dx < 0:
            self.flip = False
        if dx > 0:
            self.flip = True
    
    def start_fishing(self):
        if not self.fishing:
            self.fishing = True
            self.line_length = 0  # Reinicia la longitud del hilo
    
    def update_fishing(self):
        if self.fishing:
            self.line_length += 5  # La línea baja
            if self.line_length >= self.max_line_length:
                self.fishing = False  # Detiene el hilo cuando llega al final
    
    def draw(self, surface):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(image_flip, self.rect.topleft)  # Dibuja el personaje
        
        # Dibujar el hilo de la caña
        if self.fishing:
            line_start = (self.rect.centerx, self.rect.top + 50)  # Punto de inicio del hilo
            line_end = (self.rect.centerx, self.rect.top + 50 + self.line_length)  # Punto final del hilo
            pygame.draw.line(surface, (255, 255, 255), line_start, line_end, 2)  # Dibuja el hilo en blanco
            
            