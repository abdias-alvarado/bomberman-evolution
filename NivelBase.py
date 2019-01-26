import pygame
from Constantes import *
from Bloques import *
from Utility import Utility


class NivelBase(object):
    '''
    Clase en la que se basan todos los niveles del juego.

    '''

    listaParedes = None
    listaEnemigos = None

    def __init__(self, jugador):
        '''
        Constructor.

        Inicializa el objeto NivelBase.

        '''
        self.utility = Utility()

        self.listaParedesRemovibles = pygame.sprite.Group()
        self.listaParedes = pygame.sprite.Group()
        self.listaEnemigos = pygame.sprite.Group()
        self.listaBombas = pygame.sprite.Group()
        self.listaLlamas = pygame.sprite.Group()

        self.jugador = jugador
        self.hojaSprite = 'bloques.png'
        self.fondo = None
        self.colorFondo = NEGRO

        self.reloj = pygame.time.get_ticks()
        self.pausa = 1000

        self.nivel = 0

        paredes = [  # PARED ARRIBA
                   [BLOQUE1, 0, 0],     # Bloque 0,0
                   [BLOQUE1, 28, 0],    # Bloque 1,0
                   [BLOQUE1, 56, 0],    # Bloque 2,0
                   [BLOQUE1, 84, 0],    # Bloque 3,0
                   [BLOQUE1, 112, 0],   # Bloque 4,0
                   [BLOQUE1, 140, 0],   # Bloque 5,0
                   [BLOQUE1, 168, 0],   # Bloque 6,0
                   [BLOQUE1, 196, 0],   # Bloque 7,0
                   [BLOQUE1, 224, 0],   # Bloque 8,0
                   [BLOQUE1, 252, 0],   # Bloque 9,0
                   [BLOQUE1, 280, 0],   # Bloque 10,0
                   [BLOQUE1, 308, 0],   # Bloque 11,0
                   [BLOQUE1, 336, 0],   # Bloque 12,0
                   [BLOQUE1, 364, 0],   # Bloque 13,0
                   [BLOQUE1, 392, 0],   # Bloque 14,0
                   [BLOQUE1, 420, 0],   # Bloque 15,0
                   [BLOQUE1, 448, 0],   # Bloque 16,0
                   [BLOQUE1, 476, 0],   # Bloque 17,0
                   [BLOQUE1, 504, 0],   # Bloque 18,0
                   [BLOQUE1, 532, 0],   # Bloque 19,0
                   [BLOQUE1, 560, 0],   # Bloque 20,0
                   [BLOQUE1, 588, 0],   # Bloque 21,0
                   [BLOQUE1, 616, 0],   # Bloque 22,0
                   [BLOQUE1, 644, 0],   # Bloque 23,0
                   [BLOQUE1, 672, 0],   # Bloque 24,0
                   [BLOQUE1, 700, 0],   # Bloque 25,0
                   [BLOQUE1, 728, 0],   # Bloque 26,0
                   [BLOQUE1, 756, 0],   # Bloque 27,0
                   [BLOQUE1, 784, 0],   # Bloque 28,0
                   [BLOQUE1, 812, 0],   # Bloque 29,0
                   [BLOQUE1, 840, 0],   # Bloque 30,0
                   [BLOQUE1, 868, 0],   # Bloque 31,0
                   [BLOQUE1, 896, 0],   # Bloque 32,0
                   [BLOQUE1, 924, 0],   # Bloque 33,0
                   [BLOQUE1, 952, 0],   # Bloque 34,0
                   [BLOQUE1, 980, 0],   # Bloque 35,0

                   # PARED ABAJO
                   [BLOQUE1, 0, 784],     # Bloque 0,0
                   [BLOQUE1, 28, 784],    # Bloque 1,0
                   [BLOQUE1, 56, 784],    # Bloque 2,0
                   [BLOQUE1, 84, 784],    # Bloque 3,0
                   [BLOQUE1, 112, 784],   # Bloque 4,0
                   [BLOQUE1, 140, 784],   # Bloque 5,0
                   [BLOQUE1, 168, 784],   # Bloque 6,0
                   [BLOQUE1, 196, 784],   # Bloque 7,0
                   [BLOQUE1, 224, 784],   # Bloque 8,0
                   [BLOQUE1, 252, 784],   # Bloque 9,0
                   [BLOQUE1, 280, 784],   # Bloque 10,0
                   [BLOQUE1, 308, 784],   # Bloque 11,0
                   [BLOQUE1, 336, 784],   # Bloque 12,0
                   [BLOQUE1, 364, 784],   # Bloque 13,0
                   [BLOQUE1, 392, 784],   # Bloque 14,0
                   [BLOQUE1, 420, 784],   # Bloque 15,0
                   [BLOQUE1, 448, 784],   # Bloque 16,0
                   [BLOQUE1, 476, 784],   # Bloque 17,0
                   [BLOQUE1, 504, 784],   # Bloque 18,0
                   [BLOQUE1, 532, 784],   # Bloque 19,0
                   [BLOQUE1, 560, 784],   # Bloque 20,0
                   [BLOQUE1, 588, 784],   # Bloque 21,0
                   [BLOQUE1, 616, 784],   # Bloque 22,0
                   [BLOQUE1, 644, 784],   # Bloque 23,0
                   [BLOQUE1, 672, 784],   # Bloque 24,0
                   [BLOQUE1, 700, 784],   # Bloque 25,0
                   [BLOQUE1, 728, 784],   # Bloque 26,0
                   [BLOQUE1, 756, 784],   # Bloque 27,0
                   [BLOQUE1, 784, 784],   # Bloque 28,0
                   [BLOQUE1, 812, 784],   # Bloque 29,0
                   [BLOQUE1, 840, 784],   # Bloque 30,0
                   [BLOQUE1, 868, 784],   # Bloque 31,0
                   [BLOQUE1, 896, 784],   # Bloque 32,0
                   [BLOQUE1, 924, 784],   # Bloque 33,0
                   [BLOQUE1, 952, 784],   # Bloque 34,0
                   [BLOQUE1, 980, 784],   # Bloque 35,0

                   # PARED IZQUIERDA
                   [BLOQUE1, 0, 0],     # Bloque 0,0
                   [BLOQUE1, 0, 28],    # Bloque 1,0
                   [BLOQUE1, 0, 56],    # Bloque 2,0
                   [BLOQUE1, 0, 84],    # Bloque 3,0
                   [BLOQUE1, 0, 112],   # Bloque 4,0
                   [BLOQUE1, 0, 140],   # Bloque 5,0
                   [BLOQUE1, 0, 168],   # Bloque 6,0
                   [BLOQUE1, 0, 196],   # Bloque 7,0
                   [BLOQUE1, 0, 224],   # Bloque 8,0
                   [BLOQUE1, 0, 252],   # Bloque 9,0
                   [BLOQUE1, 0, 280],   # Bloque 10,0
                   [BLOQUE1, 0, 308],   # Bloque 11,0
                   [BLOQUE1, 0, 336],   # Bloque 12,0
                   [BLOQUE1, 0, 364],   # Bloque 13,0
                   [BLOQUE1, 0, 392],   # Bloque 14,0
                   [BLOQUE1, 0, 420],   # Bloque 15,0
                   [BLOQUE1, 0, 448],   # Bloque 16,0
                   [BLOQUE1, 0, 476],   # Bloque 17,0
                   [BLOQUE1, 0, 504],   # Bloque 18,0
                   [BLOQUE1, 0, 532],   # Bloque 19,0
                   [BLOQUE1, 0, 560],   # Bloque 20,0
                   [BLOQUE1, 0, 588],   # Bloque 21,0
                   [BLOQUE1, 0, 616],   # Bloque 22,0
                   [BLOQUE1, 0, 644],   # Bloque 23,0
                   [BLOQUE1, 0, 672],   # Bloque 24,0
                   [BLOQUE1, 0, 700],   # Bloque 25,0
                   [BLOQUE1, 0, 728],   # Bloque 26,0
                   [BLOQUE1, 0, 756],   # Bloque 27,0
                   [BLOQUE1, 0, 784],   # Bloque 28,0

                   # PARED DERECHA
                   [BLOQUE1, 980, 0],     # Bloque 0,0
                   [BLOQUE1, 980, 28],    # Bloque 1,0
                   [BLOQUE1, 980, 56],    # Bloque 2,0
                   [BLOQUE1, 980, 84],    # Bloque 3,0
                   [BLOQUE1, 980, 112],   # Bloque 4,0
                   [BLOQUE1, 980, 140],   # Bloque 5,0
                   [BLOQUE1, 980, 168],   # Bloque 6,0
                   [BLOQUE1, 980, 196],   # Bloque 7,0
                   [BLOQUE1, 980, 224],   # Bloque 8,0
                   [BLOQUE1, 980, 252],   # Bloque 9,0
                   [BLOQUE1, 980, 280],   # Bloque 10,0
                   [BLOQUE1, 980, 308],   # Bloque 11,0
                   [BLOQUE1, 980, 336],   # Bloque 12,0
                   [BLOQUE1, 980, 364],   # Bloque 13,0
                   [BLOQUE1, 980, 392],   # Bloque 14,0
                   [BLOQUE1, 980, 420],   # Bloque 15,0
                   [BLOQUE1, 980, 448],   # Bloque 16,0
                   [BLOQUE1, 980, 476],   # Bloque 17,0
                   [BLOQUE1, 980, 504],   # Bloque 18,0
                   [BLOQUE1, 980, 532],   # Bloque 19,0
                   [BLOQUE1, 980, 560],   # Bloque 20,0
                   [BLOQUE1, 980, 588],   # Bloque 21,0
                   [BLOQUE1, 980, 616],   # Bloque 22,0
                   [BLOQUE1, 980, 644],   # Bloque 23,0
                   [BLOQUE1, 980, 672],   # Bloque 24,0
                   [BLOQUE1, 980, 700],   # Bloque 25,0
                   [BLOQUE1, 980, 728],   # Bloque 26,0
                   [BLOQUE1, 980, 756],   # Bloque 27,0
                   [BLOQUE1, 980, 784],    # Bloque 28,0
                   
                   # BLOQUES CENTRALES FILA 1
                   [BLOQUE1, 90, 125],   # Bloque 28,0
                   [BLOQUE1, 180, 125],
                   [BLOQUE1, 270, 125],
                   [BLOQUE1, 360, 125],
                   [BLOQUE1, 450, 125],
                   [BLOQUE1, 540, 125],
                   [BLOQUE1, 630, 125],
                   [BLOQUE1, 720, 125],
                   [BLOQUE1, 810, 125],
                   [BLOQUE1, 900, 125],
                   [BLOQUE1, 990, 125],

                   # BLOQUES CENTRALES FILA 2
                   [BLOQUE1, 90, 250],   # Bloque 28,0
                   [BLOQUE1, 180, 250],
                   [BLOQUE1, 270, 250],
                   [BLOQUE1, 360, 250],
                   [BLOQUE1, 450, 250],
                   [BLOQUE1, 540, 250],
                   [BLOQUE1, 630, 250],
                   [BLOQUE1, 720, 250],
                   [BLOQUE1, 810, 250],
                   [BLOQUE1, 900, 250],
                   [BLOQUE1, 990, 250],

                   # BLOQUES CENTRALES FILA 3
                   [BLOQUE1, 90, 375],   # Bloque 28,0
                   [BLOQUE1, 180, 375],
                   [BLOQUE1, 270, 375],
                   [BLOQUE1, 360, 375],
                   [BLOQUE1, 450, 375],
                   [BLOQUE1, 540, 375],
                   [BLOQUE1, 630, 375],
                   [BLOQUE1, 720, 375],
                   [BLOQUE1, 810, 375],
                   [BLOQUE1, 900, 375],
                   [BLOQUE1, 990, 375],

                   # BLOQUES CENTRALES FILA 4
                   [BLOQUE1, 90, 500],   # Bloque 28,0
                   [BLOQUE1, 180, 500],
                   [BLOQUE1, 270, 500],
                   [BLOQUE1, 360, 500],
                   [BLOQUE1, 450, 500],
                   [BLOQUE1, 540, 500],
                   [BLOQUE1, 630, 500],
                   [BLOQUE1, 720, 500],
                   [BLOQUE1, 810, 500],
                   [BLOQUE1, 900, 500],
                   [BLOQUE1, 990, 500],

                   # BLOQUES CENTRALES FILA 5
                   [BLOQUE1, 90, 625],   # Bloque 28,0
                   [BLOQUE1, 180, 625],
                   [BLOQUE1, 270, 625],
                   [BLOQUE1, 360, 625],
                   [BLOQUE1, 450, 625],
                   [BLOQUE1, 540, 625],
                   [BLOQUE1, 630, 625],
                   [BLOQUE1, 720, 625],
                   [BLOQUE1, 810, 625],
                   [BLOQUE1, 900, 625],
                   [BLOQUE1, 990, 625],

                   # BLOQUES CENTRALES FILA 6
                   [BLOQUE3, 90, 750],   # Bloque 28,0
                   [BLOQUE3, 180, 750],
                   [BLOQUE3, 270, 750],
                   [BLOQUE3, 360, 750],
                   [BLOQUE3, 450, 750],
                   [BLOQUE3, 540, 750],
                   [BLOQUE3, 630, 750],
                   [BLOQUE3, 720, 750],
                   [BLOQUE3, 810, 750],
                   [BLOQUE3, 900, 750],
                   [BLOQUE3, 990, 750],
                   ]

        # Navegamos por la lista de paredes y
        # creamos los objetos de tipo Pared
        for bloque in paredes:
            item = Bloques(self.hojaSprite, bloque[0])
            item.rect.x = bloque[1]
            item.rect.y = bloque[2]
            self.listaParedes.add(item)

    def update(self):
        self.listaParedes.update()
        self.listaEnemigos.update()

    def Dibujar(self, pantalla):
        pantalla.fill(self.colorFondo)
        pantalla.blit(self.fondo, (0, 0))

        self.listaParedes.draw(pantalla)
        self.listaEnemigos.draw(pantalla)

    def DesplegarInformacion(self, pantalla):
        self.utility.MostrarTexto('Nivel: ' + str(self.nivel), 20, 'verdana',
                                  BLANCO, [80, 780], pantalla, False)

        pygame.display.flip()
        