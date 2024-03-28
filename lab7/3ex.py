import pygame 
pygame.init()

screen= pygame.display.set_mode((500,500))
white=(255,255,255)

def ball(x,y):
    pygame.draw.circle(screen,(255,0,0),(x,y),25)

x, y = 0, 0 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x+=20
            elif event.key==pygame.K_LEFT:
                x-=20
            if event.key==pygame.K_UP:
                y-=20
            elif event.key==pygame.K_DOWN:
                y+=20
        
    if x < 25:
        x = 25
    elif x > 500 - 25:
        x = 500 - 25
    if y < 25:
        y = 25
    elif y > 500 - 25:
        y = 500 - 25

    
    screen.fill(white)
    ball(x,y)
    pygame.display.update()
pygame.quit()

