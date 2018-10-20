import pygame
import time
import sys
import string
from pygame.locals import *

from pygameGUI.cursor import cursor
from pygameGUI.button import button
from pygameGUI.loadImage import loadImage
from logic.object import object

pygame.mixer.init()
#pygame.mixer.music.load("sound.mp3")
#back_sound= pygame.mixer.Sound("back.wav")
#pygame.mixer.music.play(loops=-1)


def main():
    pygame.init()
    screen=pygame.display.set_mode([1366,768])
    #pygame.display.toggle_fullscreen
    pygame.display.set_caption("Tellus")
    myCursor=cursor()
    

    #definiciones
    wallp=loadImage("backgrounds/f1.jpg",1)
    x=0
    y=0
    t1=loadImage("sprites/1.png")
    t2=loadImage("sprites/2.png")
    t3=loadImage("sprites/3.png")
    t4=loadImage("sprites/4.png")
    t5=loadImage("sprites/5.png")
    t6=loadImage("sprites/6.png")

    tt=[t1,t2,t3,t4,t5,t6]
    
    p1=objects(tt,5)

    x=0
    y=0
    while True:
        screen.blit(wallp,(0,0))
        p1.put(screen,x,y)
        myCursor.update()
        
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    y=y+100
                    p1.put(screen,x,y)
                if event.key==K_UP:
                    y=y-100
                    p1.put(screen,x,y)
                if event.key==K_LEFT:
                    x=x-100
                    p1.put(screen,x,y)
                if event.key==K_RIGHT:
                    x=x+100
                    p1.put(screen,x,y)

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        p1.update(screen)
        pygame.display.flip()
        time.sleep(0.07)

main()
