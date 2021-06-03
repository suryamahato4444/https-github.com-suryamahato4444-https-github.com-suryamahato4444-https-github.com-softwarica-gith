import pygame
pygame.init()
# python use rgb colour
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
bgd=pygame.display.set_mode((1111,650))

pygame.display.update()
game_over=False
while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

