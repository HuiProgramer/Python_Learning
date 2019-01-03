import pygame,sys
from pygame.locals import *

white = 255,255,255
black = 0,0,0

pygame.init()

print(pygame.font.get_fonts())
screen = pygame.display.set_mode((600,500))
myfront = pygame.font.SysFont('dokchampah',60)
textImage = myfront.render("Hello Pygame",True,black)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(white)
        screen.blit(textImage,(100,100))
        pygame.display.update()