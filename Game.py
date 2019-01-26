'''
Muestra la forma correcta de organizar un juego
utilizando Orientación a Objetos.

'''
import pygame
import random
from pygame.locals import *

from Llama import Llama
from Constantes import *
from Utility import Utility
from Jugador import Jugador
from Enemigo import Enemigo
from Pared import Pared
from Bomba import Bomba
from NivelUno import NivelUno
from NivelDos import NivelDos
from NivelTres import NivelTres
from NivelCuatro import NivelCuatro
from NivelCinco import NivelCinco
from NivelSeis import NivelSeis
from NivelSiete import NivelSiete
from NivelOcho import NivelOcho
from NivelNueve import NivelNueve
from NivelFinal import NivelFinal



# Iniciar el motor de juego
pygame.init()

# Definir la superficie principal
PANTALLA = pygame.display.set_mode(VENTANA)

# Definir el reloj de juego
fpsClock = pygame.time.Clock()


class Game(object):
    '''
    Esta clase representa una instancia del juego.

    Se encarga del manejo global de todo lo que
    el juego representa.

    '''

    def __init__(self):
        '''
        Constructor.

        Crea todos los objetos e inicializa los atributos
        de nuestro juego.

        '''
        self.puntuacion = 0
        self.gameOver = False

        self.iniciar = False
        self.reproducir = False

        self.posicionOpcionY = 553
        self.opcion = 1

        # Crear nuestro protagonista
        self.jugador = Jugador(10, 10)

        # Crear una lista de sprites
        self.listaSprites = pygame.sprite.Group()
        self.desplazarNiveles = pygame.sprite.Group()

        # Agregar los niveles del juego
        self.niveles = []
        self.niveles.append(NivelUno(self.jugador))
        self.niveles.append(NivelDos(self.jugador))
        self.niveles.append(NivelTres(self.jugador))
        self.niveles.append(NivelCuatro(self.jugador))
        self.niveles.append(NivelCinco(self.jugador))
        self.niveles.append(NivelSeis(self.jugador))
        self.niveles.append(NivelSiete(self.jugador))
        self.niveles.append(NivelOcho(self.jugador))
        self.niveles.append(NivelNueve(self.jugador))
        self.niveles.append(NivelFinal(self.jugador))

        # Nivel inicial
        self.nivelActual = 0


        self.jugador.nivel = self.niveles[self.nivelActual]

        # Agregar el protagonista a lista de los sprites
        self.listaSprites.add(self.jugador)

        # self.listaSprites.add(self.enemigo)

        self.utility = Utility()
        self.fondo = self.utility.CargarImagen('fondo.png')
        self.fondoMenu = self.utility.CargarImagen('MenuInicial.png')
        self.fondoCreditos = self.utility.CargarImagen('Creditos.png')
        self.fondoGanaste = self.utility.CargarImagen('Ganaste.png')
        self.fondoNivelCompleto = self.utility.CargarImagen('NivelCumplido.png')
        self.fondoPerdiste = self.utility.CargarImagen('Perdiste.png')
        self.bomberOpt = self.utility.CargarImagen('jugadorDerecha.png')
        self.bomberOpt = pygame.transform.scale(self.bomberOpt, [50, 50])

    def ProcesarEventos(self):
        '''
        Procesar los eventos dentro del juego.

        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            # El jugador presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.jugador.direccion = 'Izquierda'
                    self.jugador.CambioVelocidad(-3, 0)
                if event.key == pygame.K_RIGHT:
                    self.jugador.direccion = 'Derecha'
                    self.jugador.CambioVelocidad(3, 0)
                if event.key == pygame.K_UP:
                    self.jugador.direccion = 'Arriba'
                    self.jugador.CambioVelocidad(0, -3)
                if event.key == pygame.K_DOWN:
                    self.jugador.direccion = 'Abajo'
                    self.jugador.CambioVelocidad(0, 3)
                if event.key == pygame.K_x:
                    bomba = Bomba()
                    bomba.Plantar(self.jugador.rect.x + 2,
                                  self.jugador.rect.y)
                    self.listaSprites.add(bomba)
                    self.niveles[self.nivelActual].listaBombas.add(bomba)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.jugador.CambioVelocidad(3, 0)
                if event.key == pygame.K_RIGHT:
                    self.jugador.CambioVelocidad(-3, 0)
                if event.key == pygame.K_UP:
                    self.jugador.CambioVelocidad(0, 3)
                if event.key == pygame.K_DOWN:
                    self.jugador.CambioVelocidad(0, -3)

    def LogicaEjecucion(self):
        '''
        Este método se ejecuta por cada fotograma.
        Actualiza la posición de los objetos y la interacción
        entre los mismos.

        '''
        if not self.gameOver and self.iniciar:
            if len(self.niveles[self.nivelActual].listaEnemigos) > 0:
                if self.jugador.muerto:
                    self.gameOver = True

                if self.reproducir:
                    self.niveles[self.nivelActual].MusicaNivel()
                    self.reproducir = False
                # Mover el jugador
                self.jugador.Mover(self.niveles[self.nivelActual].listaParedes)
                self.niveles[self.nivelActual].listaEnemigos.update()
                for bomba in self.niveles[self.nivelActual].listaBombas:
                    if bomba.exploto:
                        llama = Llama(bomba.rect.center)
                        self.niveles[self.nivelActual].listaLlamas.add(Llama(bomba.rect.center))
                        self.listaSprites.add(bomba.animacion)
                        self.niveles[self.nivelActual].listaLlamas.remove(llama)
                        self.listaSprites.remove(bomba)
                        self.niveles[self.nivelActual].listaBombas.remove(bomba)

                # Mover todos los sprites
                self.listaSprites.update()
                pygame.display.flip()
            else:
                self.gameOver = True

    def Desplegar(self, pantalla):
        '''
        Dibuja los objetos sobre la superficie seleccionada.

        Parámetros:
        pantalla --> La superficie sobre la cual se dibujan los objetos.

        '''
        # pantalla.blit(self.fondo, (0,0))
        if self.iniciar:
            if not self.gameOver:
                pantalla.blit(self.niveles[self.nivelActual].fondo,
                              (0, 0))
                self.niveles[self.nivelActual].listaParedes.draw(pantalla)
                self.niveles[self.nivelActual].listaParedesRemovibles.draw(pantalla)
                self.niveles[self.nivelActual].listaEnemigos.draw(pantalla)
                self.niveles[self.nivelActual].listaLlamas.draw(pantalla)
                self.listaSprites.draw(pantalla)

            if self.gameOver and self.jugador.muerto:
                PANTALLA.blit(self.fondoPerdiste, (0, 0))
                pygame.display.flip()
                self.utility.ReproducirSonido('sonidoPerdiste.wav')
                fpsClock.tick(0.50)
                self.Resetear(0)

            if self.gameOver and not self.jugador.muerto:
                PANTALLA.blit(self.fondoNivelCompleto, (0, 0))
                pygame.display.flip()
                self.utility.ReproducirSonido('sonidoGanaste.wav')
                fpsClock.tick(0.50)
                self.nivelActual += 1
                self.Resetear(self.nivelActual)
        else:
            if self.nivelActual == 0:
                self.MenuPrincipal()
            else:
                self.iniciar = True
                self.reproducir = True

        pygame.display.flip()

    def MenuPrincipal(self):
        self.utility.ReproducirMusica('musicaInicio.mp3')
        while not self.iniciar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.Desplazar()
            PANTALLA.blit(self.fondoMenu, (0, 0))
            PANTALLA.blit(self.bomberOpt,
                          (300, self.posicionOpcionY))
            pygame.display.flip()
            fpsClock.tick(10)
        PANTALLA.fill(BLANCO)
        self.reproducir = True
        pygame.display.flip()

    def Desplazar(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]:
            if self.posicionOpcionY > 553:
                self.posicionOpcionY -= 50
                self.opcion -= 1
        if tecla[pygame.K_DOWN]:
            if self.posicionOpcionY < 653:
                self.posicionOpcionY += 50
                self.opcion += 1
        if tecla[pygame.K_RETURN]:
            if self.opcion == 1:
                self.iniciar = True
            elif self.opcion == 2:
                self.Creditos()
            else:
                exit()

    def Creditos(self):
        PANTALLA.blit(self.fondoCreditos, (0, 0))
        pygame.display.flip()
        fpsClock.tick(0.50)

    def Resetear(self, nivel=0):
        '''
        '''
        self.__init__()
        self.jugador.__init__(10, 10)
        self.listaSprites = pygame.sprite.Group()
        self.desplazarNiveles = pygame.sprite.Group()

        # Nivel inicial
        self.nivelActual = nivel

        # Nivel Siguiente
        self.nivelSiguiente = 0

        self.jugador.nivel = self.niveles[self.nivelActual]

        # Agregar el protagonista a lista de los sprites
        self.listaSprites.add(self.jugador)


def main():
    '''
    Función principal del programa.

    '''
    # Título del juego
    pygame.display.set_caption('Bomberman Evolution - Abdias Alvarado')

    # Ocultar el cursor del mouse
    pygame.mouse.set_visible(False)

    # Controlador del ciclo principal
    hecho = False

    # Crear una instancia de clase Game
    juego = Game()

    while not hecho:
        # Procesar los eventos (pulsaciones del teclado, clic del ratón...)
        # juego.MenuPrincipal(PANTALLA)

        hecho = juego.ProcesarEventos()

        # Actualizar las posiciones de todos los objetos en pantalla
        juego.LogicaEjecucion()

        # Dibujar todos los objetos
        juego.Desplegar(PANTALLA)

        # Realizar una pausa hasta el siguiente fotograma
        fpsClock.tick(60)

    # Salir de la ventana de juego
    pygame.quit()


# Llamar a la función principal
if __name__ == '__main__':
    main()
