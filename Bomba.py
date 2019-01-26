import pygame
from pygame.locals import *
from Constantes import *
from Pared import Pared
from Explosion import Explosion
from Llama import Llama

from Utility import Utility


class Bomba(pygame.sprite.Sprite):
    def __init__(self):
        '''
        Constructor.

        Inicializa los valores para el nivel.

        '''
        super().__init__()
        self.utility = Utility()
        self.explosion = list()
        self.escala = 0
        self.retraso = 0
        self.exploto = False

        self.image = self.utility.CargarImagen('bomba.png')
        self.image = pygame.transform.scale(self.image, (85, 72))

        image = self.utility.CargarImagen('bomba.png')
        image = pygame.transform.scale(self.image, (85, 72))
        self.explosion.append(image)
        image = self.utility.CargarImagen('bomba.png')
        image = pygame.transform.scale(self.image, (75, 62))
        self.explosion.append(image)

        # Definir la imagen con la que inicia el jugador
        self.image = self.explosion[0]

        # Establecemos una referencia rectangular de la superficie
        self.rect = self.image.get_rect()

        # Establecemos los vectores de velocidad
        self.cambioX = 0
        self.cambioY = 0

        # Lista de todos los sprites en los cuales podemos colisionar
        self.nivel = None
        self.activa = False

        self.llama = Llama(self.rect.center)

    def Plantar(self, x, y):
        self.utility.ReproducirSonido('plantarBomba.wav')
        self.rect.x = x
        self.rect.y = y + 10
        self.animacion = Explosion(self.rect.center)

    def Explotar(self):
        self.utility.ReproducirSonido('explosion.wav')
        self.activa = True
        self.image = self.llama.image
        self.exploto = True

    def update(self):
        '''
        Actualiza el jugador a la posición
        del cursor del mouse en la aplicación.

        '''
        if self.retraso < 100:
            if self.retraso % 20 == 0:
                if self.escala == 0:
                    self.rect.x += 4
                    self.rect.y += 4
                    self.image = self.explosion[1]
                    self.escala = 1
                else:
                    self.rect.x -= 4
                    self.rect.y -= 4
                    self.image = self.explosion[0]
                    self.escala = 0
            self.retraso += 1
        else:
            self.Explotar()


