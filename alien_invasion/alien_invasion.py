import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import AlienShip

import sys


class ElienInvation:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption(self.settings.title)
        self.ship = Ship(self)
       
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()




    def check_event(self):
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    self.keydown_events(e)
                elif e.type == pygame.KEYUP:
                    self.keyup_events(e)
                   

   

    def keydown_events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 self.ship.move_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.move_left = True
            elif event.key == pygame.K_q:
                 sys.exit()
            elif event.key == pygame.K_SPACE:
                self.fire_bullets()

    def fire_bullets(self):

        # we are creating a new instance of the bullet class 
        new_bullets =  Bullet(self)

        '''
        since the self.bullet object is a pygame sprits object we can easly assign the new bullets object
        to the class since the bullets class is a child of the pygame sprits class 
        '''
        self.bullets.add(new_bullets)

        
    def create_fleet(self):
        alien = AlienShip(self)
        self.aliens.add(alien) 
        alien_width, alien_height = alien.rect.size


        '''

         -Here we are getting the position of the first elien 
         -In the while roop we are adding new aliens if there is enough space to do so 
         -First we are checking if there is space 
         -Then we are creating a new alien ship instance 
         -We areassigning the x position to the curent x 
         -Then we are adding the new created instance into the eliens sprite group 
         -After we are adding the new accupied space to current x 
        
        ''' 
        current_x = alien_width
        while current_x < (self.settings.width - 2 * alien_width):
            self.create_alien(current_x)
            current_x += 2 * alien_width
            
            
                
            
    def create_alien(self,position_x):

        #  creating a new elien and adding it to the eliens group
        new_alien = AlienShip(self)
        new_alien.x = position_x
        new_alien.rect.x = position_x
     
        self.aliens.add(new_alien)

        
                
    def keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

                       
        
    def update_screen(self):
        #all activities that change display 
      
        self.screen.fill(self.settings.bg_color)
        self.bullets.update()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
         
    

    def run_game(self):
        while True:
            self.check_event()
            self.update_screen()
            self.ship.update() 
            self.clock.tick(60)
            
            
            

    

if __name__ == '__main__':
    game = ElienInvation()
    game.run_game()
        
                

