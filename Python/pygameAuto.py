import pygame, sys
from pygame.locals import *
    #Jukka Pirinen        8.9.2016

pygame.init()
fpsClock = pygame.time.Clock()  #ajastinkello
 
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Kaara-animaatio')

WHITE = (255, 255, 255)

Kaara = pygame.image.load('car2.gif')
KaaraX = 10
KaaraY = 200

while True: #Main Loop
    DISPLAYSURF.fill(WHITE)
    KaaraX += 3
    if KaaraX > 500:    #Kun menee reunan yli
        KaaraX = -250   #Lahtee kulkemaan alusta uudestaan

    DISPLAYSURF.blit(Kaara, (KaaraX, KaaraY))  #tama kuljettelee kuvaa
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(60)      #ajastinkello
    
# Tee pygame –pohjainen sovellus, jossa ikkunan alareunassa 
# liikkuu auto vasemmalta oikealle aina ja aina uudelleen. 
