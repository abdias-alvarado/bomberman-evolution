import pygame
from Utility import Utility
from Llama import Llama


class Explosion(pygame.sprite.Sprite):
    '''
    Representa una explosión con una diana en el juego.

    '''

    def __init__(self, centroEnemigo):
        '''
        Constructor.

        Inicializa los valores del enemigo.

        Parámetros:
        size --> Tamaño en píxeles del enemigo.
        centroEnemigo --> La coordenada (x,y) para el centro del enemigo.

        '''
        super().__init__()
        self.centroEnemigo = centroEnemigo
        self.utility = Utility()
        self.animacion = list()
        self.llama = Llama(self.centroEnemigo)
        
        self.image = self.utility.CargarImagen('explosion00.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.center = self.centroEnemigo

        self.frameRate = 75
        self.frame = 0
        self.ultimaActualizacion = pygame.time.get_ticks()

        # Cargar las explosiones
        self.CargarAnimacion()

    def CargarAnimacion(self):
        '''
        Carga la animación acorde con el tamaño solicitado.

        '''
        for x in range(5):
            sprite = self.utility.CargarImagen('explosion0{}.png'.format(x))
            image = pygame.transform.scale(sprite, (50, 50))
            self.animacion.append(image)
        self.animacion.append(self.llama.image)


    def update(self):
        '''
        Actualiza la explosión.

        '''
        ahora = pygame.time.get_ticks()

        if ahora - self.ultimaActualizacion > self.frameRate:
            self.ultimaActualizacion = ahora
            self.frame += 1
            # Si los frames son iguales a todas las imagenes
            # de la explosión, desaparecer el objeto con self.kill()
            if self.frame == len(self.animacion):
                self.kill()
            else:
                if self.frame < 5:
                    self.image = self.animacion[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = self.centroEnemigo
