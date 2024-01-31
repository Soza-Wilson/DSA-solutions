import pygame


class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.move_right = False
        self.move_left = False

        self.screen_rect = ai_game.screen.get_rect()
        # loadinmg image 
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")

        #getting images rect
        self.rect = self.image.get_rect()


        self.settings = ai_game.settings



        
        '''

        We’ll position the ship at the bottom center of the screen.
        To do so, make the value of self.rect.midbottom match the
        midbottom attribute of the screen’s rect ❹. Pygame uses
        these rect attributes to position the ship image so it’s
        centered horizontally and aligned with the bottom of the
        screen.
        '''

        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.game_speed
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.settings.game_speed

  
        
