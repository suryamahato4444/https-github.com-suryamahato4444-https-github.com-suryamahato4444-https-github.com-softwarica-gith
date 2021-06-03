import pygame
pygame.init()
clock=pygame.time.Clock()
# for game display surface
bgd=pygame.display.set_mode((1111,650))
# python use rgb colour
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
def game_loop():
   x=400
   y=500
   x_change=0
   game_over=False
   while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    #     basic movement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=+20
            elif event.key==pygame.K_RIGHT:
                x_change=-20
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
    bgd.fill(white)
    # drawing on game display
    pygame.draw.rect(bgd,red,[x,y,50,50])
    x=x-x_change
    clock.tick(50)
    pygame.display.update()

game_loop()
pygame.quit()
quit()