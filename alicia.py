import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Meg!')
clock = pygame.time.Clock() 

megio = pygame.image.load('megio.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.circle(screen, (255,0,255), (200, 200), 50, 1)
    screen.blit(megio,(50,50))
    pygame.display.update()
    clock.tick(30)