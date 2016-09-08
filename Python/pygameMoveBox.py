import pygame, sys
from pygame.locals import *
    #Jukka Pirinen  8.9.2016

WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
#Pelaaja luokka
class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
       
    def __init__(self, x, y):
                
        #Tehdaan palikka
        self.image = pygame.Surface([50, 20])
        self.image.fill(RED)
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
        #Paivitellaan palikan paikkaa
        #Siirry vasen/oikea
        self.rect.x += self.change_x

        #Siirry ylos/alas
        self.rect.y += self.change_y
 


pygame.init()

screen = pygame.display.set_mode([500, 350]) #Laitetaan naytonkoko
pygame.display.set_caption('Tehtava 5') #Otsikko
SpriteLista = pygame.sprite.Group() #Spritelista
player = Player(100, 100)           #Luodaan pelaaja ja laitetaan aloituskohta
SpriteLista.add(player)             #Laitetaan pelaaja spritelistaan
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
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
                player.changespeed(0, -1)
 
    SpriteLista.update()        #Paivitellaan
 
    screen.fill(WHITE)
 
    SpriteLista.draw(screen)    #Piirrellaan
 
    pygame.display.flip()
 
    clock.tick(100)
 
pygame.quit()

#	Tee pygame –pohjainen sovellus, jossa liikutat nuolinäppäimellä laatikkoa ruudulla
