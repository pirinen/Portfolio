import pygame, sys
from pygame.locals import *
import time
    #Jukka Pirinen        8.9.2016
 
#Varit
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Pelaaja-luokka 
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):

        pos = pygame.mouse.get_pos()    #Otetaan pelaajan sijainti hiiren sijainnista

        self.rect.x = pos[0]            #ja liikutaan vain x-akselilla
#--------------------------#
#  Pelaaja-luokka loppuu   #
#--------------------------#
#Ammus-luokka
class Bullet(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):

        self.rect.y -= 3    #liikutellaan ammusta talla vauhdilla
#--------------------------#
#   Ammus-luokka loppuu    #
#--------------------------#
#Lintu-luokka
class Lintu(pygame.sprite.Sprite):
    image = pygame.image.load('bird.gif')
    
    def __init__(self):
        
        self.image = Lintu.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10    #Aloituspaikka linnulle
        
        pygame.sprite.Sprite.__init__(self)
        
    def update(self):
        
        self.rect.x += 3    #Liikutellaan lintua talla vauhdilla
        if self.rect.x > 700:    #Kun menee reunan yli
            self.rect.x = -250   #Lahtee kulkemaan alusta uudestaan
#--------------------------#
#   Lintu-luokka loppuu    #
#--------------------------#
    #--------------------------------------------
LintuLista = pygame.sprite.Group()  #Lintulista
AmmusLista = pygame.sprite.Group()  #Ammuslista
SpriteLista = pygame.sprite.Group()

pygame.init()
screen = pygame.display.set_mode([700, 400])    #Naytonkoko
pygame.display.set_caption('Lintu-animaatio')   #Otsikko

player = Player()           #Luodaan pelaaja
SpriteLista.add(player)     #Laitetaan se spritelistaan
player.rect.y = 370         #Pelaajan paikka, alareunassa

lintu = Lintu()             #Luodaan lintu
LintuLista.add(lintu)       #Laitetaan lintulistaan
pygame.time.set_timer(USEREVENT+1, 50)
SpriteLista.add(lintu)      #Ja spritelistaan

clock = pygame.time.Clock()

done = False
#---------------------------------------#
#         Paa-ohjelma alkaa             #
#---------------------------------------#
while not done:
  
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:  #Jos painetaan MBTN
            ammus = Bullet()                        #Tehdaan ammus

            ammus.rect.x = player.rect.x    #Laitetaan ammus sinne missa pelaaja on
            ammus.rect.y = player.rect.y

            SpriteLista.add(ammus)          #Laitetaan ammus spritelistaan
            AmmusLista.add(ammus)           #ja ammuslistaan
        #Ammuslohko loppuu
        
        elif event.type == USEREVENT+1: #-------------
            lintu.update()
            
    SpriteLista.update()    #Paivitetaan 

    for ammus in AmmusLista:

        if pygame.sprite.spritecollide(ammus, LintuLista, True):    #Jos tulee osuma
            time.sleep(1)   #Pieni tauko osuman huomaamiseksi
            sys.exit(1)     #Ohjelman lopetus
 
        if ammus.rect.y < -10:      #Jos ammus menee ohi ruudusta
            AmmusLista.remove(ammus)#Poistetaan se molemmista listoista
            SpriteLista.remove(ammus)
 

    screen.fill(WHITE)
    LintuLista.draw(screen)
    AmmusLista.draw(screen)
    SpriteLista.draw(screen)

    pygame.display.flip()

    clock.tick(50)
 
pygame.quit()

#7.	Tee peli, jossa lintu lentää näytöin oikealta vasemmalle ja näytön alareunassa on ase, 
# kosta ammuttavalla luodilla yrität osua lintuun.
