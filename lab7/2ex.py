import pygame as pg
import time

pg.init()
mus1=pg.mixer.music.load("mus1.mp3")
mus2=pg.mixer.music.queue("mus2.mp3")
mus3=pg.mixer.music.queue("mus3.mp3")
clock = pg.time.Clock()
pg.mixer.music.play(-1) 
screen=pg.display.set_mode((600,400))
bgd = pg.image.load("147.jpg")

songlist=["mus1.mp3", "mus2.mp3","mus3.mp3"]
curr_song=None

run=True
play=False
i=0
while run:
    screen.blit(bgd, (0, 0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                play=not play
                if play:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key==pg.K_RIGHT:
                i+=1
                if i>=len(songlist):
                    i=i-len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()
            elif event.key==pg.K_LEFT:
                i=i-1
                if i<0:
                    i=i+len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()

    pg.display.flip()
    clock.tick(60)
                






