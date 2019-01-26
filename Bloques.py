import pygame
from Utility import Utility

# Constantes
# Éstas definen los tipos de plataformas
# (x, y, ancho, alto)
# x --> Localización en el sprite
# y --> Localización en el sprite
# ancho --> La anchura del sprite
# alto --> Altura del sprite
BLOQUE1 = (1, 1, 28, 28)
BLOQUE2 = (34, 1, 28, 28)
BLOQUE3 = (66, 0, 28, 28)
BLOQUE4 = (98, 0, 28, 28)
BLOQUE5 = (130, 66, 28, 28)


class Bloques(pygame.sprite.Sprite):
    '''
    Esta clase representa una pared que limita el movimiento
    del Jugador en pantalla.

    '''

    def __init__(self, hojaSprite, posicion):
        '''
        Constructor.

        Inicializa los valores de una Pared.

        Parámetros:
        hojaSprite --> La imagen conteniendo los sprites
                       a utilizar.

        '''
        # Llama al constructor padre
        super().__init__()

        self.utility = Utility()

        self.image = self.utility.ObtenerImagen(hojaSprite, posicion[0],
                                                posicion[1], posicion[2],
                                                posicion[3])

        self.rect = self.image.get_rect()