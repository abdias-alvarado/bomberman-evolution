import pygame
from Constantes import *
from Bloques import Bloques
from Utility import Utility
from NivelBase import NivelBase
from Pared import Pared
from Bloques import *
from Enemigo import Enemigo
from Bomba import Bomba


class NivelSiete(NivelBase):
    '''
    Contiene el diseño del primer nivel.

    '''

    def __init__(self, jugador):
        '''
        Constructor.

        Inicializa los valores para el nivel.

        '''
        NivelBase.__init__(self, jugador)
        self.utility = Utility()
        self.bombasPermitidas = 1
        self.fondo = self.utility.CargarImagen('fondo.png')
        self.nivel = 1

        # Crear las paredes que contiene el nivel
        # (posX, posY, ancho, alto)
        paredes = [  # BLOQUES DE RELLENO
                   [BLOQUE4, 135, 125],
                   [BLOQUE4, 135, 85],
                   [BLOQUE4, 135, 45],
                   [BLOQUE4, 135, 165],
                   [BLOQUE4, 135, 205],
                   [BLOQUE4, 180, 45],
                   [BLOQUE4, 180, 85],

                   [BLOQUE4, 400, 290],
                   [BLOQUE4, 400, 330],
                   [BLOQUE4, 500, 290],
                   [BLOQUE4, 500, 330],

                   [BLOQUE4, 585, 440],
                   [BLOQUE4, 635, 440],
                   [BLOQUE4, 600, 330],
                   [BLOQUE4, 645, 330],
                   ]

        # Navegamos por la lista de paredes y
        # creamos los objetos de tipo Pared
        for bloque in paredes:
            item = Bloques(self.hojaSprite, bloque[0])
            item.rect.x = bloque[1]
            item.rect.y = bloque[2]
            self.listaParedesRemovibles.add(item)

        self.listaEnemigos.add(Enemigo(800, 50, 2))

        self.listaEnemigos.update()

    def MusicaNivel(self):
        self.utility.ReproducirMusica('musicaNivel1.mp3')
