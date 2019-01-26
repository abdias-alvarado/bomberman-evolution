import pygame
import os
from Constantes import *


class Utility(object):
    '''
    Esta clase se encarga de realizar tareas comunes
    para todas las clases que componen el juego.

    '''

    def __init__(self):
        super().__init__()

    def ObtenerImagen(self, archivo, x, y, ancho, alto):
        '''
        Obtiene una imagen desde un archivo.
        El archivo puede contener una simple imagen o
        puede un grupo de imagenes que simulen una
        secuencia.

        Parámetros:
        archivo --> La ruta del archivo del cuál se extrae.
        x --> La coordenada en X para el archivo.
        y --> La coordenada en Y para el archivo.
        ancho --> El ancho de la imagen o del fragmento.
        alto --> El alto de la imagen o del fragmento.

        '''
        rutaArchivo = os.path.join('assets', 'sprites', archivo)
        cargaArchivo = pygame.image.load(rutaArchivo).convert()

        # Crear una superficie en blanco
        image = pygame.Surface([ancho, alto]).convert()

        # Copiar el sprite desde el archivo fuente
        image.blit(cargaArchivo, (0, 0), (x, y, ancho, alto))

        image.set_colorkey(BLANCO)

        return image

    def CargarImagen(self, archivo, x=-1, y=-1, colorkey=None):
        '''
        Carga una imagen desde un archivo.
        El archivo se debe encontrar en la carpeta assets\sprites.

        Parámetros:
        archivo --> El nombre del archivo a cargar.
        x --> El ancho de la imagen a obtener.
        y --> El alto de la imagen a obtener.
        colorkey --> El color de fondo de la imagen a colocar
                     en transparente.

        '''
        rutaArchivo = os.path.join('assets', 'sprites', archivo)
        image = pygame.image.load(rutaArchivo)
        image.convert()

        # Verificar si el usuario desea cambiar el color de fondo
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)

        # Si el usuario desea cambiar el tamaño de la imagen
        if x != -1 or y != -1:
            image = pygame.transform.scale(image, (x, y))

        return image

    def ReproducirSonido(self, audio):
        ruta = os.path.join('assets', 'sounds', audio)
        sonido = pygame.mixer.Sound(ruta)
        sonido.play()

    def ReproducirMusica(self, archivo):
        ruta = os.path.join('assets', 'sounds', archivo)
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()


    def MostrarTexto(self, texto, size, fuente, color, posicion, superficie,
                     centrarTexto=True):
        '''
        Muestra un texto en la superficie indicada.

        Parámetros:
        texto --> El contenido del texto a mostrar.
        size --> El tamaño del texto en pixeles.
        fuente --> La fuente del sistema a utilizar. Debe estar instalada.
        color --> El color del texto RBG o RGBA.
        posicion --> Un arreglo de [x, y] conteniendo la posición del texto.
        superficie --> La superficie sobre la que se escribe el texto
        centrarTexto --> Indica si la posición del texto es en el centro de la
                         supericie, obviando la posición que se envía.

        '''
        fuenteElegida = pygame.font.SysFont(fuente, size)
        contenido = fuenteElegida.render(texto, True, color)

        if centrarTexto:
            centrarX = (ANCHO // 2) - (contenido.get_width() // 2)
            centrarY = (ALTO // 2) - (contenido.get_height() // 2)
            superficie.blit(contenido, [centrarX, centrarY])
        else:
            superficie.blit(contenido, posicion)