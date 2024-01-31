import pygame
from pygame.sprite import Sprite

class AlienShip(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
       
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        

        #  adding elien to the top left of the screen 
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        #  adding space to the left side of the elien object (the space is equal to the width of the elien )
        self.x = float(self.rect.x)
    
    
        

