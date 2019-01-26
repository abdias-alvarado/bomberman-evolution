import pygame
from Utility import Utility


class Llama(pygame.sprite.Sprite):
    '''
    Representa una explosión con una diana en el juego.

    '''

    def __init__(self, centroBomba):
        '''
        '''
        super().__init__()
        self.centroBomba = centroBomba
        self.utility = Utility()

        self.image = self.utility.CargarImagen('explosion07.png')
        self.image = pygame.transform.scale(self.image, [150, 150])

        self.rect = self.image.get_rect()
        self.rect.center = self.centroBomba


