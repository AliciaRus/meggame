import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Meg!')
clock = pygame.time.Clock() 
oog = input("whatever you want meg")
print(oog)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)
    pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)