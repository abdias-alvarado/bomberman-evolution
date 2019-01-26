import pygame
import random
from pygame.locals import *
from Utility import Utility
from Constantes import *


class Enemigo(pygame.sprite.Sprite):
    '''
    Esta clase representa al protagonista del juego.

    Se encarga de todas las acciones del protagonista.

    '''

    def __init__(self, x, y, enemigo=1):
        '''
        Constructor.

        Inicializa los valores del jugador.

        Parámetros:
        x --> La coordenada en x en pixeles.
        y --> La coordenada en y en pixeles.

        '''
        # Llamar al constructor de la clase padre
        super().__init__()
        self.enemigo = enemigo
        self.direccion = None
        self.DefinirDireccion()
        self.neutralizado = False

        self.utility = Utility()
        self.enemigo1 = list()
        self.enemigo2 = list()
        self.enemigo3 = list()
        self.enemigo4 = list()
        self.enemigo5 = list()
        self.enemigo6 = list()

        # Cargar los enemigos
        enemigo1 = self.utility.CargarImagen('enemigoFront1.png')
        enemigo1 = pygame.transform.scale(enemigo1, (50, 50))
        self.enemigo1.append(enemigo1)
        enemigo1 = self.utility.CargarImagen('enemigoBack1.png')
        enemigo1 = pygame.transform.scale(enemigo1, (50, 50))
        self.enemigo1.append(enemigo1)

        enemigo2 = self.utility.CargarImagen('enemigoFront2.png')
        enemigo2 = pygame.transform.scale(enemigo2, (50, 50))
        self.enemigo2.append(enemigo2)
        enemigo2 = self.utility.CargarImagen('enemigoBack2.png')
        enemigo2 = pygame.transform.scale(enemigo2, (50, 50))
        self.enemigo2.append(enemigo2)

        enemigo3 = self.utility.CargarImagen('enemigoFront3.png')
        enemigo3 = pygame.transform.scale(enemigo3, (50, 50))
        self.enemigo3.append(enemigo3)
        enemigo3 = self.utility.CargarImagen('enemigoBack3.png')
        enemigo3 = pygame.transform.scale(enemigo3, (50, 50))
        self.enemigo3.append(enemigo3)

        enemigo4 = self.utility.CargarImagen('enemigoFront4.png')
        enemigo4 = pygame.transform.scale(enemigo4, (50, 50))
        self.enemigo4.append(enemigo4)
        enemigo4 = self.utility.CargarImagen('enemigoBack4.png')
        enemigo4 = pygame.transform.scale(enemigo4, (50, 50))
        self.enemigo4.append(enemigo4)

        enemigo5 = self.utility.CargarImagen('enemigoFront5.png')
        enemigo5 = pygame.transform.scale(enemigo5, (50, 50))
        self.enemigo5.append(enemigo5)
        enemigo5 = self.utility.CargarImagen('enemigoBack5.png')
        enemigo5 = pygame.transform.scale(enemigo5, (50, 50))
        self.enemigo5.append(enemigo5)

        enemigo6 = self.utility.CargarImagen('enemigoFront6.png')
        enemigo6 = pygame.transform.scale(enemigo6, (50, 50))
        self.enemigo6.append(enemigo6)
        enemigo6 = self.utility.CargarImagen('enemigoBack6.png')
        enemigo6 = pygame.transform.scale(enemigo6, (50, 50))
        self.enemigo6.append(enemigo6)

        if self.enemigo == 1:
            self.image = self.enemigo1[0]
        elif self.enemigo == 2:
            self.image = self.enemigo2[0]
        elif self.enemigo == 3:
            self.image = self.enemigo3[0]
        elif self.enemigo == 4:
            self.image = self.enemigo4[0]
        elif self.enemigo == 5:
            self.image = self.enemigo5[0]
        elif self.enemigo == 6:
            self.image = self.enemigo6[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Establecemos los vectores de velocidad
        self.cambioX = 1
        self.cambioY = 1

    def update(self):
        '''
        Actualiza el jugador a la posición
        del cursor del mouse en la aplicación.

        '''
        if self.enemigo == 1:
            if self.direccion == 'Derecha':
                self.image = self.enemigo1[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo1[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo1[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo1[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()
        elif self.enemigo == 2:
            if self.direccion == 'Derecha':
                self.image = self.enemigo2[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo2[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo2[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo2[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()
        elif self.enemigo == 3:
            if self.direccion == 'Derecha':
                self.image = self.enemigo3[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo3[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo3[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo3[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()
        elif self.enemigo == 4:
            if self.direccion == 'Derecha':
                self.image = self.enemigo4[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo4[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo4[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo4[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()
        elif self.enemigo == 5:
            if self.direccion == 'Derecha':
                self.image = self.enemigo5[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo5[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo5[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo5[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()
        elif self.enemigo == 6:
            if self.direccion == 'Derecha':
                self.image = self.enemigo6[0]
                if self.rect.x < ANCHO - 40:
                    self.rect.x += self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Izquierda':
                self.image = self.enemigo6[0]
                if self.rect.x > 28:
                    self.rect.x -= self.cambioX
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Arriba':
                self.image = self.enemigo6[1]
                if self.rect.y > 28:
                    self.rect.y -= self.cambioY
                else:
                    self.DefinirDireccion()
            elif self.direccion == 'Abajo':
                self.image = self.enemigo6[0]
                if self.rect.y < ALTO - 40:
                    self.rect.y += self.cambioY
                else:
                    self.DefinirDireccion()

    def DefinirDireccion(self):
        selector = random.randrange(1, 4)
        if selector == 1:
            self.direccion = 'Derecha'
        elif selector == 2:
            self.direccion = 'Izquierda'
        elif selector == 3:
            self.direccion = 'Arriba'
        elif selector == 4:
            self.direccion = 'Abajo'
