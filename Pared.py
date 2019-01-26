import pygame
import random
from pygame.locals import *


class Pared(pygame.sprite.Sprite):
    '''
    Esta clase representa una pared que limita el movimiento
    del Jugador en pantalla.

    '''

    def __init__(self, x, y, ancho, alto, color):
        '''
        Constructor.

        Inicializa los valores de una Pared.

        Parámetros:
        x --> La coordenada en x en pixeles.
        y --> La coordenada en y en pixeles.
        ancho --> La anchura en pixeles de la pared.
        alto --> La altura de la pared en pixeles.
        color --> El color en RGB de la pared.

        '''
        # Llama al constructor padre
        super().__init__()

        # Crear una pared con los parámetros iniciales
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)

        # Colocar la pared en la coordenadas iniciales
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y