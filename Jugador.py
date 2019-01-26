import pygame
import random
from pygame.locals import *

from Constantes import *
from Bloques import Bloques
from Utility import Utility


class Jugador(pygame.sprite.Sprite):
    '''
    Esta clase representa al protagonista del juego.

    Se encarga de todas las acciones del protagonista.

    '''

    def __init__(self, x, y):
        '''
        Constructor.

        Inicializa los valores del jugador.

        Parámetros:
        x --> La coordenada en x en pixeles.
        y --> La coordenada en y en pixeles.

        '''
        # Llamar al constructor de la clase padre
        super().__init__()
        self.utility = Utility()

        self.vidas = 1
        self.muerto = False        

        self.jugadorDerecha = list()
        self.jugadorIzquierda = list()
        self.jugadorArriba = list()
        self.jugadorAbajo = list()

        self.direccion = None

        # Cargar los sprites en las listas de animación respectivas.

        for x in range(8):
            imageArriba = self.utility.CargarImagen('jugadorEspaldaWalk{0}.png'.format(x))
            imageAbajo = self.utility.CargarImagen('jugadorFrenteWalk{0}.png'.format(x))
            imageDer = self.utility.CargarImagen('jugadorWalk{0}.png'.format(x))

            #imageArriba = pygame.transform.scale(imageArriba, (20, 40))
            #imageAbajo = pygame.transform.scale(imageAbajo, (20, 40))
            #imageDer= pygame.transform.scale(imageDer, (20, 40))

            self.jugadorArriba.append(imageArriba)
            self.jugadorAbajo.append(imageAbajo)
            self.jugadorDerecha.append(imageDer)

            imageIzq = pygame.transform.flip(imageDer, True, False)
            #imageIzq = pygame.transform.scale(imageIzq, (20, 40))
            self.jugadorIzquierda.append(imageIzq)

        self.image = self.jugadorDerecha[0]
      

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.cambioX = 0
        self.cambioY = 0

        self.nivel = None

    def update(self):
        '''
        Actualiza el jugador a la posición
        del cursor del mouse en la aplicación.

        '''
        posicionX = self.rect.x
        posicionY = self.rect.y

        if self.direccion == 'Derecha':
            sprite = int((posicionX // 10) % len(self.jugadorDerecha))
            self.image = self.jugadorDerecha[sprite]
        elif self.direccion == 'Izquierda':
            sprite = int((posicionX // 10) % len(self.jugadorIzquierda))
            self.image = self.jugadorIzquierda[sprite]
        elif self.direccion == 'Arriba':
            sprite = int((posicionY // 10) % len(self.jugadorArriba))
            self.image = self.jugadorArriba[sprite]
        elif self.direccion == 'Abajo':
            sprite = int((posicionY // 10) % len(self.jugadorAbajo))
            self.image = self.jugadorAbajo[sprite]

    def CambioVelocidad(self, x, y):
        '''
        Cambia la velocidad de movimiento del Jugadpr.
        Es aumentada a través de las pulsaciones en
        el teclado.

        Parámetros:
        x --> El aumento de velocidad en el eje x.
        y --> El aumento de velocidad en el eje y.

        '''
        self.cambioX += x
        self.cambioY += y

    def Mover(self, paredes):
        '''
        Refresca la posición del Jugador en la pantalla.

        Parámetros:
        paredes --> Los objetos de tipo Pared que componen
                    el nivel.

        '''
        # Desplazar hacia la izquierda o derecha
        self.rect.x += self.cambioX

        # Verificar si el jugador colisiona con un objeto
        # de tipo Pared
        listaImpactos = pygame.sprite.spritecollide(self, paredes,
                                                    False)
        for impacto in listaImpactos:
            # Si nos estamos desplazando a la derecha, hacemos que
            # nuestro lado derecho sea el lado izquierdo del objeto
            # que hemos tocado.
            if self.cambioX > 0:
                self.rect.right = impacto.rect.left
            else:
                # En caso contrario si nos desplazamos hacia la
                # izquierda, hacemos lo contrario.
                self.rect.left = impacto.rect.right

        # Desplazar hacia arriba o abajo
        self.rect.y += self.cambioY

        # Verificar si el jugador colisiona con un objeto
        # de tipo Pared
        listaImpactos = pygame.sprite.spritecollide(self, paredes,
                                                    False)

        for impacto in listaImpactos:
            # Si nos desplazamos hacia abajo, reseteamos la
            # posición de nuestro jugador a la parte superior
            # del objeto con el que colisionamos.
            if self.cambioY > 0:
                self.rect.bottom = impacto.rect.top
                # Caso contrario, la parte superior de nuestro
                # jugador será la posición de la parte inferior
                # del objeto con el que colisionamos.
            else:
                self.rect.top = impacto.rect.bottom

        # VERIFICAR COLISIONES CON ENEMIGOS
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.listaEnemigos,
                                                    False)
        for impacto in listaImpactos:
            self.vidas -= 1
            if self.vidas <= 0:
                self.muerto = True

        # VERIFICAR COLISIONES BOMBAS/JUGADOR
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.listaBombas,
                                                    False)
        for impacto in listaImpactos:
            if impacto.activa:
                self.nivel.listaBombas.remove(impacto)
                self.vidas -= 1
                if self.vidas <= 0:
                    self.muerto = True

        # VERIFICAR COLISIONES BOMBAS/ENEMIGOS
        for enemigo in self.nivel.listaEnemigos:
            listaImpactos = pygame.sprite.spritecollide(enemigo,
                                                        self.nivel.listaBombas,
                                                        False)
            for impacto in listaImpactos:
                if impacto.activa:
                    self.utility.ReproducirSonido('enemigoQuemado.wav')
                    self.nivel.listaBombas.remove(impacto)
                    self.nivel.listaEnemigos.remove(enemigo)
                    impacto.kill()
                else:
                    enemigo.DefinirDireccion()

        # VERIFICAR COLISIONES BOMBAS/BLOQUES
        for bloque in self.nivel.listaParedesRemovibles:
            listaImpactos = pygame.sprite.spritecollide(bloque,
                                                        self.nivel.listaBombas,
                                                        False)
            for impacto in listaImpactos:
                if impacto.activa:
                    self.nivel.listaParedesRemovibles.remove(bloque)
                    # impacto.kill()

        for bloque in paredes:
            listaImpactos = pygame.sprite.spritecollide(bloque,
                                                        self.nivel.listaBombas,
                                                        False)
            for impacto in listaImpactos:
                if impacto.activa:
                    impacto.kill()

        # VERIFICAR COLISIONES JUGADOR/PAREDES REMOVIBLES
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.listaParedesRemovibles,
                                                    False)
        for impacto in listaImpactos:
            # Si nos estamos desplazando a la derecha, hacemos que
            # nuestro lado derecho sea el lado izquierdo del objeto
            # que hemos tocado.
            if self.cambioX > 0:
                self.rect.right = impacto.rect.left
            else:
                # En caso contrario si nos desplazamos hacia la
                # izquierda, hacemos lo contrario.
                self.rect.left = impacto.rect.right

        

        # Verificar si el jugador colisiona con un objeto
        # de tipo Pared
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.listaParedesRemovibles,
                                                    False)
        for impacto in listaImpactos:
            # Si nos desplazamos hacia abajo, reseteamos la
            # posición de nuestro jugador a la parte superior
            # del objeto con el que colisionamos.
            if self.cambioY > 0:
                self.rect.bottom = impacto.rect.top
                # Caso contrario, la parte superior de nuestro
                # jugador será la posición de la parte inferior
                # del objeto con el que colisionamos.
            else:
                self.rect.top = impacto.rect.bottom

        # VERIFICAR COLISIONES ENEMIGO/PARED
        for enemigo in self.nivel.listaEnemigos:
            listaImpactos = pygame.sprite.spritecollide(enemigo,
                                                        paredes,
                                                        False)
            for impacto in listaImpactos:
                if enemigo.direccion == 'Derecha':
                    enemigo.rect.right = impacto.rect.left
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Izquierda':
                    enemigo.rect.left = impacto.rect.right
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Abajo':
                    enemigo.rect.bottom = impacto.rect.top
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Arriba':
                    enemigo.rect.top = impacto.rect.bottom
                    enemigo.DefinirDireccion()

        for enemigo in self.nivel.listaEnemigos:
            listaImpactos = pygame.sprite.spritecollide(enemigo,
                                                        self.nivel.listaParedesRemovibles,
                                                        False)
            for impacto in listaImpactos:
                if enemigo.direccion == 'Derecha':
                    enemigo.rect.right = impacto.rect.left
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Izquierda':
                    enemigo.rect.left = impacto.rect.right
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Abajo':
                    enemigo.rect.bottom = impacto.rect.top
                    enemigo.DefinirDireccion()
                elif enemigo.direccion == 'Arriba':
                    enemigo.rect.top = impacto.rect.bottom
                    enemigo.DefinirDireccion()



