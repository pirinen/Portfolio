import pygame, sys
from pygame.locals import *
import random
    #Jukka Pirinen        8.9.2016

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Pallo(pygame.sprite.Sprite):  #Pallo-luokka
    image = pygame.image.load("ball.gif")   #Ladataan pallo

    def __init__(self):

        self.image = Pallo.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(550) #arvotaan paikka pallolle
        self.rect.y = random.randrange(400)

        pygame.sprite.Sprite.__init__(self)

#Pelaaja-luokka
class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
    image = pygame.image.load("car.gif")   #Kuva
       
    def __init__(self, x, y):
                
        #Tehdaan auto
        self.image = Player.image
        self.rect = self.image.get_rect()
       
        pygame.sprite.Sprite.__init__(self)

        #Aloituskohta
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        #Vaihdellaan suuntaa
        self.change_x += x
        self.change_y += y
 
    def update(self):
        #Paivitellaan auton paikkaa
        #Siirry vasen/oikea
        self.rect.x += self.change_x

        #Siirry ylos/alas
        self.rect.y += self.change_y
    #-----------------------------
    #-----------------------------
         
SpriteLista = pygame.sprite.Group() #Spritelista
PalloLista = pygame.sprite.Group()  #---
 
pygame.init()
pallo = Pallo()         #Tehdaan eka pallo 
PalloLista.add(pallo)   #ennenkuin timer saa tehtya lisaa
pygame.time.set_timer(USEREVENT+1, 2000)        #Ajastin pallon paikanvaihdolle
screen = pygame.display.set_mode([600, 450])    #Asetetaan naytonkoko
pygame.display.set_caption('Tehtava 6')         #Otsikko

player = Player(10, 10)             #Luodaan pelaaja ja laitetaan aloituskohta
SpriteLista.add(player)             #Laitetaan pelaaja spritelistaan
clock = pygame.time.Clock()
 
done = False
 
while not done:  
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:  #Autolla ajelut alkaa
            if event.key == pygame.K_LEFT:
                player.changespeed(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(1, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -1)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 1)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-1, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 1)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -1)   #Autolla ajelut loppuu
                
        elif event.type == USEREVENT+1:     #Pallon paikan vaihtelu
            pallo = Pallo()         #Tehdaan uusi pallo
            PalloLista.empty()      #Tyhjennetaan edellinen pallo listasta
            PalloLista.add(pallo)   #Ja lisataan uusi pallo listalle

    SpriteLista.update()        #Paivitellaan
    if pygame.sprite.spritecollide(player, PalloLista, True):  #Kun osuma tulee, havitetaan pallo
        sys.exit(1)                                 #ja sammutetaan sovellus
        
    screen.fill(WHITE)
    PalloLista.draw(screen)
    SpriteLista.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(100)

pygame.quit()

#6.	Tee Spriteihin perustuva pygame – peli, jossa jahtaat jollain esineellä (tikulla, aseella, tms) 
#palloa. Pallo ilmestyy satunnaiseen paikkaan. Mikä on näytön päivitysväli, se on sinun määriteltävissä. 
#Jos esine osuu palloon, niin peli on ohi. Esinettä liikutat nuolinäppäimillä. 
